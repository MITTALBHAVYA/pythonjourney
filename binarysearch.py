def binary_search(a,b):
    low=0
    high=len(a)-1
    while low<=high:
        mid=int((low+high)/2)
        if a[mid]==b:
            return mid
        elif a[mid]>b:
            high=mid-1
        else:
            low=mid+1
            
    return -1     
        
a=[1,2,3,4,5,6,7,8,9]
b=int(input("ENTER THE NUMBER TO BE SEARCHED \n"))
result=binary_search(a,b)
print(f"okk bro here your result {result}")