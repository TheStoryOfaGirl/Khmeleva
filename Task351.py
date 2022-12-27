import pandas as pd
from sqlalchemy import create_engine
import sqlite3
conn = sqlite3.connect('currencies.db')
engine = create_engine('sqlite:///D:\\Task221\\Khmeleva\\currencies.db')
df = pd.read_csv('data_currency.csv')
df.to_sql('data_currencies', con=engine)
