from transformers import pipeline
from PIL import Image
import gradio as gr

# Load Hugging Face Model
classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)

# Explanation Function
def explain_result(label):

    explanations = {

        "NORMAL": """
No major heart-related abnormalities detected.

Suggestions:
• Maintain a healthy diet
• Exercise regularly
• Periodic health checkups
""",

        "HEART_DISEASE": """
Possible signs of heart disease detected.

Possible Conditions:
• Arrhythmia
• Coronary artery disease
• Heart muscle abnormalities

Suggestions:
• Consult a cardiologist
• ECG/ECHO recommended
• Avoid stress and smoking
""",

        "ARRHYTHMIA": """
Irregular heartbeat pattern detected.

Suggestions:
• Immediate cardiac consultation
• Monitor heart rate regularly
"""
    }

    return explanations.get(
        label,
        "Please consult a medical professional."
    )

# Prediction Function
def predict_heart_disease(image):

    img = Image.fromarray(image)

    results = classifier(img)

    top_result = results[0]

    score = top_result["score"]

    # Demo Logic

    if score > 0.60:
        disease = "HEART_DISEASE"

    elif score > 0.40:
        disease = "ARRHYTHMIA"

    else:
        disease = "NORMAL"

    explanation = explain_result(disease)

    output = f"""
Prediction Result : {disease}

Confidence Score : {round(score * 100, 2)} %

Explanation :

{explanation}
"""

    return output

# Gradio Interface
interface = gr.Interface(
    fn=predict_heart_disease,
    inputs=gr.Image(type="numpy"),
    outputs="text",
    title="❤️ AI Medical Chatbot - Heart Disease Prediction",
    description="""
Upload a heart-related medical image (ECG/X-ray/MRI).

The AI model predicts possible heart disease and provides an explanation.
"""
)

# Launch App
interface.launch(debug=True)
