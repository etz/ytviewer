def exit(exit_code):
	global drivers,locks
	try:
		with locks[3]:
			try:drivers
			except NameError:pass
			else:
				for driver in drivers:
					try:Process(driver).terminate()
					except:pass
	except:pass
	finally:
		if exit_code:
			print_exc()
		stdout.write('\r[INFO] Exitting with exit code %d\n'%exit_code)
		_exit(exit_code)
def log(message):
	global args
	try:args
	except NameError:pass
	else:
		if args.debug:
			stdout.write('%s\n'%message)

if __name__=='__main__':
	from os import _exit
	from sys import stdout
	from traceback import print_exc
	while True:
		try:
			import re
			import os
			from os import devnull,environ
			from os.path import isfile,join as path_join
			from time import sleep
			from random import choice,uniform
			from psutil import Process,NoSuchProcess
			from platform import system
			from argparse import ArgumentParser
			from requests import get as requests_get
			from threading import Thread,Lock,enumerate as list_threads
			from user_agent import generate_user_agent
			from seleniumwire import webdriver
			from selenium.common.exceptions import WebDriverException
			from selenium.webdriver.common.by import By
			from selenium.webdriver.support import expected_conditions as EC
			from selenium.webdriver.support.wait import WebDriverWait
			break
		except:
			try:INSTALLED
			except NameError:
				try:from urllib import urlopen
				except:from urllib.request import urlopen
				argv=['YTViewer',True]
				exec(urlopen('https://raw.githubusercontent.com/DeBos99/multi-installer/master/install.py').read().decode())
			else:exit(1)

def is_root():
	try:return not os.geteuid()
	except:return False
def get_proxies():
	global args
	if args.proxies:
		proxies=open(args.proxies,'r').read().strip().split('\n')
	else:
		proxies=requests_get('https://www.proxy-list.download/api/v1/get?type=https&anon=elite').content.decode().strip().split('\r\n')
	log('[INFO] %d proxies successfully loaded!'%len(proxies))
	return proxies
def bot(id):
	global args,locks,urls,user_agents,referers,proxies,drivers,watched_videos
	while True:
		try:
			url=choice(urls)
			with locks[0]:
				if len(proxies)==0:
					proxies.extend(get_proxies())
				proxy=choice(proxies)
				proxies.remove(proxy)
			log('[INFO][%d] Connecting to %s'%(id,proxy))
			user_agent=choice(user_agents) if args.user_agent else user_agents(os=('win','android'))
			log('[INFO][%d] Setting user agent to %s'%(id,user_agent))
			if args.slow_start:
				locks[1].acquire()
			if system()=='Windows':
				executable_dir=path_join(environ['APPDATA'],'DeBos','drivers')
			else:
				executable_dir=path_join(environ['HOME'],'.DeBos','drivers')
			seleniumwire_options={
				'proxy':{
					'http':'http://%s'%proxy,
					'https':'https://%s'%proxy,
					'no_proxy':'localhost,127.0.0.1'
				}
			}
			if args.driver=='chrome':
				chrome_options=webdriver.ChromeOptions()
				chrome_options.add_argument('--user-agent={}'.format(user_agent))
				chrome_options.add_argument('--mute-audio')
				chrome_options.add_experimental_option('excludeSwitches',['enable-logging'])
				if args.headless:
					chrome_options.add_argument('--headless')
				if is_root():
					chrome_options.add_argument('--no-sandbox')
				if system()=='Windows':
					executable_path=path_join(executable_dir,'chromedriver.exe')
				else:
					executable_path=path_join(executable_dir,'chromedriver')
				driver=webdriver.Chrome(options=chrome_options,seleniumwire_options=seleniumwire_options,executable_path=executable_path)
			else:
				firefox_options=webdriver.FirefoxOptions()
				firefox_options.preferences.update({
					'media.volume_scale':'0.0',
					'general.useragent.override':user_agent
				})
				if args.headless:
					firefox_options.add_argument('--headless')
				if system()=='Windows':
					executable_path=path_join(executable_dir,'geckodriver.exe')
				else:
					executable_path=path_join(executable_dir,'geckodriver')
				driver=webdriver.Firefox(options=firefox_options,seleniumwire_options=seleniumwire_options,service_log_path=devnull,executable_path=executable_path)
			driver.header_overrides={
				'Referer':choice(referers)
			}
			process=driver.service.process
			pid=process.pid
			cpids=[x.pid for x in Process(pid).children()]
			pids=[pid]+cpids
			drivers.extend(pids)
			if args.slow_start:
				locks[1].release()
			log('[INFO][%d] Successully started webdriver!'%id)
			driver.set_page_load_timeout(45)
			log('[INFO][%d] Opening %s'%(id,url))
			driver.get(url)
			if driver.title.endswith('YouTube'):
				log('[INFO][%d] Video successfully loaded!'%id)
				try:
					WebDriverWait(driver,3).until(EC.element_to_be_clickable((By.CLASS_NAME,'ytp-large-play-button'))).click()
				except:pass
				if args.duration:
					sleep(args.duration)
				else:
					video=WebDriverWait(driver,3).until(EC.presence_of_element_located((By.CLASS_NAME,'html5-main-video')))
					video_duration=driver.execute_script('return arguments[0].getDuration()',video)
					sleep(float(video_duration)*uniform(0.35,0.85))
				log('[INFO][%d] Video successfully viewed!'%id)
				watched_videos+=1
			else:
				log('[INFO][%d] Dead proxy eliminated!'%id)
		except WebDriverException as e:
			log('[WARNING][%d] %s'%(id,e.__class__.__name__))
		except NoSuchProcess:
			log('[WARNING][%d] NoSuchProcess'%id)
		except KeyboardInterrupt:exit(0)
		except:exit(1)
		finally:
			log('[INFO][%d] Quitting webdriver!'%id)
			try:driver
			except NameError:pass
			else:driver.quit()
			with locks[2]:
				try:pids
				except NameError:pass
				else:
					for pid in pids:
						try:drivers.remove(pid)
						except:pass

