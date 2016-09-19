import requests
import random
import time
import randomheader


def send_msg(jsession_id, msg, smsnumber):
    toke = jsession_id[4:]
    header = randomheader.header()
    header.update({
        'Host': 'site21.way2sms.com',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Referer': 'http://site21.way2sms.com/sendSMS?Token=' + toke,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'})

    cookie = dict(_ga='GA1.2.1259803070.1448989082', __gads='ID=2f1b44c88b3b95b7:T=1448989082:S=ALNI_MaipwWyw2hUU0fylEPb_gxGhuABig', JSESSIONID=jsession_id, _gat='1')
    payload = {'ssaction': 'ss', 'Token': toke, 'mobile': smsnumber, 'message': msg, 'msgLen': len(msg)}

    url1 = "http://site21.way2sms.com/smstoss.action"
    r1 = requests.post(url1, headers=header, cookies=cookie, data=payload)
    if r1.status_code == 200:
        if ('finished your day quota' in str(r1.content)):
            print('Message not sent. Day Quota is completed.')
            return False
        else:
            print("Message sent to : %s \n" % (smsnumber))
            return True
    else:
        print("Message not sent. Try after some time.")
        return False


def send(Text, smsnumber):
    # Way2Sms credentials
    user_number = str(input("Please enter the username: + 91"))
    password = str(input("Please enter the password: "))

    url = "http://site21.way2sms.com/Login1.action"

    # limit the character length
    msg = (Text)[0:160]

    payload = {
        'username': user_number,
        'password': password
    }

    session = requests.Session()
    # Randomly sleep for some time ;)
    time.sleep(random.uniform(1, 5))

    try:
        r = session.post(url, data=payload)
        cj = session.cookies
        # print (r.content.decode('ISO-8859-1').encode('utf8'))
        session_id = requests.utils.dict_from_cookiejar(cj)
        f_session_id = session_id['JSESSIONID']
        rrr = f_session_id
        _b = send_msg(rrr, msg, smsnumber)
        if _b is True:
            return True
        elif _b is False:
            return False

    except Exception as e:
        print('Message not sent. Error logging in to SMS vendor: \n', e)
    return False


if __name__ == '__main__':
    send('Test message from Way2Sms', '97812345678')
