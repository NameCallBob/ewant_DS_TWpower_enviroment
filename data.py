

import pandas as pd
import os
import chardet


class Data:
    """進行資料修改和預處理"""

    def TaiwanPowerGenerate() -> list:
        """
        ### 台灣電力製造資訊
        -> return

        [台電發電,民營發電,自用發電,全國發電]
        """
        now = os.getcwd()
        df = pd.read_csv(os.path.join(now, "GVopendata", "經濟部能源署_電力供給月資料.csv"))
        # 依照資料欄位可知，電力發電分為 台電、民營、自用
        columns_name = ["台電發電量", "民營電廠發電量", "自用發電設備發電量", "全國發電量"]
        result_columns = [[], [], [], []]
        print(df.isnull().value_counts())
        result_year_month = [[], []]
        # 將日期切割
        for index, row in df.iterrows():
            str_data = str(row["日期(年/月)"])
            result_year_month[0].append(int(str_data[0:4]))
            result_year_month[1].append(int(str_data[4:6]))

        df["年"] = result_year_month[0]
        df["月"] = result_year_month[1]

        for i in df.columns:
            if i == "年" or i == "月":
                for j in range(len(result_columns)):
                    result_columns[j].append(str(i))
            if columns_name[0] in i:
                result_columns[0].append(str(i))
            elif columns_name[1] in i:
                result_columns[1].append(str(i))
            elif columns_name[2] in i:
                result_columns[2].append(str(i))
            elif columns_name[3] in i:
                result_columns[3].append(str(i))
        all_data = []
        for i in range(len(result_columns)):
            all_data.append(df[result_columns[i]])

        # 取得2015年-2022年區間資料
        res = []
        for i in all_data:
            res.append(i[(i["年"] >= 2015) & (i["年"] <= 2022)])

        # res[3].to_excel(os.path.join(now,"result","TW_allPowerGenerate.xlsx"))
        # res[2].to_excel(os.path.join(now,"result","TW_SelfPowerGenerate.xlsx"))
        # res[1].to_excel(os.path.join(now,"result","TW_PeoplePowerGenerate.xlsx"))
        # res[0].to_excel(os.path.join(now,"result","TW_TWDPowerGenerate.xlsx"))
        res[3].to_csv(os.path.join(now, "result", "data_power.csv"))
        return res

    def GreenhouseGases():
        """
        台灣發電的溫室氣體排放統計
        """
        now = os.getcwd()
        df = pd.read_csv(os.path.join(now, "GVopendata", "001.csv"))
        print("資料二-台電火力發電之統計")
        print(df.isnull().value_counts())
        # df.to_excel(os.path.join(now,"result","Power_GreenhouseGases.xlsx"))

        return df

    def Company_GreenhouseGases():
        """
        公司的溫室氣體排放統計
        """
        now = os.getcwd()
        df = pd.read_csv(os.path.join(now, "GVopendata", "ghg_p_01.csv"))
        print("資料三-公司的溫室氣體排放")
        print(df.isnull().value_counts())
        for index, row in df.iterrows():
            row['app_year'] = int(row['app_year'])+2011
        # df.to_excel(os.path.join(now,"result","CompanyGreenhouseGases.xlsx"))
        return df

    def new_report_CO2_Data():
        now = os.getcwd()
        # Data.detect_encoding(os.path.join(now,"GVopendata","report.csv"))
        df = pd.read_csv(os.path.join(now, "GVopendata",
                         "report.csv"))
        df = df.drop(columns="id") ; df = df.dropna()
        print("資料四-CO2資料")
        print(df.isnull().value_counts())
        res = []
        for index, row in df.iterrows():
            res.append(int(row['year']) + 1911)
        df["year"] = res
        # df.to_excel(os.path.join(now, "result", "report.xlsx"))


        df.to_csv(os.path.join(now, "result", "data_CO2.csv"))
        # 移除千分位並轉換為數字
        columns_to_change = ['Direct emissions (metric tons CO2e)','Indirect energy emissions (metric tons CO2e)', 'Total emissions (metric tons CO2e)']
        for column in columns_to_change:
            df[column] = df[column].str.replace(',', '').astype(float)
        print(df)
        return df
    def detect_encoding(file_path):
        with open(file_path, 'rb') as f:
            raw_data = f.read()
        result = chardet.detect(raw_data)
        encoding = result['encoding']
        confidence = result['confidence']
        if encoding is None:
            return None, None
        print(encoding, confidence)
        return encoding, confidence


if __name__ == "__main__":
    # 測試使用
    TW_power_list = Data.TaiwanPowerGenerate()
    for i in TW_power_list:
        print(i)

    print(Data.GreenhouseGases())

    print(Data.Company_GreenhouseGases())

    print(Data.new_report_CO2_Data())
