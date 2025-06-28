import streamlit as st
from medical_knowledge import get_matching_disease, get_remedies

# Page configuration
st.set_page_config(page_title="HealthAI - Disease and Remedy Checker", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        body { background-color: #f4f4f4; }
        .stTextInput>div>div>input {
            padding: 10px;
        }
        .stButton>button {
            padding: 10px 20px;
            width: 100%;
        }
        .remedy-box {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 8px;
            margin-top: 20px;
            box-shadow: 0 0 5px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("🤖 HealthAI: Intelligent Disease and Remedy Advisor")
st.write("Enter symptoms (comma-separated) to get a disease prediction and suggested home remedies.")

# Form for input
with st.form("diagnosis_form"):
    symptoms_input = st.text_input("Enter symptoms:", placeholder="e.g. headache, fever, nausea")
    submit_button = st.form_submit_button("🔍 Diagnose")

# Response block
if submit_button:
    if symptoms_input.strip() == "":
        st.warning("⚠️ Please enter symptoms to proceed.")
    else:
        symptoms = [s.strip().lower() for s in symptoms_input.split(",")]
        prediction = get_matching_disease(symptoms)

        with st.container():
            if prediction:
                remedies = get_remedies(prediction)
                st.markdown(f"<div class='remedy-box'><h4>🦠 Predicted Disease: {prediction.capitalize()}</h4>", unsafe_allow_html=True)
                st.markdown("<h5>🌿 Suggested Home Remedies:</h5><ul>", unsafe_allow_html=True)
                for remedy in remedies:
                    st.markdown(f"<li>{remedy}</li>", unsafe_allow_html=True)
                st.markdown("</ul></div>", unsafe_allow_html=True)
            else:
                st.markdown("<div class='remedy-box'><h4>❌ Could not determine the disease.</h4></div>", unsafe_allow_html=True)
