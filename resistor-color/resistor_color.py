from typing import List

def color_code(color: str) -> int:
    return colors().index(color)


def colors() -> List:
    return ["black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white"]
