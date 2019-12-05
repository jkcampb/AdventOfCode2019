def main():

    part1_count = 0

    for x in range(136760, 595730+1):
        if double_check(x) & monotonic_check(x):
            part1_count += 1

    print(f"Part1: {part1_count}")

    part2_count = 0

    for x in range(136760, 595730+1):
        if exactly_two_check(x) & monotonic_check(x):
            part2_count += 1
    print(f"Part2: {part2_count}")


def double_check(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if num_str[i] == num_str[i+1]:
            return True

    return False


def exactly_two_check(num):
    num_str = str(num)
    prev_c = ''
    dupe_count = 1
    for c in num_str:
        if prev_c == c:
            dupe_count += 1
        else:
            if dupe_count == 2:
                return True
            dupe_count = 1

        prev_c = c

    if dupe_count == 2:
        return True
    else:
        return False


def monotonic_check(num):
    num_str = str(num)
    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i+1]:
            return False

    return True


if __name__ == "__main__":
    assert(exactly_two_check(111122))
    assert(not exactly_two_check(123444))

    main()
