set_data = {10,2,3,4,5}

print(set_data)

set_data.pop() # pop() removes random element, hence we cannot sure which element will be removed.
print(set_data)

set_data.clear() # clear() method clears the data i.e. makes the given set empty but still you can access it
print(set_data)

set_data = {10,2,3,4,5}
del set_data  # del removes entire variable itself from the memory, hence we cannot access it
print(set_data)