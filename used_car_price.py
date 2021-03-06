import streamlit as st
import numpy as np
import pandas as pd

import pickle

#title
st.title('Used car price prediction')
list_of_states= ('CA','FL','TX','NY','None of the above')
state=st.selectbox('Select The state:', list_of_states)
list_of_manf= ('Acura', 'Alfa', 'Alfa-Romeo','Aston', 'Aston-Martin', 'Audi', 'Bentley', 'Bmw', 'Buick','Cadillac', 'Chevrolet', 'Chrysler', 'Datsun', 'Dodge',
       'Ferrari', 'Fiat', 'Ford', 'Genesis', 'Gmc','Harley-Davidson', 'Honda', 'Hummer', 'Hyundai', 'Infiniti',
       'Jaguar', 'Jeep', 'Karma', 'Kia', 'Lamborghini', 'Land','Land Rover', 'Lexus', 'Lincoln', 'Maserati', 'Mazda',
       'Mclaren', 'Mercedes-Benz', 'Mercury', 'Mini', 'Mitsubishi','Morgan', 'Nissan', 'Not specified', 'Pontiac', 'Porsche',
       'Ram', 'Rolls-Royce', 'Rover', 'Saab', 'Saturn', 'Scion','Subaru', 'Suzuki', 'Tesla', 'Toyota', 'Volkswagen',
       'Volvo')
manf = st.selectbox('Select The Manufacturer of your car:',list_of_manf )
#tr
list_of_tran= ('Automatic', 'CVT','Manual','None')
Transmission= st.selectbox('Select The type of transmission on your car:', list_of_tran)
#feul
list_of_feul= ('Diesel', 'Electric', 'Flexible',
       'Gasoline', 'Hybrid', 'Other')
feul= st.selectbox('Select The Fuel type on your car:', list_of_feul)

list_of_eng= ('10 Cylinders', '12 Cylinders',
       '3 Cylinders', '4 Cylinders', '5 Cylinders',
       '6 Cylinders', '8 Cylinders', 'Other')
eng= st.selectbox('Select The engine type on your car:', list_of_eng)
#get user result
states=[]
manfs= []
tran=[]
feul_types =[]
engines=[]
#engine
for i in list_of_eng:
    if i == eng:
              engines.append(1)
    else:
              engines.append(0)
#state
for s in list_of_states:
    if state == s:
              states.append(1)
    else:
              states.append(0)
#manifacurers
for m in list_of_manf:
    if manf == m:
              manfs.append(1)
    else:
              manfs.append(0)
#transmissions
for t in list_of_tran:
    if Transmission == t:
              tran.append(1)
    else:
              tran.append(0)
#feul type
for f in list_of_feul:
    if feul == f:
              feul_types.append(1)
    else:
              feul_types.append(0)

year = st.text_input("Enter car's year of manufacture:  ", 0)
milage = st.text_input("enter distance in mile ('Milage'): ", 0)

states.pop()
answers = np.concatenate([[year],[milage],manfs,feul_types,tran,engines,states])


pred_btn = st.button('Predict Price')
pickle_in = open('regression/RegressionProject-main/regressor.pkl', 'rb')
regressor = pickle.load(pickle_in)
if pred_btn:
    result= regressor.predict([answers])
    result= result[0]
    result = str(round(result, 2))
    st.title(result)