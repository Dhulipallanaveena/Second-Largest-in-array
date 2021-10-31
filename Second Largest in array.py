from sys import stdin


def secondLargestElement(arr, n):
    if n<2:
        return -2147483648
    res=arr.count(arr[0])==n
    if res:
        return -2147483648
    arr.sort()
    i=n-1
    while i>0:
        if arr[i]!=arr[i-1]:
            return arr[i-1]
        else:
            i=i-1
    

        
        
     
        
                         
    
    
    
        

    
     #Your code goes here



























#Taking Input Using Fast I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n != 0:
        arr = list(map(int, stdin.readline().rstrip().split(" ")))
        return arr, n

    return list(), 0



#main
t = int(stdin.readline().rstrip())

while t > 0 : 
    
    arr, n = takeInput()
    print(secondLargestElement(arr, n))

    t -= 1
