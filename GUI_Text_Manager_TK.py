"""
Copyright © MrNemesis98, GitHub, 2026

Co-Author of this file:
- Institution:
- Mail:
- Github:

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files, to deal in the software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, and to
permit persons to whom the software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
software. The program is provided “as is”, without warranty of any kind, express or implied, including but not
limited to the warranties of merchantability, fitness for a particular purpose and noninfringement.
In no event shall the author(s) or copyright holder(s) be liable for any claim, damages or other liability, whether
in an action of contract, tort or otherwise, arising from, out of or in connection with the software or the use or
other dealings in the software.

By using GRBAS_Mate or one of its components you agree to all these conditions.

------------------------------------------------------------------------------------------------------------------------

This software contains partially modified audio material from the Perceptual Voice Quality Database:
https://data.mendeley.com/datasets/9dz247gnyb/4.
Walden, Patrick R. (2022), “Perceptual Voice Qualities Database (PVQD)”, Mendeley Data, V4, doi: 10.17632/9dz247gnyb.4


CC BY 4.0 licence description (https://creativecommons.org/licenses/by/4.0/)
The files associated with this dataset are licensed under a Creative Commons Attribution 4.0 International licence.
What does this mean?

You can share, copy and modify this dataset so long as you give appropriate credit, provide a link to the CC BY license,
and indicate if changes were made, but you may not do so in a way that suggests the rights holder has endorsed you or
your use of the dataset. Note that further permission may be required for any content within the dataset that is
identified as belonging to a third party.
"""


def window_title():
    return "GRBAS_Mate v1.0"


def label_main_headline_background(with_copyright=False):
    return ("   GRBAS_Mate   [ɡɹæps me͜ɪt̚]"
            "\t\tCopyright © MrNemesis98, GitHub, 2026") \
        if with_copyright else "   GRBAS_Mate   [ɡɹæps me͜ɪt̚]"


def label_menu_title(menu):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif Bilgisi"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Parametre Kayıtları"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Ayarlar"

    else:
        return "Bilinmeyen Değer!"


