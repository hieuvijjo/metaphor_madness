#!/usr/bin/env python3
"""Generate a random concrete object and a random abstract concept"""

import argparse
import random
import sys
from os.path import join

CONCRETE_TXT = '/Users/hieucao/projects/metaphor_maddness/concrete.txt'
ABSTRACT_TXT = '/Users/hieucao/projects/metaphor_maddness/abstract.txt'

parser = argparse.ArgumentParser()
parser.add_argument('-c',
                    '--concrete',
                    default=CONCRETE_TXT,
                    nargs='?',
                    help='path to text of concrete')
parser.add_argument('-a',
                    '--abstract',
                    default=ABSTRACT_TXT,
                    nargs='?',
                    help='path to text of abstract')
parser.add_argument('-n',
                    '--number',
                    default='1',
                    type=int,
                    nargs='?',
                    help='path to text of abstract')

args = parser.parse_args()

with open(args.concrete) as file:
    concrete = file.read().splitlines()

with open(args.abstract) as file:
    abstract = file.read().splitlines()

if len(concrete) > 0 and len(abstract) > 0:
    book = {}
    max_length = 0
    for number in range(1, args.number + 1):
        random_concrete = random.randint(0, len(concrete) - 1)
        random_abstract = random.randint(0, len(abstract) - 1)
        book[concrete[random_concrete]] = abstract[random_abstract]
        if len(concrete[random_concrete]) > max_length:
            max_length = len(concrete[random_concrete])
    for key, value in book.items():
        print(f'{key.ljust(max_length)}   {value}')
