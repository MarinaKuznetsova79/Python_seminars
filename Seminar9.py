import pandas as pd
df = pd.read_csv('california_housing_train.csv')

# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке sample_data.
# Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population).

mean = df.loc[df['population'] < 500]['median_house_value'].mean()
print(f'Cредняя стоимость дома, где кол-во людей от 0 до 500 (population): {mean}')

# Задача 42: Узнать какая максимальная households в зоне минимального значения population.

print(f'Mаксимальная households в зоне минимального значения population = {df.describe().min().households}')
Cредняя стоимость дома, где кол-во людей от 0 до 500 (population): 206683.83635227982
Mаксимальная households в зоне минимального значения population = 1.0
