def sortwithspecs(lst):
    xlst=[]
    appndr=[]
    for i in lst:
        if i[0]=='x':
            xlst.append(i)
        else:
            appndr.append(i)
    xlst.sort()
    appndr.sort()
    xlst.extend(appndr)
    return xlst

lst=['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
lst1=['bbb', 'ccc', 'axx', 'xzz', 'xaa']

print(sortwithspecs(lst))
print(sortwithspecs(lst1))
