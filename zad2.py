from numpy import random
from scipy import stats

random.seed(1)

srednia = 4
sigma = 2
ilosc = 100

zbior_liczb = random.normal(srednia, sigma, ilosc)
print("Zbiór liczb: %s" % zbior_liczb)

# D’Agostino K^2 
stat1, p1 = stats.normaltest(zbior_liczb)

# Shapiro-Wilk
stat2, p2 = stats.shapiro(zbior_liczb)

# Alfa 5%
alfa = 0.05
print("Alfa: %f" % alfa)

if (p1 > alfa):
    print("Test D’Agostino K^2: rozkład wygląda na normalny")
else:
    print("Test D’Agostino K^2: rozkład nie wygląda na normalny")

if (p2 > alfa):
    print("Test Shapiro-Wilk: rozkład wygląda na normalny")
else:
    print("Test Shapiro-Wilk: rozkład nie wygląda na normalny")

