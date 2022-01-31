import csv
'''
固定參數
    因為月份固定是 7 月，所以總共有 31 天
'''

'''
資料結構
    2000年
        中文標題
        英文標題
        1號
        2號
    ...
    2021年
        中文標題
        英文標題
        1號
        2號
    Total[22][33][34]
    Total[年][日][項]
'''
#取得所有資料
Total = []
for i in range(22):
    data = []
    if(i < 10):
        year = "../467660-200" + str(i) +"-07.csv"
    else:
        year = "../467660-20" + str(i) +"-07.csv"

    with open(year ,mode='r' ,encoding="utf-8") as csvfile:
        content = csv.reader(csvfile)
        
        for j in content:
            data.append(j)
    
    Total.append(data)

'''
根據需求需要的資料只需要 溫度、相對濕度、露點溫度、降水量
'''

for i in range(len(Total[0][0])): #確認資料的 index 在哪
    print(i ,Total[0][0][i])

'''
資料位置
    index   -->   Type
      7           氣溫
      12          露點溫度
      13          相對溼度
      31          降水量
'''

#清空中文與英文標題
for i in range(22):
    del Total[i][0]
    del Total[i][0]

#將資料提取出來並且寫入 output.csv
with open('output.csv' ,mode = 'w' ,encoding="utf-8" ,newline='') as csvfile:
    # 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)

    # 寫入標題
    writer.writerow(["氣溫", "露點溫度", "相對溼度" ,"降水量"])

    for i in range(22):
        for j in range(31):
            writer.writerow([Total[i][j][7] ,Total[i][j][12] ,Total[i][j][13] ,Total[i][j][31]])