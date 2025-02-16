import smtplib, ssl

host = "smtp.gmail.com"
port = 465
user = "pythonsendsmail8@gmail.com"
pa = "jnaz cbei djzn vzan"
sslcontext = ssl.create_default_context()
def sendemail(message,user_email):
    message = f"From: Mayank <{user}>\nTo: {user.split('@')[0]} <{user}>\nSubject: Message from {user_email}\nUser email: {user_email}\n{message}"
    try:
        with smtplib.SMTP_SSL(host, port, context=sslcontext) as server:
            server.login(user,pa)
            server.sendmail(user,user,message)
        print("Email sent")
    except Exception as e:
        print(e)

