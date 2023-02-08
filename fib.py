n = input("give me a number ")
n=int(n)
fact = 1

for i in range(1,n+1,1):
    fact=fact * i

print("the factorial of ", n, "is ", fact)
