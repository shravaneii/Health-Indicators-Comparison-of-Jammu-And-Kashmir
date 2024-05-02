
# Contingency table and chi-square test
# Assuming you want to compare counts in different categories
contingency_table = pd.crosstab(index=data['Reported_Value_for_Public_Facility'], columns=data['Reported_Value_for_Rural'])
chi2, p_value_chi = stats.chisquare(contingency_table)


print("Contingency Table:")
print(contingency_table)
print(f"Chi-square: {chi2}")
print(f"P-value (chi-square): {p_value_chi}")