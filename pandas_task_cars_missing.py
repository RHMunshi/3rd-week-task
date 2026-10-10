import pandas as pd

# df = pd.read_csv("Cars93_missing.csv")  # Read CSV file and transfer it into DataFrame

# print(df)

# df = pd.read_csv("Cars93_missing.csv")  # Transfer object Series into index column of the dataframe

# df.index = df["Make"]

# print(df)

# df = pd.read_csv("Cars93_missing.csv")

# df.loc[df["Price"] > 30, "Type"] = "Expensive"  # Change the data in the column of DataFrame according to
# some condition

# print(df[["Price", "Type"]])   

df = pd.read_csv("Cars93_missing.csv")

# # Get names of the DataFrame columns and sum of losted values DF

# print("Column names:")
# print(df.columns.tolist())

# print("\nMissing values in each column:")
# print(df.isna().sum())

# print("\nTotal missing values:")
# print(df.isna().sum().sum())

# Ex-change 2 columns, use function for it. Sort coulumn by name

# def exchange_columns(df, col1, col2):
#     columns = df.columns.tolist()

#     index1 = columns.index(col1)
#     index2 = columns.index(col2)

#     columns[index1], columns[index2] = columns[index2], columns[index1]

#     return df[columns]


# df = pd.read_csv("Cars93_missing.csv")

# df = exchange_columns(df, "Price", "MPG.city")

# df = df[sorted(df.columns)]

# print(df.head())

# Delete upper and lowe 5% in object DataFrame

# df = pd.read_csv("Cars93_missing.csv")

# lower = df["Price"].quantile(0.05)
# upper = df["Price"].quantile(0.95)

# df = df[(df["Price"] >= lower) & (df["Price"] <= upper)]

# print(df)

# ( Apply) missed values in the Column with average values.


# average_price = df["Price"].mean()

# df["Price"] = df["Price"].fillna(average_price)

# print(df["Price"])

# dict1 = {
#     "Name": ["Rajib", "Ali", "John"],
#     "Age": [28, 25, 30]
# }

# dict2 = {
#     "City": ["Dortmund", "Bochum", "Essen"],
#     "Country": ["Germany", "Germany", "Germany"]
# }

# df1 = pd.DataFrame(dict1)
# df2 = pd.DataFrame(dict2)

# df_merged = pd.concat([df1, df2], axis=1)

# print(df_merged)

#  For any column create histogram

# import matplotlib.pyplot as plt

# # df = pd.read_csv("Cars93_missing.csv")

# df["Price"].hist()

# plt.xlabel("Price")
# plt.ylabel("Number of cars")
# plt.title("Car Price Histogram")

# plt.show()

# Create Correlation Matrix for any column

df = pd.read_csv("Cars93_missing.csv")

correlation = df[
    ["Price", "Horsepower", "MPG.city", "Weight", "EngineSize"]
].corr()

print(correlation)