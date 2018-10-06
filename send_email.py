import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("gmail login", "Password")

msg = "Thank you for your interest in SER Houston."
server.sendmail("gmail login", "recipient email", msg)
server.quit()