def label_text_1(menu, var_1=0, software_version=""):
    if menu.lower() == "info":
        # Sürüm Bilgisi
        if var_1 == 1:
            text = f"""<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu yazılımın yüklü sürümü:	{software_version}
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu ilk sürüm, yaygın kullanılan GRBAS ölçeğine ait tüm parametreler için ayrıntılı açıklamalar
                    (IF-GRBAS genişletmesi dahil) içerir. Ayrıca her parametre için farklı şiddet düzeylerinde
                    açık erişimli örnek kayıtlar sunulmuştur.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu yazılım ve açık erişimli materyaller; klinik fonetik araştırmalarına katkı ve eğitim,
                    evde değerlendirme ya da KBB tanısında yardımcı bir araç olarak tasarlanmıştır.
                </p>"""
            return text
        # Gelecek Planı
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        GRBAS_Mate hâlâ geliştirme aşamasındadır. Gelecek sürümler IF-GRBAS ölçeği için daha fazla
                        örnek kayıt içerecektir. CAPE-V gibi alternatif ölçek ve ölçüm sistemleri de eklenebilir.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Ayrıca, kayıtları dinleyip IF-GRBAS’a göre değerlendirmenizi sağlayan bir eğitim modu
                        planlanmaktadır. Bu, gerçek disfonik seslerde yedi parametreyi ayırt etme becerinize
                        yönelik bir meydan okuma olarak düşünülebilir.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                        Son adım, bu yazılıma entegre edilecek otomatik ses kalitesi analiz aracıdır. Bu kısım bir
                        yüksek lisans tez projesinin parçası olacaktır ve 2026 sonbaharı için planlanmaktadır.
                    </p>"""
            return text
        # Telif
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Telif © MrNemesis98, GitHub, 2026
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                Bu yazılım MIT Lisansı ile yayımlanmıştır. Yazılımın bir kopyasını edinen herkese, yazılımı kullanma,
                kopyalama, değiştirme, birleştirme, yayımlama, dağıtma, alt lisanslama ve satma izni ücretsiz olarak verilir.
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                  Telif bildirimi ve bu izin metni, yazılımın tüm kopyalarına veya önemli bölümlerine eklenmelidir.
                  Yazılım “olduğu gibi” sağlanır; açık veya zımni hiçbir garanti verilmez. Yazar(lar) ve hak sahipleri,
                  yazılımın kullanımından doğabilecek zararlardan sorumlu değildir.
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial; color: #DB8004;">
                  GRBAS_Mate’i veya bileşenlerini kullanarak bu koşulları kabul etmiş olursun.
                </p>
                <p style="text-align: justify; line-height: 1.1; font-family: Arial;">
                İpucu: Ayarlar menüsündeki telif seçeneklerine göz at!
                </p>"""
            return text

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        text = """                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu, farklı ses bozukluklarına ait pek çok örneği dinlemenizi ve bunları uzman referanslarıyla
                    ilişkilendirmenizi sağlayan ücretsiz bir arayüzdür.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Çalışma/öğrenim amaçlı tasarlanmıştır; ancak evde değerlendirme ve profesyonel kullanım için de
                yardımcı olabilir.
                </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Bu ilk sürüm, yaygın kullanılan GRBAS ölçeğine göre çeşitli parametreler için farklı şiddet
                düzeylerinde örnek kayıtlar sunar.
                </p>
                """
        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu menüde her bir IF-GRBAS parametresi için açık ve kısa <span style="font-weight:bold;color:#0B839C;">
                    açıklamalar</span> bulabilirsin.
                    Ok tuşlarıyla sayfalar arasında gezinebilir veya aşağıdaki genel görünümden doğrudan seçim yapabilirsin.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Açıklamaları atlamak istersen, örnek seslere Kayıtlar menüsünden ulaşabilirsin
                    (soldaki gezinme çubuğunda üçüncü seçenek).
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Ayrıca sağ köşedeki kulaklık simgesine tıklayarak seçtiğin parametreye ait kayıtlara
                    doğrudan geçebilirsin.
                    </p>

                    """
        elif var_1 == 2:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Seste <span style="font-weight:bold;color:#7030A0;">Kararsızlık</span>.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu, sesin stabilitesindeki düzensizlik ve dalgalanmaların derecesini ifade eder.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Kararsız bir ses dengesiz duyulur; şiddet ve perde açısından belirgin biçimde değişebilir.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Kararsızlık, <span style="font-weight:bold;color:#0B839C;">orijinal</span>
                     GRBAS ölçeğinde yer almaz; ancak onu <span style="font-weight:bold;color:#7030A0;">genişletmek</span> için kullanılabilir.
                    </p>
                    """
        elif var_1 == 3:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bir sesin <span style="font-weight:bold;color:#7030A0;">Akıcılığı</span>, konuşmanın akışına benzer.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Konuşurken sesin ne kadar pürüzsüz ve akışkan duyulduğunu ifade eder.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Daha çok konuşma ritmi, duraklamaların yapısı ve süreklilikle ilgilidir.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Akıcılık, <span style="font-weight:bold;color:#0B839C;">orijinal</span>
                     GRBAS ölçeğinde yer almaz; ancak onu <span style="font-weight:bold;color:#7030A0;">genişletmek</span> için kullanılabilir.
                    </p>
                    """
        elif var_1 == 4:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    GRBAS ölçeğinin <span style="font-weight:bold;color:#7030A0;">Genişletilmesi</span>,
                    disfonik ses özelliklerini daha ayrıntılı yakalamak ve bazı belirtilere karşı ölçeğin duyarlılığını
                    artırmak için yapılmıştır.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Ölçek, bağlama ve araştırma hedeflerine göre, disfonik seslerin özelliklerini daha iyi tanımlayan
                    ek parametrelerle genişletilebilir.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu ölçek genişletmesinin gerekçesi için aşağıdaki çalışmaya göz at:
                        <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                            style="text-decoration:none; color:#1a73e8;">
                            Voice Quality and Dysphonia (OSF projesi - yalnızca görüntüleme)
                        </a>
                    </p>"""
        elif var_1 == 5:
            text = """                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Seste kısıklığın <span style="font-weight:bold;color:#0B839C;">Derecesi</span>.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Kısıklık; pürüzlülük, nefeslilik ve gerginlik gibi çeşitli özelliklerin bileşimidir.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Kısıklık, bu bireysel parametrelere bağlı olarak sesin genel izlenimi olarak tanımlanabilir.
                    </p>
                    """
        elif var_1 == 6:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Sesin <span style="font-weight:bold;color:#0B839C;">Pürüzlülüğü</span>.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu, ses tellerinin düzensiz titreşim algısını ifade eder; sesin pürüzlü veya “tırmalayıcı” duyulmasına
                    neden olabilir.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">

                    </p>
                    """
        elif var_1 == 7:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Sesin <span style="font-weight:bold;color:#0B839C;">Nefesliliği</span>.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu, seste havanın duyulabilir şekilde kaçmasıdır.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Ses tellerinin tam kapanmamasına işaret edebilir.
                    </p>
                    """
        elif var_1 == 8:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Sesin zayıf duyulması.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">
