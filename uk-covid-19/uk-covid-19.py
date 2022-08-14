import pandas as pd
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv(r"C:\Users\Krish\Desktop\Python\covid-19\uk-covid-19.csv")

print(df)

print(df.dtypes)

ax = df.plot(kind = 'line', x = 'Day', y = 'CasesCumulative', label = "Cases")
df.plot(kind = 'line', x = 'Day', y = 'DeathsCumulative', label = "Deaths", ax=ax)


df.plot(kind = 'bar', x = 'Day', y = 'Cases', label = "Cases", title = "UK COVID-19")
df.plot(kind = 'bar', x = 'Day', y = 'Deaths', label = "Deaths", title = "UK COVID-19")

plt.title("UK COVID-19")

plt.show()

