def get_values(values):
    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            for k in range(len(values)- j - 1):
                if values[i] + values[j] + values[k] == 2020:
                    return values[i], values[j], values[k]


with open('problem1data.txt') as f:
    values = [int(val) for val in f.read().splitlines()]
    a, b, c = get_values(values)
    print(a * b * c)
