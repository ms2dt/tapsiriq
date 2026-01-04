# 1
s="aaabbccccd"; r=""; c=1
for i in range(1,len(s)):
    if s[i]==s[i-1]: c+=1
    else: r+=s[i-1]+str(c); c=1
r+=s[-1]+str(c)
print(r)

# 2
s="hellooo!!!"; r=s[0]
for i in range(1,len(s)):
    if s[i]!=s[i-1]: r+=s[i]
print(r)

# 3
a=[3,2,5,6,7,1,2,3]; m=c=1
for i in range(1,len(a)):
    if a[i]>a[i-1]: c+=1; m=max(m,c)
    else: c=1
print(m)

# 4
a=[1,2,3,4,5]; k=2; n=len(a); b=[0]*n
for i in range(n): b[(i+k)%n]=a[i]
print(b)

# 5
a=[0,3,0,1,0,5,2]; b=[]; z=0
for x in a:
    if x==0: z+=1
    else: b.append(x)
b+=[0]*z; print(b)

# 6
n=9875
while n>9:
    s=0
    while n: s+=n%10; n//=10
    n=s
print(n)

# 7
a=[2,7,11,15]; t=9
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==t: print(i,j)

# 8
s1="listen"; s2="silent"; d={}; ok=True
for c in s1: d[c]=d.get(c,0)+1
for c in s2:
    if c not in d or d[c]==0: ok=False
    else: d[c]-=1
print(ok)

# 9
p=[(1,2),(3,4),(-1,0),(0,0)]
p.sort(key=lambda x:x[0]**2+x[1]**2)
print(p[0],p[1])

# 10
m=[[1,2,3],[4,5,6],[7,8,9]]; n=len(m); a=b=0
for i in range(n): a+=m[i][i]; b+=m[i][n-1-i]
if n%2: b-=m[n//2][n//2]
print(a,b)

# 11
t="salam".split(); d={}
for w in t: d[w]=d.get(w,0)+1
print(max(d,key=d.get), max(d.values()))

# 12
x=y=0
for c in "URR":
    if c=="U": y+=1
    if c=="D": y-=1
    if c=="R": x+=1
    if c=="L": x-=1
print((x,y) if (x,y)!=(0,0) else "qayıtdı")
