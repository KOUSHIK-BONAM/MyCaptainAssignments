nterms= int(input("number of terms:"));

n1= 0
n2= 1
count = 0

if nterms <= 0:
    print("enter only postivie number");

elif nterms== 1:
    print("the Fibonacci terms upto",nterms,"is:",n1)

else:  
    print ("The fibonacci sequence of the numbers is:")  
    while count < nterms:  
        print(n1)  
        nth = n1 + n2    
        n1 = n2  
        n2 = nth  
        count += 1
