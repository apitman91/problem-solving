def p1(n):
    """Sums all multiples of 3 and 5 less than n"""
    set = [i for i in range(1, n) if i % 3 == 0 or i% 5 ==0]
    return sum(set)

print(p1(1000))