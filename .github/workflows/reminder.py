import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to_email, subject, message):
    # E-posta gönderme işlemleri için gerekli bilgiler
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'maviliadam1@gmail.com'
    smtp_password = 'xb5rmz7pg'

    # E-posta başlık ve içeriği
    email_from = smtp_username
    msg = MIMEMultipart()
    msg['From'] = email_from
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    # SMTP sunucusu ile bağlantı kurma
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    # E-posta gönderme
    server.sendmail(email_from, to_email, msg.as_string())

    # SMTP sunucusu ile bağlantıyı kapatma
    server.quit()

def main():
    while True:
        # 2 saatte bir hatırlatıcı e-posta gönder
        send_email('maviliadam1@gmail.com', 'Su İçme Hatırlatıcı', 'Su iç amcık')
        
        # 2 saat bekleme
        time.sleep(2 * 60 * 60)  # 2 saat = 2 * 60 dakika * 60 saniye

if __name__ == "__main__":
    main()
