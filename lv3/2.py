import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
# Pomoću barplot-a prikažite na istoj slici potrošnju automobila s 4, 6 i 8 cilindara.


mtcars_4cyl=mtcars[mtcars.cyl==4]
mtcars_6cyl=mtcars[mtcars.cyl==6]
mtcars_8cyl=mtcars[mtcars.cyl==8]

mean_mpg4=mtcars_4cyl['mpg'].mean()
mean_mpg6=mtcars_6cyl['mpg'].mean()
mean_mpg8=mtcars_8cyl['mpg'].mean()

plt.bar(['4 Cilindra','6 Cilindra','8 Cilindra'], [mean_mpg4,mean_mpg6,mean_mpg8], color=['red','green','blue'])
plt.xlabel('Cilindri')
plt.ylabel('Potrosnja mpg')


# Pomoću boxplot-a prikažite na istoj slici distribuciju težine automobila s 4, 6 i 8 cilindara.

mtcars_468cyl = mtcars[(mtcars.cyl == 4) | (mtcars.cyl == 6) | (mtcars.cyl == 8)]
mtcars_468cyl.boxplot(column='wt', by='cyl', grid=False)
plt.ylabel('Weight wt')

# Pomoću odgovarajućeg grafa pokušajte odgovoriti na pitanje imaju li automobili s ručnim mjenjačem veću potrošnju od automobila s automatskim mjenjačem?
plt.figure(figsize=(8, 6))
mcars = mtcars[(mtcars.am == 1)]
acars = mtcars[(mtcars.am == 0)]

mean_mcars = mcars['mpg'].mean()
mean_acars = acars['mpg'].mean()

plt.bar(['Rucni', 'Automatik'], [mean_mcars, mean_acars], color=['red', 'blue'])
plt.ylabel('Potrosnja mpg')




mtcars.boxplot(column='mpg', by='am', grid=False)



# Prikažite na istoj slici odnos ubrzanja i snage automobila za automobile s ručnim odnosno automatskim mjenjačem.
plt.figure(figsize=(8, 6))
plt.scatter(mcars['hp'], mcars['qsec'], color='red', label='ručni')
plt.scatter(acars['hp'], acars['qsec'], color='blue', label='automatik')
plt.xlabel('HP')
plt.ylabel('QSEC')
plt.legend()

plt.show()
