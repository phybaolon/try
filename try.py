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
        
        temp1={}
        #temp1['name']=prop.split('_')[0] 
        #temp1['name']=infoline.strip()           
        temp1[prop.split('_')[0]]=scorfo
        
        if info not in idlist:
            idlist.append(info)
            scorelist.append([temp1])          
          
        else:
            tid=idlist.index(info)            
            scorelist[tid].append(temp1)               
    
    topk=[]
    # firstly, get 50 elements out of the dict
    for id in idlist:
        temp=[]
        for i in range(0,50):
            temp.append(scorelist[id][i])
        temp1=sorted(temp.iteritems(),key=operator.itemgetter(1),reverse=True)
        for j in range(51,len(scorelist[id])):
            tetdict=scorelist[id][j]
            tet=tetdict.values()[0]
            if tet>temp1[0][1]:
                temp1.insert(0, (tetdict['name'],tetdict['score']))
            elif ((tet>temp1[49][1]) and (tet<temp1[0][1])):
                inser=48
                while inser>0:                                       
                    if temp1[inser][1]>tet:
                        temp1.insert(inser+1,(tetdict['name'],tetdict['score']))
                        continue
                    inser=inser-1                 
        topk.append(temp1)              
        #topk is a list of tuple.
    
    #print topk
    for id in topk:
        for i in range(len(id)):
            print id[i][0]
            print id[i][1]
            
            
        
        
    
    # then made some choices between the names of the figures.
    
        
    
    
    
    
   
        

if __name__ == '__main__':
    main()


