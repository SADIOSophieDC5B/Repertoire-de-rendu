import pandas as pd

data = {'Id' : ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'],
'Nom de la tondeuse' : ['Tond1','Tond2','Tond3','Tond4','Tond5','Tond6','Tond7','Tond8','Tond9','Tond10','Tond11','Tond12','Tond13','Tond14','Tond15','Tond16','Tond17','Tond18','Tond19'],
'Puissance' : ['230V','240V','320V','360V','230V','240V','320V','360V','230V','240V','320V','360V','230V','240V','320V','360V','230V','240V','320V'],
'Autonomie' : ['1H','2H','3H','4h','1H','2H','3H','4h','1H','2H','3H','4h','1H','2H','3H','4h','1H','2H','3H'],
'Energie' : ['Gaz','Electrique','solaire','Electrique','Gaz','Electrique','solaire','Electrique','Gaz','Electrique','solaire','Electrique','Gaz','Electrique','solaire','Electrique','Gaz','Electrique','solaire'],
 }

df = pd.DataFrame(data)

df.to_csv('tondeuse.csv', index=False)





df = pd.read_csv("C:\\Users\\33789\\Desktop\\Python\\exo2\\tondeuse.csv")
print(df.head(20))

