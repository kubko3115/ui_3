# classification of the data using the KNN algorithm
# Jakub Belis 120755
# Fiit STU BA
from enum import Enum
import math
import random
import matplotlib.pyplot as plt
import time
import numpy as np
class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3
    PURPLE = 4
    YELLOW = 5
    

class point:
    x = int
    y = int
    color = Color
    generatedcolor = Color
    distance = float
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.distance = 0

def distance(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def getNearestNeighbours(k, point, points):
    for p in points:
        p.distance = distance(point, p)
        
    # newpoints = np.argpartition(points, k, lambda x: x.distance)
    # return newpoints[:k]
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
    start_time = time.time()
    
    points = initialpoints()
    k = 7
    for i in range(10000):
        if random.randint(0, 100) < 1:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            x = random.randint(-5000, 500)
            y = random.randint(-5000, 500)
        newpoint = point(x, y, Color.RED)
        neighbours = getNearestNeighbours(k, newpoint, points)
        newpoint.generatedcolor = Color.RED
        newpoint.color = getMostFrequentColor(neighbours)
        # print(newpoint.color)
        points.append(newpoint)
        
        if random.randint(0, 100) < 1:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            x = random.randint(-500,5000)
            y = random.randint(-5000, 500)
        newpoint = point(x, y, Color.GREEN)
        neighbours = getNearestNeighbours(k, newpoint, points)
        newpoint.generatedcolor = Color.GREEN
        newpoint.color = getMostFrequentColor(neighbours)
        # print(newpoint.color)
        points.append(newpoint)
        
        if random.randint(0, 100) < 1:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            x = random.randint(-5000, 500)
            y = random.randint(-500,5000)
        newpoint = point(x, y, Color.BLUE)
        neighbours = getNearestNeighbours(k, newpoint, points)
        newpoint.generatedcolor = Color.BLUE
        newpoint.color = getMostFrequentColor(neighbours)
        # print(newpoint.color)
        points.append(newpoint)
        
        if random.randint(0, 100) < 1:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            x = random.randint(-500,5000)
            y = random.randint(-500,5000)
        newpoint = point(x, y, Color.PURPLE)
        neighbours = getNearestNeighbours(k, newpoint, points)
        newpoint.generatedcolor = Color.PURPLE
        newpoint.color = getMostFrequentColor(neighbours)
        # print(newpoint.color)
        points.append(newpoint)
        if i % 1000 == 0:
            print(i)
            print("--- %s seconds ---" % (time.time() - start_time))
    
    end_time = time.time()
    print("Time elapsed: ", end_time - start_time)
        
    for p in points:
        if p.color == Color.BLUE:
            plt.plot(p.x, p.y, 'bo')
        elif p.color == Color.RED:
            plt.plot(p.x, p.y, 'ro')
        elif p.color == Color.GREEN:
            plt.plot(p.x, p.y, 'go')
        elif p.color == Color.PURPLE:
            plt.plot(p.x, p.y, 'mo')
        elif p.color == Color.YELLOW:
            plt.plot(p.x, p.y, 'yo')
    plt.show()
    
    z = 0
    for p in points:
        if p.generatedcolor == p.color:
            z += 1
    print("Accuracy: ", z/len(points)*100, "%")
            
    
main()
    

    