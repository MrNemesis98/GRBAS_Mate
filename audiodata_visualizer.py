from PyQt5.QtWidgets import QWidget, QStyle, QStyleOption
from PyQt5.QtCore import Qt, pyqtSignal, pyqtProperty
from PyQt5.QtGui import QPainter, QPen, QColor

import wave
import struct



class WaveformWidget(QWidget):
    seekRequested = pyqtSignal(int)  # ms

    def __init__(self, parent=None):
        super().__init__(parent)

        # Damit background/border aus Stylesheet bei custom paint sichtbar wird
        self.setAttribute(Qt.WA_StyledBackground, True)

        # Daten / Playback
        self.peaks = []          # list[float] 0..1
        self.duration_ms = 1
        self.position_ms = 0

        # Defaults (werden von CSS überschrieben)
        self._playedColor = QColor("#43A047")
        self._unplayedColor = QColor("#555555")
        self._playheadColor = QColor("#FFFFFF")

        # Optik
        self._inset = 6
        self.setMinimumHeight(60)
        self.setMouseTracking(True)

    # ---------- Helpers ----------
    @staticmethod
    def _to_qcolor(value, fallback: QColor) -> QColor:
        """Accept QColor, str, QVariant-ish values; never crash."""
        try:
            if isinstance(value, QColor):
                return value
            # manchmal kommt QVariant -> str() ist sicherer
            c = QColor(str(value))
            return c if c.isValid() else fallback
        except Exception:
            return fallback

    # ---------- Qt Properties (CSS qproperty-...) ----------
    def getPlayedColor(self):
        return self._playedColor

    def setPlayedColor(self, v):
        self._playedColor = self._to_qcolor(v, self._playedColor)
        self.update()

    playedColor = pyqtProperty(QColor, getPlayedColor, setPlayedColor)

    def getUnplayedColor(self):
        return self._unplayedColor

    def setUnplayedColor(self, v):
        self._unplayedColor = self._to_qcolor(v, self._unplayedColor)
        self.update()

    unplayedColor = pyqtProperty(QColor, getUnplayedColor, setUnplayedColor)

    def getPlayheadColor(self):
        return self._playheadColor

    def setPlayheadColor(self, v):
        self._playheadColor = self._to_qcolor(v, self._playheadColor)
        self.update()

    playheadColor = pyqtProperty(QColor, getPlayheadColor, setPlayheadColor)

    # ---------- Public API ----------
    def setPeaks(self, peaks):
        self.peaks = peaks or []
        self.update()

    def setDuration(self, ms: int):
        self.duration_ms = max(1, int(ms))

    def setPosition(self, ms: int):
        self.position_ms = max(0, int(ms))
        self.update()

    # ---------- Painting ----------
    def paintEvent(self, event):
        p = QPainter(self)
        p.setRenderHint(QPainter.Antialiasing, False)

        # 1) Stylesheet background/border/radius zeichnen
        opt = QStyleOption()
        opt.initFrom(self)
        self.style().drawPrimitive(QStyle.PE_Widget, opt, p, self)

        # Wenn noch keine Peaks da sind: nur Hintergrund/Border anzeigen
        if not self.peaks or len(self.peaks) < 2:
            return

        w = self.width()
        h = self.height()

        inset = max(0, int(self._inset))
        left = inset
        top = inset
        draw_w = max(1, w - 2 * inset)
        draw_h = max(1, h - 2 * inset)
        mid = top + draw_h // 2

        duration = max(1, int(self.duration_ms))
        pos = max(0, int(self.position_ms))
        progress = pos / duration
        if progress < 0:
            progress = 0.0
        elif progress > 1:
            progress = 1.0

        played_w = int(progress * draw_w)

        # Ungespielt
        p.setPen(QPen(self.unplayedColor, 1))
        self._draw_peaks(p, left, top, draw_w, draw_h, mid)

        # Gespielt (Clip)
        p.setPen(QPen(self.playedColor, 1))
        p.setClipRect(left, top, played_w, draw_h)
        self._draw_peaks(p, left, top, draw_w, draw_h, mid)
        p.setClipping(False)

        # Playhead
        playhead_x = left + played_w
        p.setPen(QPen(self.playheadColor, 1))
        p.drawLine(playhead_x, top, playhead_x, top + draw_h)

    def _draw_peaks(self, painter, left, top, w, h, mid):
        n = len(self.peaks)
        if n < 2:
            return

        half = (h / 2) - 1
        if half <= 0:
            return

        denom = max(1, w - 1)
        # peaks: 0..1
        for x in range(w):
            idx = int(x / denom * (n - 1))
            amp = self.peaks[idx]
            if amp < 0:
                amp = 0
            elif amp > 1:
                amp = 1
            y = int(amp * half)
            painter.drawLine(left + x, mid - y, left + x, mid + y)

    # ---------- Seek (optional) ----------
    def _x_to_ms(self, x: int) -> int:
        inset = max(0, int(self._inset))
        left = inset
        draw_w = max(1, self.width() - 2 * inset)
        x = max(left, min(x, left + draw_w))
        rel = (x - left) / draw_w
        return int(rel * max(1, int(self.duration_ms)))

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.seekRequested.emit(self._x_to_ms(e.x()))

    def mouseMoveEvent(self, e):
        if e.buttons() & Qt.LeftButton:
            self.seekRequested.emit(self._x_to_ms(e.x()))


def compute_peaks_wav_16bit(path: str, target_points: int = 900) -> list:
    """
    Liest eine 16-bit PCM WAV-Datei und berechnet normierte Peaks (0..1),
    stark downsampled auf target_points Punkte (für Waveform-Darstellung).
    """

    with wave.open(path, "rb") as wf:
        n_channels = wf.getnchannels()
        sampwidth = wf.getsampwidth()
        n_frames = wf.getnframes()

        if sampwidth != 2:
            raise ValueError("compute_peaks_wav_16bit erwartet 16-bit PCM WAV (sampwidth=2).")

        raw = wf.readframes(n_frames)
        total_samples = n_frames * n_channels

        # little-endian signed 16-bit
        samples = struct.unpack("<" + "h" * total_samples, raw)

        # Pro Frame: Max-Amplitude über alle Kanäle (macht Mono-Peaks)
        mono_abs = []
        for i in range(0, len(samples), n_channels):
            frame = samples[i:i+n_channels]
            mono_abs.append(max(abs(s) for s in frame))

        if not mono_abs:
            return []

        # Downsampling auf target_points Buckets
        step = max(1, len(mono_abs) // max(1, target_points))
        peaks = []
        max_val = 1

        for i in range(0, len(mono_abs), step):
            bucket = mono_abs[i:i+step]
            peak = max(bucket) if bucket else 0
            peaks.append(peak)
            if peak > max_val:
                max_val = peak

        # Normieren auf 0..1
        return [p / max_val for p in peaks]
