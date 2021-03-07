print("start")
sum = 0
total = 0
with open("/home/chris/brain/1-projects/python-hsk2/data/raw.txt",'r')  as reader:
    for line in reader.readlines():
        # skip the lines 'Juin 2010'
        if(line.find("Juin")==-1):
            # find the first space
            s = line.find(' ')
            notraditional = line[s+1:]
            print(line,end='')
            print(notraditional, end='')
            c = notraditional.count(' ')
            print(c)
            total = total + 1
            if(c==2):
                sum = sum + 1
    print("ok")
print("end")
print(sum,"out of",total)