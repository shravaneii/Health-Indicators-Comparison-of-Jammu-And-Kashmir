# Permutation resampling
obs_diff = avg_public - avg_rural
perm_diffs = []
for _ in range(n_bootstraps):
    perm_data = data.sample(frac=1).reset_index(drop=True)
    perm_diff = np.mean(perm_data['Reported_Value_for_Public_Facility']) - np.mean(perm_data['Reported_Value_for_Rural'])
    perm_diffs.append(perm_diff)
perm_diffs = np.array(perm_diffs)
p_value_perm = np.sum(perm_diffs >= obs_diff) / len(perm_diffs)

print(f"P-value (permutation): {p_value_perm}")
