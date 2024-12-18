import os

text_folder_path="C:/Users/ibrah/Masaüstü/data_Extraction/texts"
get_names_from="C:/Users/ibrah/Masaüstü/data_Extraction/shapee"

name_list=[]
count=0
for name in os.listdir(get_names_from):
 name_list.append(name)
 count=count+1 
 

for i in range (len(name_list)):
  name=os.path.splitext(name_list[i])[0]
  path=os.path.join(f"{text_folder_path}",f"{name}.txt")
  with open(path,'w',encoding='utf-8') as file:
   pass 
