def missingNo(arr):
  count =0
  for j in range(0,len(arr)):
    count =0
    for i in range(0,len(arr)):
      if(j+1!=arr[i]): 
        count= count +1
      if(count == len(arr)): #if all elements are false
        return (j+1)
#should print out the lowest positive number that's not in array      
array1 = [1,3,4]
print(missingNo(array1))
array2 = [3,4,-1,1]
print(missingNo(array2))
array3 = [1,2,0]
print(missingNo(array3))
array4= [2,3,5]
print(missingNo(array4))
