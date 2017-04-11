from numpy import * 
import os
from os import listdir
import sys
import math
import heapq

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
        
        temp1={}
        temp1['name']=prop            
        temp1['score']=scorfo
        
        if info not in idlist:
            idlist.append(info)
            scorelist.append([temp1])          
          
        else:
            tid=idlist.index(info)            
            scorelist[tid].append(temp1)             
                
    #print idlist  
    #print scorelist
    #print "the largest two elements of each id "    
    
    topk=[]
    for id in idlist:
        temp=heapq.nlargest(50, scorelist[idlist.index(id)], key=lambda s: s['score'])
        topk.append(temp)
    
    #print topk
    for id in topk:
        for i in range(len(id)):
            print id[i]['name']
            print id[i]['score']
            
            
        
        
    
    # then made some choices between the names of the figures.
    
        
    
    
    
    
   
        

if __name__ == '__main__':
    main()
