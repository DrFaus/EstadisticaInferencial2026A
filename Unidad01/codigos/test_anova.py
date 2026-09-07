# test de ANOVA (Analysis of Variance)
# H0: beta_1 = 0   (No hay correlación)
# H1: beta_1 ≠ 0   (Sí hay correlación)

import statsmodels.api as sm
from statsmodels.formula.api import ols
# Y ~ X
modelo_lineal = ols('gasto_general ~ unidades', data = df).fit()
tabla_anova = sm.stats.anova_lm(modelo_lineal)
tabla_anova
