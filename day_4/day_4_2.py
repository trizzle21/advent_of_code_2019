"""
However, they do remember a few key facts about the password:

It is a six-digit number.
The value is within the range given in your puzzle input.
Two adjacent digits are the same (like 22 in 122345).
Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
Other than the range rule, the following are true:

111111 meets these criteria (double 11, never decreases).
223450 does not meet these criteria (decreasing pair of digits 50).
123789 does not meet these criteria (no double).
How many different passwords within the range given in your puzzle input meet these criteria?
"""
import logging

from day_4_1 import increasing

logging.basicConfig(level=logging.DEBUG)


def pairs(value):
    iter_value = str(value)
    seen_multi_pair = False
    seen_single_pair = False
    p_0 = 0
    p_1 = 1
    p_2 = 2
    while p_2 < len(iter_value):
        is_single_pair_left = iter_value[p_0] == iter_value[p_1] != iter_value[p_2] 
        is_single_pair_right = iter_value[p_0] != iter_value[p_1] == iter_value[p_2] 
        is_double_pair = iter_value[p_0] == iter_value[p_1] == iter_value[p_2]
        if is_double_pair:
            seen_multi_pair = True
        if is_single_pair_left or is_single_pair_right:
            seen_single_pair = True
        p_0 += 1
        p_1 += 1 
        p_2 += 1
    return not seen_single_pair and seen_multi_pair


def run(start_point=124075, endpoint=580769):
    pointer = start_point
    count = 0
    while pointer < endpoint:
        if pairs(pointer) and increasing(pointer):
            count += 1
        pointer += 1
    return count


if __name__ == '__main__':
    total_combinations = run()
    logging.debug(total_combinations)
