"""
Day 1
> Fuel required to launch a given module is based on its mass. Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

> For example:

> For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
> For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
> For a mass of 1969, the fuel required is 654.
> For a mass of 100756, the fuel required is 33583.
> The Fuel Counter-Upper needs to know the total fuel requirement. To find it, individually calculate the fuel needed for the mass of each module (your puzzle input), then add together all the fuel values.
"""
from math import floor
import logging

logging.basicConfig(level=logging.DEBUG)

def calculate(value):
    return floor(value/3) - 2


def run():
    with open('day_1_input.txt', 'r') as f:
        values = f.readlines()
    values = [int(value.strip()) for value in values]
    return sum([calculate(v) for v in values])


if __name__ == '__main__':
    total_fuel = run()
    logging.debug(total_fuel)
