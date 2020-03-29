#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:57:47 2020

@author: Nicola
"""

import csv
import math
import sys
from random import randint

#print(sys.argv[1],sys.argv[2],sys.argv[3])
def eudistance(x,y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance

#initalize list of centroids
def centroidinit(num):
    SHOT_DIST_max=47
    SHOT_DIST_min=0
    CLOSE_DEF_DIST_max=53
    CLOSE_DEF_DIST_min=0
    SHOT_CLOCK_max=24
    SHOT_CLOCK_min=0
    initialcenters=[]
    for center in range(1,num+1):
        initialcenters.append((center,(randint(SHOT_DIST_min,SHOT_DIST_max),randint(CLOSE_DEF_DIST_min,CLOSE_DEF_DIST_max),randint(SHOT_CLOCK_min,SHOT_CLOCK_max))))
    return initialcenters

#create centroid dictionary
def reccreate(initialcenters):
    record={}
    for num in range(len(initialcenters)):
        record[initialcenters[num][1]]=[0,0,0,0]
    return record

def clustersum(initialcenters, player, record):  
        for row in csv.reader(sys.stdin):
            if row[19].replace(',', '').lower()==player:
                try:
                    sample=(float(row[11]),float(row[16]),float(row[8]))
                    sampleclass=None
                    for num in range(len(initialcenters)):
                        if sampleclass==None:
                            sampleclass=initialcenters[0][1]
                        elif eudistance(initialcenters[num][1],sample)<eudistance(sampleclass,sample):
                            sampleclass=initialcenters[num][1]
                        else:
                            continue
                    record[sampleclass]=[x + y for x, y in zip(record.get(sampleclass), (float(row[11]),float(row[16]),float(row[8]),1))]
                except:
                    #print('fail')
                    continue
        return record
 
def centerlist(initialcenters):
    defaultcenters=[]
    for i in initialcenters:
        defaultcenters.append(i[1])
    return defaultcenters

#parse centers
def centersplit(initcenters):
    icenters=[]
    for i in initcenters:
        ctr=()
        cen=i.strip(')').strip('(').split(',')
        for  num in cen:
            ctr=ctr+(float(num),)
        icenters.append(ctr)
    return icenters

def loadcenters(oldcenters,number):    
    centrlist=[]
    row2=oldcenters.split('\t')[0]
    centr=row2.strip("[").strip("]\n").strip().replace(', ',',').replace('),',') ').replace(")]",")").split()
    centr=centr[:-1]
    centr=centersplit(centr)
    for c in range(1,len(centr)+1):
        centrlist.append((c,centr[c-1]))
    return centrlist

    
    
    
    
    
    
if __name__ == "__main__":
    count= sys.argv[2]
    player = sys.argv[1]
    #path="D:/SkyDrive/Documents/Università/Fordham/Courses/BigData/Works/Project1/NBA/1.6/reducer.txt"
    oldcenters=sys.argv[3]
    #print (player,count,oldcenters)
    #print (oldcenters)
    if int(count)==1:
        centers=centroidinit(4)
    else:
        centers=loadcenters(oldcenters,4) 
    initrecords=reccreate(centers)
    records=clustersum(centers, player, initrecords)
    defcenters= centerlist(centers)
               
    for i in records.items():
        print ('%s\t%s\t%s' % (i[0], i[1],defcenters))

