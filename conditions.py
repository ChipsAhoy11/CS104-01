#Starting by setting temp as a variable and asking for the input of the current temperature
temp = input('Please enter the current temperature: ')
temp = int(temp)

if temp > 90:
       print('Wear Shorts')#if temp is greater than 90 do this 
elif temp > 70: 
    print('Short sleeves are fine') #if temp is greater than 70 do this 
elif temp > 50: 
    print('Wear a jacket') #if temp is greater than 50 do this 
elif temp > 32: 
    print('Wear a heavy coat') #if temp is greater than 32 do this 
else: 
    print('Stay inside') #if temp is lower than 32 do this
