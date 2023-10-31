login = 'MaximumEd'
password = '123456!'
login_input = input('Enter login: ')
password_input = input('Enter password: ')
if login != login_input and password != password_input:
    print('Access denied! Login and password do not match!')
    print("!!!!!!!!!")
elif login != login_input:
    print('Access denied! Login do not match!')
elif password != password_input:
    print('Access denied! Password do not match!')
else:
    print('Access granted!')