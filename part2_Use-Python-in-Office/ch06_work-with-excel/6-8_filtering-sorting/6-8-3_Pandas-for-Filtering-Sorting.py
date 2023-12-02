import pandas as pd

df = pd.read_excel("./test.xlsx", sheet_name="Sheet")

df_value = df.sort_values(by=["桃子", "西瓜"], ascending = False)

with pd.ExcelWriter('./test1.xlsx') as writer:
    df_value.to_excel(writer, sheet_name="Sheet_Sorted", index=False)