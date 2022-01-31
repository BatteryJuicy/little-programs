from math import sqrt

pi = 0
a = 1
times = 0
times_cap = 1000
count = 0

while count < 100000:
    pi += 1/(a**2)
    a += 1
    times += 1
    if times >= times_cap:
        print(sqrt(pi * 6))
        times = 0
    count += 1
    if count == 99999:
        input("press any key to continue: ")
        count = 0


"""
Geometry method. (it follows a diagonal and not a curve so it has a big diviation)

pi = 0
R = 10
diatomi = 0.00000001
new_diatomi = diatomi


pi += (4 * R**2 - 4 * new_diatomi * (R - new_diatomi)) / R**2
new_diatomi += diatomi
print(pi)
"""
