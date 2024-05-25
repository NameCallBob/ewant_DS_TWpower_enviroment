import pandas as pd
import matplotlib.pyplot as plt
from data import Data

# 分析之程式碼(做R語言之輸出驗證用)

# 台電資料
data_power = Data.TaiwanPowerGenerate()[3]
data_CO2 = Data.new_report_CO2_Data()

data_power = data_power[["全國發電量_總計", "年"]]
data_year_power = data_power.groupby("年").sum().reset_index()
data_year_power["year"] = data_year_power["年"]
data_year_power = data_year_power.drop(columns="年")

required_columns = ['year', 'Direct emissions (metric tons CO2e)',
                    'Indirect energy emissions (metric tons CO2e)', 'Total emissions (metric tons CO2e)']

data_CO2 = data_CO2[required_columns]
data_year_CO2 = data_CO2.groupby('year').sum().reset_index()

# 檢查兩個資料大小
print(data_year_CO2.shape)
print(data_year_power.shape)

all_data = pd.merge(data_year_CO2, data_year_power, on='year')
print(all_data)
# 計算皮爾森相關係數
pearson_corr = all_data.corr(method='pearson')
