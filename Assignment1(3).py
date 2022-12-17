Series = (1,2,3,4,5,6,7,8,9,10)
print ("Series of Numbers : ",Series)
even_num = 0
odd_num = 0
x = 0  
while(x < len(Series)):
    if Series[x] % 2 == 0:
        even_num = even_num + 1
    else:
        odd_num = odd_num + 1   
    x = x + 1    
print("Number of even numbers: ", even_num)
print("Number of odd numbers ", odd_num)
