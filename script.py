import codecademylib3_seaborn 
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# World Cup Matches
df = pd.read_csv('WorldCupMatches.csv')
print(df.head())

df['Total Goals'] = df['Home Team Goals'] + df['Away Team Goals']
print(df.head())


sns.set_style('whitegrid')
sns.set_context('poster', font_scale= 0.8)

f, ax= plt.subplots(figsize=(12,7))
ax = sns.barplot(data= df, x= 'Year', y = 'Total Goals')
ax.set_title('Goals Over The Years')

plt.show()

# Goals
df2= pd.read_csv('goals.csv')
print(df2.head())
sns.set_context('notebook', font_scale = 1.25)

f, ax2 = plt.subplots(figsize= (12,7))
sns.boxplot(data= df2, x= 'year', y= 'goals', palette= 'Spectral')
ax2.set_title('Goals')
plt.show()



