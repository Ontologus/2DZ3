import pandas as pd
from IPython.display import display
df = pd.read_csv('/content/Customers.csv', delimiter=';')
print('(1)Те, кому больше 30 и кто зарабатывает меньше 30000', '\n')
display(df[(df['Age'] > 30) & (df['Income'] < 30000)])
print('\n', '(2)Юристы с опытом работы более 5 лет', '\n')
display(df[(df['Profession'] == 'Lawyer') & (df['Work Experience'] > 5)])