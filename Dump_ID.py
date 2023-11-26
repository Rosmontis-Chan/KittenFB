import os,re,sys,json,time,requests,random
ses=requests.Session()
id,uid,tokene = [],[],[]

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
xx = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[91m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;92m' # BIRU -
p = '\x1b[0;34m' # BIRU +
asu = random.choice([m,k,h,u,b])

def banner():
    if "win" in sys.platform:os.system("cls")
    else:os.system("clear")
    print(f"""\r
            ╔╦╗╦ ╦╔╦╗╔═╗   ╦╔╦╗
             ║║║ ║║║║╠═╝───║ ║║
            ═╩╝╚═╝╩ ╩╩     ╩═╩╝
""")
def login():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
		tokene.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokene[0], cookies={'cookie':cok})
			sy2 = json.loads(sy.text)['name']
			sy3 = json.loads(sy.text)['id']
			dump(cok,token)
		except KeyError:
			login_c()
		except requests.exceptions.ConnectionError:
			print(f"{m}> Sinyal problem{xx}")
			exit()
	except IOError:
		login_c()
		
def login_c():
	try:
		banner()
		ses = requests.Session()
		print()
		cok = input(f'{xx}> Cookies {h}: ')
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
			print("{m}> Cokies invalid ")
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
					tok = re.search('"access_token": "(.*?)"', str(response7)).group(1);akses(cok)				
					token = open(".token.txt", "w").write(tok)
					cokies = open(".cok.txt", "w").write(cok)
					print()
					print(f"{xx}> Token : {h}{tok}{xx}")
					print()
					print(f"{h}> Ulangi pythonnya{xx}")
				else:
					print(f"{m}> Login gagal cek tumbal ngab{xx}")
					exit()
					
	except Exception as e:
		print(f"{m}> Cokies mokad{xx}")
		os.system('rm -rf .token.txt && rm -rf .cok.txt')
		exit()
		
def dump(cok,token):
	banner()
	try:
		pul = int(input(f'{xx}> Berapa {h}: '))
	except ValueError:
	    print(f'{m}> Gagal dump{xx}')
	    exit()
	if pul<1 or pul>1000:
	    print(f'{m}> Limit 1000{xx}')
	    exit()
	print()
	bil = 0
	for koh in range(pul):
		bil+=1
		suk = input(f'{xx}> ID '+str(bil)+f' {h}: ')
		uid.append(suk)
	print()
	name = input(f"{xx}> Name file dump {h}: ")
	simpan = ('/sdcard/DUMP-ID/' + name + '.txt').replace(' ', '_')
	file = open(simpan, 'w')
	for user in uid:
	    try:
	       params = ({'access_token': token,'fields': "friends"})
	       bas = requests.get('https://graph.facebook.com/{}'.format(user),params=params,cookies={'cookies':cok}).json()
	       for x in bas['friends']['data']:
	           try:
	               z = (x['id']+'|'+x['name'])
	               if z in id:
	                   pass
	               else:
	                   id.append(z)
	                   file.write(z+ '\n')
	                   print(z)
	           except:continue
	    except (KeyError,IOError):
	      pass
	    except requests.exceptions.ConnectionError:
	        print(f'{m}> Koneksi problem{xx}')
	        exit()
	try:
	      print()
	      print(f"{xx}> TOTAL ID {h}: "+str(len(id)))
	      print()
	      print(f"{xx}> {u}Berhasil Dump Id Dari Publik{xx}")
	      print(f"{xx}> Salin Output File ({h} {simpan} {xx})")
	      exit()
	except requests.exceptions.ConnectionError:
	    print(f'{m}> Gagal dump{xx}')
	    os.remove(simpan)
	    exit()
	except (KeyError,IOError):
		print(f'{m}> Teman tidak publik{xx}')
		os.remove(simpan)
		exit()
		
login()