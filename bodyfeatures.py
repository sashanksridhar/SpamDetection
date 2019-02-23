import csv
import os
import email
import re
from bs4 import BeautifulSoup
import nltk

from nltk.tokenize import sent_tokenize
#stop = set(stopwords.words('english'))
stop =["a", "about", "above", "after", "again", "against", "ain", "all", "am", "an", "and", "any", "are", "aren", "aren't", "as", "at", "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "couldn", "couldn't", "d", "did", "didn", "didn't", "do", "does", "doesn", "doesn't", "doing", "don", "don't", "down", "during", "each", "few", "for", "from", "further", "had", "hadn", "hadn't", "has", "hasn", "hasn't", "have", "haven", "haven't", "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "i", "if", "in", "into", "is", "isn", "isn't", "it", "it's", "its", "itself", "just", "ll", "m", "ma", "me", "mightn", "mightn't", "more", "most", "mustn", "mustn't", "my", "myself", "needn", "needn't", "no", "nor", "not", "now", "o", "of", "off", "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "re", "s", "same", "shan", "shan't", "she", "she's", "should", "should've", "shouldn", "shouldn't", "so", "some", "such", "t", "than", "that", "that'll", "the", "their", "theirs", "them", "themselves", "then", "there", "these", "they", "this", "those", "through", "to", "too", "under", "until", "up", "ve", "very", "was", "wasn", "wasn't", "we", "were", "weren", "weren't", "what", "when", "where", "which", "while", "who", "whom", "why", "will", "with", "won", "won't", "wouldn", "wouldn't", "y", "you", "you'd", "you'll", "you're", "you've", "your", "yours", "yourself", "yourselves", "could", "he'd", "he'll", "he's", "here's", "how's", "i'd", "i'll", "i'm", "i've", "let's", "ought", "she'd", "she'll", "that's", "there's", "they'd", "they'll", "they're", "they've", "we'd", "we'll", "we're", "we've", "what's", "when's", "where's", "who's", "why's", "would",'~','@','#','%','&','.', ',', '"', "'", '?', '!', ':', ';', '(', ')', '[', ']', '{', '}','/','^','<','>','\\','!','=','-']


def count_spam(text):
    c = 0
   # print(type(text))
    #print(text)
    spamwordfile = open('SpamWords.txt')
    ignorewords = spamwordfile.read()
    ignorewordsList = ignorewords.split('\n')

    spamwordfile.close()
    for i in ignorewordsList:
        if i in text:
            c = c+1
    return c

def function_words_count(text):
    c = 0
    functionwordfile = open('FunctionWords.txt')
    functionwords = functionwordfile.read()
    functionwordlist = functionwords.split('\n')
    functionwordfile.close()
    for i in text.split('\n'):
        for j in i.split(' '):
            if j in functionwordlist:
                c = c+1
    return c

def find_anchor(page):

    return len(page.find_all('a'))

def all_html(page):
    return len(page.find_all())

def imgcount(page):
    return len(page.find_all('img'))

def alphanumericcount(text):
    count = 0
    for i in text:
        if i.isalnum():
            count=count+1
    return count

def countduplicates(text):
    if text==[]:
        return 0
    count = dict()
    #words = text.split()

    for word in text:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    sum = 0
    for i in count.keys():
        if count[i]!=1:
            sum = sum+count[i]
    return sum

def minwordlt(text):
    if text==[]:
        return 0
    mins = min(len(word) for word in text)
    return mins

def countlower(text):
    count = 0
    if text==[]:
        return 0
    for i in range(0,len(text)):
        if text[i].islower():
            count = count+1
    return count

def countlines(text):
    return len(text.split('\n'))

def maxRepeating(str):
    l = len(str)
    count = 0


    for i in range(l):

        cur_count = 1
        for j in range(i + 1, l):

            if (str[i] != str[j]):
                break
            cur_count += 1

        if cur_count > count:
            count = cur_count

    return count
