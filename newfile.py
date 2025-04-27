list = [11, 22, 33, 44, 55, 2.2, 3.3, 4.4, 5.5, 6.6, "apple", "banana", "cherry", "date", "elderberry"]
print(list)

list.append(77)
print(list)

x = []
print(x)

x.insert(0, 15)
x.insert(1, 25)
x.insert(2, 35)
x.insert(3, 45)
print(x)

y = [12, 14, 18, 17, 16, 11, 13, 19, 10, 15]
print(y)

y.sort()
print(y)

y.sort(reverse=True)
print(y)

m = ["zebra", "lion", "giraffe", "elephant", "tiger", "bear", "wolf", "fox", "dog", "cat"]
print(m)

m.sort()
print(m)

m.sort(reverse=True)
print(m)

g = []
print(g)

g.insert(0, 3)
g.insert(1, 5)
g.insert(2, 7)
g.insert(3, 9)
print(g)

k = [25, 35, 45, 55, 65, 75]
print(k)

print(max(k))
print(min(k))

q = [5, 10, 15, 20, 25, 30]
print(q)

p = [35, 40, 45, 50, 55, 60, 65]
print(p)

print(q + p)

my = [7, 14, 21, 28, 35.5, "sun", 42.7, "moon"]
print(my)

my.append(100)
print(my)

my.insert(6, 88)
print(my)

my.remove(35.5)
print(my)

my.pop(0)
print(my)

my.copy()
print(my)