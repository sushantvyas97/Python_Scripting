def countstr(lst):
    ct=0
    for x in lst:
        temp=len(x)
        if temp>=2 and x[0]==x[temp-1]:
            ct+=1
    return ct

input=['axa', 'xyz', 'gg', 'x', 'yyy']
input1=['x', 'cd', 'cnc', 'kk']
input2=['bab', 'ce', 'cba', 'syanora']
print(countstr(input))
print(countstr(input1))
print(countstr(input2))
