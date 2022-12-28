import pandas as pd
import sqlite3

conn = sqlite3.connect('currencies.db')
cur = conn.cursor()
pd.set_option('expand_frame_repr', False)
vacancy = input()
def print_statistics(vacancy):
    """Формирует зарплату по строке из датафрейма

        Args:
            vacancy(str): Название вакансии
    """
    print("Динамика уровня зарплат по годам:")
    print(pd.read_sql("select strftime('%Y', published_at) as date, round(avg(salary)) as avg_salary "
                      "from vacancies "
                      "group by strftime('%Y', published_at)", conn))
    print("Динамика количества вакансий по годам:")
    print(pd.read_sql("select strftime('%Y', published_at) as date, count(salary) as count_vacancy "
                      "from vacancies "
                      "group by strftime('%Y', published_at)", conn))
    print("Динамика уровня зарплат по годам для выбранной профессии:")
    print(pd.read_sql(f"""select strftime('%Y', published_at) as date, round(avg(salary)) as avg_salary 
                    from vacancies 
                    where name like '%{vacancy}%'
                    group by strftime('%Y', published_at)""", conn))
    print("Динамика количества вакансий по годам для выбранной профессии:")
    print(pd.read_sql(f"""select strftime('%Y', published_at) as date, count(salary) as count_vacancy 
                    from vacancies 
                    where name like '%{vacancy}%'
                    group by strftime('%Y', published_at)""", conn))
    print("Уровень зарплат по городам (в порядке убывания):")
    print(pd.read_sql("select area_name, avg "
                      "from (select area_name, round(avg(salary)) as 'avg', count(salary) as 'count' "
                      "from vacancies group by area_name order by avg desc) "
                      "where count > (select count(*) from vacancies) * 0.01 limit 10", conn))
    print('Доля вакансий по городам (в порядке убывания):')
    print(pd.read_sql('select area_name, round(cast(count as real) / (select count(*) '
                      'from vacancies), 4) as percent '
                      'from (select area_name, count(salary) as count '
                      'from vacancies '
                      'group by area_name '
                      'order by count desc) limit 10', conn))
print_statistics(vacancy)