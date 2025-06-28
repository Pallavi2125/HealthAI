# ========== Medical Knowledge Base ==========
DISEASES = {
    "flu": {
        "symptoms": ["fever", "cough", "fatigue", "headache"],
        "remedies": ["Rest", "Drink warm fluids", "Use paracetamol"],
        "tip": "Avoid cold drinks. Stay isolated if coughing.",
        "alert": ""
    },
    "cold": {
        "symptoms": ["sneezing", "runny nose", "cough"],
        "remedies": ["Steam inhalation", "Vitamin C-rich foods", "Stay hydrated"],
        "tip": "Keep warm and avoid dusty environments.",
        "alert": ""
    },
    "dengue": {
        "symptoms": ["fever", "rash", "headache", "joint pain"],
        "remedies": ["Papaya leaf juice", "Plenty of fluids", "Avoid aspirin"],
        "tip": "Monitor platelet count daily.",
        "alert": "🚨 Seek immediate medical attention if fever worsens."
    },
    "malaria": {
        "symptoms": ["fever", "chills", "sweating", "vomiting"],
        "remedies": ["Antimalarial medication", "Rest", "Stay hydrated"],
        "tip": "Get a blood test immediately for confirmation.",
        "alert": "🚨 Consult a physician urgently."
    }
}

# ========== Disease Prediction Function ==========
def get_disease_predictions(user_symptoms):
    predictions = []
    for disease, info in DISEASES.items():
        match = len(set(user_symptoms) & set(info["symptoms"]))
        total = len(info["symptoms"])
        score = int((match / total) * 100)
        if match > 0:
            predictions.append({
                "Disease": disease.capitalize(),
                "Confidence": f"{score}%",
                "Remedies": info["remedies"],
                "Tip": info["tip"],
                "Alert": info["alert"]
            })
    predictions.sort(key=lambda x: int(x["Confidence"].strip('%')), reverse=True)
    return predictions
