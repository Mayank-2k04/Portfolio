import streamlit as st
import send_email

st.set_page_config("center")
st.header("Contact Us")
with st.form(key="email_form"):
    emailId = st.text_input("Your Email Address : ",key="eid",)
    mess = st.text_area("Enter Your Message : ", key="message")
    button = st.form_submit_button("Submit")
    if button:
        send_email.sendemail(mess,emailId)

