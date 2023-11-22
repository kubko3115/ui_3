# classification of the data using the KNN algorithm
# Jakub Belis 120755
# Fiit STU BA
from enum import Enum
import math
import random
import matplotlib.pyplot as plt

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    PURPLE = 4
    

class point:
    x = int
    y = int
    color = Color
    generatedcolor = Color
    distance = float
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.generatedcolor = color
        self.distance = 0

def distance(p1, p2):
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def getNearestNeighbours(k, point, points):
    for p in points:
        p.distance = distance(point, p)
    points.sort(key=lambda x: x.distance)
    return points[:k]

def getMostFrequentColor(neighbours):
    red = 0
    blue = 0
    green = 0
    purple = 0
    for n in neighbours:
        if n.color == Color.RED:
            red += 1
        elif n.color == Color.BLUE:
            blue += 1
        elif n.color == Color.GREEN:
            green += 1
        elif n.color == Color.PURPLE:
            purple += 1
    if red > blue and red > green and red > purple:
        return Color.RED
    elif blue > red and blue > green and blue > purple:
        return Color.BLUE
    elif green > red and green > blue and green > purple:
        return Color.GREEN
    elif purple > red and purple > blue and purple > green:
        return Color.PURPLE
    else:
        return Color.RED
    
def initialpoints():
    points = []
    points.append(point(-4500, -4400, Color.RED))
    points.append(point(-4100, -3000, Color.RED))
    points.append(point(-1800, -2400, Color.RED))
    points.append(point(-2500, -3400, Color.RED))
    points.append(point(-2500, -1400, Color.RED))
    
    points.append(point(4500, -4400, Color.GREEN))
    points.append(point(4100, -3000, Color.GREEN))
    points.append(point(1800, -2400, Color.GREEN))
    points.append(point(2500, -3400, Color.GREEN))
    points.append(point(2500, -1400, Color.GREEN))
    
    points.append(point(-4500, 4400, Color.BLUE))
    points.append(point(-4100, 3000, Color.BLUE))
    points.append(point(-1800, 2400, Color.BLUE))
    points.append(point(-2500, 3400, Color.BLUE))
    points.append(point(-2500, 1400, Color.BLUE))
    
    points.append(point(4500, 4400, Color.PURPLE))
    points.append(point(4100, 3000, Color.PURPLE))
    points.append(point(1800, 2400, Color.PURPLE))
    points.append(point(2500, 3400, Color.PURPLE))
    points.append(point(2500, 1400, Color.PURPLE))
    return points

def main():
    points = initialpoints()
    k = 5
    for i in range(10000):
        x = random.randint(-5000, 500)
        y = random.randint(-5000, 500)
        newpoint = point(x, y, Color.RED)
        neighbours = getNearestNeighbours(k, newpoint, points)
        newpoint.color = getMostFrequentColor(neighbours)
        points.append(newpoint)
        
        x = random.randint(5000, -500)
        y = random.randint(-5000, 500)
        newpoint = point(x, y, Color.GREEN)
        neighbours = getNearestNeighbours(k, newpoint, points)
        newpoint.color = getMostFrequentColor(neighbours)
        points.append(newpoint)
        
        x = random.randint(-5000, 500)
        y = random.randint(5000, -500)
        newpoint = point(x, y, Color.BLUE)
        neighbours = getNearestNeighbours(k, newpoint, points)
        newpoint.color = getMostFrequentColor(neighbours)
        points.append(newpoint)
        
        x = random.randint(5000, -500)
        y = random.randint(5000, -500)
        newpoint = point(x, y, Color.PURPLE)
        neighbours = getNearestNeighbours(k, newpoint, points)
        newpoint.color = getMostFrequentColor(neighbours)
        points.append(newpoint)
        
    for p in points:
        if p.color == Color.RED:
            plt.plot(p.x, p.y, 'ro')
        elif p.color == Color.BLUE:
            plt.plot(p.x, p.y, 'bo')
        elif p.color == Color.GREEN:
            plt.plot(p.x, p.y, 'go')
        elif p.color == Color.PURPLE:
            plt.plot(p.x, p.y, 'mo')
        if p.generatedcolor == Color.RED:
            plt.plot(p.x, p.y, 'r+')
        elif p.generatedcolor == Color.BLUE:
            plt.plot(p.x, p.y, 'b+')
        elif p.generatedcolor == Color.GREEN:
            plt.plot(p.x, p.y, 'g+')
        elif p.generatedcolor == Color.PURPLE:
            plt.plot(p.x, p.y, 'm+')
    plt.show()
    
main()
    

    