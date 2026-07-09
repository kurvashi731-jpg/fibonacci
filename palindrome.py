def is_palindrome(n):
    s=str(n)
    return s==s[::-1]
num =input("Enter a number:")
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not  a palindrome.")