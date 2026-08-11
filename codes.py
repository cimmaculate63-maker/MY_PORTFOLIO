import streamlit as st
st.title("OTHELLO ASSIGNMENT 1ST PYTHON PROJECT ON  STREAMLIT, PORTFOLIO WEBSITE")
st.title("MY PORTFOLIO", text_alignment='center')
st.header("NAME:NWABUNWANNE-IMMACULATE", divider='blue', text_alignment='right')
st.header("Welcome to Nwabunwanne portfolio website!", text_alignment='left')
st.divider()
st.subheader("About me")
st.text("My name is Nwabunwanne-Immaculate I am an IT student in Othello academy I own a degree in computer science and I am an experienced student in tech fields.")
st.divider()
st.header("✌SKILLS")
st.markdown("""
- PYTHON
 - JAVA
- CSS 
- HTML
""")
st.header("MY PROJECT MADE SO FAR")
st.markdown("""
- School management system
- Portfolio
- Calculator 🧮
- Abacus
- Tic Tac Toe game
- Snake game
- Rock Paper Scissors game
- Guess the number game""")

st.divider()
st.header("LOCATION")
st.write("ABA LAGOS")

st.divider()
if st.button('CONTACT'):
    st.write ("GMAIL=@gmail.com.ng")
    st.write("PHONE-NUMBER=+234111783837")
  


