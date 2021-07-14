def adjc_rep_remover(lst):
    ans=[]
    i=0
    ans.append(lst[i])
    while(i<len(lst)-1):
        i+=1
        if (lst[i]!=lst[i-1]):
            ans.append(lst[i])
            continue
        if (lst[i]==lst[i-1]):
            continue
    return ans

input1=[1,2,2,3]
input2=[2,2,3,3,3]

print(adjc_rep_remover(input1))
print(adjc_rep_remover(input2))
