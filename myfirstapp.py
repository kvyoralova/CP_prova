import streamlit as st #'import _ as _' means that you're "assigning" a shorter "variable" to the library
st.header("Hello world") #the text function displays the text between quotes and brackets
title = st.text_input("Gimme a movie title:")
st.write("The current movie title is ", title)
