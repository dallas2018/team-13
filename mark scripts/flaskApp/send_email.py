import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("mark.drobnjak@gmail.com", "*******")

msg = "Thank you for your interest in SER Houston."
server.sendmail("mark.drobnjak@gmail.com", "drobnjak.crh@gmail.com", msg)
server.quit()