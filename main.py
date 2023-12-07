# classification of the data using the KNN algorithm
# Jakub Belis 120755
# Fiit STU BA
from enum import Enum
import math
import random
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt1
import matplotlib.pyplot as plt3
import matplotlib.pyplot as plt7
import matplotlib.pyplot as plt15
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
    color1 = Color
    color3 = Color
    color7 = Color
    color15 = Color
    generatedcolor = Color
    distance = int
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.distance = 0
    def classify(self, points):
        neighbours = getNearestNeighbours(15, self, points)
        neighbours.sort(key=lambda x: x.distance)
        self.color15 = getMostFrequentColor15(neighbours)
        neighbours = neighbours[:7]
        self.color7 = getMostFrequentColor7(neighbours)
        neighbours = neighbours[:3]
        self.color3 = getMostFrequentColor3(neighbours)
        neighbours = neighbours[:1]
        self.color1 = neighbours[0].color1

def distance(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def getNearestNeighbours(k, point, points):
    for p in points:
        p.distance = distance(point, p)
    
    nparray = np.empty(len(points))
    for i in range(len(points)):
        nparray[i] = points[i].distance
    indexes = nparray.argsort()[:k]
    neighbours = []
    for i in indexes:
        neighbours.append(points[i])
    return neighbours
    

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
    
def getMostFrequentColor1(neighbours):
    red = 0
    blue = 0
    green = 0
    purple = 0
    for n in neighbours:
        if n.color1 == Color.RED:
            red += 1
        elif n.color1 == Color.BLUE:
            blue += 1
        elif n.color1 == Color.GREEN:
            green += 1
        elif n.color1 == Color.PURPLE:
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
    
def getMostFrequentColor3(neighbours):
    red = 0
    blue = 0
    green = 0
    purple = 0
    for n in neighbours:
        if n.color3 == Color.RED:
            red += 1
        elif n.color3 == Color.BLUE:
            blue += 1
        elif n.color3 == Color.GREEN:
            green += 1
        elif n.color3 == Color.PURPLE:
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
    
def getMostFrequentColor7(neighbours):
    red = 0
    blue = 0
    green = 0
    purple = 0
    for n in neighbours:
        if n.color7 == Color.RED:
            red += 1
        elif n.color7 == Color.BLUE:
            blue += 1
        elif n.color7 == Color.GREEN:
            green += 1
        elif n.color7 == Color.PURPLE:
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
    
def getMostFrequentColor15(neighbours):
    red = 0
    blue = 0
    green = 0
    purple = 0
    for n in neighbours:
        if n.color15 == Color.RED:
            red += 1
        elif n.color15 == Color.BLUE:
            blue += 1
        elif n.color15 == Color.GREEN:
            green += 1
        elif n.color15 == Color.PURPLE:
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
    
    for p in points:
        p.color1 = p.color
        p.color3 = p.color
        p.color7 = p.color
        p.color15 = p.color
    
    return points


def main():
    start_time = time.time()
    
    points = initialpoints()
    # k = 7
    for i in range(10000):
        if random.randint(0, 100) < 1:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            x = random.randint(-5000, 500)
            y = random.randint(-5000, 500)
        newpoint = point(x, y, Color.RED)
        newpoint.generatedcolor = Color.RED
        # neighbours = getNearestNeighbours(k, newpoint, points)
        # newpoint.color = getMostFrequentColor(neighbours)
        newpoint.classify(points)
        points.append(newpoint)
        
        if random.randint(0, 100) < 1:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            x = random.randint(-500,5000)
            y = random.randint(-5000, 500)
        newpoint = point(x, y, Color.GREEN)
        newpoint.generatedcolor = Color.GREEN
        newpoint.classify(points)
        points.append(newpoint)
        
        if random.randint(0, 100) < 1:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            x = random.randint(-5000, 500)
            y = random.randint(-500,5000)
        newpoint = point(x, y, Color.BLUE)
        newpoint.generatedcolor = Color.BLUE
        # neighbours = getNearestNeighbours(k, newpoint, points)
        # newpoint.color = getMostFrequentColor(neighbours)
        newpoint.classify(points)
        points.append(newpoint)
        
        if random.randint(0, 100) < 1:
            x = random.randint(-5000, 5000)
            y = random.randint(-5000, 5000)
        else:
            x = random.randint(-500,5000)
            y = random.randint(-500,5000)
        newpoint = point(x, y, Color.PURPLE)
        newpoint.generatedcolor = Color.PURPLE
        # neighbours = getNearestNeighbours(k, newpoint, points)
        # newpoint.color = getMostFrequentColor(neighbours)
        newpoint.classify(points)
        points.append(newpoint)
        if i % 1000 == 0:
            print(i)
            print("--- %s seconds ---" % (time.time() - start_time))
    
    end_time = time.time()
    print("Time elapsed: ", end_time - start_time)
        
    # for p in points:
    #     if p.color == Color.BLUE:
    #         plt.plot(p.x, p.y, 'bo')
    #     elif p.color == Color.RED:
    #         plt.plot(p.x, p.y, 'ro')
    #     elif p.color == Color.GREEN:
    #         plt.plot(p.x, p.y, 'go')
    #     elif p.color == Color.PURPLE:
    #         plt.plot(p.x, p.y, 'mo')
    #     elif p.color == Color.YELLOW:
    #         plt.plot(p.x, p.y, 'yo')
    # plt.show()
    
    for p in points:
        if p.color1 == Color.BLUE:
            plt1.plot(p.x, p.y, 'bo')
        elif p.color1 == Color.RED:
            plt1.plot(p.x, p.y, 'ro')
        elif p.color1 == Color.GREEN:
            plt1.plot(p.x, p.y, 'go')
        elif p.color1 == Color.PURPLE:
            plt1.plot(p.x, p.y, 'mo')
        elif p.color1 == Color.YELLOW:
            plt1.plot(p.x, p.y, 'yo')
    # plt1.show()
    plt1.savefig(f"plt1.png")
    
    for p in points:
        if p.color3 == Color.BLUE:
            plt3.plot(p.x, p.y, 'bo')
        elif p.color3 == Color.RED:
            plt3.plot(p.x, p.y, 'ro')
        elif p.color3 == Color.GREEN:
            plt3.plot(p.x, p.y, 'go')
        elif p.color3 == Color.PURPLE:
            plt3.plot(p.x, p.y, 'mo')
        elif p.color3 == Color.YELLOW:
            plt3.plot(p.x, p.y, 'yo')
    # plt3.show()
    plt3.savefig(f"plt3.png")
    
    for p in points:
        if p.color7 == Color.BLUE:
            plt7.plot(p.x, p.y, 'bo')
        elif p.color7 == Color.RED:
            plt7.plot(p.x, p.y, 'ro')
        elif p.color7 == Color.GREEN:
            plt7.plot(p.x, p.y, 'go')
        elif p.color7 == Color.PURPLE:
            plt7.plot(p.x, p.y, 'mo')
        elif p.color7 == Color.YELLOW:
            plt7.plot(p.x, p.y, 'yo')
    # plt7.show()
    plt7.savefig(f"plt7.png")
    
    for p in points:
        if p.color15 == Color.BLUE:
            plt15.plot(p.x, p.y, 'bo')
        elif p.color15 == Color.RED:
            plt15.plot(p.x, p.y, 'ro')
        elif p.color15 == Color.GREEN:
            plt15.plot(p.x, p.y, 'go')
        elif p.color15 == Color.PURPLE:
            plt15.plot(p.x, p.y, 'mo')
        elif p.color15 == Color.YELLOW:
            plt15.plot(p.x, p.y, 'yo')
    # plt15.show()
    plt15.savefig(f"plt15.png")
    
    
    z = 0
    for p in points:
        if p.generatedcolor == p.color1:
            z += 1
    print("Accuracy for k=1: ", z/len(points)*100, "%")
    z = 0
    for p in points:
        if p.generatedcolor == p.color3:
            z += 1
    print("Accuracy for k=3: ", z/len(points)*100, "%")
    z = 0
    for p in points:
        if p.generatedcolor == p.color7:
            z += 1
    print("Accuracy for k=7: ", z/len(points)*100, "%")
    z = 0
    for p in points:
        if p.generatedcolor == p.color15:
            z += 1
    print("Accuracy for k=15: ", z/len(points)*100, "%")
            
    
main()

    

    