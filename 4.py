def lst_elmnt_filter(tpl):
     return tpl[-1]

def sort_with_specs(lst):
    output=sorted(lst, key=lst_elmnt_filter)
    return output

input1=[(1,3), (3,2), (2,1)]
input2=[(1,7), (1,3), (3,4,5), (2,2)]

print(sort_with_specs(input1))
print(sort_with_specs(input2))
