# 1
def countd(num):    
    new_arr = [] 
    for n in range(num,-1,-1):
        new_arr.append(n)
    return new_arr
print(countd(5))
#__________________________________
# # 2 
 def print_return(arr):
     print(arr[0]) 
     return arr[1]
print(print_return([1,2]))    
# _________________________________- 
#3 

def firts_plus_len (arr):
    first = arr[0]
    length = len(arr)
    
    return first + length 
print (firts_plus_len([1,2,3,4,5]) )
#__________________
#4
def  grater_than_second (arr):
    second =arr[1]
    new = []
  
    for i in range(len(arr)):
        if arr[i] > second : 
            new.append(arr[i])
    print( len(new))
    return new 

print(grater_than_second([5,2,3,2,1,4]))

#______________________________________
#5      
def size_vale(first, second):
    new = []
    for i in range(0,first):
        new.append(second)
    return new 
print(size_vale(3,6))