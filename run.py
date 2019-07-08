import random

import sys, os

import time
def mengetik(s):

    for c in s + '\n':

        sys.stdout.write(c)

        sys.stdout.flush()

        time.sleep(random.random() * 0.1)

mengetik('Compiled By Daniyal_Arain.............')

mengetik('.')

mengetik('.')

mengetik('trying to request access...')

mengetik('..WHAT,S HAPPENING................')

mengetik('.WHO Are You ...... Request to Access From Arain Server')

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

			f = open('start.py')
print(f)
			



		else:

			print "\032[1;32mSorry Wrong Password !!!\033[00m"

			print "Back Login\n"

			sys.exit()



	else:

		print "\033[1;32mSorry..You noob !!!\033[00m"

		print "Back Login\n"

		sys.exit()



try:

	main()

except KeyboardInterrupt:

	os.system('clear')

	sys.exit()
