# import streamlit as st
# import requests

# st.title("🤖 AI Virtual Career Counsellor")

# if "messages" not in st.session_state:
#     st.session_state.messages = []

# for msg in st.session_state.messages:
#     with st.chat_message(msg["role"]):
#         st.markdown(msg["content"])

# prompt = st.chat_input("Tell me about your interests...")

# if prompt:
#     st.session_state.messages.append({"role": "user", "content": prompt})

#     response = requests.post(
#     "http://localhost:5005/webhooks/rest/webhook",
#     json={"sender": "user", "message": prompt}
# )

#     rasa_response = response.json()

#     if rasa_response:
#         bot_reply = rasa_response[0].get("text", "No response text found.")
#     else:
#         bot_reply = "🤖 I couldn't understand that. Try rephrasing."

#     st.session_state.messages.append({"role": "assistant", "content": bot_reply})

#     st.rerun()


import streamlit as st
import joblib
import time
import os

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="AI Career Counsellor",
    page_icon="D:/DS Projects/AI-Virtual-Career-Counsellor/img.png",
    layout="centered"
)

# ---------------------- LOAD MODEL SAFELY ----------------------
MODEL_PATH = "career_model.pkl"

if not os.path.exists(MODEL_PATH):
    st.error("❌ Model file not found. Please train and save the model first.")
    st.stop()

model = joblib.load(MODEL_PATH)

# ---------------------- CUSTOM STYLING ----------------------
st.markdown("""
    <style>
        .stChatMessage {
            border-radius: 15px;
            padding: 10px;
        }
        .block-container {
            padding-top: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Virtual Career Counsellor 🤖")
st.markdown("Welcome to your personalized career guidance assistant!")
# st.caption("Tell me your interests and I’ll suggest the best career paths for you.")

# ---------------------- SESSION STATE INIT ----------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------------- SIDEBAR ----------------------
st.sidebar.header("💡 Try Example Prompts")

examples = [
    "I like acting in plays",
    "I enjoy data mining",
    "I am interested in trading",
    "I like automation tools",
    "I like music production",
    "I am good at statistics and math",
    "I like entrepreneurship",
    "I enjoy building APIs"
]

for ex in examples:
    st.sidebar.write(f"• {ex}")

if st.sidebar.button("🗑 Clear Chat"):
    st.session_state.messages = []
    st.rerun()

# ---------------------- CAREER EXPLANATIONS ----------------------
career_explanations = {
    "tech": "Your interests align with programming, AI, and technology-driven careers.",
    "arts": "Your creativity and artistic skills suggest a career in creative industries.",
    "commerce": "Your business and finance interests indicate strong commercial aptitude.",
    "data": "Your analytical and mathematical strengths align with data-driven careers."
}

# ---------------------- DISPLAY CHAT HISTORY ----------------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------------- USER INPUT ----------------------
prompt = st.chat_input("Tell me about your interests...")

if prompt:
    # Save user message
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("user"):
        st.markdown(prompt)

    # ---------------------- PREDICTION ----------------------
    try:
        # If model supports probabilities
        if hasattr(model, "predict_proba"):
            probs = model.predict_proba([prompt])[0]
            top_indices = probs.argsort()[-3:][::-1]
            labels = model.classes_

            top_careers = [(labels[i], probs[i] * 100) for i in top_indices]

            response = "### 🎯 Top Career Recommendations:\n\n"

            for career, confidence in top_careers:
                explanation = career_explanations.get(career.lower(), "")
                response += f"""
                ###{career.capitalize()}

                **Confidence:** `{confidence:.2f}%`

                {explanation}

                ---
                """
        else:
            # For models like LinearSVC (no predict_proba)
            prediction = model.predict([prompt])[0]
            explanation = career_explanations.get(prediction.lower(), "")

            response = f"""
            Recommended Career: **{prediction.capitalize()}**

            {explanation}
            """

    except Exception as e:
        response = "⚠️ Something went wrong with prediction. Please check your trained model."

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": response})

    # ---------------------- TYPING EFFECT ----------------------
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        for i in range(len(response)):
            full_response += response[i]
            time.sleep(0.005)
            message_placeholder.markdown(full_response)

        # for chunk in response.split():
        #     full_response += chunk + " "
        #     time.sleep(0.02)
        #     message_placeholder.markdown(full_response)