Asteni</span>, sesin ne kadar zayıf veya kısık
                    algılandığını tanımlar.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Bu özellik, ses tellerindeki gerilimin azalmasının bir sonucudur.
                    </p>
                    """
        elif var_1 == 9:
            text = """<p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    Sesin gergin duyulması.
                    </p>
                    </p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    <span style="font-weight:bold;color:#0B839C;">Gerginlik</span>, 
                    larinks kaslarının aşırı kullanımı
                    (hiperfonksiyon) derecesini ifade eder; bu durum ses tellerini etkiler ve seste duyulabilir.
                    </p>
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">

                    </p>
                    """
        else:
            text = """
                    <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    N/V
                    </p>
                    """
        return text

    elif menu.lower() == "recordings":
        return "Çalışma Modu"

    elif menu.lower() == "training":
        text = """                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Eğitim modu şu anda geliştirme aşamasındadır.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Bu modda, disfonik ses kayıtlarını değerlendirerek beceri ve bilginizi test edebileceksiniz.
                Bir ses materyali seti verildiğinde doğru parametreyi ve şiddet düzeyini seçmeniz gerekecek.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Bu mod, aşağıdaki çalışmanın çevrimiçi deneyindeki kategori testi fikrine dayanır:
                <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF projesi - yalnızca görüntüleme)
                </a>
                .
                </p>
                """
        return text

    elif menu.lower() == "settings":
        return "Ayarlar"

    else:
        return "Bilinmeyen Değer!"


def label_text_2(menu):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        text = """                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                    GRBAS ölçeği, ses bozukluklarının değerlendirilmesinde kullanılan bir araçtır.
                    Disfoni şiddetini belirlemek, tedavi başarısını ölçmek/belgelemek ve tanıya yardımcı olmak için
                    sıklıkla kullanılır.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                GRBAS kısaltması; Degree (G), Roughness (R), Breathyness (B), Asthenia (A) ve Strain (S)
                olmak üzere beş özelliği ifade eder.
                </p>
                <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
                Bu parametreler, 0 (normalden sapma yok) ile 3 (belirgin/şiddetli sapma) arasında puanlanır.
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Parametre Kayıtları"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Ayarlar"

    else:
        return "Bilinmeyen Değer!"


def label_text_3(menu):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "home":
        text = """            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Beş temel parametreye ek olarak bu yazılım, Kararsızlık (I) ve Akıcılık (F) özellikleri için de
              açıklamalar ve ses materyali sunar.
            </p>
            <p>Bu ikisi, orijinal ölçeği IF-GRBAS’a genişletir; özellikle spazmodik disfoni gibi durumlarda
            değerlendirme bağlamında faydalıdır.
            <p>
            <p style="text-align: justify; line-height: 1.2; font-family: Arial;">
              Bu ölçek genişletmesinin gerekçesi için aşağıdaki çalışmaya bak:
              <a href="https://osf.io/dxc2e/?view_only=7e25f2b0991a4322997dd4ce99858262"
                 style="text-decoration:none; color:#1a73e8;">
                 Voice Quality and Dysphonia (OSF projesi - yalnızca görüntüleme)
              </a>
            </p>"""

        return text

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Parametre Kayıtları"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Ayarlar"

    else:
        return "Bilinmeyen Değer!"


