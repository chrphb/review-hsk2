def special_parse(line, second_separator):
    s1 = line.find(" ")
    rest = line[s1+1:]
    s2 = rest.find(second_separator)
    h = line[:s1]
    p = rest[0:s2]
    f = rest[s2+1:]
    return (h,p,f.strip())    


print("start")
total = 0
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
            else:
                r = special_parse(notraditional, " ")
                print(r)
            total = total + 1
    print("ok")
print("end")
print("out of",total)