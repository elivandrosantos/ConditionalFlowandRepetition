security_code = '123'
register_security_code = '123'

password = '1234'
register_password = '1234'

if (security_code == register_security_code) & (password == register_password):
    print('Payment made successfully')
elif (security_code != register_security_code) & (password == register_password):
    print('"Error: Invalid security code"')
elif (security_code == register_security_code) & (password != register_password):
    print('Error: Invalid password')
else:
    print('Error: Invalid security code and password')