def extract_body(fname,flag):
    l1 = []
    filename = open(fname, encoding='Latin-1')
    text = filename.read()
    if flag:
        l1.append(flag)
    else:
        l1.append(flag)
    email_body = email.message_from_string(text)


    countofspam = 0
    countoffunctionwords = 0
    countofanchors=0
    count_tags = 0
    count_image = 0
    count_alphanumeric = 0
    count_duplicate = 0
    minwordlength = 0
    count_lower = 0
    count_allcaps = 0
    count_lines =0
    count_digit = 0
    count_space = 0
    count_caps = 0
    count_chars = 0
    count_tabs = 0
    count_special = 0
    count_alpha = 0
    count_words = 0
    count_word_greaterthan6 =0
    count_word_lesserthan3 = 0
    count_quote = 0
    count_semicolon = 0
    count_comma = 0
    count_period = 0
    count_question = 0
    count_exclamation = 0
    count_multiplequestion = 0
    count_colon = 0
    count_ellipse = 0
    count_multipleexclamation = 0
    count_sentences = 0
    count_paras = 0
    count_uppersentence = 0
    count_lowersentence = 0
    count_dollar = 0
    count_capswords = 0
    count_allcapswords=0
    count_digitwords = 0
    singlelet = 0
    multilet = 0
    singledig = 0
    singlechar = 0
    maxratio = 0
    ratio = 0
    digitratio = 0
    nonratio = 0
    maxrepeating = 0
    maxlen = -1
    minchardiv=9999
    if email_body.is_multipart():
        for payload in email_body.get_payload():
            l = payload.get_payload()
            m = []
            if type(l) == type(m):
                for j in l:
                    if type(j)!=type(""):
                        continue
                    text_without_html = BeautifulSoup(j.get_payload(),features="html.parser").get_text()
                    #print(text_without_html)
                    countofspam+=count_spam(text_without_html)
                    countoffunctionwords+=function_words_count(text_without_html)
                    countofanchors+=find_anchor(BeautifulSoup(j.get_payload(),features='html.parser'))
                    count_tags+=all_html(BeautifulSoup(j.get_payload(),features="html.parser"))
                    count_image += imgcount(BeautifulSoup(j.get_payload(), features="html.parser"))
                    count_alphanumeric+=alphanumericcount(text_without_html)
                    count_lower += countlower(text_without_html)
                    count_lines += countlines(text_without_html)
                    count_chars += len(text_without_html)
                    if bool(re.search(r'[A-Z]+', text_without_html)):
                        count_allcaps += max(len(i) for i in re.findall(r'[A-Z]+', text_without_html))
                    for i in text_without_html.split():
                        if i.isupper():
                            count_allcapswords += 1
                        if i[0].isupper():
                            count_capswords += 1
                        if i.isdigit():
                            count_digitwords+=1
                        if re.match(r'(?i)^[A-Za-z]$', i):
                            singlelet = singlelet + 1
                        if re.search(r'(?i)^[A-Za-z]+$', i):
                            multilet = multilet + 1
                        if re.match(r'(?i)^[0-9]$', i):
                            singledig+= 1
                        if re.match(r'(?i)^[^a-zA-Z0-9]$', i):
                            singlechar+= 1
                    l = len(re.findall(r'[a-z]', text_without_html))
                    u = len(re.findall(r'[A-Z]', text_without_html))

                    if l != 0:
                        maxratio += u / l
                    l = len(text_without_html)
                    u = len(re.findall(r'[A-Z]', text_without_html))

                    if l != 0:
                        ratio += u / l
                    u = len(re.findall(r'[0-9]', text_without_html))

                    if l != 0:
                        digitratio += u / l
                    u = len(re.findall(r'[^a-zA-Z0-9]', text_without_html))

                    if l != 0:
                        nonratio += u / l

                    maxrepeating = maxRepeating(text_without_html)

                    for i in text_without_html.split():
                        if (maxlen < len(i)):
                            maxlen = len(i)
                    for i in text_without_html.split():
                        l = len(re.findall(r'[a-z]', i))
                        u = len(re.findall(r'[A-Z]', i))
                        d = len(re.findall(r'[0-9]', i))
                        nc = len(re.findall(r'[^a-zA-Z0-9]', text_without_html))
                        lgth = len(i)

                        ratio = (l / lgth) + (u / lgth) + (d / lgth) + (nc / lgth)
                        if minchardiv > ratio:
                            minchardiv = ratio

                    if bool(re.search(r'[A-Z]', text_without_html)):
                        count_caps += len(re.findall(r'[A-Z]', text_without_html))
                    if bool(re.search(r'[a-zA-Z]', text_without_html)):
                        count_alpha += len(re.findall(r'[a-zA-Z]', text_without_html))
                    if bool(re.search(r'[0-9]', text_without_html)):
                        count_digit += len(re.findall(r'[0-9]', text_without_html))
                    if bool(re.search(r'[ ]', text_without_html)):
                        count_space += len(re.findall(r'[ ]', text_without_html))
                    if bool(re.search(r'[\t]', text_without_html)):
                        count_tabs += len(re.findall(r'[\t]', text_without_html))
                    if bool(re.search(r'[\']', text_without_html)):
                        count_quote += len(re.findall(r'[\']', text_without_html))
                    if bool(re.search(r'[,]', text_without_html)):
                        count_comma += len(re.findall(r'[,]', text_without_html))
                    if bool(re.search(r'[.]', text_without_html)):
                        count_period += len(re.findall(r'[.]', text_without_html))
                    if bool(re.search(r'[;]', text_without_html)):
                        count_semicolon += len(re.findall(r'[;]', text_without_html))
                    if bool(re.search(r'[?]', text_without_html)):
                        count_question += len(re.findall(r'[?]', text_without_html))
                    if bool(re.search(r'[?]{2,}', text_without_html)):
                        count_multiplequestion += len(re.findall(r'[?]{2,}', text_without_html))
                    if bool(re.search(r'[!]', text_without_html)):
                        count_exclamation += len(re.findall(r'[!]', text_without_html))
                    if bool(re.search(r'[!]{2,}', text_without_html)):
                        count_multipleexclamation += len(re.findall(r'[!]{2,}', text_without_html))
                    if bool(re.search(r'[:]', text_without_html)):
                        count_colon += len(re.findall(r'[:]', text_without_html))
                    if bool(re.search(r'[()]', text_without_html)):
                        count_ellipse += len(re.findall(r'[()]', text_without_html))

                    if bool(re.search(r'[^a-zA-Z0-9 \t]', text_without_html)):
                        count_special += len(re.findall(r'[^a-zA-Z0-9 \t]', text_without_html))
                    if bool(re.search(r'[\n]{2,}', text_without_html)):
                        count_paras += len(re.findall(r'[\n]{2,}', text_without_html))
                    count_words += len(text_without_html.split())

                    for i in text_without_html.split():
                        if len(i)>=6:
                            count_word_greaterthan6+=1
                        if len(i)<=3:
                            count_word_lesserthan3+=1

                    l=[i for i in text_without_html.lower().split() if i not in stop and not i.isdigit()]
                    final = [k for k in l if not bool(re.search(r'^[^a-zA-Z]+$', k)) and not bool(re.search(r'^[a-zA-Z]$', k))]

                    count_duplicate+=countduplicates(final)
                    minwordlength=minwordlt(final)
                    count_sentences += len(sent_tokenize(text_without_html))
                    for i in sent_tokenize(text_without_html):
                        if i[0].isupper():
                            count_uppersentence+=1
                        elif i[0].islower():
                            count_lowersentence+=1
                    if bool(re.search(r'[$]', text_without_html)):
                        count_dollar += len(re.findall(r'[$]', text_without_html))




            else:
                text_without_html =  BeautifulSoup(payload.get_payload(),features="html.parser").get_text()
                #print(text_without_html)
                countofspam += count_spam(text_without_html)
                count_chars += len(text_without_html)
                countoffunctionwords += function_words_count(text_without_html)
                countofanchors += find_anchor(BeautifulSoup(payload.get_payload(), features='html.parser'))
                count_tags += all_html(BeautifulSoup(payload.get_payload(), features="html.parser"))
                count_image += imgcount(BeautifulSoup(payload.get_payload(), features="html.parser"))
                count_alphanumeric += alphanumericcount(text_without_html)
                count_lower += countlower(text_without_html)
                count_lines += countlines(text_without_html)
                if bool(re.search(r'[A-Z]+', text_without_html)):
                    count_allcaps += max(len(i) for i in re.findall(r'[A-Z]+', text_without_html))
                for i in text_without_html.split():
                    if i.isupper():
                        count_allcapswords += 1
                    if i[0].isupper():
                        count_capswords += 1
                    if i.isdigit():
                        count_digitwords += 1
                    if re.match(r'(?i)^[A-Za-z]$', i):
                        singlelet = singlelet + 1
                    if re.search(r'(?i)^[A-Za-z]+$', i):
                        multilet = multilet + 1
                    if re.match(r'(?i)^[0-9]$', i):
                        singledig += 1
                    if re.match(r'(?i)^[^a-zA-Z0-9]$', i):
                        singlechar += 1
                if bool(re.search(r'[A-Z]', text_without_html)):
                    count_caps += len(re.findall(r'[A-Z]', text_without_html))
                if bool(re.search(r'[a-zA-Z]', text_without_html)):
                    count_alpha += len(re.findall(r'[a-zA-Z]', text_without_html))
                if bool(re.search(r'[0-9]', text_without_html)):
                    count_digit += len(re.findall(r'[0-9]', text_without_html))
                if bool(re.search(r'[ ]', text_without_html)):
                    count_space += len(re.findall(r'[ ]', text_without_html))
                if bool(re.search(r'[\t]', text_without_html)):
                    count_tabs += len(re.findall(r'[\t]', text_without_html))
                if bool(re.search(r'[\']', text_without_html)):
                    count_quote += len(re.findall(r'[\']', text_without_html))
                if bool(re.search(r'[,]', text_without_html)):
                    count_comma += len(re.findall(r'[,]', text_without_html))
                if bool(re.search(r'[.]', text_without_html)):
                    count_period += len(re.findall(r'[.]', text_without_html))
                if bool(re.search(r'[;]', text_without_html)):
                    count_semicolon += len(re.findall(r'[;]', text_without_html))
                if bool(re.search(r'[?]', text_without_html)):
                    count_question += len(re.findall(r'[?]', text_without_html))
                if bool(re.search(r'[?]{2,}', text_without_html)):
                    count_multiplequestion += len(re.findall(r'[?]{2,}', text_without_html))
                if bool(re.search(r'[!]', text_without_html)):
                    count_exclamation += len(re.findall(r'[!]', text_without_html))
                if bool(re.search(r'[!]{2,}', text_without_html)):
                    count_multipleexclamation += len(re.findall(r'[!]{2,}', text_without_html))
                if bool(re.search(r'[:]', text_without_html)):
                    count_colon += len(re.findall(r'[:]', text_without_html))
                if bool(re.search(r'[()]', text_without_html)):
                    count_ellipse += len(re.findall(r'[()]', text_without_html))
                if bool(re.search(r'[^a-zA-Z0-9 \t]', text_without_html)):
                    count_special += len(re.findall(r'[^a-zA-Z0-9 \t]', text_without_html))
                if bool(re.search(r'[\n]{2,}', text_without_html)):
                    count_paras += len(re.findall(r'[\n]{2,}', text_without_html))
                count_words += len(text_without_html.split())
                for i in text_without_html.split():
                    if len(i) >= 6:
                        count_word_greaterthan6 += 1
                    if len(i) <= 3:
                        count_word_lesserthan3 += 1

                l = [i for i in text_without_html.lower().split() if i not in stop and not i.isdigit()]
                final = [k for k in l if not bool(re.search(r'^[^a-zA-Z]+$', k)) and not bool(re.search(r'^[a-zA-Z]$', k))]

                count_duplicate += countduplicates(final)

                minwordlength = minwordlt(final)
                count_sentences += len(sent_tokenize(text_without_html))
                for i in sent_tokenize(text_without_html):
                    if i[0].isupper():
                        count_uppersentence += 1
                    elif i[0].islower():
                        count_lowersentence += 1
                if bool(re.search(r'[$]', text_without_html)):
                    count_dollar += len(re.findall(r'[$]', text_without_html))
                l = len(re.findall(r'[a-z]', text_without_html))
                u = len(re.findall(r'[A-Z]', text_without_html))

                if l != 0:
                    maxratio += u / l
                l = len(text_without_html)
                u = len(re.findall(r'[A-Z]', text_without_html))

                if l != 0:
                    ratio += u / l
                u = len(re.findall(r'[0-9]',text_without_html))

                if l != 0:
                    digitratio += u / l
                u = len(re.findall(r'[^a-zA-Z0-9]', text_without_html))

                if l != 0:
                    nonratio += u / l
                if l != 0:
                    nonratio += u / l
                maxrepeating = maxRepeating(text_without_html)

                for i in text_without_html.split():
                    if (maxlen < len(i)):
                        maxlen = len(i)
                for i in text_without_html.split():
                    l = len(re.findall(r'[a-z]', i))
                    u = len(re.findall(r'[A-Z]', i))
                    d = len(re.findall(r'[0-9]', i))
                    nc = len(re.findall(r'[^a-zA-Z0-9]', text_without_html))
                    lgth = len(i)

                    ratio = (l / lgth) + (u / lgth) + (d / lgth) + (nc / lgth)
                    if minchardiv > ratio:
                        minchardiv = ratio




    else:
        text_without_html = BeautifulSoup(email_body.get_payload(),features="html.parser").get_text()
        #print(text_without_html)
        countofspam += count_spam(text_without_html)
        count_chars += len(text_without_html)
        countoffunctionwords += function_words_count(text_without_html)
        countofanchors += find_anchor(BeautifulSoup(email_body.get_payload(), features='html.parser'))
        count_tags += all_html(BeautifulSoup(email_body.get_payload(), features="html.parser"))
        count_image += imgcount(BeautifulSoup(email_body.get_payload(), features="html.parser"))
        count_alphanumeric += alphanumericcount(text_without_html)
        count_lower += countlower(text_without_html)
        count_lines += countlines(text_without_html)
        if bool(re.search(r'[A-Z]+', text_without_html)):
            count_allcaps += max(len(i) for i in re.findall(r'[A-Z]+', text_without_html))
        for i in text_without_html.split():
            if i.isupper():
                count_allcapswords+=1
            if i[0].isupper():
                count_capswords+=1
            if i.isdigit():
                count_digitwords += 1
            if re.match(r'(?i)^[A-Za-z]$', i):
                singlelet = singlelet + 1
            if re.search(r'(?i)^[A-Za-z]+$', i):
                multilet = multilet + 1
            if re.match(r'(?i)^[0-9]$', i):
                singledig += 1
            if re.match(r'(?i)^[^a-zA-Z0-9]$', i):
                singlechar += 1
        if bool(re.search(r'[A-Z]', text_without_html)):
            count_caps += len(re.findall(r'[A-Z]', text_without_html))
        if bool(re.search(r'[a-zA-Z]', text_without_html)):
            count_alpha += len(re.findall(r'[a-zA-Z]', text_without_html))
        if bool(re.search(r'[0-9]', text_without_html)):
            count_digit += len(re.findall(r'[0-9]', text_without_html))
        if bool(re.search(r'[ ]', text_without_html)):
            count_space += len(re.findall(r'[ ]', text_without_html))
        if bool(re.search(r'[\t]', text_without_html)):
            count_tabs += len(re.findall(r'[\t]', text_without_html))
        if bool(re.search(r'[\n]{2,}', text_without_html)):
            count_paras += len(re.findall(r'[\n]{2,}', text_without_html))
        if bool(re.search(r'[\']', text_without_html)):
            count_quote += len(re.findall(r'[\']', text_without_html))
        if bool(re.search(r'[,]', text_without_html)):
            count_comma += len(re.findall(r'[,]', text_without_html))
        if bool(re.search(r'[.]', text_without_html)):
            count_period += len(re.findall(r'[.]', text_without_html))
        if bool(re.search(r'[;]', text_without_html)):
            count_semicolon += len(re.findall(r'[;]', text_without_html))
        if bool(re.search(r'[?]', text_without_html)):
            count_question += len(re.findall(r'[?]', text_without_html))
        if bool(re.search(r'[?]{2,}', text_without_html)):
            count_multiplequestion += len(re.findall(r'[?]{2,}', text_without_html))
        if bool(re.search(r'[!]', text_without_html)):
            count_exclamation += len(re.findall(r'[!]', text_without_html))
        if bool(re.search(r'[!]{2,}', text_without_html)):
            count_multipleexclamation += len(re.findall(r'[!]{2,}', text_without_html))
        if bool(re.search(r'[:]', text_without_html)):
            count_colon += len(re.findall(r'[:]', text_without_html))
        if bool(re.search(r'[()]', text_without_html)):
            count_ellipse += len(re.findall(r'[()]', text_without_html))
        if bool(re.search(r'[^a-zA-Z0-9 \t]', text_without_html)):
            count_special += len(re.findall(r'[^a-zA-Z0-9 \t]', text_without_html))
        count_words += len(text_without_html.split())
        for i in text_without_html.split():
            if len(i) >= 6:
                count_word_greaterthan6 += 1
            if len(i) <= 3:
                count_word_lesserthan3 += 1

        l=[i for i in text_without_html.lower().split() if i not in stop and not i.isdigit()]
        final = [k for k in l if not bool(re.search(r'^[^a-zA-Z]+$', k)) and not bool(re.search(r'^[a-zA-Z]$',k))]

        count_duplicate += countduplicates(final)
        minwordlength = minwordlt(final)
        count_sentences += len(sent_tokenize(text_without_html))
        for i in sent_tokenize(text_without_html):
            if i[0].isupper():
                count_uppersentence += 1
            elif i[0].islower():
                count_lowersentence += 1
        if bool(re.search(r'[$]', text_without_html)):
            count_dollar += len(re.findall(r'[$]', text_without_html))
        l = len(re.findall(r'[a-z]', text_without_html))
        u = len(re.findall(r'[A-Z]', text_without_html))

        if l != 0:
            maxratio += u / l
        l = len(text_without_html)
        u = len(re.findall(r'[A-Z]', text_without_html))

        if l != 0:
            ratio += u / l
        u = len(re.findall(r'[0-9]', text_without_html))

        if l != 0:
            digitratio += u / l
        u = len(re.findall(r'[^a-zA-Z0-9]', text_without_html))

        if l != 0:
            nonratio += u / l
        maxrepeating= maxRepeating(text_without_html)


        for i in text_without_html.split():
            if (maxlen < len(i)):
                maxlen = len(i)


        for i in text_without_html.split():
            l = len(re.findall(r'[a-z]', i))
            u = len(re.findall(r'[A-Z]', i))
            d = len(re.findall(r'[0-9]', i))
            nc = len(re.findall(r'[^a-zA-Z0-9]', text_without_html))
            lgth = len(i)

            ratio = (l / lgth) + (u / lgth) + (d / lgth) + (nc / lgth)
            if minchardiv > ratio:
                minchardiv = ratio




    print(minchardiv)
    l1.append(countofspam)
    l1.append(countoffunctionwords)
    l1.append(countofanchors)
    l1.append(count_tags)
    l1.append(count_tags-countofanchors)
    l1.append(count_image)
    l1.append(count_alphanumeric)
    l1.append(count_duplicate)
    l1.append(minwordlength)
    l1.append(count_lower)
    l1.append(count_allcaps)
    l1.append(count_lines)
    l1.append(count_digit)
    l1.append(count_space)
    l1.append(count_caps)
    l1.append(count_chars)
    l1.append(count_tabs)
    l1.append(count_special)
    l1.append(count_alpha)
    l1.append(count_words)
    if (count_words != 0):
        l1.append(count_chars / count_words)
    else:
        l1.append(0)
    l1.append(count_word_greaterthan6)
    l1.append(count_word_lesserthan3)
    l1.append(count_quote)
    l1.append(count_comma)
    l1.append(count_period)
    l1.append(count_semicolon)
    l1.append(count_question)
    l1.append(count_multiplequestion)
    l1.append(count_exclamation)
    l1.append(count_multipleexclamation)
    l1.append(count_colon)
    l1.append(count_ellipse)
    l1.append(count_sentences)
    l1.append(count_paras)
    if count_paras!=0:
        l1.append(count_sentences/count_paras)
    else:
        l1.append(0)
    if count_paras!=0:
        l1.append(count_words/count_paras)
    else:
        l1.append(0)
    if count_paras!=0:
        l1.append(count_chars/count_paras)
    else:
        l1.append(0)
    if count_sentences!=0:
        l1.append(count_words/count_sentences)
    else:
        l1.append(0)
    l1.append(count_uppersentence)
    l1.append(count_lowersentence)
    l1.append(count_dollar)
    l1.append(count_capswords)
    l1.append(count_allcapswords)
    l1.append(count_digitwords)
    l1.append(multilet)
    l1.append(singlelet)
    l1.append(singledig)
    l1.append(singlechar)
    l1.append(maxratio)
    l1.append(ratio)
    l1.append(digitratio)
    l1.append(nonratio)
    l1.append(maxrepeating)
    l1.append(maxlen)
    l1.append(minchardiv)
    with open("E:\\SpamDetection\\bodyfeatures1.csv", 'a') as csv_file:
        filewriter = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

        filewriter.writerow(l1)


