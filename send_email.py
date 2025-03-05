import smtplib, ssl
import streamlit as st
host = "smtp.gmail.com"
port = 465
user = "pythonsendsmail8@gmail.com"
pa = st.secrets("PYTHONEMAILPASS")  #environmental variable
sslcontext = ssl.create_default_context()
def sendemail(message,user_email):
    message = f"From: Mayank <{user}>\nTo: {user.split('@')[0]} <{user}>\nSubject: Message from {user_email}\nUser email: {user_email}\n{message}"
    try:
        with smtplib.SMTP_SSL(host, port, context=sslcontext) as server:
            server.login(user,pa)
            server.sendmail(user,user,message)
        return True
    except Exception:
        return False

