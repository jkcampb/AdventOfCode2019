def main():
    filename = './input.txt'

    input_num = 5

    with open(filename, "r") as fh:
        line_code = [int(x) for x in fh.read().split(',')]

    print("Part 1:")
    process_input(line_code.copy(), 1)
    print("Part 2:")
    process_input(line_code.copy(), 5)


def process_input(line_code, input):
    pos = 0
    while pos != -1:
        line_code, pos, output_num = process_optcode(line_code, pos, input)
        if output_num is not None:
            print(f"output: {output_num}")


def process_optcode(optcode, pos, input):
    new_pos = -1
    output = None

    full_instr = full_code(optcode[pos])

    if full_instr[3:] == "03":
        optcode[optcode[pos+1]] = input
        new_pos = pos + 2
    elif full_instr[3:] == "04":
        output = optcode[optcode[pos+1]]
        new_pos = pos + 2
    elif full_instr[3:] == "99":
        print("Hit 99")
    else:
        if full_instr[2] == "0":
            x_param = optcode[optcode[pos+1]]
        else:
            x_param = optcode[pos+1]
        if full_instr[1] == "0":
            y_param = optcode[optcode[pos+2]]
        else:
            y_param = optcode[pos+2]

        if int(full_instr[4]) == 1:
            optcode[optcode[pos+3]] = x_param + y_param
            new_pos = pos + 4
        elif int(full_instr[4]) == 2:
            optcode[optcode[pos+3]] = x_param * y_param
            new_pos = pos + 4
        elif int(full_instr[4]) == 7:
            optcode[optcode[pos+3]] = int(x_param < y_param)
            new_pos = pos + 4
        elif int(full_instr[4]) == 8:
            optcode[optcode[pos+3]] = int(x_param == y_param)
            new_pos = pos + 4
        elif int(full_instr[4]) == 5:
            if x_param != 0:
                new_pos = y_param
            else:
                new_pos = pos + 3
        elif int(full_instr[4]) == 6:
            if x_param == 0:
                new_pos = y_param
            else:
                new_pos = pos + 3
        else:
            print(f"Bad optcode at {pos}")
            print(optcode)

    return optcode, new_pos, output


def full_code(x):
    return f"{x:05d}"


if __name__ == '__main__':
    test1 = [1002, 4, 3, 4, 33]
    assert(process_optcode(test1, 0, 1)[0] == [1002, 4, 3, 4, 99])
    test2 = [3, 2, -1]
    assert(process_optcode(test2, 0, 100)[0] == [3, 2, 100])

    main()