path = 'E:\\SpamDetection\\ham_test'
with open("E:\\SpamDetection\\bodyfeatures1.csv", 'w') as csv_file:
    filewriter = csv.writer(csv_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL,lineterminator='\n')

    filewriter.writerow(['Class','count of spam words','count of function words','count of HTML anchors','count of all tags','count of all tags not anchor','count of image tags','count of alphanumeric','count of duplicate words','min word length','count of lower case','longest capitalized word','count of lines','count of digits','count of whitespaces','count of uppercase chars','count of all chars','count of tabs','count of specials','count of alpha chars','count of words','average word lt','count of words whose lt is greater than 6','count of words whose lt is lesser than 3','count of single qoutes','count of commas','count of periods','count of semicolon','count of question marks','count of multiple question marks','count of exclamation','count of multiple exclamation','count of colons','count of ellipses','count of sentences','count of paras','avg number of sentences per para','avg no of words per para','avg no of chars per para','avg no of words per sentence','no of sentences beginning with caps','no of sentences beginning with lower','frequency of $','count of capitalized words','count of all caps','count of digit words','words with only letters','only single letter words','only single digit words','single chars','max ratio of uppercase letters to lowercase letters of each word.','Max of ratio of uppercase letters to all characters of each word','max ratio of digits to all chars in a word','Max of ratio of non-alphanumeric characters to all characters of each word','Max of the longest repeating character','Max of the character lengths of words','minimum char diversity'])
i = 0
for filename in os.listdir(path):
    i = i+1
    print(i)
    extract_body(path+"\\"+filename,0)

path = 'E:\\SpamDetection\\spam_test'
i = 0
for filename in os.listdir(path):
    i = i+1

    print(i)
    extract_body(path+"\\"+filename,1)
#extract_body('E:\\SpamDetection\\spam_train\\0297.9e6095368b4e8258e967798cea8fe40e',0)