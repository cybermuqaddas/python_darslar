
'''while True:
    matn = input("nimadir yozing (to'xtash uchun 'stop' deb yozing): ")
    if matn==('stop'):
        print("Dastur to'xtatildi.")
        break
    print(f"Siz yozgan matn: {matn}")'''

'''while True:
    son = input("Son kiriting: ")
    if float(son)<0:
        print("Dastur tugatildi!")
        break
    print(f"Siz kiritgan son:{son}")'''

'''while True:
    son = input("Son kiriting: ")
    son = int(son)
    if son==0:
        continue
    print(f"Siz kiritgan son:{son}")'''
    
'''son = []
for i in range(1,100):
    if i%3==0:
        son.append(i)
print(son)'''

'''parol = 'python123'
while True:
    savol = input("Parolni kiriting: ")
    if savol == parol:
        print("Xush kelibsiz!")
        break
    else:
      print("parol xato! Qayta urininb ko'ring.")'''
      
'''for i in range(0,20,2):
    print(i,end=' ')'''
    
'''son = int(input("Qaysi sonning karra jadvali kerak: "))
print(f"\n--{son} sonining karra jadvali(for)---")
for i in range(1,11):
    natija = son * i
    print(f"{son} * {i} = {natija}")'''
    
'''son = int(input("Qaysi sonning karra jadvali kerak: "))
i=1
print(f"\n--{son} sonining karra jadvali(while)---")
while i<=10:
    natija = son * i
    print(f"{son} * {i} = {natija}")
    i+=1'''

'''a = int(input("a sonini kiriting: ")) 
b = int(input("b sonini kiriting: "))   
summa = 0
for i in range(a,b+1):
    summa+=i
print(f"{a} va {b} orasidagi sonlar yig'indisi:{summa}")'''
'''a = int(input("a sonini kiriting: ")) 
b = int(input("b sonini kiriting: "))   
summa = 1
for i in range(a,b+1):
    summa*=i
print(summa)'''
'''a = int(input("a sonini kiriting: ")) 
b = int(input("b sonini kiriting: "))  
if a%2 !=0:
    a+=1 
sonlar = []
for i in range(a,b+1,2):
    sonlar.append(i)
print(sonlar)'''
'''a = int(input("Birinchi sonni kiriting: ")) 
b = int(input("Ikkinchi sonni kiriting: "))    

# 1. Agar a b dan katta bo'lsa, ularning o'rnini almashtiramiz
if a > b:
    a, b = b, a

# 2. Agar a juft bo'lsa, uni keyingi toq songa o'tkazamiz
if a % 2 == 0:
    a += 1

toq_sonlar = []

# 3. Toq sondan boshlab 2 qadam bilan yuramiz
for i in range(a, b + 1, 2):
    toq_sonlar.append(i)

print(f"Tartiblangan oraliq: {a} dan {b} gacha")
print(f"Topilgan toq sonlar: {toq_sonlar}")'''
'''a = int(input("Birinchi sonni kiriting: ")) 
b = int(input("Ikkinchi sonni kiriting: ")) 
juft_yigindi = 0
toq_kopaytma = 1
toq_son_bormi = False
for i in range(a,b+1):
    if i %2 ==0:
        juft_yigindi += i
    else:
        toq_kopaytma *=i
        toq_son_bormi = True
if not toq_son_bormi:
    toq_kopaytma = 0
print(f"Juft sonlar yig'indisi: {juft_yigindi}")
print(f"Toq sonlar ko'paytmasi: {toq_kopaytma}")'''
'''sum = 0
N = int(input("N natural sonini kiriting: "))
for i in range(1,N+1):
    if N%i != 0:
        sum +=i
print(sum)'''
'''N = int(input("N natural sonini kiriting: "))
sum = 0
for i in range(1,N):
    if N%i == 0:
        sum +=i
if sum == N:
    print("mukammal son")
else:
    print("Mukammal son emas")'''
'''N = int(input("N natural sonini kiriting: "))
yigindi = 0
son = N
while son > 0:
    raqam = son % 10
    yigindi += raqam
    son = son //10
    
print(f"{N} sonining raqamlari yigindisi:{yigindi}")'''

'''yigindi = 0
while True:
    n = int(input("Son kiriting(toxtatish uchun 0): "))
    if n==0:
        break
    yigindi +=n
print(yigindi)'''

'''a = int(input("Birinchi sonni kiriting: ")) 
b = int(input("Ikkinchi sonni kiriting: ")) 
while a != b:
    if a > b:
        a = a-b
    else:
        b = b-a
print(f"EKUB: {a}")'''
    
'''a = int(input("Birinchi sonni kiriting: ")) 
b = int(input("Ikkinchi sonni kiriting: ")) '''
text ="Python"
print(text[0])
        
        
