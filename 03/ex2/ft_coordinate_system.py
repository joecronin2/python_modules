import math


def distance(p1: tuple[int, int, int], p2: tuple[int, int, int]) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coordinates(coord_string: str) -> tuple[int, int, int]:
    print(f'Parsing coordinates: "{coord_string}"')
    try:
        x_str, y_str, z_str = coord_string.split(",")
        position = (int(x_str), int(y_str), int(z_str))
        print(f"Parsed position: {position}")
        return position
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}")
        raise


if __name__ == "__main__":
    origin = (0, 0, 0)
    spawn_point = (10, 20, 5)
    print(f"Position created: {spawn_point}")
    print(
        f"Distance between {origin} and {spawn_point}: "
        f"{round(distance(origin, spawn_point), 2)}"
    )
    parsed_position = parse_coordinates("3,4,0")
    print(
        f"Distance between {origin} and {parsed_position}: "
        f"{distance(origin, parsed_position)}"
    )
    print('Parsing invalid coordinates: "abc,def,ghi"')
    try:
        parse_coordinates("abc,def,ghi")
    except ValueError:
        pass
    print("Unpacking demonstration:")
    x: int
    y: int
    z: int
    x, y, z = parsed_position
    print(f"Player at x={x}, y={y}, z={z}")
    print(
        f"Coordinates: "
        f"X={x}, Y={y}, Z={z}"
    )
