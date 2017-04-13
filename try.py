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
        temp=[]
        if len(scorelist[idnum])<k:
            temp=scorelist[idnum]
            temp1=sorted(temp,key=lambda a_tuple:a_tuple[1],reverse=True)
        else:            
            for i in range(0,k):
                temp.append(scorelist[idnum][i])
            temp1=sorted(temp,key=lambda a_tuple:a_tuple[1],reverse=True)
            for j in range(k,len(scorelist[idnum])):
                tet=scorelist[idnum][j]            
                if tet[1]>temp1[k-1][1]:
                    temp1[k-1]=tet
                    sensor=k-2
                    while sensor>0:
                        if temp1[sensor][1]<temp1[sensor+1][1]:
                            q=temp1[sensor]
                            temp1[sensor]=temp1[sensor+1]
                            temp1[sensor+1]=q
                            sensor=sensor-1
                        #print sensor
                        else:
                            sensor=0                
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





