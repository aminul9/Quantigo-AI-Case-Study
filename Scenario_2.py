#!/usr/bin/env python
# coding: utf-8

# In[2]:


import json
import os
import codecs


# In[6]:


def merge_file_given_directory(path):
    dir_list = os.listdir(path)
    merge_file={}
 
    for file_name in dir_list:
        ##print(file_name)
    
        with open(path+file_name,'r') as infile:
            data=json.load(infile)  
    
        for item in data['objects']:
            if 'classTitle' in item:
                if(item['classTitle']=='Vehicle'):
                    item['classTitle']='car'
                    ##print("****YES VICH***")
                elif(item['classTitle']=='License Plate'):
                    item['classTitle']='number'    
            
            ##print("****YES***"+item['classTitle'])
        merge_file[file_name]=data   

    data=json.dumps(merge_file,indent=2)

    with open("formatted_"+file_name,"w") as f:
        json.dump(data,f)
    print(data)


# In[7]:


merge_file_given_directory("json_file/")




