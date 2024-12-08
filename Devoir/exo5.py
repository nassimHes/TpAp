
name1 = input("enter the name of the first runner : ")
time1 = float(input("enter the time of the first runner : "))
name2 = input("enter the name of the second runner : ")
time2 = float(input("enter the time of the second runner : "))

print("Runner 1 : ")
print("Name : " , name1)
print("Time (in seconds): " , time1)
print("Runner 2 : ")
print("Name : " , name2)
print("Time (in seconds): " , time2)

if time1>time2 : print( name1 , " is faster")
elif time1<time2 : print(name2 , " is faster")
else : print( name1, " and " , name2 , " have the same time")