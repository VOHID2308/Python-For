mx_telefon_narxi = 0
min_telefon_narxi = 999
for i in range(5 ):
    son = int(input("narxni kiritng : "))
    if son > mx_telefon_narxi:
        mx_telefon_narxi = son 
    if son < min_telefon_narxi:
        min_telefon_narxi =son

print(min_telefon_narxi,"u eng kichik narx")
print(mx_telefon_narxi,"u eng katta narx")
# Har safar agar son biz berib qoygan sondan katta yoki
#kichikligini tekshiradi va moboda katta yoki kichik boladigan bolsa 
#Kerakli mx_telefon_narxi yoki teskarisiga tenglab boraveradi
#va oxrida oxirgi tebglab olgan sonni print orqali chiqaradi