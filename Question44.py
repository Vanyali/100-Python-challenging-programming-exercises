'''
Write a program which can filter even numbers in a list by using filter function. The list is: [1,2,3,4,5,6,7,8,9,10].

Hints:

Use filter() to filter some elements in a list.
Use lambda to define anonymous functions.

'''

lst = [1,2,3,4,5,6,7,8,9,10]

even_numbers = list(filter(lambda x: x%2== 2, lst))
print(even_numbers)


li = [1,2,3,4,5,6,7,8,9,10]
evenNumbers = filter(lambda x: x%2==0, li)

#In Python 3 filter and map and reduce are now iterable. Like generator we can only iterate over it one of a time.
#Check Various prints with next.
print(evenNumbers.__next__())
print(evenNumbers.__next__())
print(evenNumbers.__next__())
print(evenNumbers.__next__())
print(evenNumbers.__next__())
print(evenNumbers.__next__())

#See each iterations grabs the correct answer until reach end and knows and top stop. That's why empty brackets!