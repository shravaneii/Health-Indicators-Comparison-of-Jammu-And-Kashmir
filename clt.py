# Apply central limit theorem (CLT) for confidence intervals
# Assuming large sample size, use z-value of 1.96 for 95% confidence interval
se_public = np.std(data['Reported_Value_for_Public_Facility']) / np.sqrt(len(data))
ci_public = (avg_public - 1.96 * se_public, avg_public + 1.96 * se_public)

se_rural = np.std(data['Reported_Value_for_Rural']) / np.sqrt(len(data))
ci_rural = (avg_rural - 1.96 * se_rural, avg_rural + 1.96 * se_rural)

print(f"95% CI (CLT): {ci_public}")

print(f"95% CI (CLT): {ci_rural}")
