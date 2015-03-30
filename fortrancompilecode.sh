#!/bin/bash
#Compile code:
gfortran -c Potcalc.f90
f2py -c --f90flags='-fPIC -O3 -funroll-loops -ffast-math -march=native' -m f90pot Potcalc.f90 --fcompiler=gfortran
