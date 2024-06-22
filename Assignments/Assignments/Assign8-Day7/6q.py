##Rename key city to location in the following dictionary
##
##sampleDict = {
##"name": "Kelly",
##"age":25,
##"salary": 8000,
##"city": "New york"
##}

sampleDict = {"name": "Kelly","age":25,"salary": 8000,"city": "New york"}
sampleDict["location"]=sampleDict.pop("city")
print(sampleDict)
