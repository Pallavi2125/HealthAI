import streamlit as st
from medical_knowledge import get_matching_disease, get_remedies

# Set the page title and layout
st.set_page_config(page_title="HealthAI - Disease and Remedy Checker", layout="centered")

# App title
st.title("🤖 HealthAI: Intelligent Disease and Remedy Advisor")
st.markdown("Enter symptoms below (comma-separated) to get a disease prediction and home remedies.")

# Input form
with st.form("diagnose_form"):
    symptoms_input = st.text_input("Enter symptoms (comma-separated)", placeholder="e.g. headache, fever, nausea")
    submitted = st.form_submit_button("🔍 Diagnose")

# If the form is submitted
if submitted:
    if symptoms_input.strip() == "":
        st.warning("⚠️ Please enter at least one symptom.")
    else:
        symptoms = [s.strip().lower() for s in symptoms_input.split(",")]
        prediction = get_matching_disease(symptoms)

        if prediction:
            remedies = get_remedies(prediction)
            st.success(f"🦠 Predicted Disease: {prediction.capitalize()}")
            st.markdown("### 🌿 Suggested Home Remedies:")
            for remedy in remedies:
                st.markdown(f"- {remedy}")
        else:
            st.error("❌ Could not determine the disease.")
