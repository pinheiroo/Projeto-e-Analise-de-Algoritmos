def Doces(camp:list,i:int,memo:list):
    if memo[i]==None:
        if i<0:
            return 0
        else:
            memo[i] = max(camp[i] + Doces(camp,i-2,memo),Doces(camp,i-1,memo))
    return memo[i]


dim = list(input().split())
while dim[0]!='0' and dim[1]!='0':
    m = int(dim[0])
    n = int(dim[1])


    camp = [[None for _ in range(n)]for _ in range(m)]
    memo = [None for _ in range(n)]
    A = [None for _ in range(m)]

    for i in range(m):
        camp[i] = list(input().split())
        for j in range(n):
            numero=int(camp[i][j])
            camp[i][j]=numero

    for i in range(m):
        A[i]=Doces(camp[i],len(camp[i])-1,memo)
        memo = [None for _ in range(n)]
        
    memo = [None for _ in range(m)]
    print(Doces(A,m-1,memo))
    print(memo)
    dim = list(input().split())