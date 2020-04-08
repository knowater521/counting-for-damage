
"""
数组[序号，位置，全伤加成，物伤加成，暴伤加成，暴击率加成，攻速加成]
col [ 0    1       2         3        4        5          6  ]

"""
def setInfo(num=0, posi=0, allDa=0, phyDa=0, DouDa=0, rate=0, speed=0):
    return [num, posi, allDa, phyDa, DouDa, rate, speed]


danding1 = [0, 1, 0, 0.2, 0, 0.15, 0]
danding2 = [0, 2, 0, 0.2, 0.3, 0, 0]
danding3 = [0, 3, 0.3, 0, 0, 0, 0.15]
danding_2 = [0, 2, 0, 0.3, 0.2, 0, 0]
danding_3 = [0, 3, 0, 0, 0, 0, 0]

kafuka1 = [1, 1, 0.2, 0, 0.2, 0, 0]
kafuka2 = [1, 2, 0, 0.4, 0, 0, 0]
kafuka3 = [1, 3, 0, 0, 0, 0.2, 0]
kafuka_2 = [1, 2, 0.45, 0, 0, 0, 0]
kafuka_3 = [1, 3, 0, 0, 0, 0, 0]

dilake1 = setInfo(2, 1, rate=0.2)
dilake2 = setInfo(2, 2, allDa=0.66)
dilake3 = setInfo(2, 3, phyDa=0.2)
dilake_2 = setInfo(2, 2, phyDa=0.35)
dilake_3 = setInfo(2, 3)

singo1 = [danding1, kafuka1, dilake1]
singo2 = [danding2, kafuka2, dilake2]
singo3 = [danding3, kafuka3, dilake3]

double = [danding_2, kafuka_2, dilake_2]
trible = [danding_3, kafuka_3, dilake_3]

dic = ["但丁", "卡夫卡", "迪拉克"]

rating=[]

def count(a, b, c):
    result = []
    for i in range(2, 7):
        result.append(a[i]+b[i]+c[i])

    if(a[0]==b[0]==c[0]):
        for i in range(len(result)):
            result[i] += double[a[0]][i+2]

    elif((a[0]==b[0]) or (a[0]==c[0]) or (b[0]==c[0])):
        if((a[0]==b[0]) or (a[0]==c[0])):
            for i in range(len(result)):
                result[i] += trible[a[0]][i+2]
        elif(b[0]==c[0]):
            for i in range(len(result)):
                result[i] += trible[b[0]][i+2]

    return result

flag = 0
up = 0
mid = 0
down = 0
for i in range(len(singo1)):
    for j in range(len(singo2)):
        for k in range(len(singo3)):
            result = count(singo1[i], singo2[j], singo3[k])
            #print(type(result[0]))
            damagerate = (1 + result[0]) * (1 + result[1]) * (1 + result[2]) * (1 + result[3]) * (1 + result[4])
            damagerate = round(damagerate, 4)
            rating.append(damagerate)
            cur1 = singo1[i][0]
            cur2 = singo2[j][0]
            cur3 = singo3[k][0]
            print("==============================================================")
            print("伤害倍率: " + str(damagerate))
            print("上位: " + str(singo1[cur1]))
            print("中位: " + str(singo2[cur2]))
            print("下位: " + str(singo3[cur3]))
            print("上位: " + dic[cur1])
            print("中位: " + dic[cur2])
            print("下位: " + dic[cur3])
            if (damagerate >= flag):
                flag = damagerate
                up = singo1[i][0]
                mid = singo2[j][0]
                down = singo3[k][0]
            """print(damagerate)
            print(flag)"""
rating.sort(reverse=True)

print(rating)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("最优搭配")
print("伤害倍率: " + str(flag))
print("上位: " + str(singo1[up]))
print("中位: " + str(singo2[mid]))
print("下位: " + str(singo3[down]))
print("上位: " + dic[up])
print("中位: " + dic[mid])
print("下位: " + dic[down])

