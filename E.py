#На острове живут рыцари и лжецы, их дома расположены по кругу. Они очень любят делиться друг с другом новостями, причём рыцарь
#говорит новость как услышал, а лжец переверает. В нулевой день приезжает путешественник и сообщает жителю дома №1 новость (ложную или истинную).
# а следующее утро житель дома №1 сообщает её своему соседу из дома №2, на второй день житель дома №2 говорит новость соседу из дома №3 и т.д.
#Если лжец говорит правду, он становится рыцарем, а если рыцарь говорит ложь, он умирает вечером того же дня. Если сосед из дома i не находит
#соседа из дома i+1, он идёт к следующему дому. Последний выживший сам с собой не разговаривает. Требуется узнать, кто останется на острове
#через M дней распространения новости.
#Формат входных данных
#Первая строка - N - число жителей острова, через пробел 0 или 1 - истинность новости.
#Далее N строк с описанием жителей, начиная с дома №1: имя и 0 или 1 - лжец или рыцарь.
#M - число дней.
#Формат выходных данных
#Строки с описанием выживших, как во входных данных.


s = input().split()
n = int(s[0])
new = int(s[1])
arr = []
for i in range(0, n):
    s = input().split()
    arr.append([s[0], int(s[1])])


#print(arr)
m = int(input())
cur_new = new
i1 = 0
for k in range(0,m):
    if len(arr) == 1:
        break
    i = i1 % len(arr)
    #print(i1, arr[i], cur_new)
    cur_per = arr[i]
    if arr[i][1] == 1:
        if cur_new != 1:
            arr.pop(i)
            i1 -= 1
    else:
        if cur_new == 1:
            cur_new = 0
        else:
            cur_new = 1
            arr[i][1] = 1
        #if new == cur_new:
    #print(cur_new, arr)
    i1 += 1


for a in arr:
    print(a[0], a[1])
