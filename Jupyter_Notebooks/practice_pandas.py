import pandas as pd

df= pd.DataFrame({
    "Name": [
        "Venegas, Luis",
        "Nieves, Mily",
        "Nieves, Carlos",
    ],
    "Age": [22, 35, 58],
    "Sex": ["male", "female", 'female'],
})

# print(df)


# ?----------------------
# titanic = pd.read_csv('titanic.csv')

# __________________________
# print(titanic)
# print(titanic.head(8))
# print(titanic.tail(8))
# print(titanic.dtypes)

# _____________________

# titanic.to_excel('titanic.xlsx', sheet_name='passengers', index=False)