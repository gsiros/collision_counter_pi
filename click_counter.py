import time

d = int(input("How many digits of pi would you like to calculate? "))

def countClicksOfCol(n):

    start = time.time()
    m1 = 100 ** (n - 1)
    m2 = 1
    u1 = 100
    u2 = 0
    counter = 0

    while True:

        counter += 1

        #Here I used the elastic collision formulas.
        nu1 = (((m1 - m2) / (m1 + m2)) * (u1)) + (((2 * m2) / (m1 + m2)) * (u2))
        nu2 = (((2 * m1) / (m1 + m2)) * (u1)) + (((m2 - m1) / (m1 + m2)) * (u2))

        if nu2 > 0:
            counter += 1

            u2 = -nu2
            u1 = nu1
        elif nu2 < 0:
            u2 = nu2
            u1 = nu1

        if u1 < u2 and u1 <= 0 and u2 <= 0:
            break
    end = time.time()

    print(counter)
    print("(Runtime: {:1.5f}s)".format(end-start))

countClicksOfCol(d)
