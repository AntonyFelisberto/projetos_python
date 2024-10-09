myset={"iPhone","Pixel","Samsung"}
print(myset)

mySet = {"iPhone", "Pixel", "Samsung"}
for mbl in mySet:
  print(mbl)

mySet = {"iPhone", "Pixel", "Samsung"}
mySet.add('OnePlus')
print(mySet) # prints {'iPhone', 'Samsung', 'OnePlus', 'Pixel'}

"""
Method	Description	Usage
add()	to add an element to the set	mySet.add('value')
clear()	to remove all the elements from the set	mySet.clear()
pop()	to remove last element from the set	mySet.pop()
remove()	to remove a specified element from the set	mySet.remove("value")
del()	to delete a set	del myset
copy()	to return a copy of the set	copySet = mySet.copy()
difference()	to return a set containing the difference between two or more sets	mySet3 = mySet1.difference(mySet2)
difference_update()	to remove the items present in a set that are also included in another set	mySet1.difference_update(mySet2)
discard()	to remove a specified item	mySet.discard("value")
intersection()	to return a set which is the intersection of two other sets	mySet3 = mySet1.intersection(mySet2)
intersection_update()	to remove the items in this set that are not present in other set	mySet1.intersection_update(mySet2)
isdisjoint()	to return whether two sets have a intersection or not	mySet3 = mySet1.isdisjoint(mySet2)
issubset()	to return whether another set contains this set or not	mySet3 = mySet1.issubset(mySet2)
issuperset()	to return whether this set contains another set or not	mySet3 = mySet1.issuperset(mySet2)
symmetric_difference()	to return a set with the symmetric differences of two sets	mySet3 = mySet1.symmetric_difference(mySet2)
symmetric_difference_update()	to insert the symmetric differences from this set and another	mySet1.symmetric_difference_update(mySet2)
union()	to return a set containing the union of sets	mySet3 = mySet1.union(mySet2)
update()	to update the set with the union of this set and others	mySet1.update(mySet2)
"""