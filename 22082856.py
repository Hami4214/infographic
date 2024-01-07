#github repo link
#https://github.com/Hami4214/infographic
#student id 22082856

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Your data
data = pd.read_csv("data_file.csv")
df = pd.DataFrame(data)

# Set a Seaborn style
sns.set_theme(style="whitegrid")

# Sort the data by gross box office in descending order
df.sort_values(by='Gross box office (£ million)', ascending=False, inplace=True)

# Plotting
plt.figure(figsize=(14, 8))

# Bar plot with a color gradient based on gross box office
bars = sns.barplot(data=df, x='Gross box office (£ million)', y='Title', hue='Gross box office (£ million)',
                   palette="Paired", dodge=False)

# Adding labels and title
plt.title('Top 10 Foreign Language Films Released in the UK and Republic of Ireland (2021)', fontsize=18, fontweight='bold')
plt.xlabel('Gross box office (£ million)', fontsize=14)
plt.ylabel('Film Title', fontsize=14)

# Adding data labels for each bar
for bar, label in zip(bars.patches, df['Gross box office (£ million)']):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{label:.2f}M', va='center', ha='left', fontsize=10)

# Add a horizontal line for the average
average_gross = df['Gross box office (£ million)'].mean()
plt.axvline(average_gross, color='red', linestyle='--', linewidth=2, label=f'Average: £{average_gross:.2f}M')

# Beautify the plot
plt.legend(title='Gross Box Office (£ million)', title_fontsize='12')
plt.tight_layout()

# Adding annotations
plt.annotate('Average Gross', xy=(average_gross, 10), xytext=(average_gross + 0.2, 8),
             arrowprops=dict(facecolor='black', shrink=0.05), fontsize=12)

plt.savefig("22082856.png")





#line plot
data1 = pd.read_csv("data1.csv")
df = pd.DataFrame(data1)

# Set a custom color palette
colors = sns.color_palette("pastel")

# Plotting
plt.figure(figsize=(12, 6))

# Line plot for different distributors
sns.lineplot(data=df, x=df.index, y='Box office gross (£ million)', hue='Distributor', marker='o', markersize=10, palette=colors, linewidth=2)

# Adding labels and title
plt.title('Box Office Gross with Different Distributors', fontsize=18, fontweight='bold')
plt.xlabel('Film Index', fontsize=14)
plt.ylabel('Box Office Gross (£ million)', fontsize=14)

# Adding data labels for each point
for i, txt in enumerate(df['Number of weeks at number one']):
    plt.annotate(f'Weeks: {txt}', (i, df['Box office gross (£ million)'][i]),
                 textcoords="offset points", xytext=(0, 5), ha='center', fontsize=10)

# Beautify the plot
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend(title='Distributor', title_fontsize='12')
plt.tight_layout()

# Adding a background color
background_color = "#f5f5f5"
plt.gca().set_facecolor(background_color)
plt.savefig('box_office_gross_plot.png', format='png', bbox_inches='tight', dpi=300)
plt.savefig("22082856.png")




#bar plot

data_file = pd.read_csv("data_file1")

df = pd.DataFrame(data_file)

# Set a color palette for better visualization
colors = sns.color_palette('viridis', len(df))

# Plotting
plt.figure(figsize=(12, 6))
bars = plt.bar(df['Title'], df['Box office gross (£ million)'], color=colors)

# Adding labels and title
plt.title('Box Office Gross of Top 14 Movies', fontsize=22, fontweight='bold')
plt.xlabel('Movie Title', fontsize=14)
plt.ylabel('Box Office Gross (£ million)', fontsize=14)

# Rotating x-axis labels for better readability
plt.xticks(rotation=45, ha='right', fontsize=12)

# Adding data labels on top of each bar
for bar, label in zip(bars, df['Box office gross (£ million)']):
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.2, f'{label:.1f}', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.savefig("22082856.png")




#pie plot


data_file1 = pd.read_csv("data-file")

df = pd.DataFrame(data_file1)

# Calculate the percentage admissions for each year
df['Percentage'] = (df['Admissions (million)'] / df['Admissions (million)'].sum()) * 100

# Identify slices with values above a certain threshold for labeling
label_threshold = 10 # Adjust the threshold as needed
labels = df[df['Percentage'] > label_threshold]['Year'].astype(str)

# Plotting
colors = plt.cm.Paired(range(len(df)))

plt.figure(figsize=(10, 8))
pie_wedge_collection, texts, autotexts = plt.pie(df['Percentage'], labels=None, autopct='%1.1f%%', startangle=140,
                                                 colors=colors, wedgeprops=dict(width=0.8, edgecolor='w'),
                                                 labeldistance=1.05, pctdistance=0.6)

# Add labels for slices with higher values
for label, autotext in zip(labels, autotexts):
    autotext.set_text(f'{label}\n{df[df["Year"] == int(label)]["Percentage"].values[0]:.1f}%')

plt.title('Annual UK Cinema Admissions (2012-2021)', fontsize=16, fontweight='bold')
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.savefig("22082856.png")
