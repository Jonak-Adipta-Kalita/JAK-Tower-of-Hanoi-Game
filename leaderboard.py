import pandas as pd

from src.db import Database
from tabulate import tabulate

db = Database()
data = db.get_leaderboard_data()

df = pd.DataFrame(data=data)
print(tabulate(df.values.tolist(), headers=["Username", "Score"], tablefmt="pretty"))
