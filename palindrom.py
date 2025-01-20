#palindrom Number


num=input("enter a number")

if num==num[::-1]:
    print(num,"is a palindrome number")
else:
    print(num,"is not a palindrome number")
