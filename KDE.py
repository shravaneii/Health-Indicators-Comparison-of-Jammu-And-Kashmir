plt.figure(figsize=(12, 8))

# Plot KDE for Reported_Value_for_Public_Facility
plt.subplot(2, 2, 1)
sns.kdeplot(hmis_data['Reported_Value_for_Public_Facility'], color='blue', shade=True)
plt.xlabel('Reported Value for Public Facility')
plt.ylabel('Density')
plt.title('Kernel Density Plot of Reported Value for Public Facility')


# Plot KDE for Reported_Value_for_Rural
plt.subplot(2, 2, 3)
sns.kdeplot(hmis_data['Reported_Value_for_Rural'], color='green', shade=True)
plt.xlabel('Reported Value for Rural')
plt.ylabel('Density')
plt.title('Kernel Density Plot of Reported Value for Rural')


plt.tight_layout()
plt.show()
