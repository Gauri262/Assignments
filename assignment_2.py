#Arithmetic operator
print("Arithmetic operator:")

print(" 3 + 4 = ",3+4)
print(" 7 - 5 = ",7-5)
print(" 3 * 4 = ",3*4)
print(" 10 / 5 = ",10/5)
print(" 10 // 5 = ",10//5)
print(" 10 % 5 = ",10%5)
print(" 10**5 = ",10**5)

#Assignment operator
print("Assignment operator")

a=5
print("value of a is:", a)
a+=5
print("a +=5 ",a)
a-=1
print("a -=1 ",a)
a*=5
print("a *=5 ",a)
a/=9
print("a /=9 ",a)
a%=3
print("a %=3 ",a)
a//=2
print("a //=2 ",a)

#comparison operator
print("comparison operator")
b=10
c=15
print("a == b? ",a==b)
print("a != b? ",a!=b)
print("a > b? ",a>b)
print("a < b? ",a<b)
print("a >= b? ",a>=b)
print("a <= b? ",a<=b)

#logical comparison
print("logical comparison")
d=True
e=False
print("d and e = ",d and e)
print("d or e = ",d or e)
print("not e = ", not e)

#bitwise operator
print("bitwise operator")
f=8
g=9
print("f >> g = ",f>>g)
print("f << g = ",f<<g)

#identity operator
print("identity operator")
print("f is g ? ", f is g)
print("f is not g ? ", f is not g)

#membership operator
print("membership operator")
arr=["a","b","c"]
print("'b'' is present in arr?",'b' in arr)
print("'b' is not present in arr?",'b' not in arr)