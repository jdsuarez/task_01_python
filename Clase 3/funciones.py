name = input('Introduce your name please: ')
print('your name is: ' + name)
##------------------------------------------
salary = input('Introduce your salary please: ')
print('your salary is: ' + str(int(salary)+200000))
atv = 0.19
print('The atv over your salary is: ' + str((float(salary)+200000)*atv))
print('the total value is: '+ str((float(salary)+200000) + (float(salary)+200000)*atv))