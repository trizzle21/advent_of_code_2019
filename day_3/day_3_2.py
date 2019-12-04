import logging
from collections import namedtuple, OrderedDict

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



def vectorize(vector: str, start_point, step):
    direction, magnitude = directions[vector[0]], int(vector[1:])
    points = {}
    current_point = start_point
    for idx in range(0, magnitude):
        new_point = Point(
            current_point.x + (1 * direction.x), 
            current_point.y + (1 * direction.y)
        )
        points[step] = new_point
        step += 1
        current_point = new_point
    last_step = step
    return points, last_step


def build_walk(vectors):
    points = OrderedDict()
    step = 0
    current_point = Point(0, 0)
    for vector in vectors:
        new_points, step = vectorize(vector, current_point, step)
        points.update(new_points)
        current_point = new_points[max(points.keys())]
    return points


def run():
    vectors =  _get_vectors()
    walk_a =  build_walk(vectors[0])
    walk_b = build_walk(vectors[1])
    intersections = set(walk_a.values()).intersection(set(walk_b.values()))
    idxs_a = [ walk_a[point] for point in intersections ]
    idxs_b = [ walk_b[point] for point in intersections ]
    return min(idxs_a) + min(idxs_b)


if __name__ == '__main__':
    max_walk = run()
    logging.debug(max_walk)
