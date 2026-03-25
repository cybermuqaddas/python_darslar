'''soz = "Python"
print(soz[0],soz[-1])'''

'''soz = "Programming"
print(soz[3:7])'''
soz = 'Hello'
'''for harf in soz:
    print(harf)'''
'''fruit = ['apple','banana']
fruit.append('cherry')
print(fruit)'''
'''fruit = ['apple','banana']
fruit.insert(1,"orange")'''
'''fruit = ['apple','banana','orange']
fruit.remove('banana')
print(fruit)'''
'''fruit = ['apple','banana','orange']
fruit.clear()
print(fruit)
if  'banana' in fruit:
    print("Bor")'''
'''colors = ("red", "green", "blue", "yellow")
print(colors[-1])'''
'''fruits = ("apple", "banana", "mango", "kiwi")
if 'orange' in fruits:
    print("Yesss")
else:
    print("Afsuuuss")'''
'''tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple3 = tuple1 + tuple2
print(tuple3)'''
'''data = (10, 20, 30, 40, 50)
for dt in data:
    print(dt)'''
'''nums  = (5,10,15,20,25)
son = int(input("Son kiriting: "))
if son in nums:
    print('Son bor')'''
'''son = (1,2,3,4,5,6,7,8,9)
for i in son:
    if i%2==0:
        print(i)'''    
'''sonlar = (10, 20, 30, 40, 50)
yigindi = sum(sonlar)

print(f"Jami yig'indi: {yigindi}")'''

'''d = 11200
son = int(input("Pul miqdorini kiriting: "))
valyuta = son/d
print(f"Sizning pulingiz {valyuta} dollar")'''

'''son = int(input("Son kiriting: "))
son1 = son
a = son1 //1000
b = (son1//100)% 10
d = a * b
print(d)'''
 
'''son = int(input("Son kiriting: "))
son1 = son
a = son1 //100
b = (son1//10)%10
c = son1 % 10
d = (b*100+c*10+a)  
print(d) '''

'''n = int(input("Sekund kiriting: "))
kun = n // 86400
qoldiq_sekund = n % 86400
soat = qoldiq_sekund // 3600
qoldiq_sekund %=3600
minut = qoldiq_sekund // 60
sekund = qoldiq_sekund % 60

print(f"Output: {kun} kun {soat} soat {minut} minut")'''

'''n = int(input("Son kiriting: "))
if n>0:
    print(n*15)
else:
    print(n)'''
'''a = int(input("1-sonnin kiriting: "))
b = int(input("2-sonnin kiriting: "))
c = int(input("3-sonnin kiriting: "))
if a==b:
    print(c)
elif b==c:
    print(a)
elif a==c:
    print(b)
else:
    print(a*b*c)'''
'''a = int(input("Yilni kiriting: "))
if 0<a<50000:
    asr = (a+99)//100
    print(f"{a}-yil {asr}-asrga tegishli.")'''

'''a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
if a==b**2 or b==a**2:
    print("Bir ikkinchisini kvadrati")
else:
    print("Shunchaki sonlar")'''

'''oy = int(input("Oy raqamini kiriting: "))
if 1<=oy<=2:
    fasl='QISH'
elif 3<=oy<=5:
    fasl = 'BAHOR'
elif 6<=oy<=8:
    fasl = 'YOZ'
elif 9<=oy<=12:
    fasl='KUZ'
else:
    print("1 dan 12 gacha bolgan raqamlarni kiriting!")
print(f"hozir {fasl} - fasli")'''
'''a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
yigindi = 0
for i in range(a+1,b):
    yigindi+=i
print(yigindi)'''
'''a = int(input("1-sonni kiriting: "))
b = int(input("2-sonni kiriting: "))
d = b**a
print(f"{b} ning {a} - darajasi:{d} ga teng")'''

'''n = int(input("n sonini kiriting: "))

if n <= 0:
    print("n musbat bo'lishi kerak")
else:
    temp_n = n # Asl qiymatni saqlab turamiz
    while n % 3 == 0:
        n //= 3
    
    if n == 1:
        print(f"{temp_n} - 3 ning darajasi")
    else:
        print(f"{temp_n} - 3 ning darajasi emas")'''

