import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("mark.drobnjak@gmail.com", "*******")

msg = "YOUR MESSAGE!"
server.sendmail("mark.drobnjak@gmail.com", "drobnjak.crh@gmail.com", msg)
server.quit()