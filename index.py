import pandas as pd
import matplotlib.pyplot as plt

# 匯入電力相關資料
df = pd.read_csv("經濟部能源署_電力供給月資料.csv")

# 依照資料欄位可知，電力發電分為 台電、民營、自用
columns_name = ["台電發電量","民營電廠發電量","自用發電設備發電量","全國發電量"]
result_columns = [[],[],[],[]]

result_year_month = [[],[]]
# 將日期切割
for index , row in df.iterrows():
    str_data = str(row["日期(年/月)"])
    result_year_month[0].append(str_data[0:4])
    result_year_month[1].append(str_data[4:6])
    
df["年"] = result_year_month[0]
df["月"] = result_year_month[1]

for i in df.columns:
    if i =="年" or i =="月":
        for j in range(len(result_columns)):
            result_columns[j].append(str(i))
    if columns_name[0] in i :
        result_columns[0].append(str(i))
    elif columns_name[1] in i :
        result_columns[1].append(str(i))
    elif columns_name[2] in i :
        result_columns[2].append(str(i))
    elif columns_name[3] in i :
        result_columns[3].append(str(i))


df_TW = df[result_columns[3]]
df_TW_power = df[result_columns[0]]
df_people = df[result_columns[1]]
df_self = df[result_columns[2]]

# data_2023 = []
# df_TW_power[df_TW["年"] == "2023"].plot(
#     y=df_TW_power['月']
# )
# plt.show()
# 依照for迴圈輸出每個月發電量變化
for i in df["年"].unique():
    for i in result_columns[]