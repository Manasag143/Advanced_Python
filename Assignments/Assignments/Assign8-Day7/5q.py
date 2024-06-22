##display all the keys with value 200 from the following dictionary.
##sampleDict = {'a': 100, 'b': 200, 'c': 300,’d’:200}

sampleDict = {'a': 100, 'b': 200, 'c': 300, 'd':200}
for i,j in enumerate(sampleDict):
    if sampleDict[j]==200:
        print(j)
