import smtplib
import requests
import datetime
import glob
import sys
import json


def send_mail(user, spec_id):
    found = False
    for fname in glob.glob('specs/*.json'):
        with open(fname, 'r', encoding="utf-8") as g:
            spec = json.load(g)
            if not 'id' in spec: continue
            found = spec['id'] == spec_id
            if found: break
    if not found: return -1
    client = str(spec['client'])

    if 1:
        # try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login('XXXX@gmail.com', 'PASSWORD')
        sent_from = 'YYYY@gmail.com'
        to = ['DDD@FFF.com', 'RRR@TTT.com']
        subject = 'SERVICE X OF: ' + user + ' wants you to YYY  for the client' + client
        body = 'Click <A URL> if want to give pass to an action' + spec_id + '}
        email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
        server.sendmail(sent_from, to, email_text)
        server.close()
        return 1


# except:
#   print('Something went wrong...')

if __name__ == '__main__':
    send_mail(sys.argv[1], sys.argv[2])
