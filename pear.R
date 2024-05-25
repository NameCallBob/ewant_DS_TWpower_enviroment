# 讀取台電資料
data_power <- read.csv("data_power.csv")
data_CO2 <- read.csv("data_CO2.csv")

# 取需要的欄位
data_power <- data_power[, c("年", "全國發電量_總計")]
colnames(data_power) <- c("year", "total_power")

required_columns <- c("year", "Direct emissions (metric tons CO2e)", "Indirect energy emissions (metric tons CO2e)", "Total emissions (metric tons CO2e)")
data_CO2 <- data_CO2[, required_columns]

# 合併資料
all_data <- merge(data_power, data_CO2, by = "year")

# 計算相關係數
pearson_corr <- cor(all_data)

# 輸出合併後的資料
print(all_data)
