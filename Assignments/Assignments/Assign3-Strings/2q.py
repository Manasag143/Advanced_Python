# 2. Define a procedure histogram() that takes a list of integers and prints a histogram to the screen. For example, histogram([4, 9, 7]) should print the following:
# # ****
# # *********
# # *******

def histogram(list1):
    for i in list1:
        print("*" * i)
n = int(input("how many integers you want in histogram "))
list = []
for i in range(0,n):
    list.append(int(input("Enter integer")))
print("histogarm: ",list)
histogram(list)
