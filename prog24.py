# -*- coding: utf-8 -*-
"""
Created on Mon Dec 22 08:59:22 2025

@author: 23csc11
"""

import pandas as pd
import matplotlib.pyplot as plt 


titanic = pd.read_csv("Titanic.csv")
print(titanic)

soton_alive = titanic[(titanic['embark_town'] == 'Southampton') & (titanic['alive'] == 'yes')]

print("Display the details of people whose embark_town is Southampton and who are alive\n",soton_alive)

alive_who = titanic[titanic['alive'] == 'yes']['who'].value_counts()
plt.plot(alive_who.index, alive_who.values, marker='D', color='red')
plt.title("Survivors by Category (Who)")
plt.show()

plt.scatter(titanic['class'].astype(str), titanic['sex'], alpha=0.05)
plt.title("Class vs Sex Distribution")
plt.show()

dead_3rd = titanic[(titanic['class'] == 'Third') & (titanic['alive'] == 'no')].groupby('sex').size()

print("Display the count of third class passengers who are dead according to sex\n",dead_3rd)

lone_town = titanic[titanic['alone'] == True]['embark_town'].value_counts().idxmax()

print("Which embark town has the highest number of lone passengers\n",lone_town)
