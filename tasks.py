#1.List Iteration and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.
list = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
for x in list:
    if (x%5==0):
     print(x)
     if (x==150):break
    
#2. Reverse the list in python using FOR loop
list1 = [10, 20, 30, 40, 50]
for i in reversed(list1):
  print(i)

#2.Reverse the list in python using FOR loop
list1 = [10, 20, 30, 40, 50]
list1.reverse()
for i in list1:
  print(i)
  
#3.Display numbers from -10 to -1 using for loop
mylist=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
mylist.reverse()
for i in mylist:
  print(i)

#3.Display numbers from -10 to -1 using for loop
mylist=[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
for i in reversed(mylist):
  print(i)

#3.Display numbers from -10 to -1 using for loop
for i in range(-10,0):
  print(i)

#4.Display a message “Done” after successful execution of for loop
for i in range(6):
 print(i, end=" ")
if i==5:
    print("Done!")

#5.Create a function that can accept two arguments name and age and print its value
def demo(name,age):
  print(name,age)
demo("Krishna",30)

#6.Write a function calculation()
def calculation(a,b):
    return a+b, a-b
res = calculation(40, 10)
print(res)

#7. Create a function showEmployee()
def showEmployee(name, salary=9000):
    print("Employee", name, "salary is:", salary)

showEmployee("Ben", 9000)
showEmployee("Ben")

#8.Generate a Python list of all the even numbers between 4 to 30
start,end=4,30
for num in range(start, end):
  if num%2==0:
   print(num,end=" ")

#9.Return the largest item from the given list
aList = [4, 6, 8, 24, 12, 2]
aList.sort()
print(aList[5])

#9.Return the largest item from the given list
bList = [4, 6, 8, 24, 12, 2]
print(max(bList))

#10.two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res = dict(zip(keys, values))
print(res)

#10.two lists convert it into the dictionary
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res = {keys[i]: values[i] for i in range(len(keys))}
print(res)


  
