def main():
    filename = './input.txt'

    fh = open(filename, "r")

    total = 0
    for line in fh:
        fuel = int(line)
        total += reduce_fuel(fuel)

    print(int(total))


def reduce_fuel(x):
    add = int(float(x)/3) - 2

    if add > 0:
        return add + reduce_fuel(add)
    else:
        return 0


if __name__ == '__main__':
    assert (reduce_fuel(1969) == 966)
    assert (reduce_fuel(100756) == 50346)

    main()