'''print("Kamida 1ta 8 raqami bor ikki xonali sonlar: ") 
for i in range(10,100):
    onlar = i//10
    birlar = i%10
    if onlar == 8 or birlar ==8:
        print(i,end=" ")'''
'''print("Palindrom sonlar ro'yxati: ")
for i in range(100,1000):
    yuzlar = i //100
    birlar = i % 10
    if yuzlar == birlar:
        print(i,end=" ")'''
'''n = int(input("Son kiriting: "))
xona = len(str(abs(n)))
print(xona)'''
'''n = int(input("Son kiriting: "))
for i in range(n):
    print(n,end=" ")'''

'''numbers = [3, 6, 9, 12, 15, 18, 21] 
juft = []
for i in numbers:
    if i%2==0:
        juft.append(i)
        print(i,end=" ")'''
        
'''sonlar = [3, 6, 9, 12, 15, 18, 21] 
eng_katta = sonlar[0]
eng_kichik = sonlar[0]
for son in sonlar:
    if son > eng_katta:
        eng_katta = son
        if son < eng_kichik:
            eng_kichik = son
print("Ro'yxat:",sonlar)
print("Eng katta son:",eng_katta)
print("Eng kichik son:",eng_kichik)'''
'''words = ['python', 'is', 'fun', 'to', 'learn']  
words.sort(key=len)
print(words)'''
'''words = ['python', 'is', 'fun', 'to', 'learn'] 
sorted_words = sorted(words,key=len)
print(sorted_words)'''
'''nums = [1,2,3,2,4,5,1,6]
takrorlar = []
for son in nums:
  if nums.count(son) > 1 and son not in takrorlar:
    takrorlar.append(son)
print("Takrorlangan sonlar: ",takrorlar)'''

'''nums = [1,2,3,4,5,6,7,8]
for i in range(len(nums) -1, -1, -1):
    print(nums[i],end=' ')'''
'''fruits = ['apple', 'banana', 'cherry']
n_fruits = []
for index,fruit in enumerate(fruits):
    n_fruits.append(fruit)
    n_fruits.append(index)
print(n_fruits)'''
'''data = ['a', 'b', 'a', 'c', 'b', 'a'] 
dict_data = {}
for son in data:
       if son in dict_data:
           dict_data[son]+=1
       else:
           dict_data[son]=1
print(dict_data)'''
            
'''matrix = [[1,2,3],[4,5,6],[7,8,9]]
diagonal = []
for i in range(len(matrix)):
    diagonal.append(matrix[i][i])
print(diagonal)'''
'''nums= [4, 5, 6, 4, 7, 5, 8]
unikal = []
for num in nums:
    if nums.count(num)==1:
        unikal.append(num)
print(unikal)'''
'''t1 = (3,1,5)
t2= (4,2)
t3 = sorted(t1 + t2)
print(t3)'''
'''t = (1, 2, 2, 3, 4, 2, 5)
natija = t.count(2)
print(f"2 raqami {natija} marta qatnashgan.")'''
'''t = (10,25,17,25,8)
eng_katta = max(t)
indeks = t.index(eng_katta)
print(f"Eng katta qiymat: {eng_katta}")
print(f"Uning birinchi indeksi: {indeks}")'''
'''t = (1, 2, 3, 4)
t_list = list(t)
t_list[3]=100
t = tuple(t_list)
print(t)'''   
'''t = (2,4,6,8,10)
son = int(input("Son kiriting: "))
if son in t:
        print("Siz kiritgan son tupleda bor")
else:
        print("Siz kiritgan son tupleda yo'q")'''

'''t = (10,20,30,40,50)
lt = list(t)
lt[0],lt[-1]=lt[-1],lt[0]
t = tuple(lt)
print(t)'''

'''data = [(2, 3), (1, 4), (3, 2), (2, 1)] 
data.sort(key=lambda x:x[1])
print(data) '''
'''nums= ((1,2,3), (4,5), (6,)) 
l = 0
for ichki_tuple in nums:
    l += sum(ichki_tuple)
print(f"Jami yigindi: {l}")'''
'''t = (1, 2, 3, 4, 5)
teskari = t[::-1]
print(teskari)'''
        
words = ('apple', 'banana', 'kiwi', 'strawberry') 
sorted_words = sorted(words,key=len)
print(sorted_words)     
        
        
        
        
        
        