from itertools import chain, permutations
from typing import Final, List
from sys import argv

Colors = List[List[str]]

POSSIBLE_COLORS: Final[str] = "bgrw"

def split_input(input_: List[str]) -> Colors:
    splitted = {"".join(sorted(i)) for i in (k.lower() for k in input_) if len(i) > 1 and len(i) < 7 and all(False for j in i if j not in POSSIBLE_COLORS)}
    return list(splitted)


def color_combiations(colors: Colors) -> str:
    if not colors:
        return ""

    combinations = [set(permutations(i, len(i))) for i in colors]
    print(combinations)
    string_from_combinations = "|".join(["-".join(i) for i in chain.from_iterable(combinations)])
    return string_from_combinations


if __name__ == "__main__":
    input_ = argv[1:]
    if input_:
        splitted_strings = split_input(input_)
        print(color_combiations(splitted_strings))
