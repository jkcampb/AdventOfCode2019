def main():
    # Part 1 test
    test1_orbits = build_tree('./test1.txt')

    test1_total_num = find_indirect(test1_orbits) + find_direct(test1_orbits)

    assert(test1_total_num == 42)

    # Part 1 solution
    orbits = build_tree('./input.txt')
    total_num = find_indirect(orbits) + find_direct(orbits)

    print(f"Part 1 answer: {total_num}")

    # Part 2 test
    test2_orbits = build_tree('./test2.txt')
    test2_you_parents = orbit_list(test2_orbits, "YOU")
    test2_san_parents = orbit_list(test2_orbits, "SAN")

    assert(transfer_len(test2_you_parents, test2_san_parents, "D") == 4)

    # Part 2 solution
    you_parents = orbit_list(orbits, "YOU")
    san_parents = orbit_list(orbits, "SAN")
    intersections = list(set(you_parents) & set(san_parents))

    transfers = []
    for intersection in intersections:
        transfers.append(transfer_len(you_parents, san_parents, intersection))

    min_transfers = min(transfers)
    print(f"Part 2 answer: {min_transfers}")


def build_tree(filename):

    orbits = {}
    with open(filename, "r") as fh:
        for line in fh:
            orbit = {}
            orbit_parts = line.rstrip('\n').split(')')
            orbits[orbit_parts[1]] = orbit_parts[0]
    return orbits


def find_indirect(orbits):
    total_indirect = 0
    for body in orbits.keys():
        parent = orbits[body]
        while parent != "COM":
            parent = orbits[parent]
            total_indirect += 1

    return total_indirect


def orbit_list(orbits, start):
    transfer_list = []
    orbit = start
    while orbit != "COM":
        orbit = orbits[orbit]
        transfer_list.append(orbit)

    return transfer_list


def transfer_len(list1, list2, inter):
    return list1.index(inter) + list2.index(inter)


def find_direct(orbits):
    return len(set(orbits.keys()))


if __name__ == "__main__":
    main()
