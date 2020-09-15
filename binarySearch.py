# Python program for implementation of Binary Serach
# Function needs an Soterd array and element to be found
pos = -1
def BinarySearch(arr,x):
    lb = 0       # Lower bound of list arr
    ub= len(arr)-1 # Upper bound of list arr
    
    # Traverse through all array elements 
    while lb <= ub:
        # mid is the index of mid position in list arr
        mid = (lb + ub) // 2
        #  Condtion to check wheather the element if found or not
        if arr[mid] == x:
            #return True and set pos where the serached no is found
            globals()['pos'] = mid+1
            return True
        #shifting of mid positon 
        else:
            if arr[mid] < x:
                lb = mid
            else:
                ub = mid
    # If no elenmt if found function will return False
        
# TEST
a = [2,23,54,75,87,203,242,424]
n = 75
if BinarySearch(a,n):
    print(pos)


