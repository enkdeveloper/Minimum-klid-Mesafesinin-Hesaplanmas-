import math

n = int(input("Lütfen 2 nokta gireceğinizi belirtiniz"))

points = []

for i in range(n):
    x, y = map(float, input("{}. noktanın x ve y koordinatlarını aralarında boşluk bırakarak girin: ".format(i + 1)).split())
    points.append((x, y))

def euclideanDistance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return math.sqrt(abs((x2 - x1) ** 2) + abs((y2 - y1) ** 2))

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

if distances:
    min_distance = min(distances)
    print("Minimum Mesafe:", min_distance)
else:
    print("Lütfen 2 nokta giriniz.")
