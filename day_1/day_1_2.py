"""
Fuel itself requires fuel just like a module - take its mass, divide by three, round down, and subtract 2. However, that fuel also requires fuel, and that fuel requires fuel, and so on. Any mass that would require negative fuel should instead be treated as if it requires zero fuel; the remaining mass, if any, is instead handled by wishing really hard, which has no mass and is outside the scope of this calculation.

So, for each module mass, calculate its fuel and add it to the total. Then, treat the fuel amount you just calculated as the input mass and repeat the process, continuing until a fuel requirement is zero or negative. For example:

A module of mass 14 requires 2 fuel. This fuel requires no further fuel (2 divided by 3 and rounded down is 0, which would call for a negative fuel), so the total fuel required is still just 2.
At first, a module of mass 1969 requires 654 fuel. Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, which requires 5 fuel, which requires no further fuel. So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.
"""


from math import floor
import logging

logging.basicConfig(level=logging.DEBUG)


def calculate(value, total=0):   
    new_value = floor(value/3) - 2 
    if (new_value <= 0):
        return total
    total += new_value
    return calculate(new_value, total) 
    
    
def run():
    with open('day_1_input.txt', 'r') as f:
        values = f.readlines()
    values = [int(value.strip()) for value in values]
    return sum([calculate(v) for v in values])


if __name__ == '__main__':
    total_fuel = run()
    logging.debug(total_fuel)
