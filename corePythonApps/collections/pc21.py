set_data = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#set_data.remove(50) # remove method will raise an exception if key is not available in set
set_data.remove(9)

[print(item) for item in set_data]

set_data.discard(8)
print(set_data)

set_data.discard(30) # discard method removes element if available otherwise simply it ignores that key and will not raise exception
print(set_data)