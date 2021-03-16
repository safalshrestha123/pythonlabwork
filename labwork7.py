'''you live 4 miles from university .the bus drives at 25mph but spends 2 minutes at each of the 10
stops on the way .How long will the bus journey take ? Alternatively,you could run to university . you jog the first
mile at 7mph , then run the next two at 15 mph, before jogging the last at 7 mph again. will this be quiker
or slower than the bus?'''

'''s= int(input('enter the distance (in miles):'))
v= int(input('enter the speed of bus(in mph)'))
t= int(input('enter the time bus stops(in mint):'))
x= (s/v*60)+t
print(x)'''

living_miles_apart= 4
drives_velocity = 25
time_taken= ((living_miles_apart/drives_velocity)*60)

# 2 mint in each stop

time_spend=20
total_time= time_taken+time_spend
print(f'Total time taken by bus is {total_time}')

#jogging

jog_one= ((1/7)*60)
jog_two= ((1/15)*60)
jog_three= ((1/7)*60)
time_walk_time= jog_one+jog_two+jog_three

print(f'time taken by running is {time_walk_time}')
if (time_walk_time<total_time):
    print('Taking bus is slower tha running')
else:
    print('taking bus is quicker than running')
