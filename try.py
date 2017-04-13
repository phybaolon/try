from numpy import * 
import os
from os import listdir
import sys
import math
import operator
import time


start = time.clock()


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
        #temp1['name']=prop.split('_')[0] 
        #temp1['name']=infoline.strip()           
        
        
        if info not in idlist:
            idlist.append(info)
            scorelist.append([temp1])          
          
        else:
            tid=idlist.index(info)            
            scorelist[tid].append(temp1)               
    
    k=50
    topk=[]
    # firstly, get top 50 elements 
    for idnum in range(0,len(idlist)):
        #
        temp=scorelist[idnum]
        temp1=[]
        if len(temp)<k:            
            temp1=sorted(temp,key=lambda a_tuple:a_tuple[1],reverse=True)
        else:            
            temp1=sorted(temp,key=lambda a_tuple:a_tuple[1],reverse=True)[:50]              
        topk.append(temp1)       
        #topk is a list of tuple.
    
    #print topk
    for id in topk:
        for i in range(len(id)):
            print id[i][0]
            print id[i][1]
            
    end = time.clock()
    print "read: %f s" % (end - start)        
        
        
    
    # then made some choices between the names of the figures.
    
        
    
    
    
    
   
        

if __name__ == '__main__':
    main()






