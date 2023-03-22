import json;
from datetime import datetime
import matplotlib.pyplot as pt
f = open('C:\\Users\\udaya\\OneDrive\\Documents\\Software\\Work_Spaces\\Workspace\\Data_Science\\Step_Count_Using_Heart_Beat_Analysis\\BLEData_Sharika_2022_03_26.json')
print("uu")
# returns JSON object as 
# a dictionary
dic = json.load(f)
#print(dic)
#print(dic.keys())
print(type(dic))

#Question 2
print(dic['captured_data'].keys())
print(dic['captured_data']['hr'].keys())
print(dic['captured_data']['slp'].keys())
print(dic['captured_data']['act'].keys())
print(dic['captured_data']['bat'].keys())
print(dic['captured_data']['err'].keys())


#print(len(dic['captured_data']['hr']['RR in ms']))
#print(len(dic['captured_data']['hr']['HR in BPM']))
#print(dic['captured_data']['hr']['RR in ms'])
#print(dic['captured_data']['hr']['HR in BPM'])
#print(type(dic['captured_data']['hr']['RR in ms']))
#print(type(dic['captured_data']['hr']['HR in BPM']))
time_in_millis=dic['captured_data']['hr']['RR in ms']
bpm=dic['captured_data']['hr']['HR in BPM']

# Python code to get the Cumulative sum of a list

new_list=[]
j=0
for i in range(0,len(time_in_millis)):
    j+=time_in_millis[i]
    new_list.append(j)
    
#print(new_list[len(new_list)-10::])
milli_second=new_list[-1]
'''
for i in range(0,len(time_in_millis)):
        time_in_millis[i] = time_in_millis[i]/1000 
'''
print("Time in Date time Format: ",datetime.fromtimestamp(milli_second//1000))
#print(datetime.fromtimestamp(1))            # here the timestamp represents the time between the year 1970 to 2038
#print(datetime.fromtimestamp(0))

color = ['green' if x<5 else 'red' for x in dic['captured_data']['act']['step count']]

pt.scatter(time_in_millis,dic['captured_data']['hr']['HR in BPM'],color = 'red')
#print(len(time_in_millis),len(dic['captured_data']['act']['step count']))
#print(len(time_in_millis),len(dic['captured_data']['act']['step count'][:len(time_in_millis)-1]))
#print(len(time_in_millis),len(dic['captured_data']['hr']['HR in BPM']))
#print(len(time_in_millis[:len(dic['captured_data']['act']['step count'])-1]))
#print(dic['captured_data']['act']['step count'])
#print(dic['captured_data']['hr']['HR in BPM'])
#print(dic['captured_data']['act']['step count'])
pt.show()
pt.scatter(dic['captured_data']['hr']['HR in BPM'][:len(dic['captured_data']['act']['step count'])],dic['captured_data']['act']['step count'],color = color)
pt.show()