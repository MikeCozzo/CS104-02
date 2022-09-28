temp = input("please enter current temperature:")
print ("temperature is:" + temp)
if int(temp)>90:
    print("wear shorts")
elif int(temp)>70:
    print("short sleeves are fine")
elif int(temp)>50:
    print("wear a jacket")
elif int(temp)>32:
    print ("wear a heavy coat")
else:
    print("wear a coat")
