n = int(input("Nechta son kiritasiz : "))
mx_son = 0
min_son = 999
for i in range(n ):
    son = int(input("sonni kiriting : "))
    if son > mx_son:
        mx_son = son 
    if son < min_son:
        min_son = son 
natija =( min_son + mx_son) / 2 

print("Ortancha qitmati ", natija)
# Bu yerda ikkita eng katta va eng kichik sonlarni iflar orqali 
# Hisoblab oxirida ortancha hisobini ekranga chiqaradi