def label_text_4(menu, var_1=0):

    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        if var_1 == 1:
            text = "Giriş (1/3)"
        elif var_1 == 2:
            text = "Giriş (2/3)"
        elif var_1 == 3:
            text = "Giriş (3/3)"
        else:
            text = "N/V"

        return text

    elif menu.lower() == "description":
        if var_1 == 1:
            text = "Giriş (1/9)"
        elif var_1 == 2:
            text = "Kararsızlık (2/9)"
        elif var_1 == 3:
            text = "Akıcılık (3/9)"
        elif var_1 == 4:
            text = "Genişletme (4/9)"
        elif var_1 == 5:
            text = "Derece (5/9)"
        elif var_1 == 6:
            text = "Pürüzlülük (6/9)"
        elif var_1 == 7:
            text = "Nefeslilik (7/9)"
        elif var_1 == 8:
            text = "Asteni (8/9)"
        elif var_1 == 9:
            text = "Gerginlik (9/9)"
        else:
            text = "N/V"
        return text

    elif menu.lower() == "recordings":
        return "Filtre Seçimi"

    elif menu.lower() == "training":
        return "Yakında:"

    elif menu.lower() == "settings":
        return "Ayarlar"

    else:
        return "Bilinmeyen Değer!"


def label_text_5(menu):
    if menu.lower() == "info":
        return "Sürüm Bilgisi"

    elif menu.lower() == "copyright":
        text = """                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                  Telif © MrNemesis98, GitHub, 2025
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                Bu yazılım MIT Lisansı ile yayımlanmıştır. Yazılımın bir kopyasını edinen herkese, yazılımı kullanma,
                kopyalama, değiştirme, birleştirme, yayımlama, dağıtma, alt lisanslama ve satma izni ücretsiz olarak verilir.
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                  Telif bildirimi ve bu izin metni, yazılımın tüm kopyalarına veya önemli bölümlerine eklenmelidir.
                  Yazılım “olduğu gibi” sağlanır; açık veya zımni hiçbir garanti verilmez. Yazar(lar) ve hak sahipleri,
                  yazılımın kullanımından doğabilecek zararlardan sorumlu değildir.
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial; color: #DB8004;">
                  GRBAS_Mate’i veya bileşenlerini kullanarak bu koşulları kabul etmiş olursun.
                </p>
                <p style="text-align: justify; line-height: 1.5; font-family: Arial;">
                İpucu: Ayarlar menüsündeki telif seçeneklerine göz at!
                </p>
                """
        return text

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        text = """                <p style="text-align: justify; line-height: 1.2; font-family: Arial; color: #DB8004;">
                    Not: Bu yazılımı kullanmadan önce telif beyanını incele (sağ üstteki ilk menü).
                </p>
                """
        return text

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Filtrelenmiş Ses Dosyaları"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        text = """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 22px; color: #8B0000;">
                    Not: Tüm değişikliklerin uygulanması için uygulama yeniden başlatılmalıdır.
                </p>"""
        return text

    else:
        return "Bilinmeyen Değer!"


def label_text_6(menu, var=0):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Medya Oynatıcı"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFF;">
                        GRBAS_Mate Görünümünü Belirle
                    </p>"""
        elif var == 2:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                            GRBAS_Mate İçinde Telif Bildirimleri
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 30px; color: #FFFFFF;">
                                                Medya Oynatıcı Davranışı
                      </p>"""

    else:
        return "Bilinmeyen Değer!"


def label_text_7(menu):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Parametre"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Renk Teması:
                            </p>"""

    else:
        return "Bilinmeyen Değer!"


