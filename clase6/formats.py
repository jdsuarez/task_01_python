num1 = 15
num2 = 43

message = 'The numbers are '+ str(num1) + ', ' + str(num2)
print(message)

message = 'the numbers are {}, {}'.format(num1,num2)
print(message)

message = 'the numbers are {1}, {0}'.format(num1,num2)
print(message)

message = 'the numbers are %d, %d'%(num1,num2)
print(message)

message = f'the numbers are {num1}, {num2}'
print(message)