from statsmodels.stats.proportion import proportions_ztest

count = [8502, 8279]      #  Showing returners in each group
nobs = [44700, 45489]     # Showingtotal players in each group

z_stat, p_value = proportions_ztest(count, nobs)
print(z_stat, p_value)
