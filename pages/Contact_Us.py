import streamlit as st
import send_email

st.set_page_config(page_title="Contact Us",layout="centered")
st.header("Contact Us")
with st.form(key="email_form"):
    emailId = st.text_input("Your Email Address : ",key="eid",)
    mess = st.text_area("Enter Your Message : ", key="message")
    button = st.form_submit_button("Submit")
    if button:
        if send_email.sendemail(mess,emailId):
            st.success("Your message was sent successfully!",icon="✅")
        else:
            st.error("We ran into an error! Try again later.",icon="🚨")