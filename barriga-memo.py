def opt(n:int,A:list,i:int,j:int,memo:list):
    if i>=n:
        return 0
    if A[i][1]>=A[j][1] or (A[i][2] == 'VERMELHO' and A[j][2] == 'LARANJA') or (A[i][2] == 'LARANJA' and A[j][2] == 'AZUL') or (A[i][2] == 'AZUL' and A[j][2] == 'VERDE') or (A[i][2] == 'VERDE' and A[j][2] == 'VERMELHO'):
        return opt(n,A,i+1,j,memo)
    elif memo[i]==None:
        memo[i] = max(A[i][0] + opt(n,A,i+1,i,memo),opt(n,A,i+1,j,memo))
    return memo[i]



oi = input()
while oi!='0':
    n = int(oi)+1
    A = list([None for _ in range(3)]for _ in range(n))

    for i in range(n-1):
        A[i]=list(input().split())
        for j in range(2):
            numero = int(A[i][j])
            A[i][j] = numero

    A[n-1] = [0,9999,'BASE']

    memo = [None for _ in range(n+1)]
    A.sort(key=lambda x: x[1],reverse = True)
    print(opt(n,A,0,0,memo))
    oi = input()