
# coding: utf-8

# In[71]:


import pandas as Pd
df = Pd.read_excel("Read_DID_Config_Sheet.xlsx",sheet_name="Sheet1")# Reaing parameter sheet/configuration excel sheet

f=open("Read_DID_22_template.py",'r') #opening template test case in read mode
x=f.read()                            #storing testcase code in object x
#print("x=",x)
f.close()                             #closing file

for i in range(len(df.axes[0])):     #iterates row number of times in config excel sheet
    #print(i)
    y='"'+df.SW_Val[i]+'"'           
    z='"'+df.Data_Identifier[i]+'"'
    #print(y,'\n','\n')
    new_file=x.replace('SW_label',y) #replacing SW_label in test case with y
    #print(new_file,'\n','\n')
    new_file=x.replace("Data_Identifier",z) #replacing Data_Identifier in test case with z
    #print(new_file,'\n','\n')
    #######################################
    """
    create file and save file
    """
    file_name="RDBI_"+str(df.Data_Identifier[i]).replace(' ','_')+"_testcase.py"
    #print(file_name)
    f=open(file_name,'w')         #opening file in write mode or creating a new file
    f.write(x)                    #writing the changed testcase to newfile
    f.close()                     #closing the file

    
    

