import re
filepath1 = 'mini.log'
filepath2="statistics.log"
with open(filepath1) as fp:
    line=fp.readline()
    dic={}
    days=["Mon","Tue","Wed","Thu","Fri","Sat"]
    while(line):
        if(line[0:3] in days):
            key=line.strip()
            dic[key]={}
            line=fp.readline()  
            while(line[0:3] not in days and line):
                attr=line.split(":")[0].strip()
                rhs=line.split(":")[1].strip()
                if(attr=="Latency"):
                    nums=re.findall("\d+.?\d*",rhs)
                    if(nums):
                        dic[key][attr]=nums[0]
                        dic[key]["Jitter"]=nums[1]
                elif(attr=="Download" or attr=="Upload" or attr=="Packet Loss"):
                    x=re.match("\d+.?\d*",rhs)
                    if(x):
                        dic[key][attr]=x.group()       
                line=fp.readline()
    for i in dic:
        print(i)
        print(dic[i],"\n")
