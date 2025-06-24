n = int(input("N ni kiriting : "))

j_son_yig = 0
t_son_yig = 0

for i in range(n + 1):
    if i % 2 == 0 :
        j_son_yig += i
    if i % 2 != 0 :
        t_son_yig += i 

print("juft sonlar yigindisi >> ", j_son_yig)
print("toq sonlar yiginsisi >>", t_son_yig)
# Bu har bitta juft sonni juft songa qoshadi va oxrida natijasini chiqaradi
# Barcha toq sonlarda ham shunaqa jaroyon boladi 