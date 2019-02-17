import email
import os
import dateutil.parser
import csv
import re

from bs4 import BeautifulSoup

def extract_date(text):
    e = email.parser.Parser().parsestr(text)
    #print(e['date'])
    return dateutil.parser.parse(e['date'])
def extract_from(text):
    e = email.parser.Parser().parsestr(text)
    return (e['from'])
def extract_to(text):
    e = email.parser.Parser().parsestr(text)
    return (e['to'])
def reply_to(text):
    e = email.parser.Parser().parsestr(text)
    return (e['reply-to'])
def extract_header(fname,flag):
    l1 = []
    filename = open(fname,encoding='Latin-1')
    text = filename.read()
    email_body = email.message_from_string(text)
    #print(email_body.is_multipart())

    #print(email_body)
    dt = extract_date(text)
    if flag:
        l1.append('Spam')
    else:
        l1.append('Ham')
    l1.append(dt.year)
    l1.append(dt.month)
    l1.append(dt.day)
    l1.append(dt.hour)
    l1.append(dt.minute)
    l1.append(dt.second)
    f = extract_from(text)
    #print(f)
    if f !=None:
        op = re.search(r'google',f)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'aol', f)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'gov', f)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'mil', f)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'yahoo', f)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'example', f)
        if op:
            #print(op)
            l1.append(1)
        else:
            l1.append(0)
    else:
        for j in range(0,6):
            l1.append(0)
    t = extract_to(text)
    #print(t)
    if t!=None:
        op = re.search(r'hotmail', t)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'aol', t)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'msn', t)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'localhost', t)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'yahoo', t)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'example', t)
        if op:
            # print(op)
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'google', t)
        if op:
            # print(op)
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'gov', t)
        if op:
            # print(op)
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'mil', t)
        if op:
            # print(op)
            l1.append(1)
        else:
            l1.append(0)
        tl = t.split('\n')
        count = 0
        for j in tl:
            tj = j.split(' ')
            count = count+len(tj)
        #print(count)
        l1.append(count)
    else:
        for j in range(0,10):
            l1.append(0)
    rt = reply_to(text)
    #print(rt)
    if rt!= None:
        op = re.search(r'google', rt)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'hotmail', rt)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'mil', rt)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'yahoo', rt)

        if op:

            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'aol', rt)
        if op:
            l1.append(1)
        else:
            l1.append(0)
        op = re.search(r'gov', rt)
        if op:
            # print(op)
            l1.append(1)
        else:
            l1.append(0)

    else:
        for j in range(0, 6):
            l1.append(0)

    e = email.parser.Parser().parsestr(text)
    if e['x-mailer']!=None:
        l1.append(e['x-mailer'])
    else:
        l1.append("")
    ct = e['content-type']
    if ct!=None:
        op = re.search(r'text',ct)
        if op :
            l1.append(1)
            l1.append(0)
            l1.append(0)
        else:
            l1.append(0)
            if re.search(r'multipart',ct):
                if re.search(r'mixed',ct):
                    l1.append(1)
                    l1.append(0)
                elif re.search(r'alternate',ct):
                    l1.append(0)
                    l1.append(1)
                else:
                    l1.append(0)
                    l1.append(0)
            else:
                l1.append(0)
                l1.append(0)
    else:
        for j in range(0,3):
            l1.append(0)

    with open("E:\\SpamDetection\\headerfeatures.csv", 'a') as csv_file:
        filewriter = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

        filewriter.writerow(l1)

    '''for i in e :
        print(i)'''
    '''if email_body.is_multipart():
        for payload in email_body.get_payload():
            # if payload.is_multipart(): ...
            text_without_html = BeautifulSoup(payload.get_payload()).get_text
            print(text_without_html)
    else:
        text_without_html = BeautifulSoup(email_body.get_payload()).get_text()
        print(text_without_html)
       # print(email_body.get_payload())'''


def maxRepeating(str):
    l = len(str)
    count = 0

    res = str[0]
    for i in range(l):

        cur_count = 1
        for j in range(i + 1, l):

            if (str[i] != str[j]):
                break
            cur_count += 1

        if cur_count > count:
            count = cur_count
            res = str[i]
    return count
