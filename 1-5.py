s=input()
l=[]
key="ICE"
m=int(len(s)/3)
key=key*m+"ICE"
for i in range (len(s)):
    c=ord(s[i])^ord(key[i])
    l.append(hex(c))
a="".join(l)
a=a.replace("0x","")
print(a)   
