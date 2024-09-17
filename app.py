import streamlit as st
import pandas as pd
import numpy as np
import pickle
import matplotlib.pyplot as plt
import plotly.express as px
# Load model
svc = pickle.load(open('svc.pkl', 'rb'))


symptoms_dict ={
    'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2, 'continuous_sneezing': 3, 'shivering': 4, 'chills': 5,
    'joint_pain': 6, 'stomach_pain': 7, 'acidity': 8, 'ulcers_on_tongue': 9, 'muscle_wasting': 10, 'vomiting': 11,
    'burning_micturition': 12, 'spotting_ urination': 13, 'fatigue': 14, 'weight_gain': 15, 'anxiety': 16,
    'cold_hands_and_feets': 17, 'mood_swings': 18, 'weight_loss': 19, 'restlessness': 20, 'lethargy': 21,
    'patches_in_throat': 22, 'irregular_sugar_level': 23, 'cough': 24, 'high_fever': 25, 'sunken_eyes': 26,
    'breathlessness': 27, 'sweating': 28, 'dehydration': 29, 'indigestion': 30, 'headache': 31, 'yellowish_skin': 32,
    'dark_urine': 33, 'nausea': 34, 'loss_of_appetite': 35, 'pain_behind_the_eyes': 36, 'back_pain': 37,
    'constipation': 38, 'abdominal_pain': 39, 'diarrhoea': 40, 'mild_fever': 41, 'yellow_urine': 42,
    'yellowing_of_eyes': 43, 'acute_liver_failure': 44, 'fluid_overload': 45, 'swelling_of_stomach': 46,
    'swelled_lymph_nodes': 47, 'malaise': 48, 'blurred_and_distorted_vision': 49, 'phlegm': 50,
    'throat_irritation': 51, 'redness_of_eyes': 52, 'sinus_pressure': 53, 'runny_nose': 54, 'congestion': 55,
    'chest_pain': 56, 'weakness_in_limbs': 57, 'fast_heart_rate': 58, 'pain_during_bowel_movements': 59,
    'pain_in_anal_region': 60, 'bloody_stool': 61, 'irritation_in_anus': 62, 'neck_pain': 63, 'dizziness': 64,
    'cramps': 65, 'bruising': 66, 'obesity': 67, 'swollen_legs': 68, 'swollen_blood_vessels': 69,
    'puffy_face_and_eyes': 70, 'enlarged_thyroid': 71, 'brittle_nails': 72, 'swollen_extremeties': 73,
    'excessive_hunger': 74, 'extra_marital_contacts': 75, 'drying_and_tingling_lips': 76, 'slurred_speech': 77,
    'knee_pain': 78, 'hip_joint_pain': 79, 'muscle_weakness': 80, 'stiff_neck': 81, 'swelling_joints': 82,
    'movement_stiffness': 83, 'spinning_movements': 84, 'loss_of_balance': 85, 'unsteadiness': 86,
    'weakness_of_one_body_side': 87, 'loss_of_smell': 88, 'bladder_discomfort': 89, 'foul_smell_of urine': 90,
    'continuous_feel_of_urine': 91, 'passage_of_gases': 92, 'internal_itching': 93, 'toxic_look_(typhos)': 94,
    'depression': 95, 'irritability': 96, 'muscle_pain': 97, 'altered_sensorium': 98, 'red_spots_over_body': 99,
    'belly_pain': 100, 'abnormal_menstruation': 101, 'dischromic _patches': 102, 'watering_from_eyes': 103,
    'increased_appetite': 104, 'polyuria': 105, 'family_history': 106, 'mucoid_sputum': 107, 'rusty_sputum': 108,
    'lack_of_concentration': 109, 'visual_disturbances': 110, 'receiving_blood_transfusion': 111,
    'receiving_unsterile_injections': 112, 'coma': 113, 'stomach_bleeding': 114, 'distention_of_abdomen': 115,
    'history_of_alcohol_consumption': 116, 'fluid_overload.1': 117, 'blood_in_sputum': 118,
    'prominent_veins_on_calf': 119, 'palpitations': 120, 'painful_walking': 121, 'pus_filled_pimples': 122,
    'blackheads': 123, 'scurring': 124, 'skin_peeling': 125, 'silver_like_dusting': 126, 'small_dents_in_nails': 127,
    'inflammatory_nails': 128, 'blister': 129, 'red_sore_around_nose': 130, 'yellow_crust_ooze': 131
}

