#using if else elif 
#if else elif is used in conditions 
#if is used to check conditon and if the condition fails then it goes with elif 
# if all the conditions fails to be true then it goes with else

#temp classifier
temp= 22
if temp>30:
    print("weather is hot today")
elif temp>20:
    print("weather is warm outside")
elif temp>10:
    print("weather is cool")
else:
    print("weather is cold outside")

#else as fallback
username="Kirtika"
if len(username)>0:
    print(f"welcome,{username}")
else:
    print("error:username cannot be empty")

#setting a default value
username=''
display_name= username if username else "guest"
print("welcome",display_name)

#MATCH it is used to avoid the use of if else or elif instead use MATCH to perfrom diff action on diff condition
day =4 
match day:
    case 1:
        print("mon")
    case 2:
        print("tues")
    case 3:
        print("wed")
    case 4:
        print("thurs")
    case 5:
        print("fri")
    case 6:
        print("sat")
    case 7:
        print("sun")
#combine values instead writing eacg condition
day=4
match day:
    case 1|2|3|4|5:
        print("today is weekday")
    case 6|7:
        print("today is weekend")

#while loop 
#we can run a statement as long as it is true
i=1
while i<6:
    print(i)
    i +=1

#by using break we can stop the loop even if the statement is true
i=1
while i <6:
    print(i)
    if i ==3:
        break
    i+=1

#by using continue we can skip that iteration 
i=1
while i <6:
    print(i)
    if i==3:
        continue
    i+=1

#while loop with if else statement
i=1
while i <6:
    print(i)
    i+=1
else:
    print("i is no longer less than 6")

#for loop 
#we can execute a set of statement once for each item in list,set,tuple
fruits=["banana","apple","pienapple","cherry"]
for x in fruits:
    print(x)
    if x == "apple":
     break

#continue:skip the iteration
for x in fruits:
    if x == "apple":
     continue
    print(x)

#Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished")

#Break the loop when x is 3, and see what happens with the else block.
for x in range(3):
    print(x)
    if x==3:
        break
