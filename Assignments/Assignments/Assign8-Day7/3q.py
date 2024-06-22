##3. Display the value of key history from the following dictionary
##the value of key ‘history’ from the below dict
##sampleDict = {
##"class":{
##"student":{
##"name":"Mike",
##"marks":{
##"physics":70,
##"history":80
##}
##}
##}
##}

d = {"class":{"student":{"name":"Mike","marks":{"physics":70,"history":80}}}}
print(d["class"]["student"]["marks"]["history"])

