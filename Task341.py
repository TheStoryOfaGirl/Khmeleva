import pandas as pd
import math


def get_salary(row):
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
            ratio_cur = currencies[currencies['date']
                                   == f'01/{row.published_at[5:7]}/{row.published_at[:4]}'][salary_currency].values[0]
            salary = salary * ratio_cur if not math.isnan(ratio_cur) else None
        elif salary_currency != 'RUR':
            salary = None
    return salary


pd.set_option('expand_frame_repr', False)
file = 'vacancies_dif_currencies.csv'
df = pd.read_csv(file, nrows=100)
currencies = pd.read_csv('data_currency.csv')
df.insert(1, 'salary', None)
df['salary'] = df.apply(lambda row: get_salary(row), axis=1)
df.pop('salary_from')
df.pop('salary_to')
df.pop('salary_currency')
df.to_csv("vacancies_result_100.csv", index=False)