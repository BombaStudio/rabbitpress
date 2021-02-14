from os import *
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
"""
to be continued
http-adobe-coldfusion-apsa1301.nse
http-google-malware.nse
http-svn-enum.nse
http-affiliate-id.nse
http-grep.nse
http-svn-info.nse
http-apache-negotiation.nse         
http-headers.nse                        http-title.nse
http-apache-server-status.nse       http-hp-ilo-info.nse                    http-tplink-dir-traversal.nse
http-aspnet-debug.nse               http-huawei-hg5xx-vuln.nse              http-trace.nse
http-auth-finder.nse                http-icloud-findmyiphone.nse            http-traceroute.nse
http-auth.nse                       http-icloud-sendmsg.nse                 http-trane-info.nse
http-avaya-ipoffice-users.nse       http-iis-short-name-brute.nse           http-unsafe-output-escaping.nse
http-awstatstotals-exec.nse         http-iis-webdav-vuln.nse                http-useragent-tester.nse
http-axis2-dir-traversal.nse        http-internal-ip-disclosure.nse         http-userdir-enum.nse
http-backup-finder.nse              http-joomla-brute.nse                   http-vhosts.nse
http-barracuda-dir-traversal.nse    http-jsonp-detection.nse                http-virustotal.nse
http-bigip-cookie.nse               http-litespeed-sourcecode-download.nse  http-vlcstreamer-ls.nse
http-brute.nse                      http-ls.nse                             http-vmware-path-vuln.nse
http-cakephp-version.nse            http-majordomo2-dir-traversal.nse       http-vuln-cve2006-3392.nse
http-chrono.nse                     http-malware-host.nse                   http-vuln-cve2009-3960.nse
http-cisco-anyconnect.nse           http-mcmp.nse                           http-vuln-cve2010-0738.nse
http-coldfusion-subzero.nse         http-methods.nse                        http-vuln-cve2010-2861.nse
http-comments-displayer.nse         http-method-tamper.nse                  http-vuln-cve2011-3192.nse
http-config-backup.nse              http-mobileversion-checker.nse          http-vuln-cve2011-3368.nse
http-cookie-flags.nse               http-ntlm-info.nse                      http-vuln-cve2012-1823.nse
http-cors.nse                       http-open-proxy.nse                     http-vuln-cve2013-0156.nse
http-cross-domain-policy.nse        http-open-redirect.nse                  http-vuln-cve2013-6786.nse
http-csrf.nse                       http-passwd.nse                         http-vuln-cve2013-7091.nse
http-date.nse                       http-phpmyadmin-dir-traversal.nse       http-vuln-cve2014-2126.nse
http-default-accounts.nse           http-phpself-xss.nse                    http-vuln-cve2014-2127.nse
http-devframework.nse               http-php-version.nse                    http-vuln-cve2014-2128.nse
http-dlink-backdoor.nse             http-proxy-brute.nse                    http-vuln-cve2014-2129.nse
http-dombased-xss.nse               http-put.nse                            http-vuln-cve2014-3704.nse
http-domino-enum-passwords.nse      http-qnap-nas-info.nse                  http-vuln-cve2014-8877.nse
http-drupal-enum.nse                http-referer-checker.nse                http-vuln-cve2015-1427.nse
http-drupal-enum-users.nse          http-rfi-spider.nse                     http-vuln-cve2015-1635.nse
http-enum.nse                       http-robots.txt.nse                     http-vuln-cve2017-1001000.nse
http-errors.nse                     http-robtex-reverse-ip.nse              http-vuln-cve2017-5638.nse
http-exif-spider.nse                http-robtex-shared-ns.nse               http-vuln-cve2017-5689.nse
http-favicon.nse                    http-sap-netweaver-leak.nse             http-vuln-cve2017-8917.nse
http-feed.nse                       http-security-headers.nse               http-vuln-misfortune-cookie.nse
http-fetch.nse                      http-server-header.nse                  http-vuln-wnr1000-creds.nse
http-fileupload-exploiter.nse       http-shellshock.nse                     http-waf-detect.nse
http-form-brute.nse                 http-sitemap-generator.nse              http-waf-fingerprint.nse
http-form-fuzzer.nse                http-slowloris-check.nse                http-webdav-scan.nse
http-frontpage-login.nse            http-slowloris.nse                      http-wordpress-brute.nse
http-generator.nse                  http-sql-injection.nse                  http-wordpress-enum.nse
http-git.nse                        https-redirect.nse                      http-wordpress-users.nse
http-gitweb-projects-enum.nse       http-stored-xss.nse                     http-xssed.nse

"""
help = """
\033[1;32;40m·─────────────────────────────────────────────────·
\033[1;32;40m|\033[1;33;40m set target      \033[1;32;40m└──>\033[1;33;40m set target for testing     \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m scan nmap       \033[1;32;40m└──>\033[1;33;40m scan target with nmap      \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m scan wordpress  \033[1;32;40m└──>\033[1;33;40m scan target with wordpress \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m help            \033[1;32;40m└──>\033[1;33;40m help                       \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m exit            \033[1;32;40m└──>\033[1;33;40m exit                       \033[1;32;40m|
\033[1;32;40m·─────────────────────────────────────────────────·
"""
help_nmap = """
\033[1;32;40m·─────────────────────────────────────────────────·
\033[1;32;40m|\033[1;33;40m ftp             \033[1;32;40m└──>\033[1;33;40m scan target for ftp        \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m ftp             \033[1;32;40m└──>\033[1;33;40m scan target for http        \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m help            \033[1;32;40m└──>\033[1;33;40m help                       \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m back            \033[1;32;40m└──>\033[1;33;40m back main menu             \033[1;32;40m|
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
def nmap_scan(rpr,target):
	npt = "nmap"
	np = rpr+"[\033[1;31;40m"+npt+"\033[1;32;40m]"
	logn = "\033[1;32;40m└─"+np+"─>\033[0;37;40m"
	target = target.replace('http://','')
	target = target.replace('https://','')
	while True:
		k = input(logn)
		if k == "back":
			break
		if k == "ftp":
			nptftp = "nmap/ftp"
			npftp = rpr+"[\033[1;31;40m"+nptftp+"\033[1;32;40m]"
			lognftp = "\033[1;32;40m└─"+npftp+"─>\033[0;37;40m"
			op = input("""
