from multiprocessing import Pool

import pandas as pd
from datetime import datetime
from functools import partial
import math

from Task232 import Report


def get_statistic_by_year(f, vacancy, area_name, statistics):
    df = pd.read_csv(f)
    df["salary"] = df[['salary_from', 'salary_to']].mean(axis=1)
    year = int(f[15:19])
    statistics[0] = (year, int(df["salary"].mean()))
    statistics[1] = (year, df[(df['name'] == vacancy) & (df['area_name'] == area_name)]['salary'].mean() if
                     math.isnan(df[(df['name'] == vacancy) & (df['area_name'] == area_name)]['salary'].mean()) else
                     int(df[(df['name'] == vacancy) & (df['area_name'] == area_name)]['salary'].mean()))
    statistics[2] = (year, len(df))
    statistics[3] = (year, len(df[(df["name"] == vacancy) & (df['area_name'] == area_name)]))
    return statistics

def get_statistic_by_city(file):
    df = pd.read_csv(file)
    df = df[df['area_name'].map(df['area_name'].value_counts()) > len(df) * 0.01]
    df["salary"] = df[['salary_from', 'salary_to']].mean(axis=1)
    cities = df["area_name"].unique()
    stat1 = {city: [] for city in cities}
    stat2 = {city: 0 for city in cities}
    for city in cities:
        stat1[city] = df[df['area_name'] == city]['salary'].mean() \
            if math.isnan(df[df['area_name'] == city]['salary'].mean()) \
            else int(df[df['area_name'] == city]['salary'].mean())
        stat2[city] = round(len(df[df['area_name'] == city]) / len(df), 4)
    stat1 = dict(sorted(stat1.items(), key=lambda x: x[1], reverse=True)[:10])
    stat2 = dict(sorted(stat2.items(), key=lambda x: x[1], reverse=True)[:10])
    return [stat1, stat2]


if __name__ == '__main__':
    file = input('Введите название файла: ')
    vacancy = input('Введите название вакансии: ')
    area_name = input('Введите название региона: ')
    df = pd.read_csv(file)
    df["years"] = df["published_at"].apply(lambda s: datetime.strptime(s, "%Y-%m-%dT%H:%M:%S%z").year)
    years = df["years"].unique()
    salary_by_years = {year: [] for year in years}
    vac_salary_by_year = {year: [] for year in years}
    vac_by_years = {year: 0 for year in years}
    vac_count_by_years = {year: 0 for year in years}
    statistics = [salary_by_years, vac_salary_by_year, vac_by_years, vac_count_by_years]
    files = []
    for year in years:
        data = df[df["years"] == year]
        data.to_csv(f"csv_files\\year_{year}.csv")
        files.append(f"csv_files\\year_{year}.csv")
    p = Pool()
    output = list(p.map(partial(get_statistic_by_year, vacancy=vacancy, area_name=area_name, statistics=statistics), files))
    salary_by_years = {stat[0][0]: stat[0][1] for stat in output}
    vac_salary_by_year = {stat[1][0]: stat[1][1] for stat in output}
    vac_by_years = {stat[2][0]: stat[2][1] for stat in output}
    vac_count_by_years = {stat[3][0]: stat[3][1] for stat in output}
    res_city, res_city_vac = get_statistic_by_city(file)
    statistics = [salary_by_years, vac_salary_by_year, vac_by_years, vac_count_by_years, res_city, res_city_vac]
    rp = Report()
    rp.generate_excel(vacancy, statistics)
    rp.generate_image(vacancy, statistics)
    rp.generate_pdf(vacancy)
    print('Уровень зарплат по городам (в порядке убывания):', res_city)
    print('Доля вакансий по городам (в порядке убывания):', res_city_vac)
    print("Динамика уровня зарплат по годам для выбранной профессии и региона:", vac_salary_by_year)
    print("Динамика количества вакансий по годам для выбранной профессии и региона", vac_count_by_years)




