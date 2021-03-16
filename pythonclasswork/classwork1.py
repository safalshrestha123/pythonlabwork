'''write aprogram to find am or pm from the time given by the user
'''
time = int(input('enter the time:'))
if time <= 12:
    print('it is am ')
else:
    print("it is pm")