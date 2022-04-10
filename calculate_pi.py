from random import randint as ri

accuracy = 1000
accuracy_squared = accuracy**2
def generate_points():
    x = ri(0, accuracy)
    y = ri(0,accuracy)
    return (x, y)

def points_ration(point):
    if int(point[0])**2 + int(point[1])**2 <= accuracy_squared: #checking if the point is in the circle with radius 1
        return True
    return False

points_in_circle = 0
points = 0

for i in range(0, accuracy_squared):
    point = generate_points()
    points_in_circle += int(points_ration(point))
    points += 1

pi = 4*(points_in_circle/points)
print(pi)