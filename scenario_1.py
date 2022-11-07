#!/usr/bin/env python
# coding: utf-8

# In[108]:


import json


# In[109]:


out_put_dic={
       "dataset_name": '',
       "image_link": "",
       "annotation_type": "image",
        "annotation_objects": {
           "vehicle": {
               "presence": 0,
               "bbox": []
           },
           "license_plate": {
               "presence": 0,
               "bbox": []
           }
       },
       "annotation_attributes": {
           "vehicle": {
               "Type": None,
               "Pose": None,
               "Model": None,
               "Make": None,
               "Color": None
           },
           "license_plate": {
               "Difficulty Score": None,
               "Value": None,
               "Occlusion": None
           }
       }
   }


# In[120]:


def read_file(file_name):
    print(file_name)
    with open(file_name,'r') as infile:
        data_infile=json.load(infile)
        
    out_put_dic['dataset_name']=file_name
    
    
    for data in data_infile['objects']:
        if 'classTitle' in data:
            if data["classTitle"]=='Vehicle':
                for data_tags in data["tags"]:
                    out_put_dic['annotation_attributes']['vehicle'][data_tags['name']]=data_tags['value'];
                    
                out_put_dic['annotation_objects']["vehicle"]['presence']=1;
                for points in data['points']['exterior']:
                    out_put_dic['annotation_objects']["vehicle"]['bbox'].append(points[0])
                    out_put_dic['annotation_objects']["vehicle"]['bbox'].append(points[1])
            
            if data["classTitle"]=='License Plate':
                out_put_dic['annotation_attributes']['license_plate']['Occlusion']=0;
                for data_tags in data["tags"]:
                    out_put_dic['annotation_attributes']['license_plate'][data_tags['name']]=data_tags['value'];
                    
                out_put_dic['annotation_objects']["license_plate"]['presence']=1;
                print(data['points'])
                for points in data['points']['exterior']:
                    out_put_dic['annotation_objects']["license_plate"]['bbox'].append(points[0])
                    out_put_dic['annotation_objects']["license_plate"]['bbox'].append(points[1])
        
    ##Out put write in a file
    data=json.dumps(out_put_dic,indent=2)
    with open("formatted_"+file_name,"w") as f:
        json.dump(data,f)
    print(data)


# In[121]:


read_file("pos_0.png.json")


# In[ ]:




