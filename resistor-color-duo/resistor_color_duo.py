from typing import List

def value(colors: List) -> int:
    return int(f"{color_code(colors[0])}{color_code(colors[1])}")

def color_code(color: str) -> int:
    return color_list().index(color)

def color_list() -> List:
    return ["black", "brown", "red", "orange", "yellow",
            "green", "blue", "violet", "grey", "white"]
