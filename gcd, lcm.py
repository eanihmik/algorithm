def solution(n, m):
    gcd = 1
    a = 1
    while a <= min(n, m):
        if (n % a == 0 and m % a == 0):
            gcd = a
        a += 1

    lcm = n * m
    b = n * m
    while b >= max(n, m):
        if (b % n == 0 and b % m == 0):
            lcm = b
        b -= 1
    answer = [gcd, lcm]
    return answer
