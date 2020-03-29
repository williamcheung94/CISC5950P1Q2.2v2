#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:03:34 2020

@author: Nicola
"""


import sys

#parse initial centers
def centerparse(center):
    ctr=()
    for i in center:
        ctr=ctr+(float(i),)
    return ctr
        

#sum over all the mappers and compute hit rate
def sumbycenter():
    recordtot = {}
    for line in sys.stdin:
        print(line)
        line = line.strip()
        center, shots = line.split('\t')
        shots=shots.strip("[").strip("]\n").replace(',', '').split()
        shots=[int(n) for n in shots]
        center=center.strip(')').strip('(').split(', ')
        center=centerparse(center)
        try:
    
            recordtot[center] = [x + y for x, y in zip(recordtot.get(center,[0,0]), (int(shots[0]),int(shots[1])))]
        except ValueError:
            pass
        break
    for key in recordtot:
        recordtot[key]=recordtot[key][0]/recordtot[key][1]
    return recordtot

#get hit rate by centroid
def bestzone(recordtot):
    final = {y:x for x,y in recordtot.items()}
    max_value = max(final.keys()) 
    print (str(final[max_value]) +' '+str(max_value))



if __name__ == "__main__":
    recordtot=sumbycenter()
    bestzone(recordtot)


