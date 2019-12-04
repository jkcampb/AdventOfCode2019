def main():
    filename = './input.txt'

    with open(filename, "r") as fh:
        line_code = [int(x) for x in fh.read().split(',')]

    line_code[1] = 12
    line_code[2] = 2

    pos = 0
    while pos != -1:
        line_code, pos = process_optcode(line_code, pos)

    print(line_code[0])


def process_optcode(optcode, pos):
    new_pos = -1

    if optcode[pos] == 1:
        optcode[optcode[pos+3]] = optcode[optcode[pos+1]] + \
            optcode[optcode[pos+2]]
        new_pos = pos + 4
    elif optcode[pos] == 2:
        optcode[optcode[pos+3]] = optcode[optcode[pos+1]] * \
            optcode[optcode[pos+2]]
        new_pos = pos + 4
    elif optcode[pos] == 99:
        print("Hit 99")
    else:
        print("Bad optcode")

    return optcode, new_pos


if __name__ == '__main__':
    assert process_optcode([1, 0, 0, 0, 99], 0)[0] == [2, 0, 0, 0, 99]
    assert process_optcode([2, 3, 0, 3, 99], 0)[0] == [2, 3, 0, 6, 99]
    assert process_optcode([1, 1, 1, 4, 99, 5, 6, 0, 99], 0)[0] == \
        [1, 1, 1, 4, 2, 5, 6, 0, 99]
    assert process_optcode([1, 1, 1, 4, 2, 5, 6, 0, 99], 4)[0] == \
        [30, 1, 1, 4, 2, 5, 6, 0, 99]

    main()
