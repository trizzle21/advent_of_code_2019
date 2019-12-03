"""
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
"""
import logging
from collections import namedtuple

logging.basicConfig(level=logging.DEBUG)

Point = namedtuple('Point', ['x', 'y'])
FILENAME_TEST = 'day_3_test.txt'
FILENAME_REAL = 'day_3_input.txt'

directions = {
    'U': Point(0, 1),
    'D': Point(0, -1),
    'L': Point(-1, 0),
    'R': Point(1, 0) 
}


def _get_vectors():
    with open(FILENAME_REAL) as f:
        inputs = f.readlines()
    inputs[0] = inputs[0][:-1]
    return [inputs[0].split(','), inputs[1].split(',')]


def manhattan_distance(point_a, point_b):
    return abs(point_a.x - point_b.x) + abs(point_a.y - point_b.y)


def vectorize(vector: str, start_point):
    direction, magnitude = directions[vector[0]], int(vector[1:])
    points = []
    current_point = start_point
    for idx in range(0, magnitude):
        new_point = Point(
            current_point.x + (1 * direction.x), 
            current_point.y + (1 * direction.y)
        )
        points.append(new_point)
        current_point = new_point
    return points


def calculate_points(vectors):
    points = set()
    current_point = Point(0, 0)
    for vector in vectors:
        new_points = vectorize(vector, current_point)
        points.update(new_points)
        current_point = new_points[-1]
    return points


def run():
    vectors =  _get_vectors()
    set_a =  calculate_points(vectors[0])
    set_b = calculate_points(vectors[1])
    intersections = list(set_a.intersection(set_b))
    return min([manhattan_distance(point, Point(0,0)) for point in intersections])


if __name__ == '__main__':
    max_manhattan_distance = run()
    logging.debug(max_manhattan_distance)
