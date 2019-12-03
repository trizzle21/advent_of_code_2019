"""
determine what pair of inputs produces the output 19690720
"""
import logging
from day_2_1 import run as engine

logging.basicConfig(level=logging.DEBUG)
TARGET_VALUE = 19690720


def run():
    for val_1 in range(0,99):
        for val_2 in range(0, 99):
            output = engine(val_1, val_2)
            if output == TARGET_VALUE:
                return val_1, val_2
    else:
        raise Exception("No value found")

if __name__ == '__main__':
    noun, verb = run()
    final_value = 100 * noun + verb
    logging.debug(f"noun: {noun}, verb: {verb}")
    logging.debug(final_value)