diseases_list = {15: 'Fungal infection', 4: 'Allergy', 16: 'GERD', 9: 'Chronic cholestasis', 14: 'Drug Reaction', 33: 'Peptic ulcer diseae', 1: 'AIDS', 12: 'Diabetes ', 17: 'Gastroenteritis', 6: 'Bronchial Asthma', 23: 'Hypertension ', 30: 'Migraine', 7: 'Cervical spondylosis', 32: 'Paralysis (brain hemorrhage)', 28: 'Jaundice', 29: 'Malaria', 8: 'Chicken pox', 11: 'Dengue', 37: 'Typhoid', 40: 'hepatitis A', 19: 'Hepatitis B', 20: 'Hepatitis C', 21: 'Hepatitis D', 22: 'Hepatitis E', 3: 'Alcoholic hepatitis', 36: 'Tuberculosis', 10: 'Common Cold', 34: 'Pneumonia', 13: 'Dimorphic hemmorhoids(piles)', 18: 'Heart attack', 39: 'Varicose veins', 26: 'Hypothyroidism', 24: 'Hyperthyroidism', 25: 'Hypoglycemia', 31: 'Osteoarthristis', 5: 'Arthritis', 0: '(vertigo) Paroymsal  Positional Vertigo', 2: 'Acne', 38: 'Urinary tract infection', 35: 'Psoriasis', 27: 'Impetigo'}


description = pd.read_csv("description.csv")
precautions = pd.read_csv("precautions_df.csv")
medications = pd.read_csv("medications.csv")
workout = pd.read_csv("workout_df.csv")
diets = pd.read_csv("diets.csv")



def helper(disease):
    desc = description[description['Disease'] == disease]['Description'].values[0]
    pre = precautions[precautions['Disease'] == disease][['Precaution_1', 'Precaution_2', 'Precaution_3', 'Precaution_4']].values[0]
    med = medications[medications['Disease'] == disease]['Medication'].values
    diet = diets[diets['Disease'] == disease]['Diet'].values
    wrkout = workout[workout['disease'] == disease]['workout'].values
    return desc, pre, med, diet, wrkout

# Model prediction function
def get_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))  # Initialize the input vector
    for item in patient_symptoms:
        if item in symptoms_dict:
            input_vector[symptoms_dict[item]] = 1  # Set the corresponding symptoms to 1

    # Ensure that input_vector is a 2D array
    input_vector = np.reshape(input_vector, (1, -1))

    # Predict the disease index
    predicted_disease_index = svc.predict(input_vector)[0]

    return diseases_list.get(predicted_disease_index, "Disease not found")  # Return the disease name or default message




st.set_page_config(page_title="Medical Recommendation System", page_icon="🏥", layout="wide")


with st.sidebar:
    st.title("Symptom Checker 🩺")
    st.write("Select your symptoms and get a prediction.")
    selected_symptoms = st.multiselect('Select your symptoms:', list(symptoms_dict.keys()))


if st.button("Predict Disease"):
    if selected_symptoms:
        predicted_disease = get_predicted_value(selected_symptoms)
        desc, pre, med, diet, wrkout = helper(predicted_disease)

        # Disease Prediction Section
        st.success(f"### Predicted Disease: {predicted_disease}")

        # Layout improvements using columns
        st.write("---")
        st.write("### Disease Information")

        col1, col2 = st.columns([1, 1])

        with col1:
            st.write("#### Description")
            st.info(desc)

            st.write("#### Precautions")
            for i, precaution in enumerate(pre):
                st.write(f"**{i + 1}.** {precaution}")

        with col2:
            st.write("#### Medications")
            for med_item in med:
                st.write(f"- {med_item}")

            st.write("#### Workout")
            for workout_item in wrkout:
                st.write(f"- {workout_item}")

            st.write("#### Diet")
            for diet_item in diet:
                st.write(f"- {diet_item}")


        top_symptoms = {
            'fever': 80,
            'cough': 76,
            'headache': 60,
            'fatigue': 58,
            'sore throat': 54,
            'shortness of breath': 50,
            'loss of taste': 45,
            'muscle pain': 40,
            'nausea': 35,
            'vomiting': 30
        }


        symptom_df = pd.DataFrame(list(top_symptoms.items()), columns=['Symptom', 'Frequency'])


        fig = px.bar(symptom_df,
                     x='Symptom',
                     y='Frequency',
                     title="Top 10 Most Common Symptoms",
                     labels={'Frequency': 'Occurrences'},
                     color='Frequency',
                     color_continuous_scale='Blues')

        fig.update_layout(
            xaxis_title="Symptoms",
            yaxis_title="Frequency",
            template='plotly_white',
            title_x=0.5  # Center the title
        )

        st.write("---")
        st.write("### Symptom Insights 📊")
        st.plotly_chart(fig)


st.write("---")
st.write("### General Health Tips 🩺")


health_tips = [
    "Drink at least 8 glasses of water per day.",
    "Exercise regularly to stay fit and healthy.",
    "Get at least 7-8 hours of sleep every night.",
    "Maintain a balanced diet rich in vitamins and minerals.",
    "Avoid excessive alcohol consumption and smoking.",
    "Manage stress through meditation, yoga, or other relaxation techniques."
]

for tip in health_tips:
    st.write(f"💡 {tip}")


st.write("---")
st.write("""
    ### "The greatest wealth is health." – Virgil
""")


st.markdown("""
    <style>
    .stApp {
        background-color: #f0f2f6;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 5px;
    }
    .stSidebar {
        background-color: #e0e7ff;
    }
    .stMarkdown {
        font-family: 'Roboto', sans-serif;
    }
    </style>
""", unsafe_allow_html=True)
