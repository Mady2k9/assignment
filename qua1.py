# 1. Create the below pattern using nested for loop in Python.
#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*
for i in range(5):
    for j in range(i+1):
        print("*",end="")
    print()
for i in range(5):
    for j in range(5-i):
        print("*",end="")
    print()