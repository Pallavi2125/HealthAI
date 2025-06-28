from flask import Flask, request, render_template_string
from medical_knowledge import get_matching_disease, get_remedies

app = Flask(_name_)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>HealthAI - Disease and Remedy Checker</title>
    <style>
        body { font-family: Arial; padding: 20px; background: #f4f4f4; }
        input, button { padding: 10px; margin-top: 10px; width: 100%; }
        .response { background: #fff; padding: 15px; margin-top: 20px; border-radius: 8px; }
    </style>
</head>
<body>
    <h2>🤖 HealthAI: Intelligent Disease and Remedy Advisor</h2>
    <form method="POST">
        <label>Enter symptoms (comma-separated):</label>
        <input name="symptoms" placeholder="e.g. headache, fever, nausea" />
        <button type="submit">Diagnose</button>
    </form>
    {% if prediction %}
        <div class="response">
            <h4>🦠 Predicted Disease: {{ prediction }}</h4>
            <h5>🌿 Suggested Home Remedies:</h5>
            <ul>
                {% for remedy in remedies %}
                    <li>{{ remedy }}</li>
                {% endfor %}
            </ul>
        </div>
    {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    remedies = []
    if request.method == "POST":
        symptoms_input = request.form["symptoms"]
        symptoms = [s.strip().lower() for s in symptoms_input.split(",")]
        prediction = get_matching_disease(symptoms)
        remedies = get_remedies(prediction) if prediction else ["Could not determine the disease."]
    return render_template_string(HTML_TEMPLATE, prediction=prediction, remedies=remedies)

if _name_ == "_main_":
    app.run(debug=True, host="0.0.0.0", port=5000)
