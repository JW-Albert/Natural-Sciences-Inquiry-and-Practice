import csv
import xlsxwriter

#調用檢查完的資料
Total = []
for i in range(22):
    with open("../檢查資料/output.csv" ,mode='r' ,encoding="utf-8") as csvfile:
        content = csv.reader(csvfile)
        
        for j in content:
            Total.append(j)


#將數據存入 Excel 表格中
wb = ""
wb = xlsxwriter.Workbook("圖表化數據.xlsx")

ws = ""
ws = wb.add_worksheet("折線圖")

ws.write_string(0 ,0 ,"氣溫")
ws.write_string(0 ,1 ,"露點溫度")
ws.write_string(0 ,2 ,"相對溼度")
ws.write_string(0 ,3 ,"降水量")

for i in range(1 ,683 ,1):
    ws.write_number(i ,0 ,float(Total[i][0]))
    ws.write_number(i ,1 ,float(Total[i][1]))
    ws.write_number(i ,2 ,float(Total[i][2]))
    ws.write_number(i ,3 ,float(Total[i][3]))


#繪製折線圖  氣溫
chart = wb.add_chart({'type': 'line'})

chart.add_series({
    "values" : "折線圖!$A$2:$A$683",
    'line':{'color':'red'},
})

chart.set_title({'name': '氣溫(°C)'})
chart.set_y_axis({'name': '°C'})

chart.set_size({'width':1185 ,'height':768})

ws.insert_chart('F1', chart, {'x_offset': 25, 'y_offset': 10})


#繪製折線圖  露點溫度
chart = wb.add_chart({'type': 'line'})

chart.add_series({
    "values" : "折線圖!$B$2:$B$683",
    'line':{'color':'red'},
})

chart.set_title({'name': '露點溫度'})
chart.set_y_axis({'name': '°C'})

chart.set_size({'width':1185 ,'height':768})

ws.insert_chart('F26', chart, {'x_offset': 25, 'y_offset': 10})


#繪製折線圖  相對溼度
chart = wb.add_chart({'type': 'line'})

chart.add_series({
    "values" : "折線圖!$C$2:$C$683",
    'line':{'color':'red'},
})

chart.set_title({'name': '相對溼度'})
chart.set_y_axis({'name': '%'})

chart.set_size({'width':1185 ,'height':768})

ws.insert_chart('R1', chart, {'x_offset': 25, 'y_offset': 10})


#繪製折線圖  降水量
chart = wb.add_chart({'type': 'line'})

chart.add_series({
    "values" : "折線圖!$D$2:$D$683",
    'line':{'color':'red'},
})

chart.set_title({'name': '降水量'})
chart.set_y_axis({'name': 'mm'})

chart.set_size({'width':1185 ,'height':768})

ws.insert_chart('R26', chart, {'x_offset': 25, 'y_offset': 10})

wb.close()