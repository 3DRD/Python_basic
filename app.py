# Part of modules
# utils.py part of this file
# also contains three ways to input list of integers
# import utils
from utils import max_from_list,min_from_list

n=int(input("Enter size of List "))
number=[]
# Type 1
# num=input("Enter the list of numbers seperated by space")
# num2=num.split()
# for i  in num2:
#     number.append(int(i))
# print(number)

#Type 2 using one line for loop
# n = int(input("Enter the size of the list "))
# print("\n")
# number = list(int(num) for num in input("Enter the list numbers separated by space ").strip().split())[:n]
# print("User List: ", number)

# Type 3 using map function
# Syntax : map(fun, iter)
# often used to create another list after some operation on main list
# fun : It is a function to which map passes each element of given iterable.
# iter : It is a iterable which is to be mapped.

number = list(map(int, input("Enter the list numbers separated by space ").strip().split()))[:n]
print("User List: ", number)

print(f' MAX : {max_from_list(number)}')
print(f' MIN : {min_from_list(number)}')

