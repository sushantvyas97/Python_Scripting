import re
str1="""Interface		IP-Address	OK? 	Method Status	Protocol
FastEthernet0/0	192.168.1.242	YES 	manual up	up 
FastEthernet1/0        unassigned	YES 	unset		down 
Serial2/0              	192.168.1.250	YES 	manual up	up 
Serial3/0              	192.168.1.233	YES 	manual up	up 
FastEthernet4/0        unassigned	YES 	unset  		down	
FastEthernet5/0        unassigned	YES        unset 		down"""
x=str1.split("\n")
x=x[1:]
print(x)
for each in x:
    each=each.strip()
    r=re.match("\w+['/']\w",each).group()
    print(r,end=", ")
    if (each.find("manual up")!=-1):
        print("manual up")
    else:
        print("unset")

