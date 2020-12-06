with open('map.txt') as file:
    map = []
    for line_num, line in enumerate(file):
        new_array = []
        for index, character in enumerate(line):
            if character == "\n":
                break
            new_array.append(character == "#")
        map.append(new_array)
    width = len(map[0])
    print(f"height: {len(map)}, width:{width}")

    def lookup(x, y):
        if y >= len(map):
            return None
        print(f"{x} % {width}")
        print(f"({x}[{x % width}],{y},{map[y][x % width]})")
        return map[y][x % width]

    def find_end(x, y, slope_x, slope_y, tree_count):
        x += slope_x
        y += slope_y
        result = lookup(x, y)
        if result is None:
            return tree_count
        if result:
            tree_count += 1
            print(f"Tree Count: {tree_count}")
        return find_end(x, y, slope_x, slope_y, tree_count)


    a = find_end(0, 0, 1, 1, 0)
    b = find_end(0, 0, 3, 1, 0)
    c = find_end(0, 0, 5, 1, 0)
    d = find_end(0, 0, 7, 1, 0)
    e = find_end(0, 0, 1, 2, 0)

    print(f"{a}*{b}*{c}*{d}*{e} = {a*b*c*d*e}")