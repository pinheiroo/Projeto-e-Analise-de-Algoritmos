def Doces(camp:list,i:int):
    if i<0:
        return 0
    else:
        return max(camp[i] + Doces(camp,i-2),Doces(camp,i-1))


dim = list(input().split())
while dim[0]!='0' and dim[1]!='0':
    m = int(dim[0])
    n = int(dim[1])


    camp = [[None for _ in range(n)]for _ in range(m)]
    A = [None for _ in range(m)]
    for i in range(m):
        camp[i] = list(input().split())
        for j in range(n):
            numero=int(camp[i][j])
            camp[i][j]=numero

    for i in range(m):
        A[i]=Doces(camp[i],len(camp[i])-1)
    print(A)
    print(Doces(A,m-1))
    dim = list(input().split())