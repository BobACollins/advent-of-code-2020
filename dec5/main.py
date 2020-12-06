with open('input.txt') as file:
    seats = {
        int(
            line.translate(
                str.maketrans({'R': "1", "F": "0", "B": "1", "L": "0", "\n": None})
            ),
            2,
        )
        for line in file
    }
    max_num = max(seats)
    min_num = min(seats)
    print(f"Highest is {max_num}")
    other_seats = set(range(max_num)).difference(seats)
    my_seat = next(seat for seat in other_seats if min_num < seat < max_num)
    print(f"My seat is: {my_seat}")