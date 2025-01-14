# a=89
# b=77
# c=66
# d=70
# e=90

# avg= a+b+c+d+e/5

# if(avg>100):
#     print("Average is greater than 100")
#     print("Grade: A")
# elif(avg>80):
#     print("Average is greater than 80")
#     print("Grade: B")

# elif(avg>60):
#     print("Average is greater than 60")
#     print("Grade: C")

# else:
#     print("Average is less than 60")
#     print("Grade: F")

# score = 40
# if score>=90:
#     print("grade:A")

# elif score>=70:
#     print("grade:C")
# elif score>=60:
#     print("grade:D")
# else:
#    print("grade:F")

# weather=str(input("choose your favourite weather:"))
# if weather == "sunny":
#     print("It's a beautiful day!")

# elif weather == "rainy":
#     print("It's raining today.")
# else:
#     print("build a snowman")

# Ride=int(input("choose your favourite Ride:"))
# if Ride<3:
#     print("walk")

# elif Ride >15:
#     print("car")
# else:
#     print("bike")

# order_size=str(input("choose order:"))
# extra_shot=bool(input("chooseextra shot"))
# if extra_shot == True:
#     coffee = order_size+"coffee with extra shot"
#     print(coffee)
# else:
 
#     print("no coffee")

#check leap year

# year =int(input("enter a year:"))

# if(year%400==0) or (year%4==0 and year%100!=0):
#     print(year, "is a leap year")
# else:
#     print(year, "is not a leap year")

   
# pet =str(input("enter your pet:"))
# age =int(input("Enter the age of your pet:"))

# if(age<=2):
#     print("puppy food",pet)
# elif(age>=5):
#     print("cat food", pet)
# else:
#     print("no food", pet)

#how many positive numbers are there in the list
# list=10
# c=0
# for i in range(1,list+1):
#     if i%2==0:
#         c+=1

# print("number of even numbers:",c)

#multiplication

# number = int(input("enter a no:"))
# for i in range(1, 11 ): 
#     if i==5:
#         continue
#     print(number,'x',i,'=',number*i)

#reverse a string
# input_str="python"
# reversed_str=""

# for char in input_str:
#     reversed_str = char + reversed_str

# print("Reversed string:", reversed_str)

# #find the first non-repeating character in the string

# input_str = "teeteraabc"

# for char in input_str:
#     print(char)
#     if input_str.count(char)==1:
#         print("First non-repeating character:", char)
#         break

#find the factorial of a number
# number = 5
# factorial=1
# while(number>0):
#     print("Current number:", number)
#     factorial *=number
#     number-=1
# print("Factorial:", factorial)

# while True:
#     number = int(input("enter a number b/w 1 to 10:"))
#     if 1<=number<=10:
#         print("Valid number!")
#         break
#     else:
#         print("Invalid number!")

#check nummber is prime or not

# number = 18
# is_prime = True
# if number>1:
#     for i in range(2,number):
#         if(number%2==0):
#             is_prime = False
#             break

# print(is_prime)

#check duplicate exist?
# items=["apple","bananna","orange","apple","mango"]

 # using a set to remove duplicates
# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("duplicate item", item)
#         break
#     unique_item.add(item)

# import time
# wait_time=1
# max_retries=5
# attempts=0

# while attempts<max_retries:
#     print("attempts",attempts+1,"-wait time", wait_time)
#     time.sleep(wait_time)
#     attempts+=1
#     wait_time*=2


# import math
# def sum(radius):
#    area = math.pi*radius**2
#    cercumfearence = 2*math.pi*radius
#    return area, cercumfearence

# result1 , result2= sum(3)

# print("area:", result1,"cercumfearence:", result2)

def test(name="user"):
      return "Hello,"+ name+"!"

print(test()) 
