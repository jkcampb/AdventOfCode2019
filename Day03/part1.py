import numpy as np


def main():
    filename = './input.txt'

    fh = open(filename, "r")

    wires = []
    for line in fh:
        wires.append(line.rstrip('\n').split(','))

    x_min, x_max, y_min, y_max = find_size(wires)

    grid = np.zeros([x_max - x_min + 1, y_max - y_min + 1])

    for wire in wires:
        grid += make_wire_grid(wire, x_min, x_max, y_min, y_max)

    cross_points = [[x[0] + x_min, x[1] + y_min]
                    for x in np.argwhere(grid == 2)]
    cross_points = [x for x in cross_points if x != [0, 0]]

    print("Part1:")
    print(min([abs(x[0]) + abs(x[1])
               for x in cross_points]))

    cross_distances = []
    for cross_point in cross_points:
        total_dist = 0
        for wire in wires:
            total_dist += dist_to_cross(wire, cross_point)

        cross_distances.append(total_dist)

    print("Part2:")
    print(min(cross_distances))


def dist_to_cross(wire, cross_point):
    x_pos, y_pos = 0, 0

    total_steps = 0

    for order in wire:
        direction = order[0]
        steps = int(order[1:])

        if direction == "U":
            if cross_point[0] == x_pos:
                if y_pos < cross_point[1] <= y_pos + steps:
                    return total_steps + abs(cross_point[1] - y_pos)
            y_pos += steps
            total_steps += steps
        elif direction == "D":
            if cross_point[0] == x_pos:
                if y_pos - steps <= cross_point[1] < y_pos:
                    return total_steps + abs(cross_point[1] - y_pos)
            y_pos -= steps
            total_steps += steps
        elif direction == "R":
            if cross_point[1] == y_pos:
                if x_pos < cross_point[0] <= x_pos + steps:
                    return total_steps + abs(cross_point[0] - x_pos)

            x_pos += steps
            total_steps += steps
        elif direction == "L":
            if cross_point[1] == y_pos:
                if x_pos - steps <= cross_point[0] < x_pos:
                    return total_steps + abs(cross_point[0] - x_pos)

            x_pos -= steps
            total_steps += steps

    print("No cross found")


def make_wire_grid(wire, x_min, x_max, y_min, y_max):

    grid = np.zeros([x_max - x_min + 1, y_max - y_min + 1])

    x_pos = -1*x_min
    y_pos = -1*y_min

    for order in wire:
        direction = order[0]
        steps = int(order[1:])

        if direction == "U":
            grid[x_pos, y_pos:y_pos+steps] = 1
            y_pos += steps
        elif direction == "D":
            grid[x_pos, y_pos-steps:y_pos] = 1
            y_pos -= steps
        elif direction == "R":
            grid[x_pos:x_pos+steps, y_pos] = 1
            x_pos += steps
        elif direction == "L":
            grid[x_pos-steps:x_pos, y_pos] = 1
            x_pos -= steps

    return grid


def find_size(wires):
    x_min, x_max, y_min, y_max = 0, 0, 0, 0

    for wire in wires:
        x_pos, y_pos = 0, 0
        for order in wire:
            direction = order[0]
            steps = int(order[1:])

            if direction == "U":
                y_pos += steps
                y_max = max(y_pos, y_max)
            elif direction == "D":
                y_pos -= steps
                y_min = min(y_pos, y_min)
            elif direction == "R":
                x_pos += steps
                x_max = max(x_pos, x_max)
            elif direction == "L":
                x_pos -= steps
                x_min = min(x_pos, x_min)

    return x_min, x_max, y_min, y_max


if __name__ == '__main__':
    assert (dist_to_cross(['R8', 'U5', 'L5', 'D3'], [6, 5]) == 15)
    assert (dist_to_cross(['U7', 'R6', 'D4', 'L4'], [6, 5]) == 15)
    assert (dist_to_cross(['R8', 'U5', 'L5', 'D3'], [3, 3]) == 20)
    assert (dist_to_cross(['U7', 'R6', 'D4', 'L4'], [3, 3]) == 20)

    main()
