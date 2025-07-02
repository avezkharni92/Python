#Need to find Average Temoer given number of days and Give how many days temp is more than average 
# 1. Take the integer input of number of days
# 2. Take the input from User for temperature for each day. Use for loop
# 3. Calculate the average of temperature by taking the complete sum
# 4. Make a list / Array to put each days temp. 
# 5. start with variable as 0 and Run through each element of list 
#    and if that value is more than the aveage value increment a variable


numDays = int(input("Enter the number of Days:"))
total = 0
temp_list = []

for i in range(numDays):
    temp = float(input("Enter Day" + str(i+1) + "Temperature :"))
    total+= temp
    temp_list.append(temp)

avg = round(total/numDays, 2)
print(f"Average of temperature is {avg}")
num_high_temp = 0

for j in temp_list:
    if j > avg:
        num_high_temp += 1

print(num_high_temp)
