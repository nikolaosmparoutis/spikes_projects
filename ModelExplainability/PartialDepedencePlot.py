
from sklearn.inspection import plot_partial_dependence
from sklearn.ensemble import HistGradientBoostingRegressor
from sklearn.datasets._california_housing import fetch_california_housing

df = fetch_california_housing(as_frame=True)
print(df)
x = df['data']
y = df['target']

est = HistGradientBoostingRegressor().fit(x, y)
est.score(x, y)
features = ['HouseAge',  'HouseAge', ['MedInc', 'HouseAge']]
plot_partial_dependence(est, x, features=features)

"""We can clearly see an interaction between the two features: 
for an Median income > 4.5, the House price is Dependent on HouseAge, 
for MedIncome  <  4.5 NO STRONG depedence HousePricing and HouseAge.
Makes sense ! Many Rich people Create more brand new Houses so they affect the House prices.
if we lived in Sao Paolo the very low income will not affect the  Relationship(Prices, Population)
because everyone is poor. 
"""

from matplotlib import pyplot as plt
plt.gca()
plt.show()

"""Disadvantages of PDP:
- The realistic maximum number of features in a partial dependence function is two.
- The assumption of independence is the biggest issue with PD plots. It is assumed that the feature(s) for 
which the partial dependence is computed are not correlated with other features.
One solution to this problem is Accumulated Local Effect plots or short ALE plots 
that work with the conditional instead of the marginal distribution.
-By plotting the individual conditional expectation curves instead of the aggregated line,
 we can uncover heterogeneous effects.
"""

