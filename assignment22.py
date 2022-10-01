# 1. Write a recursive python function to calculate sum of first N natural numbers
# 2. Write a recursive python function to calculate sum of first N odd natural numbers
# 3. Write a recursive python function to calculate sum of first N even natural numbers
# 4. Write a recursive python function to calculate sum of squares of first N natural
# numbers
# 5. Write a recursive python function to calculate sum of cubes of first N natural numbers
# 6. Write a recursive python function to calculate the factorial of a number.
# 7. Write a recursive python function to calculate sum of the digits of a given number
# 8. Write a recursive python function to print binary of a given decimal number.
# 9. Write a recursive python function to print octal of a given decimal number
# 10. Write a recursive python function to find the Nth term of the Fibonacci series.


# 1) .................................
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return n + sum(n-1)
# print(sum(int(input("Enter n : "))))


# 2) .......................................
# def sum_odd(x,n):
#     if x>n:
#         return 0
    
#     return x+sum_odd(x+2,n)
# print(sum_odd(1,int(input("Enter n : "))))


# 3) ..............................
# def sum(n):
#     if n==2:
#         return 2
#     else:
#         return n + sum(n-2)
# print(sum(int(input("Enter


# 4) ..................................
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return pow(n,2) + sum(n-1)
# print(sum(int(input("Enter n : "))))


# 5) ..................................
# def sum(n):
#     if n==1:
#         return 1
#     else:
#         return pow(n,3) + sum(n-1)
# print(sum(int(input("Enter n : "))))


# 6) ..................................
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n * fact(n-1)
# print(fact(int(input("Enter n : "))))

# 7) .....................................
# def sum(n):
#     if n==0:
#         return 0
#     else:
#         return (n%10 + sum(n//10))

# print(sum(int(input("Enter n : "))))


# 8) ..................................
# def binary(n):
#     if n==0:
#         return 0
#     else:
#         return bin(n)
    
# print(binary(int(input("enter n : "))


# 9) .....................................
# def binary(n):
#     if n==0:
#         return 0
#     else:
#         return oct(n)
    
# print(binary(int(input("enter n : "))

# 10) .............................
def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return (fib(n-1)+ fib(n-2))
    
a=int(input("Enter N : "))
for i in range(a):
    print(fib(i))
