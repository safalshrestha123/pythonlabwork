'''10. Write a prohram to convert sec into day, hours,minute and day.'''

second= int(input('Enter the value for second:'))

day= (((second//60)//60)//24)
print(f'Total day for given seconds:{day}')

hour= ((second//60)//60)
print(f'Total hour for given seconds:{hour}')

minute= (second//60)
print(f'Total minute for given second:{minute}')

