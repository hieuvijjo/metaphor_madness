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
                    help='path to text of concrete')
parser.add_argument('-a',
                    '--abstract',
                    default=ABSTRACT_TXT,
                    help='path to text of abstract')
parser.add_argument('-n',
                    '--number',
                    default='1',
                    const='1',
                    type=int,
                    nargs='?',
                    help='path to text of abstract')

args = parser.parse_args()

with open(args.concrete) as file:
    concretes = file.read().splitlines()

with open(args.abstract) as file:
    abstracts = file.read().splitlines()

# __import__('pprint').pprint(vars(args))

if len(concretes) > 0 and len(abstracts) > 0:
    book = {}
    max_length = 0
    random_concretes = random.sample(concretes, args.number)
    for item in random_concretes:
        if len(item) > max_length:
            max_length = len(item)
    random_abstracts = random.sample(abstracts, args.number)
    for index in range(0, args.number):
        print(f'{random_concretes[index].ljust(max_length+3)}'
              f'{random_abstracts[index]}')
