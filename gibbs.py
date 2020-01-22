#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 08:47:16 2020

@author: EMR

Script to compute the orbital elements given three coplanar position vectors via 
Gibbs method.
"""

# TODO:
# add distinction between ijk and pqw coords if required
# add read vectors from file option

import argparse
import numpy as np
import sys

description = """Program to compute orbital elements given three coplanar position 
vectors r1, r2, r3 via Gibbs method."""
parser = argparse.ArgumentParser(description =  description,
                                 formatter_class = argparse.RawTextHelpFormatter)
group = parser.add_mutually_exclusive_group()
group.add_argument('-ijk', action = 'store_true', help = 'r vectors given in ijk coords; default')
group.add_argument('-pqw', action = 'store_true', help = 'r vectors given in perifocal coords')
parser.add_argument('-r1', '--position1', type = float, nargs = 3, help = 'first position vector')
parser.add_argument('-r2', '--position2', type = float, nargs = 3, help = 'second position vector')
parser.add_argument('-r3', '--position3', type = float, nargs = 3, help = 'third position vector')

if len(sys.argv) == 1:
    parser.print_help(sys.stderr)
    sys.exit(1)
args = parser.parse_args()

mu = 1

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
else:
    D = np.cross(r1, r2) + np.cross(r2, r3) + np.cross(r3, r1)
    N = r3_mag * np.cross(r1, r2) + r1_mag * np.cross(r2, r3) + r2_mag * np.cross(r3, r1)
    S = (r2_mag - r3_mag) * r1 + (r3_mag - r1_mag) * r2 + (r1_mag - r2_mag) * r3
    
    D_mag = np.linalg.norm(D)
    N_mag = np.linalg.norm(N)
    S_mag = np.linalg.norm(S)
    
    test_orbit = np.dot(D, N)
    if test_orbit <= 0:
        print 'vectors cannot descript a two body orbit'
    else:
        B = np.cross(D, r2)
        L = np.sqrt(mu/ (D_mag * N_mag))
        
        v2 = (L / r2_mag) * B + L * S
        
        p = N_mag / D_mag
        e = S_mag / D_mag
        
        print 'semi-latus rectum: %f' % p
        print 'eccentricity: %f' % e

if not args.pqw:
    pass