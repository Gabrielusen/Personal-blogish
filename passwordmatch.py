import re


capReg = re.compile(r'.*[A-Z].*')
lowerReg = re.compile(r'.*[a-z].*')
digitReg = re.compile(r'.*\d.*')


def check_password(text):
    if capReg.search(text) and lowerReg.search(text) and digitReg.search(text):
        return "Strong password"
    else:
        return 'Weak password'


while True:
    pw = input('Enter your password: ')
    print(check_password(pw))
