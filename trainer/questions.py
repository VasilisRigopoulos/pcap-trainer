import math
import random

random.seed(2026)

def random_float():
    x = random.randint(1,9) + random.randint(1,9) / 10
    return random.choice([x,-x])

def q_floor():
    x = random_float()
    return(f'math.floor({x})', math.floor(x))


def q_ceil():
    x = random_float()
    return(f'math.ceil({x})', math.ceil(x))


def q_trunc():
    x = random_float()
    return(f'math.trunc({x})', math.trunc(x))


def q_hypot():
    k = random.randint(1,9)
    return(f'math.hypot({3 * k, 4 * k})', math.hypot(3 * k, 4 * k) ) # pure efficiency


def q_sqrt():
    x = random.randint(2,30)
    return(f'math.sqrt({x * x})', x)


def q_factorial():
    x = random.randint(3,6)
    return(f'math.factorial({x})', math.factorial(x))

def make_question():
    return KINDS[random.randint(0, len(KINDS) - 1 )]()

KINDS = [q_floor, q_ceil, q_trunc, q_hypot, q_sqrt, q_factorial]
LOW, HIGH = -1000, 1000