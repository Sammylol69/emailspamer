import fade
import smtplib
import ssl
import certifi

def email():
  em = "▓█████  ███▄ ▄███▓ ▄▄▄       ██▓ ██▓    \n▓█   ▀ ▓██▒▀█▀ ██▒▒████▄    ▓██▒▓██▒    \n▒███   ▓██    ▓██░▒██  ▀█▄  ▒██▒▒██░    \n▒▓█  ▄ ▒██    ▒██ ░██▄▄▄▄██ ░██░▒██░    \n░▒████▒▒██▒   ░██▒ ▓█   ▓██▒░██░░██████▒\n░░ ▒░ ░░ ▒░   ░  ░ ▒▒   ▓▒█░░▓  ░ ▒░▓  ░\n ░ ░  ░░  ░      ░  ▒   ▒▒ ░ ▒ ░░ ░ ▒  ░\n   ░  ░       ░         ░  ░ ░      ░  ░"
  faded_text = fade.pinkred(em)
  print(faded_text)


print("\033c")
email()

sender_email = "s36735992@gmail.com"
receiver_email = str(input("Enter a email: "))
password = "lftf omcu heuv rqyc"

smtp_address = "smtp.gmail.com"
smtp_port = 465

subject = str(input("Email subject: "))
body = str(input("Email body: "))

message = f"Subject: {subject}\n\n{body}"

context = ssl.create_default_context()

context.load_verify_locations(certifi.where())

with smtplib.SMTP_SSL(smtp_address, smtp_port, context=context) as server:
    server.login(sender_email, password)
    for x in range(int(input("How much emails: "))):
     server.sendmail(sender_email, receiver_email, message)
     print("Email sent successfully.")