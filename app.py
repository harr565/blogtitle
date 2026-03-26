import streamlit as st
import random

st.title("📝 Blog Title Generator")
st.write("Generate creative blog titles instantly!")

# Inputs
topic = st.text_input("Enter your blog topic (e.g., AI, cooking, travel):")
style = st.selectbox("Choose a style:", ["Catchy", "Professional", "Fun", "Inspirational"])

# Title templates
templates = {
    "Catchy": [
        "10 Secrets About {topic} You Didn’t Know",
        "Why Everyone Is Talking About {topic}",
        "The Ultimate Guide to {topic}",
    ],
    "Professional": [
        "Understanding {topic}: A Complete Overview",
        "Best Practices in {topic}",
        "How {topic} Is Shaping the Future",
    ],
    "Fun": [
        "Adventures in {topic}: A Fun Journey",
        "Laugh, Learn, and Love {topic}",
        "Crazy Facts About {topic} You’ll Enjoy",
    ],
    "Inspirational": [
        "How {topic} Can Change Your Life",
        "The Power of {topic} in Everyday Living",
        "Dream Big: Achieving Through {topic}",
    ]
}

# Button
if st.button("Generate Title"):
    if topic:
        chosen_template = random.choice(templates[style])
        title = chosen_template.format(topic=topic)
        st.subheader("Your Blog Title:")
        st.write(title)
    else:
        st.warning("Please enter a topic.")