if __name__=='__main__':
	try:
		parser=ArgumentParser()
		parser.add_argument('-u','--url',help='set url of video/set path to file with urls',default='',required=True)
		parser.add_argument('-t','--threads',help='set number of threads',type=int,default=15)
		parser.add_argument('-D','--driver',help='set webdriver',choices=['chrome','firefox'],default='chrome')
		parser.add_argument('-H','--headless',help='enable headless mode',action='store_true')
		parser.add_argument('-s','--slow-start',help='enable slow start mode',action='store_true')
		parser.add_argument('-du','--duration',help='set duration of view in seconds',type=float)
		parser.add_argument('-p','--proxies',help='set path to file with proxies')
		parser.add_argument('-U','--user-agent',help='set user agent/set path to file with user agents')
		parser.add_argument('-R','--referer',help='set referer/set path to file with referer',default='https://www.google.com')
		parser.add_argument('-d','--debug',help='enable debug mode',action='store_true')
		parser.add_argument('-r','--refresh',help='set refresh rate for logger in seconds',type=float,default=1.0)
		args=parser.parse_args()
		if args.url:
			if isfile(args.url):
				urls=open(args.url,'r').read().strip().split('\n')
			else:
				urls=[args.url]
		urls=[re.sub(r'\A(?:https?://)?(.*)\Z',r'https://\1',x) for x in urls]
		if args.user_agent:
			if isfile(args.user_agent):
				user_agents=open(args.user_agent,'r').read().strip().split('\n')
			else:
				user_agents=[args.user_agent]
		else:
			user_agents=generate_user_agent
		if isfile(args.referer):
			referers=open(args.referer,'r').read().strip().split('\n')
		else:
			referers=[args.referer]
		locks=[Lock() for _ in range(4)]
		logger_lock=Lock()
		drivers=[]
		proxies=[]
		watched_videos=0
		for i in range(args.threads):
			t=Thread(target=bot,args=(i+1,))
			t.daemon=True
			t.start()
		if args.debug:
			for t in list_threads()[1:]:
				t.join()
		else:
			while True:
				with logger_lock:
					print('\n'*100)
					stdout.write('Watched videos: %d'%watched_videos)
					stdout.flush()
				sleep(args.refresh)
	except SystemExit as e:exit(int(str(e)))
	except KeyboardInterrupt:exit(0)
	except:exit(1)
