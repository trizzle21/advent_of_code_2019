"""
Here are the initial and final states of a few more small programs:

1,0,0,0,99 becomes 2,0,0,0,99 (1 + 1 = 2).
2,3,0,3,99 becomes 2,3,0,6,99 (3 * 2 = 6).
2,4,4,5,99,0 becomes 2,4,4,5,99,9801 (99 * 99 = 9801).
1,1,1,4,99,5,6,0,99 becomes 30,1,1,4,2,5,6,0,99.

"""
import logging

logging.basicConfig(level=logging.DEBUG)

ops = {
    1: lambda x, y: x + y,
    2: lambda x, y: x * y
}
CHUNK_SIZE = 4

def _get_values():
    with open('day_2_input.txt', 'r') as f:
        values = f.readlines()
    return [int(value) for value in values[0].split(',')]


def calculate(values):
    for idk in range(0, len(values), CHUNK_SIZE):
        chunk = values[idk:idk + CHUNK_SIZE]
        if chunk[0] == 99 or len(chunk) < 4:
            continue
        input_1, input_2 = values[chunk[1]], values[chunk[2]]
        final_position = chunk[3]
        values[final_position] = ops[chunk[0]](input_1, input_2)
    return values[0]


def run(noun=12, verb=2):
    values = _get_values()
    values[1] = noun
    values[2] = verb
    return calculate(values)
 

if __name__ == '__main__':
    final_value = run()
    logging.debug(final_value)
