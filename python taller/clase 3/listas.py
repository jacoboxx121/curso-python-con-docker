array = ["futbol", "pc", 18.6, 18, ["hola", "mundo"], True, False]



print(array[0]) 
print(array[4])  
print(array[0:3])  
print(len(array))  
array.append(66)  
print(array)
array.pop()
print(array)
array.remove("pc")
print(array)
array.clear()
print(array)

array2 = ["futbol", "mundo", 18.6, 18, ["hola", "mundo"], True, False]
array3 = array + array2
print(array3)
print("futbol" in array3)
print(array3.index("baloncesto"))  # This will raise an error if "baloncesto" is not in the list