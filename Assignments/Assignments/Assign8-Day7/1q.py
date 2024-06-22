##1. the two lists convert it into the dictionary
##
##keys = ['Ten', 'Twenty', 'Thirty']
##values = [10, 20, 30]
##Expected output:
##
##{'Ten': 10, 'Twenty': 20, 'Thirty': 30}

l1=['Ten','Twenty','Thirty']
l2=[10,20,30]
d1=zip(l1,l2)
print (dict(d1))
