import math
import pandas as pd
from sqlalchemy import create_engine
import sqlite3


def get_salary(row):
    """Формирует зарплату по строке из датафрейма

        Args:
            row(Any): Строка из датафрейма
        Returns:
            float: Возвращает сформированную зарплату
    """
    salary_from = row.salary_from
    salary_to = row.salary_to
    salary_currency = row.salary_currency
    salary = row.salary
    if type(salary_currency) is str:
        if not math.isnan(salary_from) and not math.isnan(salary_to):
            salary = (salary_from + salary_to) / 2
        elif not math.isnan(salary_from):
            salary = salary_from
        elif not math.isnan(salary_to):
            salary = salary_to
        if salary_currency != 'RUR' and salary_currency in ["BYR", "USD", "EUR", "KZT", "UAH"]:
            date = f'01/{row.published_at[5:7]}/{row.published_at[:4]}'
            ratio_cur = cur.execute(f"""select {salary_currency} from data_currencies where date='{date}'""").fetchone()[0]
            salary = salary * ratio_cur if ratio_cur is not None else float('NaN')
        elif salary_currency != 'RUR':
            salary = float('NaN')
    return salary


conn = sqlite3.connect('currencies.db')
cur = conn.cursor()
engine = create_engine('sqlite:///D:\\Task221\\Khmeleva\\currencies.db')
pd.set_option('expand_frame_repr', False)
file = 'vacancies_dif_currencies.csv'
df = pd.read_csv(file)
df.insert(1, 'salary', float('NaN'))
df['salary'] = df.apply(lambda row: get_salary(row), axis=1)
df.pop('salary_from')
df.pop('salary_to')
df.pop('salary_currency')
df['published_at'] = df['published_at'].apply(lambda s: s[:10])
df.to_sql('vacancies', con=engine, index=False)