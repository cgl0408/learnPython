import pandas as pd

name = ["蒙其·D·魯夫", "羅羅亞·索隆", "娜美", "騙人布", "賓什莫克·香吉士", "多尼多尼·喬巴", "妮可·羅賓", "佛朗基", "布魯克"]
occupation = ["船長", "劍士", "航海士", "狙擊手", "廚師", "醫生", "考古學家", "船匠", "音樂家"]

# 建立 dict
straw_hat_dict = {"name": name,
                  "occupation": occupation
}

# 建立第一個 data frame
straw_hat_df = pd.DataFrame(straw_hat_dict)

name = ["蒙其·D·魯夫", "多尼多尼·喬巴", "妮可·羅賓", "布魯克"]
devil_fruit = ["橡膠果實", "人人果實", "花花果實", "黃泉果實"]

# 建立 dict
devil_fruit_dict = {"name": name,
                    "devil_fruit": devil_fruit
}

# 建立第二個 data frame
devil_fruit_df = pd.DataFrame(devil_fruit_dict)

# 連接
straw_hat_merged = pd.merge(straw_hat_df, devil_fruit_df, how = "right")#左右代表取方向為標準
#取共通的陣列名,左右決定採用何者以他的行數為標準
print(straw_hat_merged)

name = ["娜菲鲁塔利·薇薇"]
occupation = ["阿拉巴斯坦王國公主"]
princess_vivi_dict = {"name": name,
                      "occupation": occupation
}


princess_vivi_df = pd.DataFrame(princess_vivi_dict, index = [len(straw_hat_df)])

# 新增一個觀測值
straw_hat_df_w_vivi = pd.concat([straw_hat_df, princess_vivi_df],axis=0)
print(straw_hat_df_w_vivi)

age = [19, 21, 20, 19, 21, 17, 30, 36, 90, 18]
age_dict = {"age": age
}

# 建立第三個 data frame
age_df = pd.DataFrame(age_dict)

# 新增一個變數欄位
straw_hat_df_w_vivi_age = pd.concat([straw_hat_df_w_vivi, age_df], axis = 1)
print(straw_hat_df_w_vivi_age.stack())#此方法把資料結構變成長的
