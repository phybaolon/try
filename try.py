from numpy import * 
import os
from os import listdir
import sys
import math
import operator
#import heapq

INFILE_LIST = '/data/face_attributes/130-139_1face_attributes.txt'
INFILE_LIST = sys.argv[1]

def main():    
    fr=open(INFILE_LIST)
    arrayOLines=fr.readlines()
    m=len(arrayOLines)/2
    #print m*2
        
    scorelist=[]    
      
    idlist=[]    
    
    for i in range(1,m+1):
        infoline=arrayOLines[2*(i-1)]
        scoreline=arrayOLines[2*i-1]
        
        infosplit=infoline.strip().split('/')
        info=infosplit[6]
        prop=infosplit[7]
        
        scoresplit=scoreline.strip().split(' ')
        scorfo=float(scoresplit[1])
        
        temp1=(infoline.strip(),scorfo)        
        
        if info not in idlist:
            idlist.append(info)
            scorelist.append([temp1])          
          
        else:
            tid=idlist.index(info)            
            scorelist[tid].append(temp1)               
    
    topk=[]
    # firstly, get top 50 elements 
    for id in idlist:
        idnum=idlist.index(id)
        temp=[]
        for i in range(0,50):
            temp.append(scorelist[idnum][i])
        temp1=sorted(temp,key=lambda a_tuple:a_tuple[1],reverse=True)
        for j in range(51,len(scorelist[idnum])):
            tet=scorelist[idnum][j]            
            if tet[1]>temp1[0][1]:
                temp1.insert(0, tet)
            elif ((tet[1]>temp1[49][1]) and (tet[1]<temp1[0][1])):
                inser=48
                while inser>0:                                       
                    if temp1[inser][1]>tet:
                        temp1.insert(inser+1,tet)
                        continue
                    inser=inser-1                 
        topk.append(temp1)              
        #topk is a list of tuple.
    
    #print topk
    for id in topk:
        for i in range(len(id)):
            print id[i][0]
            print id[i][1]
            
            
if __name__ == '__main__':
    main()





