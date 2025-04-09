import streamlit as st  


st.title("🚀 `Growth Mindset Challenge`")
st.write("Welcome to the Growth Mindset Challenge! Develop your skills through challenges and reflection.")


if "journal_entries" not in st.session_state:
    st.session_state.journal_entries = [] 


st.header("📌 Daily Growth Challenge")
challenge_options = [
    "Try something new today!",
    "Learn from a past mistake.",
    "Help someone without expecting anything in return.",
    "Write down three things you are grateful for."
]
selected_challenge = st.selectbox("Choose today's challenge:", challenge_options)
st.success(f"Your challenge for today: {selected_challenge}")


st.header("📊 Progress Tracker")
progress = st.slider("How much progress have you made today?", 0, 100, 50)
st.progress(progress / 100)


st.header("💡 Daily Motivation")
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "The only way to do great work is to love what you do.",
    "Believe in yourself and all that you are. Know that there is something inside you greater than any obstacle."
]
st.write(f"**Quote of the day:** *{quotes[progress % len(quotes)]}*")


st.header("🧠 Growth Mindset Quiz")
question = "What should you do when you make a mistake?"
options = ["Give up", "Learn from it", "Blame others"]
answer = st.radio(question, options)

if st.button("Submit Answer"):
    if answer == "Learn from it":
        st.success("✅ Correct! A growth mindset means learning from mistakes.")
    else:
        st.error("❌ Try again! Growth mindset encourages learning from mistakes.")


st.header("📖 Your Growth Journal")
user_entry = st.text_area("Write about today's experience and learning:")

if st.button("Save Entry"):
    if user_entry.strip(): 
        entry = f"📌 **Challenge:** {selected_challenge}\n🔹 **Progress:** {progress}%\n📝 **Journal:** {user_entry}"
        st.session_state.journal_entries.append(entry)  
        st.success("📝 Entry saved successfully! Keep journaling.")


if st.session_state.journal_entries:
    st.header("📜 Your Previous Journal Entries")
    for idx, entry in enumerate(reversed(st.session_state.journal_entries)):  
        with st.expander(f"Entry {len(st.session_state.journal_entries) - idx}"):
            st.markdown(entry) 

# FOOTER
st.markdown("---")
st.write("🚀 Keep growing, keep learning!")