def extract_subject(fname,flag):
    l1 = []
    filename = open(fname,encoding='Latin-1')
    text = filename.read()
    if flag:
        l1.append('Spam')
    else:
        l1.append('Ham')
    e = email.parser.Parser().parsestr(text)
    l1.append(len(e['subject']))
    print(e['Subject'])
    c = 0
    for i in e['subject'].split(' '):
        if re.search('([A-Z])', i):
            c = c+1
    l1.append(c)

    c = 0
    singledig = 0
    muldig = 0
    for i in e['subject'].split(' '):
        if i.isupper():
            c = c+1
        if re.match('^\d$', i):
            singledig = singledig+1
        if re.search(r'^\d{2,}$',i):
            muldig=muldig+1
    l1.append(c)
    l1.append(singledig)
    l1.append(muldig)
    singlelet = 0
    multilet = 0
    for i in e['subject'].split(' '):

        if re.match(r'(?i)^[a-z]$', i):
            singlelet= singlelet+1
        if re.search(r'(?i)^[a-z]+$',i):
            multilet=multilet+1
    l1.append(singlelet)
    l1.append(multilet)
    letandnum = 0
    for i in e['subject'].split(' '):
        if re.match(r'^(?=.*?[a-zA-Z]).*\d', i):
            letandnum =letandnum + 1
    l1.append(letandnum)
    singlechar = 0
    for i in e['subject'].split(' '):
        if re.match(r'^[^a-zA-Z0-9]$', i):
            singlechar =singlechar + 1
    l1.append(singlechar)


    l = len(re.findall(r'[a-z]', e['subject']))
    u = len(re.findall(r'[A-Z]', e['subject']))
    maxratio = 0
    if l!=0:
        maxratio = u/l
    l1.append(maxratio)


    l = len(e['subject'])
    u = len(re.findall(r'[A-Z]', e['subject']))
    ratio = 0
    if l != 0:
        ratio = u / l
    print(ratio)
    l1.append(ratio)
    print(maxratio)


    u = len(re.findall(r'[0-9]',e['subject']))
    digitratio = 0
    if l!=0:
        digitratio = u/l
    print(digitratio)
    l1.append(digitratio)


    u = len(re.findall(r'[^a-zA-Z0-9]', e['subject']))
    nonratio = 0
    if l != 0:
        nonratio = u / l
    print(nonratio)
    l1.append(nonratio)

    i = maxRepeating(e['subject'])
    print(i)
    l1.append(i)

    maxlen = 0
    for i in e['subject'].split():
        if(maxlen < len(i)):
            maxlen = len(i)
    print(maxlen)
    l1.append(maxlen)

    minchardiv = 9999
    for i in e['subject'].split():
        l = len(re.findall(r'[a-z]', i))
        u = len(re.findall(r'[A-Z]', i))
        d = len(re.findall(r'[0-9]', i))
        nc = len(re.findall(r'[^a-zA-Z0-9]', e['subject']))
        lgth = len(i)

        ratio = (l/lgth)+(u/lgth)+(d/lgth)+(nc/lgth)
        if minchardiv>ratio:
            minchardiv = ratio
    print(minchardiv)
    l1.append(minchardiv)

    with open("E:\\SpamDetection\\subjectfeatures.csv", 'a') as csv_file:
        filewriter = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

        filewriter.writerow(l1)

path = 'E:\\SpamDetection\\ham_train'
with open("E:\\SpamDetection\\headerfeatures.csv", 'w') as csv_file:
    filewriter = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

    filewriter.writerow(['Class','Year', 'Month', 'Day', 'Hour', 'Minute', 'Second','From Google?','From AOL?','From Gov?','From MIL?','From Yahoo','From example?','To hotmail?','To aol?','To MSN?','To localhost?','To yahoo?','To example?','To google?','To gov?','To mil?','Count of TO Mails','Reply to Google','Reply to Hotmail','Reply to MIL','Reply to Yahoo','Reply to AOL','Reply to Gov','X-Mailman Server','Is Text?','Is Multipart/Mixed?','Is Multipart/Alternative?'])
i = 0
for filename in os.listdir(path):
    i = i+1
    print(i)
    extract_header(path+"\\"+filename,0)

path = 'E:\\SpamDetection\\spam_train'
i = 0
for filename in os.listdir(path):
    i = i+1
    print(i)
    extract_header(path+"\\"+filename,1)


path = 'E:\\SpamDetection\\ham_train'
with open("E:\\SpamDetection\\subjectfeatures.csv", 'w') as csv_file:
    filewriter = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

    filewriter.writerow(['Class','no of chars','No of capitalised words','No of words with all caps','Single digits','more than one Digits','single letters','only letters','letters and numbers','single chars','Ratio to upper to lower chars','Ratio of upper to all chars','Ratio of Digits to all chars','Ration of non alphanumeric to all chars','Count of max repeating char','max of character lengths','minimum char diversity'])
i = 0
for filename in os.listdir(path):
    i = i+1
    print(i)
    extract_subject(path+"\\"+filename,0)

path = 'E:\\SpamDetection\\spam_train'
i = 0
for filename in os.listdir(path):
    i = i+1
    print(i)
    extract_subject(path+"\\"+filename,1)