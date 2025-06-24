min_son = 999999  # Juda katta son bilan boshlasak ham boladi 

for i in range(7):
    son = int(input("Son kiriting: "))
    if son < min_son:
        min_son = son

print("Eng kichik son:", min_son)
