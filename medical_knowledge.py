# ================== Medical Knowledge Base ==================

DISEASES = {
    "flu": {
        "symptoms": ["fever", "cough", "fatigue", "headache"],
        "remedies": ["Rest", "Drink warm fluids", "Use paracetamol"],
        "tip": "Avoid cold drinks. Stay isolated if coughing.",
        "alert": ""
    },
    "cold": {
        "symptoms": ["sneezing", "runny nose", "cough", "mild fever"],
        "remedies": ["Steam inhalation", "Vitamin C-rich foods", "Stay hydrated"],
        "tip": "Keep warm and avoid dusty environments.",
        "alert": ""
    },
    "dengue": {
        "symptoms": ["fever", "rash", "headache", "joint pain", "low platelet count"],
        "remedies": ["Papaya leaf juice", "Plenty of fluids", "Avoid aspirin"],
        "tip": "Monitor platelet count daily and avoid dehydration.",
        "alert": "🚨 Seek immediate medical attention if fever worsens."
    },
    "malaria": {
        "symptoms": ["fever", "chills", "sweating", "vomiting", "muscle pain"],
        "remedies": ["Antimalarial medication", "Rest", "Stay hydrated", "Use mosquito nets"],
        "tip": "Get a blood test immediately for confirmation.",
        "alert": "🚨 Consult a physician urgently."
    },
    "typhoid": {
        "symptoms": ["high fever", "abdominal pain", "constipation", "fatigue", "loss of appetite"],
        "remedies": ["Antibiotics", "Boiled water", "Soft foods", "Oral rehydration"],
        "tip": "Do not self-medicate. Maintain hygiene.",
        "alert": "🚨 Go to hospital if fever worsens."
    },
    "covid-19": {
        "symptoms": ["fever", "dry cough", "breathing difficulty", "loss of smell", "tiredness"],
        "remedies": ["Isolation", "Paracetamol", "Steam inhalation", "Hydration"],
        "tip": "Wear a mask and isolate.",
        "alert": "🚨 Visit a COVID clinic if symptoms increase."
    }
}

# ================== Prediction Logic ==================

def get_disease_predictions(user_symptoms):
    predictions = []
    user_symptoms = [s.strip().lower() for s in user_symptoms if s.strip()]

    if not user_symptoms:
        return []

    for disease, info in DISEASES.items():
        disease_symptoms = [s.lower() for s in info["symptoms"]]
        match_count = sum(1 for symptom in user_symptoms if any(symptom in ds for ds in disease_symptoms))
        total = len(disease_symptoms)
        if match_count > 0:
            score = int((match_count / total) * 100)
            predictions.append({
                "Disease": disease.capitalize(),
                "Confidence": f"{score}%",
                "Remedies": info["remedies"],
                "Tip": info["tip"],
                "Alert": info["alert"]
            })

    predictions.sort(key=lambda x: int(x["Confidence"].strip('%')), reverse=True)
    return predictions
