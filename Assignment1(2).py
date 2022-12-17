Name =(input ("Enter the Name: "))
print ("Input : ",Name)   
Reverse = ""  
x = len(Name) 
while x > 0:   
    Reverse = Reverse + Name [x - 1]
    x = x - 1
print ("Output : ",Reverse)