from src.mail.init_mail import mail
from flask_mail import Message

def send_mail():
    msg = Message("Hello", sender="sneakypotato.hello@gmail.com", recipients=["ashwanikamal.im421@gmail.com"])
    mail.send(msg)