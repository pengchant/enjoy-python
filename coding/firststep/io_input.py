def reverse(text):
    return text[::-1]

def is_palindrome(text):
    return text == reverse(text)

something = input("Enter text:")
if is_palindrome(something):
    print('yes,it is a palidrome')
else:
    print('no,it is not a palindrome')


