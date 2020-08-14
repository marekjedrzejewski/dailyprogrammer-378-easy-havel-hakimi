def front_elimination(number, sequence):
    s = sequence[:]
    for i in range(number):
        s[i] -= 1
    return s
