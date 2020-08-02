#This is a Calorie Counting Machine...
#Coolstuff bro.

print("Hi Bro! \n")
print("Calorie Counting V1 Starting... \n")

print("Today's Date?")
date = str(input())
print("Breakfast Calories?")
bfast_cal = int(input())
print("Lunch Calories?")
lunch_cal = int(input())
print("Dinner Calories?")
dinner_cal = int(input())
cal_sum = bfast_cal + lunch_cal + dinner_cal
print("Calorie content for " + date + ": "+ str(cal_sum))