import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("SERjobs@gmail.com", "*******")

msg = "Thank you for your interest in SER Houston. We look forward to following up with you!"
server.sendmail("SERjobs@gmail.com", "recipient email", msg)
server.quit()