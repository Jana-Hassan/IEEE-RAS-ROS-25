def is_palindrome(w):
    return w == w[::-1]

w = input()
if is_palindrome(w):
    print(f"The word '{w}' is a palindrome.")
else:
    print(f"The word '{w}' is not a palindrome.")