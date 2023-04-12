import pandas as pd

mtcars = pd.read_csv('mtcars.csv')

# Kojih 5 automobila ima najveću potrošnju? (koristite funkciju sort)

mtcars = mtcars.sort_values(by='mpg', ascending=True)

print(mtcars[0:5])

# Koja tri automobila s 8 cilindara imaju najmanju potrošnju?
mtcars = mtcars.sort_values(by='mpg', ascending=False)
print(mtcars[(mtcars.cyl == 8)].head(3))


# Kolika je srednja potrošnja automobila sa 6 cilindara?
mtcars_6 = mtcars.query('cyl==6')
print(mtcars_6)
mean_mtcars_6 = mtcars_6['mpg'].mean()
print("Srednja vrijednost potrosnje 6cyl: ", mean_mtcars_6)


# Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?
mtcars_4 = mtcars[(mtcars.cyl == 4) & (mtcars.wt >= 2.000) & (mtcars.wt <= 2200)]
print(mtcars_4)
mean_mtcars_4 = mtcars_4['mpg'].mean()
print(mean_mtcars_4)


# Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?
mtcars_a = mtcars[mtcars.am == 0]
print(mtcars_a)
print("Broj automobila s automatskim mjenjačem: ",len(mtcars_a))


mtcars_m = mtcars[mtcars.am == 1]
print("Broj automobila s manualnim mjenjačem: ",len(mtcars_m))

# Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?

print("Broj automobila s automatskim mjenjačem i preko 100 konjskih snaga: ",len(mtcars_a[mtcars_a.hp > 100]))



# Kolika je masa svakog automobila u kilogramima?

mtcars['KG'] = mtcars.wt * 453
print(mtcars)

















