import json
from datetime import datetime, date, time, timedelta

# Utility parsing
def special_parse(line, second_separator):
    s1 = line.find(" ")
    rest = line[s1+1:]
    s2 = rest.find(second_separator)
    h = line[:s1]
    p = rest[0:s2]
    f = rest[s2+1:]
    return {"hanzi":h,"pinyin":p,"fr":f.strip()}    

# Load data (initialization)
def initial_load():
    print("start")
    total = 0
    terms = []
    with open("/home/chris/brain/1-projects/python-hsk2/data/raw.txt",'r')  as reader:
        for line in reader.readlines():
            # skip the lines 'Juin 2010'
            if(line.find("Juin")==-1):
                # find the first space
                s = line.find(' ')
                notraditional = line[s+1:]
                #print(line,end='')
                #print(notraditional, end='')
                if(line.find("#")!=-1):
                    r = special_parse(notraditional, "#")
                    print(r)
                    terms.append(r) 
                else:
                    r = special_parse(notraditional, " ")
                    print(r)
                    terms.append(r)
                total = total + 1
        print("ok")
    #print(terms)
    print("end")
    print("out of",total)
    return terms

# Create the initial study plan
def create_study_plan(terms):
    STUDYMAX = 20
    revised = []
    count = 0
    mydate = datetime.today()
    for term in terms:
        count += 1 
        if(count%STUDYMAX==0):
            mydate += timedelta(days=1)
        t = mydate.strftime('%Y-%m-%d')
        print("add",t)
        term["study"] = t
        revised.append(term)
    return revised

# Export to JSON
def export_json(terms):
    with open("/home/chris/brain/1-projects/python-hsk2/data/study.json",'w')  as writer:
        json.dump(terms, writer)

# Import the JSON back
def import_json():
    with open("/home/chris/brain/1-projects/python-hsk2/data/study.json",'r')  as reader:
        data = json.load(reader)
    return data

def play(terms):
    print("Let's play !!!!!!!!! (q to quit)")
    mydate = datetime.today().strftime('%Y-%m-%d')    
    for term in terms:
        if(term["study"]==mydate):
            print(term["hanzi"], term["pinyin"], "?")  
            c=input("...")  
            if(c=="q"):
                exit(0)
            print(term["fr"])
    print("Well Done !!!!")

terms = initial_load()
revised = create_study_plan(terms)
#print(revised)
export_json(revised)
data = import_json()
print(data)
play(data)
print("done")

