#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:47:16 2020

@author: EMR

Script to compute the orbital elements given three coplanar position vectors via 
Gibbs method.
"""

import argparse
import numpy as np
import sys
import re

description = """Program to compute orbital elements given three coplanar position 
vectors r1, r2, r3 via Gibbs method."""
parser = argparse.ArgumentParser(prog = 'Gibbs', description =  description,
                                 formatter_class = argparse.RawTextHelpFormatter)
subparser = parser.add_subparsers(help = 'choose input method')
file_parser = subparser.add_parser('file', help = 'read input from file')
file_parser.add_argument('FILE', help = 'file from which to read input')
term_parser = subparser.add_parser('term', help = 'read input from command line')
term_parser.add_argument('-r1', '--position1', type = float, nargs = 3, help = 'first position vector',
required = True, metavar = ('x', 'y', 'z'))
term_parser.add_argument('-r2', '--position2', type = float, nargs = 3, help = 'second position vector',
required = True, metavar = ('x', 'y', 'z'))
term_parser.add_argument('-r3', '--position3', type = float, nargs = 3, help = 'third position vector',
required = True, metavar = ('x', 'y', 'z'))

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

mu = 1

if args.FILE:
    p = re.compile(r".+,.+,.+")
    positions = []
    for line in open(args.FILE, 'r'):
        if line.strip().startswith('#'):
            continue
        else:
            if p.match(line):
                position = [float(n) for n in line.split(',')]
                positions.append(position)
    
    r1 = np.array(positions[0])
    r2 = np.array(positions[1])
    r3 = np.array(positions[2])
else: 
    r1 = np.array(args.position1)
    r2 = np.array(args.position2)
    r3 = np.array(args.position3)

r1_mag = np.linalg.norm(r1)
r2_mag = np.linalg.norm(r2)
r3_mag = np.linalg.norm(r3)

test_coplanar = np.dot(r1, np.cross(r2, r3))
test_coplanar = int(test_coplanar * 10**4)
if test_coplanar != 0:
    print 'position vectors are not coplanar'
    print 'r1: ', r1
    print 'r2: ', r2
    print 'r3: ', r3
else:
    D = np.cross(r1, r2) + np.cross(r2, r3) + np.cross(r3, r1)
    N = r3_mag * np.cross(r1, r2) + r1_mag * np.cross(r2, r3) + r2_mag * np.cross(r3, r1)
    S = (r2_mag - r3_mag) * r1 + (r3_mag - r1_mag) * r2 + (r1_mag - r2_mag) * r3
    
    D_mag = np.linalg.norm(D)
    N_mag = np.linalg.norm(N)
    S_mag = np.linalg.norm(S)
    
    test_orbit = np.dot(D, N)
    if test_orbit <= 0:
        print 'vectors cannot describe a two body orbit'
    else:
        B = np.cross(D, r2)
        L = np.sqrt(mu/ (D_mag * N_mag))
        
        v2 = (L / r2_mag) * B + L * S
        p = N_mag / D_mag
        e = S_mag / D_mag
        
        Q = S / S_mag
        W = N / N_mag
        P = np.cross(Q, W)
        
        print 'Results:'
        print 'semi-latus rectum: %f' % p
        print 'eccentricity: %f' % e
        print 'velocity v2 = ', v2
        

