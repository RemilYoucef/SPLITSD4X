import os 
import numpy as np
import pandas as pd
import codecs, json 
import math


from neighbors_generation import *

def patterns (P, split_point, data, att_names_) :
    
    
    patt_dict = dict()
    rank = 0
    for s,p in P.items() :
        
        description = ''
        it = 0
        d = dict ()
        while (it < len(p)) :
            a,op,v = p[it],p[it+1],p[it+2]
            if a not in d :
                d[a] = [np.min(data[:,a]) ,
                        np.max(data[:,a]) ]

            if op == '>' :
                #update le min
                d[a][0] = max(v,d[a][0])

            else : 
                #update le max
                d[a][1] = min(v,d[a][1])

            it += 3
                                                
        print ('subrgoup',rank)
        
        for att, value in d.items():
            if att < split_point : 
                print(round(value[0],2),"<",att_names_[att],"<=",round(value[1],2))
                description += str(round(value[0],2)) + ' < ' + att_names_[att] + ' <= ' + str(round(value[1],2)) +'  \n'
            
            else : 
                if value [0] < 0.5  : 
                    print(att_names_[att],"=",'0')
                    description += att_names_[att] + ' = ' + '0' +'  \n'
                    
                else :
                    print(att_names_[att],"=",'1')
                    description += att_names_[att] + ' = ' + '1' +'  \n'
         
        patt_dict[s] = description 
        print("-------------------------------------------------------------------")
        rank += 1
    
    return patt_dict



def patterns_sc (P, split_point, data, att_names_, data_means, data_stds) :
    
    
    patt_dict = dict()
    rank = 0
    for s,p in P.items() :
        
        description = ' '
        it = 0
        d = dict ()
        while (it < len(p)) :
            a,op,v = p[it],p[it+1],p[it+2]
            v = v * data_stds[a] + data_means[a]
            if a not in d :
                d[a] = [np.min(data[:,a]) * data_stds[a] + data_means[a],
                        np.max(data[:,a]) * data_stds[a] + data_means[a]]

            if op == '>' :
                #update le min
                d[a][0] = max(v,d[a][0])

            else : 
                #update le max
                d[a][1] = min(v,d[a][1])

            it += 3
                                                
        print ('subrgoup',rank)
        
        for att, value in d.items():
            if att < split_point : 
                print(round(value[0],2),"<",att_names_[att],"<=",round(value[1],2))
                description += str(round(value[0],2)) + ' < ' + att_names_[att] + ' <= ' + str(round(value[1],2)) +'  \n'
            
            else : 
                if value [0] < 0.5  : 
                    print(att_names_[att],"=",'0')
                    description += att_names_[att] + ' = ' + '0' +'  And  \n'
                    
                else :
                    print(att_names_[att],"=",'1')
                    description += att_names_[att] + ' = ' + '1' +'  And  \n'
         
        patt_dict[s] = description
        #print(patt_dict[s])
        print("-------------------------------------------------------------------")
        rank += 1
    
    return patt_dict

