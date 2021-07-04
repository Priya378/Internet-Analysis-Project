import re
filepath1 = 'mini.log'
filepath2="statistics.log"
with open(filepath2) as fp:
    line=fp.readline()
    dic={}
    days=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
    while(line):
        if(line[0:3] in days):
            key=line.strip()[:-9]
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
                elif(attr=="Server"):
                    x=re.match("[^\(]+",rhs)
                    if(x):
                        dic[key][attr]=x.group().strip()       
                line=fp.readline()
