##This is just a personal proof-of-concept to test an algorithm for
##comparing lists and finding common values across
import collections

r1 = {'course list':[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
      'requirement':'ethnicity'}
r2 = {'course list':[1,2,4,8,16,32,64,128],
      'requirement':'history'}
##r3 = {'course list':[1,2,4,9,16,25,36,49,64,81,100],
##      'requirement':'writing'}
superList = [r1,r2]
##superList.append(r3)
listOut = []

##print(superList)

c2d = {}

for r in superList:
    for c in r['course list']:
        if c in c2d:
            c2d[c].append(r['requirement'])
        else:
            c2d[c] = [r['requirement']]

print(c2d)

