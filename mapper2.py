#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:57:47 2020

@author: Nicola
"""
#!/usr/bin/python
import csv
import math
import sys
from random import randint

def eudistance(x,y):
    distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(x, y)]))
    return distance


#create centroid dictionary
def reccreate(centers):
    record={}
    for num in range(len(centers)):
        record[centers[num][1]]=[0,0]
    return record

def shotsum(initialcenters, player, record):   
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
                shot=0
                if row[13]=='made':
                    shot=1
                record[sampleclass]=[x + y for x, y in zip(record.get((sampleclass),[0,0]), (shot,1))]
            except:
                #print('fail')
                continue
    return record
    
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
    player =  sys.argv[1]
    #path="D:/SkyDrive/Documents/Università/Fordham/Courses/BigData/Works/Project1/NBA/1.6/reducer.txt"
    finalcentroids=sys.argv[2]
    centers=loadcenters(finalcentroids,4)
    initrecords=reccreate(centers)
    records=shotsum(centers, player, initrecords)
    for i in records.items():
        print ('%s\t%s' % (i[0], i[1]))
 
