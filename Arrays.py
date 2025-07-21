<<<<<<< HEAD
import array
arr= array.array("i",[1,2,3,4,5,6])
print(arr)

arr[0]
arr.append(7)
print(arr)

arr.insert(6,8)
print(arr) 

arr.remove(8)
print(arr)

arr1=array.array('i',[9,10,11])
arr.extend(arr1)
print(arr)
 
temp_list=[12,13,14]
arr.fromlist(temp_list)
print(arr)

arr.remove(14)
print(arr)

arr.pop()
print(arr)

print(arr.index(11))

arr.reverse()
print(arr)

print(arr[0:4])
print(arr)

import numpy as np
twoDArray=np.array([[11,15,16,6],[2,4,1,5],[45,12,45,67]])
print(twoDArray)

newTwoDArray=np.insert(twoDArray,0,[[2,4,5]],axis=1)
=======
import array
arr= array.array("i",[1,2,3,4,5,6])
print(arr)

arr[0]
arr.append(7)
print(arr)

arr.insert(6,8)
print(arr) 

arr.remove(8)
print(arr)

arr1=array.array('i',[9,10,11])
arr.extend(arr1)
print(arr)
 
temp_list=[12,13,14]
arr.fromlist(temp_list)
print(arr)

arr.remove(14)
print(arr)

arr.pop()
print(arr)

print(arr.index(11))

arr.reverse()
print(arr)

print(arr[0:4])
print(arr)

import numpy as np
twoDArray=np.array([[11,15,16,6],[2,4,1,5],[45,12,45,67]])
print(twoDArray)

newTwoDArray=np.insert(twoDArray,0,[[2,4,5]],axis=1)
>>>>>>> 03f848e (Ignore virtual environment)
print(newTwoDArray)