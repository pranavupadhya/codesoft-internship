# APPEND
# use list.append()
''' adds one element at the end
and also merge two list'''
list1 = [1,2,3,4,5,6,7]
list2 = ["mango",'faijan','grapes']
print(list1)
print(list2)
print(len(list1))
print(len(list2))
print(list1[1:])
print(list2[-3:])
list1.append("riya")
print(list1)
list1.append("khan")
print(list1)
list1.append(list2)
print(list1)


l1 = [1,'light','amritsar',99.0]
l2 = ['t,u,p,l,e']
print(l1)
print(l2)
l1.append("faijan")
l1.append('riya')
print(l1)
print(l2)
l1.append(l2)
l2.append(l1)
print(l1)
print(l2)

# list.sort()
# arrange in asscending order
''' it can not determine
the order of string in 
list.sort'''
l3 = [2,54,65,45,2,4,6,1,9,6,8]
print(l3)
print(len(l3))
l3.sort()
print(l3)

# 2nd question
l = [2, 4,6,7,2,8,4,7,]
print(l)
l.sort()
print(l)

l5 = ['banana','litchi','apple']
l5.sort()
print(l5)


# list.sort(reverse=True)
''' arranges in 
descending order'''
l3.sort(reverse=True)
l.sort(reverse=True)
print(l3)
print(l)
# REVERSE
# reverse the list
a = [1,2,3,4,5,6,7,8] 
print(a)
print(type(a))
print(len(a))
print(a[1:5])
print(a[-8:])
a.sort()
print(a)
a.sort(reverse=True)
print(a)
a.reverse()
print(a)
a.append("faijan khan")
print(a)


b=[1,2,3]
b.reverse()
print(b)

c= [1,2,3,4,5,6,7,8]
c.reverse()
print(c)


# sort in str
''' in str sort is used
and arrnges by 1st letter
of a words'''
d=["aaram","how",'main','tum']
d.sort()
print(d)
d.sort(reverse=True)
print(d)
print(d.reverse())

# INSERT
''' adds a new element at 
a particular index(position)
and merge new list with 
old list'''
list = [1,2,3,4,5,6,7,8]
print(list)
list.insert(4,"faijan")
print(list)
list.insert(8,'riya')
print(list)

# EXTEND
''' in extend adds new element
to seperate one by one letter
as a string in square backet
with comma'''

f = [1,2,3,4,5,6]
print(f)
f.extend('apple')
print(f)
f.extend('kalua')
print(f)

# REMOVE
# use list.remove(int,str,etc)
''' it reomves a particular first
choosen element'''

l1 = [2,1,3,4,1,6,1,7]
l1.remove(1)
print(l1)
l1.remove(7)
print(l1)

# POP
''' removing an element by 
taking their position of a list
and also can print the
elements by taking their position
'''
l1=[1,2,45.5,87,2+3j,8,"faijan"]
print(l1)
print(len(l1))
print(l1[1:4])
print(l1[-5:len(l1)])
l1.pop(6)
print(l1)
l1.pop(3)
print(l1)

# 2nd question
l2 = [1,"faijan", 'riya','rahul',89.0, 78]
print(l2)
print(l2.pop(5))
print(l2.pop(4))
print(l2.pop(2))

# CLEAR
''' it clears the all elements
from the list'''
l = [1,2,3,4,5,6,7,'how are u?']
print(l)
l.clear()
print(l)
print(l.clear())

# DELETE
''' it delete element by 
taking their position'''
l = [1,2,3,4,5,6,7,2+3j]
print(l) 
del l[1]
print(l)
del l[5]
print(l)
del l[::2]
''' [::2] means delete all element
which is not multiple of 2'''
print(l)

# INDEX
''' it counts the first occurence 
position of a element in a list'''
f = [1,2,4,6,7,"faijan",'rahul',89.8,90.6]
print(f) 
f.index(2)
print(f)
print(f.index(2))
print(f.index("faijan"))
print(f.index('rahul'))

p = [1,2,2,3,4,5,43,4,3,5,3,5]
print(p)
print(p.index(2))
print(p.index(4))
print(p.index(5))


# COUNT
''' it count(how many times an element is ocuurs)
in a list'''
l=[1,2,3,4,5,4,3,21,1,2,3,4]
print(l)
print(l.count(1))
print(l.count(2))
print(l.count(5))


# sum,minimum,maximum in a list
b = [1,2,-3, 5 ,-5,10,4]
print(b)
print(max(b)) # biggest number in a list
print(min(b)) # smallest number in a list
print(sum(b)) # addition of list
print(len(b)) # length of list


# COPY
l1 = [1,2,3,4,5,6]
print(l1)
l2=l1.copy()
print(l2)