def countdown():
    for i in range(10, 0, -1):
        print(i)


def multiplication_table():
    number = int(input("Please enter a number to show the multiplication table for: "))
    for i in range(1, number + 1):
        print(f"{number} times {i} is {number * i}")

def playlist():
    tracks = ["Track A", "Track B", "Track C"]
    for index, track in enumerate(tracks, start=1):
        print(f"{index}. {track}")

def coordinates():
    x_min = 1
    x_max = 3
    y_min = 1
    y_max = 4

    for x in range(x_min, x_max + 1):
        for y in range(y_min, y_max):
            print(f"({x}, {y})")

def print_grid(width, height):
    cell_spaces = 3
    underscores_per_cell = 3
    corner = '+'
    cell_content = ' '
    horizontal_edge = '-'
    vertical_edge = '|'

    for _ in range(height):
        print((corner + horizontal_edge * underscores_per_cell) * width + corner)
        print((vertical_edge + cell_content * cell_spaces) * width + vertical_edge)
    print((corner + horizontal_edge * underscores_per_cell) * width + corner)



if __name__ == "__main__":
    print_grid(5,5)