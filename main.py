import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/myphoto.jpeg")

with col2:
    st.title("Mayank Kapoor")
    content = """
    I am Mayank, a passionate and driven tech enthusiast with a strong\
     foundation in Data Structures & Algorithms (DSA) and Object-Oriented\
      Programming (OOP). I have worked on front-end web-development and also\
       developed a basic library management tool using Python and MySQL. Ranked\
        5th in the city in PCM with 94.9%. My problem-solving skills and analytical\
         thinking reflect in my projects and achievements. Currently, I am\
          also exploring automation and app development, including a hostel room\
           cleaning appointment system and a secure login solution for college websites.\
            Beyond academics, I am part of an international team that builds RC planes\
             for global competitions, where I oversee aerodynamics and manufacturing. \
             This hands-on experience\
              complements my technical expertise and fuels my passion for engineering.
    """
    st.info(content)
st.info("Below are some of the pyhon projects I have build. Feel free to contact me!")
# Add link to contact me page

df = pd.read_csv("data.csv",sep=";")

col3, col4 = st.columns(2)

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
