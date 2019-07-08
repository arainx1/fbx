import random

import sys, os

import time
def mengetik(s):

    for c in s + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(random.random() * 0.2)

mengetik('Compiled By Daniyal_Arain.............')

mengetik('.')

mengetik('.')

mengetik('trying to request access...')

mengetik('..WHAT,S HAPPENING................')

mengetik('.WHO Are You ...... Request to Access From Daniyal Arain Server')

mengetik('.Requesting....')

mengetik('......................................')

mengetik('..Request Accepted.!.')

mengetik('...')

mengetik('...')

mengetik('Access Granted')

mengetik('100%')

mengetik ('Arain~Server+ip6_1337ok+80)')

mengetik (' Successfully All Done ~ Relaxd & Enjoy ')
os.system('clear')

print ("\033[1;32mEnter UserName&Password:)")

print ("\033[1;32m = Or contact Directly To Daniyal_Arain ")

username = 'root'      

password = 'toor'


def restart():

	ngulang = sys.executable

	os.execl(ngulang, ngulang, *sys.argv)



def main():

	uname = raw_input("username : ")

	if uname == username:

		pwd = raw_input("password : ")



		if pwd == password:

			print "\033[1;32mSAMPAI JUMPA", 

			sys.exit()



		else:

			print "\032[1;32mSorry Passwordmu salah cok !!!\033[00m"

			print "Back Login\n"

			restart()



	else:

		print "\033[1;32mSorry..anda noob !!!\033[00m"

		print "Back Login\n"

		restart()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	restart()
