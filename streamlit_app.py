import streamlit as st
from src.pipeline.predict_pipeline import PredictPipeline,CustomData
st.set_page_config(
    page_title = "Student Exam Performance Predictor",
    page_icon = "🎓",
    layout = "centered"
)

st.title("🎓 Student Exam Performance Predictor")

st.write("Enter the student details beow to predict the Maths Score.")

gender = st.selectbox(
    "Gender",
    ['male','female']
)

race_ethinicity = st.selectbox(
    "Race / Ethnicity",
    ['group A' , "group B" , 'group C' , 'group D' , 'group E']
)

parental_level_of_education = st.selectbox(
    "Parental Level of Education",
    [
        "associate's degree",
        "bachelor's degree",
        "high school",
        "master's degree",
        "some college",
        "some high school"
    ]
)

lunch = st.selectbox(
    "Lunch Type",
    ['free/reduced' ,"standard"]
)

test_preparation_course = st.selectbox(
    "Test Preparation Course",
    ['none','completed']
)

reading_score = st.number_input(
    "Reading Score",
    min_value = 0,
    max_value = 100,
    value = 50
)
writing_score = st.number_input(
    "writing Score",
    min_value = 0,
    max_value = 100,
    value = 50
)

if st.button("Predict Maths SCore"):
    data = CustomData(
        gender = gender,
        race_ethnicity=race_ethinicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    pred_df = data.get_data_as_data_frame()

    pipeline = PredictPipeline()

    prediction = pipeline.predict(pred_df)

    st.success(f"Predict Maths Score: **{prediction[0]:.2f}**")