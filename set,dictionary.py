'''fruits = {'olma','banan','kiwi'}
vegetables = {'carrot','potato','cucember'}
yangi = fruits.union(vegetables)
fruits.add("mango")
fruits.update(["mandarin","orange"])
fruits.remove("olma")
fruits.discard("banan")
for item in fruits:
print(yangi)'''
'''guruh1 = {"Ali", "Vali", "Sami"}
guruh2 = {"Sami", "G'ani", "Ali"}
umumiy = guruh1.intersection(guruh2)
print(umumiy) '''
'''a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.symmetric_difference(b))'''
'''fruits = set()
fruits.add('olma')
fruits.add('anor')
fruits.add('behi')
print(fruits)'''
'''colors = {"red","blue","green"}
colors.remove("red")
colors.discard("green")
print(colors)'''
'''A = {1,2,3}
B = {3,4,5}
print(A.union(B))
print(A.intersection(B))'''
'''son = set()
son.add(1)
son.add(2)
son.add(3)
son.add(4)
son.add(5)
print(son)'''
'''nums = [1,2,2,3,4,4,5]
s_nums = set(nums)
print(s_nums)'''
'''guruh1 = {"Ali", "Vali", "Sami", "Olim"}
guruh2 = {"Sami", "G'ani", "Ali"}
faqat_birinchida = guruh1 - guruh2
print(faqat_birinchida)'''
'''son = {1,2,3,4,5,6,7}
son1 = int(input("Son kiriiting: "))
if son1 in son:
    print("Bor")
else:
    print("Yo'q")'''
'''set1 = {'Ali','Vali','Gani','Toshmamat'}
set2 = {'Ali','Guli','Gani','Jompulat'}
print(set1.intersection(set2))'''
'''student = {
"name":"Ali",
"age":20,
"city":"Tashkent"
}
student["email"] ="test@gmail.com"
print(student["name"])
print(student.get("age"))
if "name" in student:
	print("Bor ✅")'''
'''profile = {}
profile["name"] =input("Ism: ")
profile["age"] =int(input("Yosh: "))
profile["city"] =input("Shahar: ")
profile['age']+=1
print(profile)'''
'''raqamlar = (1, 2, 3, 4, 5)

birinchi, *qolganlari = raqamlar

print(birinchi)   # 1
print(qolganlari) # [2, 3, 4, 5] (Bu qolgan qismni yana list qilib beradi)'''
'''profile = {}

profile["name"] =input("Ism: ")
profile["age"] =int(input("Yosh: "))
profile["city"] =input("Shahar: ")

print(profile)'''
'''
profil ={}
profil["name"] = input("Ism: ")
profil["age"] = input("yosh: ")
profil ["city"] = input("shahar: ")
print(profil)'''
'''profil = {
    'name': input("Ism:"),
    'age': int(input("yosh")),
    'city':input('shahar:')}
profil['age']+=1
profil['email'] = input("Emailingizni kiriting: ")
if 'phone' in profil:
    print("Bor")
else:
    print("Yo'q")
profil = {"name": "Ali", "age": 25}

if "phone" in profil:
    print(profil["phone"])
else:
    print("Yo‘q")'''
'''profil ={}
profil["name"] = input("Ism: ")
profil["age"] = input("yosh: ")
profil ["city"] = input("shahar: ")
print(profil)
for qiymat in profil.values():
    if isinstance(qiymat, (int, float)):
        print(qiymat)'''
        
'''profil = {"name": "Ali", "age": 25, "city": "Toshkent", "height": 175.5}

# Lug'at qiymatlarini birma-bir tekshiramiz
for qiymat in profil.values():
    if isinstance(qiymat, (int, float)):
        print(qiymat)
profil.pop('age')
profil.clear()'''
talabalar = [] # Bo'sh list yaratamiz

# 3 marta takrorlanadigan sikl
for i in range(1, 4):
    print(f"{i}-talaba ma'lumotlarini kiriting:")
    
    # Har safar yangi dictionary yaratamiz
    talaba = {
        'name': input("Ism: "),
        'age': int(input("Yosh: ")),
        'city': input("Shahar: ")
    }
    
    # Uni listga qo'shamiz
    talabalar.append(talaba)

print("\nBarcha talabalar ro'yxati:")
print(talabalar)
