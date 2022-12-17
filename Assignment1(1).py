Var=(input("Enter end number: "))
Num=(int(Var))

Val_1 = 0
Val_2 = 1
print(Val_1,end=" ")

while Val_2 < Num:
    print(Val_2,end=" ")
    
    (Val_1 , Val_2) = (Val_2 , (Val_1+Val_2))
    
  