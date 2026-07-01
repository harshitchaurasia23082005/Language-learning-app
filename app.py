import streamlit as st
from data import words 
#Title
st.title("Language Learning App")

#Sliderbar
st.sidebar.title("Language Learning App")
st.sidebar.write("Welcome")
st.sidebar.write("Practice English and Hindi vocabulary")

menu = st.sidebar.radio(
      "Menu",
      ["Home", "Flashcard", "Quiz", "About"]
)
#Language Selection
language = st.selectbox(
      "Choose Translation Direction",
      ["English - Hindi", "Hindi - English"]
)
#Search Box
search =  st.text_input("Search a word")

#About Page
if menu == "About":
      st.title("About Project")
      
      st.write("Language Learning App")
      
      st.write("Features:")

      st.write("Learn English and Hindi words")
      st.write("Flashcards")
      st.write("Quiz")
      st.write("Score")
      st.write("Progress Bar")
      st.write("Search")

      st.write("Made using Python and Streamlit")

      st.stop()
#Flashcards
st.header("Daily Flashcards")

for word in words:
      
      if search:
            if search.lower() not in word["english"].lower() and search not in word["hindi"]:
                  continue
            if language == "English - Hindi":
                  st.subheader(word["english"])
                  st.write("Hindi:", word["hindi"])
            else:
                  st.subheader(word["hindi"])
                  st.write("English:", word["english"])

                  st.write("Pronunciation:", word["pronunciation"])
                  st.markdown("_____")       
#Quiz
st.header("Quiz")


score = 0

for word in words:
    user_answer = st.text_input(
        f"What is the Hindi meaning of '{word['english']}'?",
        key=word["english"] 
    )
    if user_answer:
        if user_answer == word["answer"]:
                st.success("Correct")
                score += 1
        else:
                st.error(f"Wrong! Correct Answer:{word['answer']}")
#Score
                st.write("### Your Score:", score, "/", len(words))
#Progress Bar
progress = score / len(word)

st.write("### Learning Progress")
st.progress(progress)
st.write(f"{int(progress*100)}% Completed")