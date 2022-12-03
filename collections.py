# Collections = single variable used to store multiple variables
# List = [] ordered and changeable ,Duplicates OK
# Tuple = () ordered and unchangeable,Duplicates Ok faster
# Sets = {} unordered and immutable,No duplicates

fruits = ["apple","orange","mango"]
print("apple" in fruits)
# same for others
# this will return a boolean
# if you want to insert a value at certain index
fruits.insert(0,"pineapple")
# to sort a list any order use fruits.sort()
fruits.count("apple")
# returns the number of times apple has occured in the list
