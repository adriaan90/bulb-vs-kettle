import streamlit as st
import datetime

st.title('Cost of boiling excess water')

kettleWattRating = st.slider('Kettle power rating (Watt):',
                            1000, 5000,step=500)

bulbWattRating = st.slider("Bulb power rating (Watt)",
                           1,20,step=1)

cupBoilDuration = st.slider("Time water boiled (mm:ss)",
                            datetime.time(minute=0,second=0, microsecond=0),
                            datetime.time(minute=5, second=0,microsecond=0),
                            step=datetime.timedelta(seconds = 1),
                            format="mm:ss")

totalBoilingDuration = (cupBoilDuration.hour+
                        cupBoilDuration.minute/60+
                        cupBoilDuration.second/3600)

totalWaterBoiled = st.slider('Total water boiled (liters)',
                             0.1,3.0,step=0.05) #Liter
excessBoiled = st.slider('Water not used (liters)',
                         0.0,3.0,step=0.05) #Liter

excessTime = totalBoilingDuration*(excessBoiled/totalWaterBoiled) 

lightAnHour = bulbWattRating/1000
equivalentBulbHours = excessTime/lightAnHour

st.write(f"One bulb burning {round(equivalentBulbHours,1)} hours.")



