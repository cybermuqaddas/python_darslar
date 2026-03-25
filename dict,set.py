'''set1 = {1,2,3,4}
set2 =  {3,4,5,6} 
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.difference(set2))
print(set1.symmetric_difference(set2))
print(max(set1))
print(max(set2))
print(min(set1))
print(min(set2))
for i in set2:
    if i>2:
        print("Yaxshi natija")
    else:
        print("Keyinroq urininb koring")
elementlar_soni = len(set2)
print(elementlar_soni)'''
'''royxat = [1,2,3,4,5,5,6,54,33,4,4,4]
nimadir = set(royxat)
print(nimadir)'''
'''sonlar = {5,6,7,1,234,5,78,93,58,129}
yigindi = sum(sonlar)
print(f"Setdagi elementlar yigindi:{yigindi}")'''
'''set1 = {1,2,3,4,5,6}
set2 = {2,4,6}
natija =set2.issubset(set1)
print(natija)'''
'''set1 = {1,2,3}
set2 = {3,4,5}
farq = set1.symmetric_difference(set2)
print(farq)
print(len(farq))'''
'''set1 = {1,2,3}
set2 = {2,3,4}
set3 = {3,4,5}
u_elementlar = set1.intersection(set2,set3)
print(u_elementlar)'''
'''matn = "salom dunyo salom python dunyo "
sozlar_set = set(matn.split())
unikal_soni = len(sozlar_set)
print(sozlar_set)
print(unikal_soni)'''
'''sonlar_set = set()
print("5ta raqam kiriting: ")
for i in range (5):
    raqam = int(input(f"{i+1}-raqam: "))
    sonlar_set.add(raqam)
print("\nEndi 3ta raqam kiriting va ularni tekshiramiz:")
for i in range(3):
    t_raqam = int(input(f"{i+1}-tekshiriladigan raqam:" ))
    if t_raqam in sonlar_set:
        print(f"{t_raqam} raqami setda mavjud.")
    else:
        print(f"{t_raqam} raqami setda yo'q")
print(f"\nSiz yaratgan set: {sonlar_set}")'''
'''country = {"Uzbekistan": "Tashkent", "France": "Paris",
"Japan": "Tokyo"}
print(country.keys())
print(country.values())'''
'''cars = {"Chevrolet": "USA", "BMW": "Germany", "Hyundai":
"Korea"}
for moshina,davlat in cars.items():
    print(f"{moshina}:{davlat}")'''
'''marks ={"Ali": 78, "Laylo": 90, "Sardor": 65, "Aziza": 87}
print(sum(marks.values()))'''
'''marks ={"Ali": 78, "Laylo": 90, "Sardor": 65, "Aziza": 87}
jami = 0
for ball in marks.values():
    jami+= ball
print(f"Jami ball:{jami}")'''
'''scores ={"Ali": 85, "Laylo": 92, "Sardor": 88}
eng_yuqori_ball = max(scores.values())
print(eng_yuqori_ball)'''
'''results = {"Ali": 75, "Laylo": 88, "Sardor": 92, "Aziza": 69}
print("80 balldan yuqori natijalar: ")
print("-"*25)
for ism,ball in results.items():
    if ball>80:
        print(f"{ism}:{ball} ball")'''
'''students = {
 "Ali": {"math": 90, "english": 85},
"Laylo": {"math": 88, "english": 92}}
Laylo_english = students["Laylo"]["english"]
print(f"Layloni english bahosi: {Laylo_english}")'''
'''countries = {"uzb":
"Tashkent", "rus": "Moscow", "jpn": "Tokyo"}
countries['Uzbekistan'] = countries.pop('uzb')
print(countries)'''
words = ["apple", "banana", "apple", "orange", "banana",
"apple"]
'''count_dict = {}
for item in words:
    if item in count_dict:
        count_dict[item] +=1
    else:
        count_dict[item]=1
print(count_dict)'''

'''a ={"x": 1, "y": 2}
b ={"y": 3, "z": 4}
c = a | b
print(c)'''
sales = {"January": 1200, "March": 3400, "February": 2100, "April": 800}
sorted_sales = sorted(sales.items(),key=lambda item:item[1],reverse=True)
for month,year in sorted_sales:
    print(f"{month}:{year}")

