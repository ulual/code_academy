#Code that uses poorly chosen variable names.
xxx = 10000
yyy = 0.1
zzz = 5

for iii in range(zzz):
    print(xxx * (1 + yyy)**iii)

#Code that uses meneangful variable names.
investments = 10000
yearly_return = 0.1
years = 5

for year in range(years):
    print(investments * (1 + yearly_return) ** year)