
# T-test
t_stat, p_value_t = stats.ttest_ind(data['Reported_Value_for_Public_Facility'], data['Reported_Value_for_Rural'])

print(f"P-value (t-test): {p_value_t}")
print()