\033[1;32;40m├\033[1;33;40m[0]\033[0;37;40m With all
\033[1;32;40m├\033[1;33;40m[1]\033[0;37;40m ftp-anon.nse
\033[1;32;40m├\033[1;33;40m[2]\033[0;37;40m ftp-brute.nse
\033[1;32;40m├\033[1;33;40m[3]\033[0;37;40m ftp-proftpd-backdoor.nse
\033[1;32;40m├\033[1;33;40m[4]\033[0;37;40m ftp-vsftpd-backdoor.nse
\033[1;32;40m├\033[1;33;40m[5]\033[0;37;40m ftp-bounce.nse
\033[1;32;40m├\033[1;33;40m[6]\033[0;37;40m ftp-syst.nse
\033[1;32;40m├\033[1;33;40m[7]\033[0;37;40m ftp-vuln-cve2010-4221.nse
\033[1;32;40m├\033[1;33;40m[c]\033[0;37;40m Cancel
\033[1;32;40m└-"""+lognftp)
			if op == "c":
				pass
			if op == "0":
				system("""nmap --script "ftp*" -p 21 """+target)
			if op == "1":
				system("""nmap --script ftp-anon.nse -p 21 """+target)
			if op == "2":
				system("""nmap --script ftp-brute.nse -p 21 """+target)
			if op == "3":
				system("""nmap --script ftp-proftpd-backdoor.nse -p 21 """+target)
			if op == "4":
				system("""nmap --script ftp-vsftpd-backdoor.nse -p 21 """+target)
			if op == "5":
				system("""nmap --script ftp-bounce.nse -p 21 """+target)
			if op == "6":
				system("""nmap --script ftp-syst.nse -p 21 """+target)
			if op == "7":
				system("""nmap --script ftp-vuln-cve2010-4221.nse -p 21 """+target)
		if k == "help":
			print(help_nmap)
		if k == "http":
			system("""nmap --script "http*" -p 80 """+target)
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
