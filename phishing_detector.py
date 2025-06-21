
import streamlit as st
import joblib
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# Load models and vectorizer
rf_model = joblib.load('random_forest_model.pkl')
xgb_model = joblib.load('xgboost_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Set up aesthetic - straight up used chatgpt for this, how else is one to deal with HTML elements and colours?
st.set_page_config(page_title="Phishing Detector", layout="centered")
st.markdown("<h1 style='text-align: center; color: #0072B5;'>Phishing Email Detector</h1>", unsafe_allow_html=True)

# Sidebar
model_choice = st.sidebar.radio("Choose a model", ("Random Forest", "XGBoost"))

# Text input
user_input = st.text_area("Paste the email text here:")

if user_input:
    vectorized_input = vectorizer.transform([user_input])
    if model_choice == "Random Forest":
        prediction = rf_model.predict(vectorized_input)
    else:
        prediction = xgb_model.predict(vectorized_input)

    st.write("### Prediction:")
    st.success("Phishing Email" if prediction[0] == 1 else "Not a Phishing Email")

    # Wordcloud
    st.write("### Wordcloud of Your Email")
    wc = WordCloud(background_color='white', width=800, height=400).generate(user_input)
    fig, ax = plt.subplots()
    ax.imshow(wc, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
