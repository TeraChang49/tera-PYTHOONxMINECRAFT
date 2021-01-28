A=[10,25,31]
for i in range(len(A)):
    for j in range(1,len(A)):
        if A[i]<A[j]:
            T=A[i]
            A[i]=A[j]
            A[j]=T
print(A)