glass1 = "milk"
glass2 = "juice"

temp = glass1                  #The Values in Variables 'glass1' and 'glass2' are swapped using a temporary variable 'temp' as shown beside.
glass1 = glass2
glass2 = temp

print("Glass 1 has " + glass1)
print("Glass 2 has " + glass2)