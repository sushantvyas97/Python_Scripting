def printdict(dict):
    x=dict["New Arrivals"]
    r=(x["WEB"])
    print(r)
    r = (x["COOKING"])
    print(r)
    r =(x["CHILDREN"])
    print(r)

bookstore={"New Arrivals":{"COOKING":["Everyday Italian", "Giada De Laurent is", "2005", "30.00"], "CHILDREN":["Harry Potter",
                           "J K. Rowling", "2005", "29.99"], "WEB":["Learning XML", "Erik T. Ray", "2003", "39.95"]}}

print("\tBOOKSTORE")
printdict(bookstore)
