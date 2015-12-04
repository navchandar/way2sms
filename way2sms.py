import requests
import pdb

def send_msg(jsession_id):
	print  "Login successful ! "
	number=int(raw_input("Please enter the number to whome you want to send the message :"))
	msg=raw_input("Enter the message of 160 characters to send :")
	while len(msg)>160:
		msg=raw_input("Enter the message of 160 characters to send :")
	toke=jsession_id[4:]
	header={
	'Host':'site21.way2sms.com',
	'User-Agent':'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:42.0) Gecko/20100101 Firefox/42.0',
	'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language':'en-US,en;q=0.5',
	'Accept-Encoding':' gzip, deflate',
	'Referer':'http://site21.way2sms.com/sendSMS?Token='+toke,
	'Connection':'keep-alive',
	'Content-Type':'application/x-www-form-urlencoded',
	'Content-Length':'105'
	}

	cookie=dict( _ga='GA1.2.1259803070.1448989082', __gads='ID=2f1b44c88b3b95b7:T=1448989082:S=ALNI_MaipwWyw2hUU0fylEPb_gxGhuABig',JSESSIONID=jsession_id,_gat='1')
	payload={
		'ssaction':'ss','Token':toke,'mobile':number,'message':msg,'msgLen':leng
	}
	url1="http://site21.way2sms.com/smstoss.action"
	r1=requests.post(url1,headers=header,cookies=cookie,data=payload)
	if r1.status_code==200:
		print "Message sent "
	else:
		print "Message not sent. Please try after some time"

url="http://site21.way2sms.com/Login1.action"
user_number=raw_input("Please enter the username for way2sms.com ")
password_=raw_input('please enter the password ')
payload={
	'username':user_number,
	'password':password_
}

# print p.cookies
session=requests.Session()
print "Please wait while we are login in website "
try:
	r=session.post(url,data=payload)
	cj=session.cookies
	# print r.content.decode('ISO-8859-1').encode('utf8')
	session_id=requests.utils.dict_from_cookiejar(cj)
	f_session_id= session_id['JSESSIONID']
	rrr=f_session_id
	send_msg(rrr)
except:
	print "Wrong password(Check your password or tryafter sometime) or Issue with the website! Kindly try after some time "
