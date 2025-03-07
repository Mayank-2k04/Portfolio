import streamlit as st
import pandas as pd

#run using -> streamlit run Home.py

st.set_page_config("Home",layout="wide")
col1, col2 = st.columns([0.8,1.2])

with col1:
    st.image("images/myphoto.jpeg", width=550)

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
             """
    st.info(content)
st.info("Below are some of the python projects built by me !!! Feel free to contact me.")
# Add link to contact me page

df = pd.read_csv("data.csv",sep=";")

col3, space, col4 = st.columns([1.5, 0.1, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{index+1}.png")
        url = row["url"]
        if url != "In progress":
            st.link_button(label="Source Code",url=url)
        else:
            st.link_button(label=url,url="")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(f"images/{index + 1}.png")
        url = row["url"]
        if url != "In progress":
            st.link_button(label="Source Code", url=url)
        else:
            st.link_button(label=url,url="")
