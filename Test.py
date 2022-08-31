from datetime import timedelta, date, datetime
import xml.etree.ElementTree as ET
import json,csv
from pytz import timezone
import pytz

#for xml question no 1
def update_date(x,y):
    DEPART = date.today() + timedelta(days = x)
    RETURN = date.today() + timedelta(days = y)
    #please provide your file path
    tree = ET.parse("C:\\Users\\Bivor\\Downloads\\python_exe\\Updated_Python_exercises_QA_Engr\\test_payload1.xml")
    root = tree.getroot()
    child = root[0]
    for innerchild in child[2]:
        if innerchild.tag == 'DEPART':
            innerchild.text = DEPART.strftime('%Y-%m-%d')
        elif innerchild.tag == 'RETURN':
            innerchild.text = RETURN.strftime('%Y-%m-%d')
        
    with open("newtestpayload.xml", "wb") as f:
        f.write(ET.tostring(root))


#for json question no 2
def update_jsonfile(jsonelements):
    #please provide4 your file path
    f = open('C:\\Users\\Bivor\\Downloads\\python_exe\\Updated_Python_exercises_QA_Engr\\test_payload.json')
    data = json.load(f)
    for key,val in list(data.items()):
        if key == jsonelements:
            data.pop(key)
        else:
            if isinstance (val, dict):
                for ikey,ival in list(val.items()):
                    if ikey == jsonelements:
                        val.pop(ikey)
    with open("new_test_payload.json", "w") as outfile:
        outfile.write(json.dumps(data))


#for jmeter question 3
def parse_jmeterlogfile():
    date_format='%Y-%m-%d %H:%M:%S %Z'
    #please provide your file path
    with open('C:\\Users\\Bivor\\Downloads\\python_exe\\Updated_Python_exercises_QA_Engr\\Jmeter_log1.jtl') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                line_count+=1
            else:
                if row[3] != '200':
                    timestamp = int(row[0])            
                    newdate = datetime.fromtimestamp(timestamp/1000)
                    date = newdate.astimezone(timezone('US/Pacific'))
                    print("Label : {} , response_code : {}, response_message: {}, failure_message: {}, timezone: {}".format(row[2],row[3],row[4],row[8],date.strftime(date_format)))
            

if __name__ =='__main__':
    update_date(3,4)
    update_jsonfile("outParams")
    parse_jmeterlogfile()
    



