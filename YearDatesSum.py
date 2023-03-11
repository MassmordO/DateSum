Year = int(input("Введите год: "))
logic = False
DAtesSum =0
if Year%4==0 and Year%100!=0 or Year%400==0 :
    logic = True
    print("Вискосный год")
else : 
    logic = False
    print("Невискосный год")
for i in range(1,13):
    if i == 2:
        if logic:
            for j in range(1,30):
                DAtesSum += sum(map(int,str(j)))
        else:
            for j in range(1,29):
                DAtesSum += sum(map(int,str(j)))
    elif i in (1,3,5,7,8,10,12):
        for j in range(1,32):
            DAtesSum += sum(map(int,str(j)))
    else:
        for j in range(1,31):
            DAtesSum += sum(map(int,str(j)))
print(DAtesSum)