#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 17:03:34 2020

@author: Nicola
"""


import sys


#parse initial centers
def centersplit(initcenters):
    icenters=[]
    for i in initcenters:
        ctr=()
        cen=i.strip(')').strip('(').split(',')
        for  num in cen:
            ctr=ctr+(float(num),)
        icenters.append(ctr)
    return icenters
        

#sum over all the mappers
def sumbycenter():
    recordtot = {}
    for line in sys.stdin:
        line = line.strip()
        center, values, initcenters = line.split('\t')
        values=values.strip("[").strip("]\n").replace(',', '').split()
        values=[float(n) for n in values]
        initcenters=initcenters.strip("[").strip("]\n").strip().replace(', ',',').replace('),',') ').split()
        initcenters=centersplit(initcenters)
        try:
            recordtot[center] = [x + y for x, y in zip(recordtot.get(center,[0,0,0,0]), (float(values[0]),float(values[1]),float(values[2]),int(values[3])))]
        except ValueError:
            pass
    return initcenters,recordtot

#compute new centers
def computecenters(recordtot):
    newcenters=[]
    for i in recordtot.items():
        if int(i[1][3]==0):
            newcenters.append((round(i[1][0]/(i[1][3]+1),1),round(i[1][1]/(i[1][3]+1),1),round(i[1][2]/(i[1][3]+1),1)))
        else:
            newcenters.append((round(i[1][0]/i[1][3],1),round(i[1][1]/i[1][3],1),round(i[1][2]/i[1][3],1)))
    return newcenters

if __name__ == "__main__":
    initcenters,recordtot=sumbycenter()
    newcenters=computecenters(recordtot)
    
    if all(item in initcenters for item in newcenters)==False:
        print (str(newcenters)+' '+str(0))
    else:
        print(str(newcenters)+' '+str(1))


