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
args = parser.parse_args()

with open(args.concrete) as file:
    concrete = file.read().splitlines()

with open(args.abstract) as file:
    abstract = file.read().splitlines()

random_concrete = random.randint(0, len(concrete) - 1)
random_abstract = random.randint(0, len(abstract) - 1)

if len(concrete) > 0 and len(abstract) > 0:
    print(f'{concrete[random_concrete]} {" "*7} {abstract[random_abstract]}')
