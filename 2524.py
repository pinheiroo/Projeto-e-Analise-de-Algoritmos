#versão 1 (não consegui memoizar)
def ContaBalas(children:int,packs:list,i:int):
    if i == 0:
        return 0
    if sum(packs)%children == 0:
        return i
    else:
        top_i = 0
        for j in range(len(packs)):
            if packs[j] != 0:
                prev = packs[j]
                packs[j]=0
                top_i = max(top_i,ContaBalas(children,packs,i-1))
                packs[j]=prev
        return top_i

#versão 2 (memiozada e funcional)
'''
def ContaBalas(children:int,packs:list,lenp:int,sump:int,count:int,memo:list):
    if lenp < 0:
        memo[lenp][count] = 0
    if memo[lenp][count]==None:
        if sump%children == 0:
            memo[lenp][count] = len(packs)-count
        else:
            memo[lenp][count] = max(ContaBalas(children,packs,lenp-1,sump,count,memo),ContaBalas(children,packs,lenp-1,sump-packs[lenp-1],count+1,memo))
    return memo[lenp][count]
'''
dim = input().split()
while dim != '0 0':
    children = int(dim[0])
    mount = int(dim[1])

    packs = input().split()
    for i in range(mount):
        numero = int(packs[i])
        packs[i] = numero

    memo = [[None for _ in range(len(packs)+1)]for _ in range(len(packs)+1)]
    print(ContaBalas(children,packs,len(packs)))
    dim = input().split()