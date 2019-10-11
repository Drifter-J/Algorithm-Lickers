def solution(S:str,T:str)->str:
    queue = list(S)
    bucket = str()
    for i,c in enumerate(T):
        while i>0:

        if  c == S[i]:
            bucket += c
            queue.pop(i)
            i+=1
    

S="cba"
T="abcd"
solution(S,T)
