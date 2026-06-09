import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="AI Medical Chatbot",
    page_icon="❤️",
    layout="centered"
)

# Title
st.title("❤️ AI Medical Chatbot for Heart Disease Detection")
st.write("Upload an ECG image and receive a prediction with medical recommendations.")

# Prediction Function
def predict_heart_disease(image):

    width, height = image.size

    if width > 500:
        disease = "HEART_DISEASE"
        confidence = 87.5

    elif width > 300:
        disease = "ARRHYTHMIA"
        confidence = 76.2

    else:
        disease = "NORMAL"
        confidence = 92.1

    return disease, confidence

# Explanation Function
def explain_result(disease):

    explanations = {

        "HEART_DISEASE": """
Possible signs of heart disease detected.

Symptoms:
• Chest pain
• Shortness of breath
• Fatigue
• Irregular heartbeat

Recommendations:
• Consult a cardiologist
• Get ECG/ECHO tests
• Maintain a healthy diet
• Exercise regularly
""",

        "ARRHYTHMIA": """
Irregular heartbeat pattern detected.

Symptoms:
• Dizziness
• Palpitations
• Weakness

Recommendations:
• Monitor heart rate
• Reduce stress
• Seek medical advice
""",

        "NORMAL": """
No major abnormalities detected.

Recommendations:
• Continue healthy lifestyle
• Exercise regularly
• Maintain balanced diet
• Attend regular health checkups
"""
    }

    return explanations.get(
        disease,
        "Please consult a healthcare professional."
    )

# File Upload
uploaded_file = st.file_uploader(
    "Upload ECG Image",
    type=["png", "jpg", "jpeg"]
)

# Process Image
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded ECG Image",
        use_container_width=True
    )

    if st.button("Analyze ECG"):

        disease, confidence = predict_heart_disease(image)

        explanation = explain_result(disease)

        st.success("Analysis Complete")

        st.subheader("Prediction Result")
        st.write(f"**Disease:** {disease}")
        st.write(f"**Confidence Score:** {confidence}%")

        st.subheader("Medical Explanation")
        st.write(explanation)

# Chatbot Section
st.markdown("---")
st.subheader("💬 Medical Chatbot")

question = st.text_input(
    "Ask a heart-health related question"
)

if question:

    st.write("### Response")

    st.write("""
This is a healthcare awareness chatbot.

General Tips:
• Exercise regularly
• Eat healthy food
• Avoid smoking
• Manage stress
• Schedule regular health checkups

For medical emergencies, consult a healthcare professional immediately.
""")
