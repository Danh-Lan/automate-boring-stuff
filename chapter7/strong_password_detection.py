#! python
# strong_password_detection.py - Check for good enough password

import re 

lengthCheck = re.compile(r'.{8,}')
uppercaseCheck = re.compile(r'.*[A-Z].*')
lowercaseCheck = re.compile(r'.*[a-z].*')
digitCheck = re.compile(r'.*[0-9].*')

def main():
  password = 'Az12345678'
  if (lengthCheck.fullmatch(password) and
    uppercaseCheck.fullmatch(password) and
    lowercaseCheck.fullmatch(password) and
    digitCheck.fullmatch(password)):

    print("Password is strong.")
  else:
    print("Password is not strong.")

if __name__ == "__main__":
  main()
