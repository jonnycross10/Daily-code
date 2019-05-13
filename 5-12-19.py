def numberDecoded(str):
  value = 0
  length = len(str)
  for i in range(0,length):
      value= value + (length-i) 
      i=i+1
  return value


str = '123'
print(numberDecoded(str))
str1 = '12'
print(numberDecoded(str1))
str2 = '1534234'
print(numberDecoded(str2))
