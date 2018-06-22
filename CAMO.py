import time
import webbrowser
import winsound
name = input('Enter your name: ')

if name != 'Chris':
	print('Hello '+name)
	clearance == input('Please input your clearance code: ')
else:
	print('Welcome back sir!' )
	clearance = input('Please input your clearance code: ')
	if clearance == '2564':
			time.sleep(2)
			print('Clearance code accepted!')
			request1 = input('What would you like me to do for you? ') 

			if request1 == 'Search':
				searchfor = input('What would you like me to search for? ')
				webbrowser.open('https://www.google.co.in/#q='+searchfor)
			elif request1 == 'Open':
				openapp = input('Which app would you like me to open?')

			elif request1 == "Play Tunes":
				playtune = input('What song would you like me to play? ')
				if playtune == 'Dirty Deeds':
					winsound.PlaySound('DirtyDeedsDoneDirtCheap.wav', winsound.SND_FILENAME)
				elif playtune == 'Free Fallin':
					winsound.PlaySound('TomPettyFreeFalling.wav', winsound.SND_FILENAME)
				elif playtune == "I won't back down":
					winsound.PlaySound('tom-petty-i-wont-back-down', winsound.SND_FILENAME)
	else:
			time.sleep(2)
			print('Clearance code denied!')
			print('STEALTH has been informed of your attempt to impersonate our director.')

