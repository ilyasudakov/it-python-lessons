import pandas as pd
import matplotlib.pyplot as plt


# Создание Series
temperature_data = pd.Series([36.6, 36.7, 36.8, 36.5, 37.0, 37.2, 37.1], name='Temperature')

# Создание DataFrame
data = {
    'Day': ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье'],
    'Temperature': [36.6, 36.7, 36.8, 36.5, 37.0, 37.2, 37.1],
    'Pulse': [70, 72, 75, 68, 80, 78, 76]
}
medical_records = pd.DataFrame(data)

# Фильтрация данных
high_temperature = medical_records[medical_records['Temperature'] > 37.0]

# Сортировка данных
sorted_records = medical_records.sort_values(by='Pulse', ascending=False)

# Группировка и агрегирование данных
average_temperature_by_day = medical_records.groupby('Day')['Temperature'].mean()

# График температур
medical_records.plot(x='Day', y='Temperature', kind='line')
plt.title('Температурный график')
plt.xlabel('День')
plt.ylabel('Температура')
plt.show()

# Гистограмма пульса
medical_records['Pulse'].plot(kind='hist')
plt.title('Гистограмма пульса')
plt.xlabel('Пульс')
plt.ylabel('Частота')
plt.show()
