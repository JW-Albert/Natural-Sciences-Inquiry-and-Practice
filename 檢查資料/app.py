import csv

#調用提取完的資料
Total = []
for i in range(22):
    with open("../資料提取/output.csv" ,mode='r' ,encoding="utf-8") as csvfile:
        content = csv.reader(csvfile)
        
        for j in content:
            Total.append(j)


'''
資料結構
    Total[683][4]
'''

#檢查資料是否有例外
print("例外檢查開始")
for i in range(1 ,683 ,1):
    for j in range(4):
        try:
            float(Total[i][j])
        except:
            print("Total[{:}][{:}]: {:}".format(i ,j ,Total[i][j]))
            print("執行例外處理")
            Total[i][j] = 0
print("例外檢查結束")

#再次檢查資料是否有例外
print("例外檢查開始")
for i in range(1 ,683 ,1):
    for j in range(4):
        try:
            Total[i][j] = float(Total[i][j])
        except:
            print("Total[{:}][{:}]: {:}".format(i ,j ,Total[i][j]))
            Total[i][j] = 0.0
print("例外檢查結束")

'''
檢查到的例外事件
    Total[174][3]: X
    Total[200][3]: /
    Total[201][3]: /
    Total[211][3]: /
    Total[212][3]: /
    Total[266][3]: /
    Total[276][3]: /
    Total[292][3]: /
    Total[296][3]: /
    Total[308][3]: /
    Total[334][3]: /
    Total[393][3]: /
    Total[472][3]: /
    Total[483][3]: /
    Total[503][3]: /
    Total[504][3]: /
    Total[527][3]: /
    Total[570][3]: /
    Total[590][3]: /
    Total[591][3]: /
    Total[648][3]: /
    Total[656][3]: /
    Total[682][3]: /

例外事件數量
    共 23 件

例外處理
    將值定義為 0
'''

#檢查資料有無負值
print("負值檢查開始")
for i in range(1 ,683 ,1):
    for j in range(4):

        if(Total[i][j] < 0):
            print("Total[{:}][{:}]: {:}".format(i ,j ,Total[i][j]))
            print("執行負值處理")
            Total[i][j] = Total[i][j] * -1
print("負值檢查結束")

#再次檢查資料有無負值
print("負值檢查開始")
for i in range(1 ,683 ,1):
    for j in range(4):
        if(Total[i][j] < 0.0):
            print("Total[{:}][{:}]: {:}".format(i ,j ,Total[i][j]))
            print("執行負值處理")
            Total[i][j] = Total[i][j] * -1
print("負值檢查結束")

