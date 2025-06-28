from difflib import SequenceMatcher

MEDICAL_KNOWLEDGE = {
    "cold": {
        "symptoms": ["cough", "sneezing", "runny nose", "sore throat", "congestion"],
        "remedies": [
            "Drink warm fluids like herbal tea",
            "Use a humidifier to keep air moist",
            "Take steam inhalation",
            "Gargle with salt water",
            "Rest well and stay hydrated"
        ]
    },
    "fever": {
        "symptoms": ["high temperature", "sweating", "chills", "headache", "weakness"],
        "remedies": [
            "Drink plenty of fluids like water and soups",
            "Place a cool, damp cloth on your forehead",
            "Take rest in a cool environment",
            "Eat light food and avoid spicy items"
        ]
    },
    "diabetes": {
        "symptoms": ["frequent urination", "excessive thirst", "hunger", "fatigue", "blurred vision"],
        "remedies": [
            "Consume fenugreek seeds soaked overnight",
            "Exercise regularly to manage blood sugar",
            "Avoid sugary and processed foods",
            "Eat high-fiber foods like leafy greens"
        ]
    },
    "headache": {
        "symptoms": ["pain in head", "nausea", "sensitivity to light", "tightness in scalp"],
        "remedies": [
            "Apply peppermint oil on the forehead",
            "Drink ginger tea",
            "Avoid bright lights and loud noises",
            "Practice deep breathing and relaxation"
        ]
    },
    "indigestion": {
        "symptoms": ["bloating", "heartburn", "nausea", "gas", "stomach discomfort"],
        "remedies": [
            "Drink warm water with lemon",
            "Chew fennel seeds after meals",
            "Avoid oily and spicy food",
            "Practice yoga or mild walking"
        ]
    },
    "sore throat": {
        "symptoms": ["pain in throat", "difficulty swallowing", "dry throat", "scratchy feeling"],
        "remedies": [
            "Gargle with warm salt water",
            "Drink turmeric milk at night",
            "Suck on honey or herbal lozenges",
            "Drink ginger tea or warm fluids"
        ]
    },
    "asthma": {
        "symptoms": ["shortness of breath", "wheezing", "chest tightness", "coughing"],
        "remedies": [
            "Steam inhalation with eucalyptus oil",
            "Avoid cold air and dust",
            "Practice breathing exercises like pranayama",
            "Consume honey with ginger juice"
        ]
    },
    "constipation": {
        "symptoms": ["difficulty passing stool", "infrequent bowel movements", "bloating"],
        "remedies": [
            "Drink warm water with lemon on an empty stomach",
            "Eat fiber-rich foods like bananas and oats",
            "Include flax seeds or isabgol in your diet",
            "Exercise regularly"
        ]
    },
    "acidity": {
        "symptoms": ["burning in chest", "acid reflux", "indigestion", "nausea"],
        "remedies": [
            "Drink cold milk or eat curd",
            "Chew basil leaves or fennel seeds",
            "Avoid oily and spicy food",
            "Take coconut water in the morning"
        ]
    },
    "cough": {
        "symptoms": ["dry cough", "wet cough", "throat irritation", "chest pain while coughing"],
        "remedies": [
            "Drink honey with warm water",
            "Use ginger-tulsi tea",
            "Steam inhalation with menthol",
            "Avoid cold food and drinks"
        ]
    }
}

def get_matching_disease(symptoms):
    best_match = None
    best_score = 0

    for disease, data in MEDICAL_KNOWLEDGE.items():
        match_score = sum(
            SequenceMatcher(None, s.lower(), known.lower()).ratio()
            for s in symptoms
            for known in data["symptoms"]
        )
        if match_score > best_score:
            best_score = match_score
            best_match = disease

    return best_match if best_score > 1.0 else None

def get_remedies(disease):
    return MEDICAL_KNOWLEDGE.get(disease, {}).get("remedies", ["No remedy available."])
