import email
from bs4 import BeautifulSoup
filename = open("E:\\SpamDetection\\spam\\0001.bfc8d64d12b325ff385cca8d07b84288")
text = filename.read()
email_body = email.message_from_string(text)

if email_body.is_multipart():
    for payload in email_body.get_payload():
        # if payload.is_multipart(): ...
        text_without_html = BeautifulSoup(payload.get_payload()).get_text
        print(text_without_html)
else:
    text_without_html = BeautifulSoup(email_body.get_payload()).get_text()
    print(text_without_html)
   # print(email_body.get_payload())