'''
檢查到的負值事件
    Total[34][3]: -5.4
    Total[35][3]: -4.9
    Total[36][3]: -2.8
    Total[37][3]: -5.5
    Total[42][3]: -3.9
    Total[51][3]: -4.9
    Total[54][3]: -2.1
    Total[55][3]: -2.4
    Total[56][3]: -2.6
    Total[57][3]: -3.5
    Total[60][3]: -1.7
    Total[61][3]: -1.6
    Total[67][3]: -4.5
    Total[68][3]: -1.8
    Total[69][3]: -6.0
    Total[70][3]: -1.5
    Total[71][3]: -2.1
    Total[72][3]: -5.8
    Total[73][3]: -3.1
    Total[74][3]: -6.6
    Total[78][3]: -6.4
    Total[79][3]: -3.5
    Total[90][3]: -2.1
    Total[92][3]: -3.7
    Total[93][3]: -4.1
    Total[97][3]: -4.6
    Total[101][3]: -5.3
    Total[102][3]: -5.7
    Total[112][3]: -5.7
    Total[115][3]: -4.2
    Total[116][3]: -6.2
    Total[125][3]: -1.7
    Total[126][3]: -1.5
    Total[127][3]: -0.4
    Total[128][3]: -1.3
    Total[129][3]: -1.7
    Total[138][3]: -5.3
    Total[139][3]: -6.8
    Total[140][3]: -2.9
    Total[141][3]: -6.1
    Total[142][3]: -0.8
    Total[143][3]: -5.9
    Total[149][3]: -5.3
    Total[150][3]: -1.9
    Total[151][3]: -1.6
    Total[152][3]: -1.1
    Total[157][3]: -5.7
    Total[162][3]: -2.9
    Total[172][3]: -1.2
    Total[173][3]: -0.2
    Total[175][3]: -1.8
    Total[176][3]: -2.2
    Total[183][3]: -2.0
    Total[184][3]: -1.9
    Total[194][3]: -2.3
    Total[195][3]: -0.8
    Total[198][3]: -5.8
    Total[199][3]: -1.5
    Total[202][3]: -4.7
    Total[203][3]: -3.3
    Total[208][3]: -4.4
    Total[209][3]: -7.8
    Total[210][3]: -4.1
    Total[213][3]: -2.1
    Total[214][3]: -2.8
    Total[215][3]: -5.9
    Total[216][3]: -1.3
    Total[226][3]: -5.5
    Total[246][3]: -4.9
    Total[253][3]: -5.9
    Total[254][3]: -4.3
    Total[256][3]: -2.2
    Total[257][3]: -1.8
    Total[258][3]: -4.4
    Total[259][3]: -3.5
    Total[265][3]: -1.3
    Total[275][3]: -1.4
    Total[277][3]: -1.1
    Total[278][3]: -2.7
    Total[279][3]: -4.8
    Total[282][3]: -2.8
    Total[284][3]: -5.6
    Total[288][3]: -6.7
    Total[289][3]: -3.6
    Total[290][3]: -3.8
    Total[291][3]: -5.6
    Total[293][3]: -2.8
    Total[294][3]: -6.7
    Total[295][3]: -4.5
    Total[297][3]: -4.6
    Total[298][3]: -4.3
    Total[321][3]: -7.9
    Total[324][3]: -3.0
    Total[325][3]: -5.0
    Total[326][3]: -5.2
    Total[330][3]: -4.8
    Total[331][3]: -2.0
    Total[332][3]: -4.5
    Total[335][3]: -4.7
    Total[336][3]: -0.3
    Total[337][3]: -0.4
    Total[339][3]: -2.1
    Total[350][3]: -4.3
    Total[351][3]: -3.6
    Total[352][3]: -2.2
    Total[353][3]: -3.4
    Total[354][3]: -4.0
    Total[355][3]: -0.6
    Total[357][3]: -4.5
    Total[358][3]: -3.2
    Total[359][3]: -3.1
    Total[360][3]: -3.2
    Total[361][3]: -4.3
    Total[367][3]: -5.9
    Total[368][3]: -7.2
    Total[369][3]: -2.0
    Total[377][3]: -5.6
    Total[391][3]: -4.8
    Total[392][3]: -4.3
    Total[394][3]: -4.7
    Total[395][3]: -4.3
    Total[396][3]: -1.2
    Total[397][3]: -3.8
    Total[399][3]: -5.1
    Total[400][3]: -2.2
    Total[402][3]: -1.3
    Total[403][3]: -1.2
    Total[407][3]: -4.8
    Total[411][3]: -6.1
    Total[412][3]: -5.0
    Total[415][3]: -5.5
    Total[416][3]: -1.0
    Total[417][3]: -3.1
    Total[418][3]: -4.0
    Total[419][3]: -3.9
    Total[420][3]: -4.5
    Total[421][3]: -0.9
    Total[422][3]: -0.9
    Total[423][3]: -4.0
    Total[424][3]: -4.7
    Total[439][3]: -5.0
    Total[450][3]: -6.3
    Total[451][3]: -3.0
    Total[452][3]: -6.2
    Total[453][3]: -5.6
    Total[455][3]: -7.5
    Total[456][3]: -2.8
    Total[457][3]: -1.3
    Total[469][3]: -7.1
    Total[470][3]: -4.0
    Total[471][3]: -1.4
    Total[473][3]: -2.1
    Total[477][3]: -6.7
    Total[478][3]: -6.3
    Total[480][3]: -3.6
    Total[484][3]: -0.5
    Total[485][3]: -3.6
    Total[498][3]: -6.0
    Total[501][3]: -2.8
    Total[505][3]: -3.3
    Total[506][3]: -2.2
    Total[507][3]: -3.2
    Total[508][3]: -7.2
    Total[519][3]: -6.5
    Total[522][3]: -5.2
    Total[528][3]: -7.0
    Total[530][3]: -6.1
    Total[531][3]: -4.9
    Total[532][3]: -4.7
    Total[533][3]: -5.1
    Total[534][3]: -3.1
    Total[542][3]: -7.1
    Total[543][3]: -4.0
    Total[548][3]: -5.6
    Total[549][3]: -2.0
    Total[555][3]: -2.9
    Total[556][3]: -0.3
    Total[557][3]: -84.1
    Total[558][3]: -1.5
    Total[560][3]: -1.0
    Total[565][3]: -2.9
    Total[566][3]: -5.5
    Total[569][3]: -6.6
    Total[571][3]: -4.0
    Total[572][3]: -4.0
    Total[574][3]: -2.7
    Total[575][3]: -5.1
    Total[577][3]: -2.5
    Total[578][3]: -6.0
    Total[580][3]: -0.9
    Total[592][3]: -4.0
    Total[600][3]: -2.9
    Total[607][3]: -2.5
    Total[608][3]: -2.4
    Total[609][3]: -2.9
    Total[610][3]: -2.1
    Total[612][3]: -8.3
    Total[616][3]: -5.4
    Total[617][3]: -6.6
    Total[618][3]: -5.7
    Total[620][3]: -5.5
    Total[633][3]: -7.8
    Total[634][3]: -7.6
    Total[640][3]: -6.4
    Total[647][3]: -6.0
    Total[649][3]: -0.2
    Total[650][3]: -1.2
    Total[651][3]: -2.5
    Total[655][3]: -6.5
    Total[657][3]: -6.1
    Total[658][3]: -5.5
    Total[664][3]: -6.0
    Total[665][3]: -5.9
    Total[666][3]: -3.3
    Total[670][3]: -6.8
    Total[672][3]: -5.7
    Total[673][3]: -4.6
    Total[675][3]: -4.7
    Total[676][3]: -5.0
    Total[679][3]: -5.9
    Total[681][3]: -5.3

負值事件數量
    共 221 件

負值事件處理
    將值定義為 0
'''


#輸出最終版本
for i in range(683):
        print(Total[i])


#儲存例外處理
with open('output.csv' ,mode = 'w' ,encoding="utf-8" ,newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入標題
    writer.writerow(["氣溫", "露點溫度", "相對溼度" ,"降水量"])

    for i in range(1 ,683 ,1):
        writer.writerow([Total[i][0] ,Total[i][1] ,Total[i][2] ,Total[i][3]])

'''
異常資料數
    221 + 23 = 244

總資料數
    682 * 4 = 2428

資料異常率
    10.0494 %
'''