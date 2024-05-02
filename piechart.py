
"""# Pie Chart for Reported_Value_for_Public_Facility wrt Code_And_Section"""

# Filter the DataFrame for sections excluding M9
filtered_data = hmis_data[hmis_data['Code_And_Section'] != 'M9']

# Group by 'Code_And_Section' and sum the values for each section
grouped_data = filtered_data.groupby('Code_And_Section')['Reported_Value_for_Public_Facility'].sum()

# Determine which section to explode
explode = [0.1 if section == 'M9 [CHILD IMMUNISATION]' else 0 for section in grouped_data.index]

# Creating a pie chart with shadow effect and exploding a specific section
plt.figure(figsize=(8, 6))
patches, texts, autotexts = plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)

# Adjust the transparency of autopct texts to control the shadow intensity
for autotext in autotexts:
    autotext.set_alpha(0.5)

plt.title('Reported Value for Public Facility by Code and Section')
plt.legend(title='Code and Section', loc='center left', bbox_to_anchor=(1, 0.7))
plt.show()

"""# Pie Chart for Reported_Value_for_Rural wrt Code_And_Section"""

# Filter the DataFrame for sections excluding M9
filtered_data = hmis_data[hmis_data['Code_And_Section'] != 'M9']

# Group by 'Code_And_Section' and sum the values for each section
grouped_data = filtered_data.groupby('Code_And_Section')['Reported_Value_for_Rural'].sum()

# Determine which section to explode
explode = [0.1 if section == 'M9 [CHILD IMMUNISATION]' else 0 for section in grouped_data.index]

# Creating a pie chart with shadow effect and exploding a specific section
plt.figure(figsize=(8, 6))
patches, texts, autotexts = plt.pie(grouped_data, labels=grouped_data.index, autopct='%1.1f%%', startangle=140, explode=explode, shadow=True)

# Adjust the transparency of autopct texts to control the shadow intensity
for autotext in autotexts:
    autotext.set_alpha(0.5)

plt.title('Reported Value for Rural by Code and Section')
plt.legend(title='Code and Section', loc='center left', bbox_to_anchor=(1, 0.7))
plt.show()
