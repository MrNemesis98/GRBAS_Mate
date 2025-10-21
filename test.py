from fractions import Fraction

from wuggy import WuggyGenerator


g = WuggyGenerator()
g.load("orthographic_english")
for match in g.generate_classic(
    ["Klo", "Bürste"],
    ncandidates_per_sequence=30, max_search_time_per_sequence=2):
    print(match["pseudoword"])



