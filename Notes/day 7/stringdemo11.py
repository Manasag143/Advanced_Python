s="this is ....string"
lst=s.split(' ')
print(lst)
lst=s.split('...')
print(lst)
s="Rajat,Revati,Rajan"
lst=s.split(",")
print(lst)
s1=":".join(lst)
print(s1)

s1="this is test"
lst=[*s1]
print(lst)
s3="".join(lst)
print(s3)