def label_text_8(menu, var=0):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Şiddet"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        if var == 1:
            return """<p style="text-align: left; qproperty-alignment: AlignVCenter; line-height: 1.2; 
            font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Dil:
                      </p>"""
        elif var == 3:
            return """<p style="text-align: center; line-height: 1.2; font-family: Robo; font-size: 25px; color: #FFFFFF;">
                                Ses İşleme Kalitesi:
                      </p>"""

    else:
        return "Bilinmeyen Değer!"


def label_text_9(menu):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Konuşmacı Cinsiyeti"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Ayarlar"

    else:
        return "Bilinmeyen Değer!"


def label_text_10(menu):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Artikülasyon Türü"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Ayarlar"

    else:
        return "Bilinmeyen Değer!"

def label_text_11(menu):
    if menu.lower() == "info":
        return "Bilgi Merkezi"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Kayıtlar"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Ayarlar"

    else:
        return "Bilinmeyen Değer!"


# Textual input for buttons --------------------------------------------------------------------------------------------

def button_assistance_1(menu):
    if menu.lower() == "info":
        return "Sürüm Açıklaması"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Parametre Kayıtları"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Genel / Arayüz"

    else:
        return "Bilinmeyen Değer!"


def button_assistance_2(menu):
    if menu.lower() == "info":
        return "Gelecek Planı"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Parametre Kayıtları"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Telif Options"

    else:
        return "Bilinmeyen Değer!"


def button_assistance_3(menu):
    if menu.lower() == "info":
        return "Telif Statement"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Parametre Kayıtları"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Medya Oynatıcı"

    else:
        return "Bilinmeyen Değer!"


def button_assistance_4(menu):
    if menu.lower() == "info":
        return "Telif Statement"

    elif menu.lower() == "copyright":
        return "Telif"

    elif menu.lower() == "faq":
        return "Kullanım Kılavuzu"

    elif menu.lower() == "home":
        return "Ana Sayfa"

    elif menu.lower() == "description":
        return "Parametre Açıklamaları"

    elif menu.lower() == "recordings":
        return "Parametre Kayıtları"

    elif menu.lower() == "training":
        return "Eğitim Modu"

    elif menu.lower() == "settings":
        return "Şimdi Yeniden Başlat"

    else:
        return "Bilinmeyen Değer!"


def QComboBox_parameter_filter():
    return ["(I) Kararsızlık", "(F) Akıcılık", "(G) Derece", "(R) Pürüzlülük",
            "(B) Nefeslilik", "(A) Asteni", "(S) Gerginlik", "Tümü"]


def QComboBox_severity_filter():
    return ["Düzey 0", "Düzey 1", "Düzey 2", "Düzey 3", "Artan 0-3", "Tümü"]


def QComboBox_gender_filter():
    return ["Erkek", "Kadın", "Tümü"]


def QComboBox_articulation_filter():
    return ["Ünlü", "Cümle", "Tek dosyada ikisi", "Tümü"]


def QComboBox_colour_choice():
    return ["Açık", "Koyu"]


def QComboBox_language_choice():
    return ["English", "Deutsch", "Italiano", "Español", "Français", "Polski", "Türkçe"]


def QCheckbox_copyright_home():
    return "   Show Telif Notice in Ana Sayfa Menu"


def QCheckbox_copyright_headline():
    return "   Show Telif Notice in Main Headline"


def QCheckbox_remember_faf():
    return "   Filtreli dosyaları hatırla"


def QCheckbox_remember_mps():
    return "   Oynatıcı ayarlarını hatırla"


def QCheckbox_autoplay_recordings():
    return "   Play Kayıtlar Automatically after Loading"


def QComboBox_audio_render_quality_choice():
    return ["Debug:\t\t1 FPS",
            "Eco:\t\t10 FPS",
            "Normal:\t33 FPS",
            "High:\t\t60 FPS",
            "Ultra:\t\t100 FPS"]
