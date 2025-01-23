x = 3
y= float(3.8)
print(x, y)

print(type(y))
import random
print(random.randint(1, 6))
x = "   m, ,a,l,i,k"
print(x[1])
for u in "m,a,l , ik":
    print(u)
print(len(x))
print("ma l" not in x)
print(x[2:])
for n in x:
    print(n)
    if n == "l":
        break 
print(x.strip())
print(x.replace("l", "j"))
# print(x.split(","))
print(x + "ki")
print("x,{} {}".format(4444, "mmmm"))
f = "b"
h = "b"
print(f is not h)
j = ["malik", "amzat", "chika"]
print(j[1:2])
print("malijk" in j)
j.insert(1, "ayodeji")
j.append("mary")
print(j)
kk = ["bolaji", "tope", "rejoice"]
j.extend(kk)
print(j)
j.pop()
print(j)
for i in range(len(j)):
    print(j[i])
lk = [x.upper() for x in j if "a" in x]
print(lk)
ll = [x if x != "tope" else "temitope" for x in j]
print(ll)
j.sort()
print(j)
# pp = [78, 9, 87, 1, 3]
pp = [100, 20, 75, 50]
pp.sort(key=lambda n: n - 50)
print(pp)
