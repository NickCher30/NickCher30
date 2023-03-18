s = input().split()
a =dict()
for i in range(0, len(s) - 1, +2):
    a[int(s[i])]  =int(s[i + 1])
print(a)
list_d = list(a.items())
print(list_d)
list_d.sort(key=lambda i: i[1])
print(list_d)

result = []
for aa in  list_d:
        result.append(aa[0])
print(result)