import csv
import parser
dict = {'name': 'krunal', 'age': 26, 'education': 'Engineering'}
with open('data.csv', 'w') as f:
    for key in dict.keys():
        f.write("%s, %s\n" % (key, dict[key]))
for i in parser.dic:
    print(i)
    print(parser.dic[i],"\n")