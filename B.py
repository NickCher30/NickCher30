#Двоичная куча - двоичное дерево, в котором выполняются три условия: 1. Значение в любой вершине не меньше, чем значения ее потомков. 2. На i-ом слое 2 i вершин, кроме последнего. 3. Последний слой заполняется слева направо.
#О свойствах 2 и 3 мы уже побеспокоились за Вас. Элемент под номером 0 является корнем дерева. Для элемента под номером i потомки будут
#иметь номера 2*i+1 и 2*i+2 . Например, для элемента 0 потомки будут иметь номера 1 и 2 . Ваша задача проверить данный вам массив на выполнение свойства 1 .
#Формат входных данных
#Дано натуральное число N ≤ 10 5 . Далее идут N элементов |a i | ≤ 10 6 .
#Формат выходных данных
#Необходимо вывести одно слово без кавычек: "YES", если свойство выполняется, иначе "NO".

n = int(input())
arr = input().split()
for i in range(0, n):
    arr[i] = int(arr[i])
f = 0
for i in range(0, n):
    if 2 * i + 1 < n:
        if arr[i] < arr[2 * i + 1]:
            f = 1
            break
    if 2 * i + 2 < n:
        if arr[i] < arr[2 * i + 2]:
            f = 1
            break

if f == 0:
    print("YES")
else:
    print("NO")