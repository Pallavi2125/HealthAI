import streamlit as st
from medical_knowledge import get_disease_predictions

# ========== Streamlit UI Setup ==========
st.set_page_config(page_title="HealthAI Pro - Disease & Remedy Checker", layout="centered")

# CSS Styling
st.markdown("""
    <style>
        .remedy-box {
            background-color: #fff;
            padding: 1.2rem;
            margin-bottom: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        }
    </style>
""", unsafe_allow_html=True)

# ========== Title ==========
st.title("🤖 HealthAI Pro")
st.subheader("AI-powered Disease & Remedy Advisor")
st.write("Enter your symptoms to get real-time diagnosis, home remedies, doctor tips & alerts.")

# ========== Input Section ==========
with st.form("diagnosis_form"):
    symptoms_input = st.text_input("📝 Enter symptoms (comma-separated):", placeholder="e.g. fever, cough, headache")
    submitted = st.form_submit_button("🔍 Diagnose")

# ========== Prediction Results ==========
if submitted:
    if not symptoms_input.strip():
        st.warning("⚠️ Please enter at least one symptom.")
    else:
        symptoms = [s.strip().lower() for s in symptoms_input.split(",")]
        results = get_disease_predictions(symptoms)

        if results:
            for item in results:
                st.markdown("<div class='remedy-box'>", unsafe_allow_html=True)
                st.subheader(f"🦠 {item['Disease']} (Confidence: {item['Confidence']})")
                st.markdown("### 🌿 Home Remedies")
                for remedy in item["Remedies"]:
                    st.markdown(f"- {remedy}")
                st.markdown(f"**💡 Doctor Tip:** {item['Tip']}")
                if item["Alert"]:
                    st.error(item["Alert"])
                st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.info("❗ No known disease matched. Try more common symptoms.")

# ========== Footer ==========
st.markdown("---")
st.markdown("🧠 Built with ❤️ by HealthAI Team | SmartInternz + IBM Granite")
