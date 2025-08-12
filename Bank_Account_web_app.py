import numpy as np
import pickle
import streamlit as st

model = pickle.load(open("RandomForestClassifier_Model_Bank_Account.pkl",'rb' ))


country_mapping = {
    'Kenya': 0, 
    'Rwanda': 1, 
    'Tanzania': 2,
    'Uganda': 3
    }


education_mapping ={
    'Secondary education': 3,
    'No formal education': 0,
    'Vocational/Specialised training': 5,
    'Primary education': 2,
    'Tertiary education': 4, 
    'Other/Dont know/RTA': 1
    }


job_mapping={
    'Self employed': 9 ,
    'Government Dependent': 4,
    'Formally employed Private': 3,
    'Informally employed': 5 ,
    'Formally employed Government': 2, 
    'Farming and Fishing': 1,
    'Remittance Dependent': 8, 
    'Other Income': 7,
    'Dont Know/Refuse to answer': 0,
    'No Income': 6
}

def Bank_Account_prediction(user_input):
    #convert data into an array
    input_array = np.asarray(user_input)

    
    #reshaped data into a two dimensional array
    reshaped_array = input_array.reshape(1, -1)

    #getting predicction
    prediction =model.predict(reshaped_array)
    if prediction == 0:
        return "no, won't have a bank account"
    else:
        return "yes, will have a bank account"
    
    
    
        
def main():
    st.title("Bank Account Prediction Web App")

    country = st.selectbox("select Country:", list(country_mapping.keys()))
    encoded_country = country_mapping[country]
    location_type = st.text_input("location? 0 for Rural/ 1 for Urban")
    cellphone_access = st.text_input("cellphone_access? 1 for yes/ 0 for no")
    age= st.text_input("age_of_respondent")
    gender = st.text_input("gender_of_respondent? 1 for  Male/ 0 for Female")
    education_level = st.selectbox(" select education level:", list(education_mapping.keys()))
    encoded_education = education_mapping[education_level]
    job_type = st.selectbox("select job type:", list(job_mapping.keys()))
    encoded_job_type = job_mapping[job_type]
    

    prediction = ""

    if st.button("predict"):
        prediction = Bank_Account_prediction([(encoded_country), int(location_type), int(age), (encoded_education), (encoded_job_type), int(cellphone_access), int(gender)])
        st.success(prediction)

        
if  __name__ == "__main__":
    main()
