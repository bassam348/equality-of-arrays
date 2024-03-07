#Task 5
#identifing wich list will he create
print("the first list")
Arr1=[]
while True:
#checking if the input integer or not    
    while True:
        try:
            first_input = int(input("please insert your number "))
            break
        except ValueError:
            print("invalid input ")
#puting the input in the list            
    Arr1.append(first_input)
#Asking the user if he wants to finish this list    
    n=input("""If you want to finish insert "no"  
if you do not want press any key
 """)          
    if n =="no": 
        break
print(Arr1)
#identifing wich list will he create
print("the second list")
Arr2=[]
while True:
#checking if the input integer or not    
    while True:
        try:
            second_input = int(input("please insert your number "))
            break
        except ValueError:
            print("invalid input ")
#puting the input in the list                    
    Arr2.append(second_input)
#Asking the user if he wants to finish this list     
    n=input("""If you want to finish insert "no"  
if you do not want press any key
 """)          
    if n =="no": 
        break
print(Arr2)
#Rearrenge the lists
Arr1.sort(reverse=False)    
Arr2.sort(reverse=False)
#checking if the lists are equal or not
if Arr1 == Arr2 :
    print("lists are equal = True")
else:
    print("lists are equal = False")     