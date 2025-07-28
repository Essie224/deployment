import numpy as np
import pickle
import streamlit as st

#loading the model

model = pickle.load(open(r"C:\Users\HP\Desktop\gomycode_1\logistic_model_1.pkl", "rb"))

def performance_prediction(user_input):
    #convert data into an array
    input_array = np.asarray(user_input)

    #reshaped data into a two dimensional array
    reshaped_array = input_array.reshape(1, -1)

    #getting predicction
    prediction =model.predict(reshaped_array)
    if prediction == 0:
        return "This student did not pass"
    else:
        return "This student passed!!!"

def main():
    st.title("Citrone Performance Web App")

    Quiz_summary = st.text_input("Quiz Summary score")
    Assignment_summary = st.text_input("Assignment Summary score")
    Grade_Point_Average = st.text_input("Learner's Grade point Average score")
    Age = st.text_input("Learner's Age")
    Children = st.text_input("Does learner have Children? 1 yes/ 0 for no")
    Completed_Nysc = st.text_input("Completed Nysc ? 1 for yes/ 0 for no")
    Gender = st.text_input("What is learner's gender? 1 for  Male/ 0 for Female")

    performance = ""

    if st.button("Eligibility Result"):
        performance = performance_prediction([float(Quiz_summary), float(Assignment_summary), float(Grade_Point_Average), int(Age), int(Children), int(Completed_Nysc), int(Gender)])
        st.success(performance)

if  __name__ == "__main__":
    main()

