Input = ["www.annauniv.edu", "www.google.com", "www.ndtv.com",
         "www.website.org", "www.bis.org.in",
         "www.rbi.org.in"]

def domain_filter(Input):
    return Input.split('.')[-1]

Output = sorted(Input, key=domain_filter)

print("Initial list:")
print(Input)
print("Sorted list:")
print(Output)
