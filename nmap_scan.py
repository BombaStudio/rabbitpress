"""
├[0] With all
├[1] http-sql-injection.nse
├[2] http-csrf.nse
├[3] http-phpmyadmin-dir-traversal.nse
├[4] http-robots.txt.nse
├[5] http-dombased-xss.nse
├[6] http-svn-info.nse
├[7] http-wordpress-enum.nse
├[8] http-headers.nse
├[9] http-phpself-xss.nse
├[10] http-apache-server-status.nse
├[11] http-wordpress-brute.nse
├[12] http-stored-xss.nse
├[13] http-wordpress-users.nse
├[14] http-xssed.nse
├[15] http-passwd.nse
├[c] Cancel
"""
help_nmap = """
\033[1;32;40m·─────────────────────────────────────────────────·
\033[1;32;40m|\033[1;33;40m ftp             \033[1;32;40m└──>\033[1;33;40m scan target for ftp        \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m http            \033[1;32;40m└──>\033[1;33;40m scan target for http       \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m help            \033[1;32;40m└──>\033[1;33;40m help                       \033[1;32;40m|
\033[1;32;40m|\033[1;33;40m back            \033[1;32;40m└──>\033[1;33;40m back main menu             \033[1;32;40m|
\033[1;32;40m·─────────────────────────────────────────────────·
"""
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
			nptftp = "nmap/http"
			npftp = rpr+"[\033[1;31;40m"+nptftp+"\033[1;32;40m]"
			lognftp = "\033[1;32;40m└─"+npftp+"─>\033[0;37;40m"
			op = input("""
\033[1;32;40m├\033[1;33;40m[0]\033[0;37;40m With all
\033[1;32;40m├\033[1;33;40m[1]\033[0;37;40m http-sql-injection.nse
\033[1;32;40m├\033[1;33;40m[2]\033[0;37;40m http-csrf.nse
\033[1;32;40m├\033[1;33;40m[3]\033[0;37;40m http-phpmyadmin-dir-traversal.nse
\033[1;32;40m├\033[1;33;40m[4]\033[0;37;40m http-robots.txt.nse
\033[1;32;40m├\033[1;33;40m[5]\033[0;37;40m http-dombased-xss.nse
\033[1;32;40m├\033[1;33;40m[6]\033[0;37;40m http-svn-info.nse
\033[1;32;40m├\033[1;33;40m[7]\033[0;37;40m http-wordpress-enum.nse
\033[1;32;40m├\033[1;33;40m[8]\033[0;37;40m http-headers.nse
\033[1;32;40m├\033[1;33;40m[9]\033[0;37;40m http-phpself-xss.nse
\033[1;32;40m├\033[1;33;40m[10]\033[0;37;40m http-apache-server-status.nse
\033[1;32;40m├\033[1;33;40m[11]\033[0;37;40m http-wordpress-brute.nse
\033[1;32;40m├\033[1;33;40m[12]\033[0;37;40m http-stored-xss.nse
\033[1;32;40m├\033[1;33;40m[13]\033[0;37;40m http-wordpress-users.nse
\033[1;32;40m├\033[1;33;40m[14]\033[0;37;40m http-xssed.nse
\033[1;32;40m├\033[1;33;40m[15]\033[0;37;40m http-passwd.nse 
\033[1;32;40m├\033[1;33;40m[c]\033[0;37;40m Cancel
\033[1;32;40m└-"""+lognftp)
			if op == "0":
				system("""nmap --script "http*" -p 21 """+target)