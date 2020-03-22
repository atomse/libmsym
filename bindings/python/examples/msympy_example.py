#!/usr/bin/python

import sys
import random
import argparse
import libmsym as msym
import numpy as np
import libmsym.interfaces


def read_xyz(fin):
    length = int(fin.readline())
    comment = fin.readline()[:-1]
    elements = []
    results = {
        'symbols': [],
        'positions': []
    }
    for i in range(0, length):
        line = fin.readline().split()
        name = line[0]
        coordinates = map(float, line[1:4])
        results['symbols'].append(name)
        results['positions'].append(coordinates)
    return results


def write_xyz(fout, elements, comment):
    fout.write("%d\n%s\n" % (len(elements), comment))
    for e in elements:
        v = e.coordinates
        fout.write("%s %.14f %.14f %.14f\n" % (e.name, *v))



def test(args):
    atoms_dict = read_xyz(args.infile)
    results = libmsym.interfaces.get_symmetry_info(atoms_dict)
    print(results)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('infile', type=argparse.FileType('r'))
    parser.add_argument('outfile', type=argparse.FileType('w'))
    args = parser.parse_args()
    test(args)
