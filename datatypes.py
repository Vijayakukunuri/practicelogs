mystring="vijaya"
# reverse index starts from end
print(mystring[::-1])
print(mystring[:-1])
print(mystring[-2:-4])
# replace : to a old char to new char
print(mystring.replace("a","b"))
# index : to show the index
print(mystring.index("j",1,4))
# find: find the index from given range
print(mystring.find("i",1,5))
# count : repeated laters or nums
print(mystring.count("a"))
#check whether it is alphabets
print(mystring.isalpha())
newstr="nani"
#isdecimal : only for decimal values
print(newstr.isdecimal())

# advance datatypes

# list
mylist=[2,3,4,["surya","B",23,76.7],"vijaya"]
print(mylist)
mylist.append("obj")
print(mylist)
mylist.insert(-29,56)
print(mylist)
mylist.pop()
print(mylist)
mylist.pop(5)
print(mylist)
mylist.count(4)
print(mylist)
print(mylist.index(2))
# mylist.extend("extend")
# print(mylist.extend("extend"))
mylist.reverse()
print(mylist)
del mylist

# tuple
tup1=("surya","nani",5,7,8,9,8)
print(tup1)
print(tup1.count(8))
tup2=tup1
print(tup2)
tup2=("a","vijaya",3,765,9.09)
print(tup2)
del tup1

# set
set1={"nani","surya",(1,2,3,4,5)}
print(set1)
set1.add("add")
print(set1)
set1.update("separate")
print(set1)
set1.pop()
print(set1)
# set1.remove("sury")//it throws error beyond set//
# print(set1)
set1.discard("sury")#it doesnt throw error
print(set1)
# set1.clear()
# print(set1)
set2=set1
print(set2)
# set2.remove("ad")
# print(set2)
set2.discard("ad")
print(set2)
set3={1,2,3,4,"nani"}
set1.union(set3)
print(set3)
print(set1.intersection(set3))
print(set1.difference(set3))
set1.difference_update(set3)
print(set3)
print(set1.issubset(set3))
print(set1.issuperset(set3))
print(set1.symmetric_difference(set3))






