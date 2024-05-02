# Bootstrap resampling for confidence intervals
n_bootstraps = 1000
boot_means_public = [np.mean(np.random.choice(data['Reported_Value_for_Public_Facility'], len(data))) for _ in range(n_bootstraps)]
boot_means_rural = [np.mean(np.random.choice(data['Reported_Value_for_Rural'], len(data))) for _ in range(n_bootstraps)]
ci_boot_public = np.percentile(boot_means_public, [2.5, 97.5])
ci_boot_rural = np.percentile(boot_means_rural, [2.5, 97.5])

print(f"95% CI (Bootstrap): {ci_boot_public}")
print()

print(f"95% CI (Bootstrap): {ci_boot_rural}")
print()
