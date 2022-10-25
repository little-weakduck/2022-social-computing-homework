import jieba
import csv

result = csv.reader(open(r'外卖评论.csv', 'r'))
print(result)
for jcs in result:
    if jcs[0] == '0':
        print(jcs[1])
