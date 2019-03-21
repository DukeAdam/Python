# Implement a recursive math function
def function(n):
    if n == 2:
        return 2
    else: return 4*function(n-1)-3*n


read = int(input())
print(function(read))