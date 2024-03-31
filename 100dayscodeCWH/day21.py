#functions mahagatha
#default argument
def average(num1=10,num2=20):
    print((num1+num2)/2)
average()
#can ask for change in values
average(20)
average(30,50)
#keyword argument 
def average2(numb1,numb2):
    print((numb1+numb2)/2)
average2(numb2=6,numb1=4)
#required argument 
def average3(n1,n2):
    print((n1+n2)/2)
average3(1,3)
#variable length argument
def average4(*s):
    sum=s[0]+s[1]+s[2]
    print(sum/len(s))
average4(5,6,9)
#return statement 
def average5(*s):
    sum=s[0]+s[1]+s[2]
    return sum/len(s)
ans=average5(8,9,7)
print(ans)