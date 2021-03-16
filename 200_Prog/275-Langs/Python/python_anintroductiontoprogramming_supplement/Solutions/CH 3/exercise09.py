# Palindrome
print("This program tests for palindromes.")
s = input("Enter a string to be tested: ")
j = len(s)-1
ok = True
for i in range (0, len(s)//2):
    if s[i] != s[j]:
        print ("This is not a palindrome.")
        ok = False
        break
    j = j - 1
if ok:
    print ("This is a palindrome.")
print ("----------------------------------------")
