""" 11/4/2019 """

""" Author: Duy Nguyen """
listed = [123,17,1862,1,246,7,8,90,31,1]
inlist = [123,17,4689,2,724,1]

for item in listed:
    for item1 in inlist:
        if item == item1:
            print(item)
        else:
            print("no match")

print("*"*20)

print()
def comp(listed, inlist):
    for val in listed:
        if val in inlist:
            print("Good")
        print("No")


comp(listed, inlist)