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
    STUDYMAX = 30
    revised = []
    count = 0
    mydate = datetime.today()
    for term in terms:
        count += 1 
        if(count%STUDYMAX==0):
            mydate += timedelta(days=1)
        t = mydate.strftime('%Y-%m-%d')
        #print("add",t)
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

# Trivial learning algorithm: if there is an error: next day, if this is OK, then day+2
def with_next_study_date(term,input):
    mydate = datetime.today()
    if(input=="w"):
        mydate += timedelta(days=1)
        t = mydate.strftime('%Y-%m-%d')
    else:
        mydate += timedelta(days=2)
        t = mydate.strftime('%Y-%m-%d')
    term["study"]=t
    return term

# Main Play Loop
def play(terms):
    print("Let's play !!!!!!!!! (q to quit)")
    mydate = datetime.today().strftime('%Y-%m-%d')
    study_revised = []
    quit = False
    for term in terms:
        date_time_obj = datetime.strptime(term["study"], '%Y-%m-%d')
        if(quit==False and date_time_obj <= datetime.today()):
            print(term["hanzi"], term["pinyin"], "?")  
            c=input("...")  
            if(c=="q"):
                quit = True
            else:
                term = with_next_study_date(term,c)
                print(term)
            print(term["fr"])
        study_revised.append(term)
    print("Well Done !!!!")
    return study_revised

print("Start... 1 to init, 2 to play")
select = input()
if(select=="1"):
    terms = initial_load()
    revised = create_study_plan(terms)
    #print(revised)
    export_json(revised)
if(select=="2"):
    data = import_json()
    #print(data)
    study = play(data)
    export_json(study)
print("End")

