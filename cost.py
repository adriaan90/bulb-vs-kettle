import datetime

bulbWattRating = 6 #Watt
kettleWattRating = 3000 #Watt
cupBoilDuration = datetime.time(0,1,30) #datetime.time object 00:01:30
kiloWattHourCost = 1.02 #kWhour electricity cost of utility provider in £

costOfBoiling = kiloWattHourCost*(cupBoilDuration.hour+cupBoilDuration.minute/60+cupBoilDuration.second/3600)


boilAnHour = kiloWattHourCost*kettleWattRating/1000
lightAnHour = kiloWattHourCost*bulbWattRating/1000

totalWaterBoiled = 0.75 #Liter
excessBoiled = 0.25 #Liter
excessCost = costOfBoiling*(excessBoiled/totalWaterBoiled) 

equivalentBulbHours = excessCost/lightAnHour

theoreticalEnergy = totalWaterBoiled*4.184*80/3600
theoreticalTime = theoreticalEnergy/(kettleWattRating/1000)