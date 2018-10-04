import time
import webbrowser
import winsound
name = input('Enter your name: ')

if name != 'Chris':
	print('Hello '+name)
	clearance = input('Please input your clearance code: ')
	if clearance == '1287':
				time.sleep(2)
				print('Clearance code accepted!')
				request1 = input('What would you like me to do for you?')
				if request1 == 'Search':
								searchfor = input('What would you like me to search for? ')
								webbrowser.open('https://www.google.co.in/#q='+searchfor)
				elif request1 == "Play Tunes":
						playtune == input('What song would you like me to play? ')
						if playtune == 'Dirty Deeds':
								winsound.PlaySound('DirtyDeedsDoneDirtCheap.wav', winsound.SND_FILENAME)
								print('Done Dirt Cheap')
						elif playtune == 'Free Fallin':
								winsound.PlaySound('TomPettyFreeFalling.wav', winsound.SND_FILENAME)
						elif playtune == "I won't back down":
								winsound.PlaySound('tom-petty-i-wont-back-down', winsound.SND_FILENAME)
	else:
			time.sleep(2)
			print('Clearance code denied!')
			print('STEALTH has been informed of your attempt to impersonate our agents.')
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
					print('Done Dirt Cheap')
				elif playtune == 'Free Fallin':
					winsound.PlaySound('TomPettyFreeFalling.wav', winsound.SND_FILENAME)
				elif playtune == "I won't back down":
					winsound.PlaySound('tom-petty-i-wont-back-down', winsound.SND_FILENAME)
			elif request1 == 'Projects'
					print('Current Projects are Project Flage, Project Hero, and Project STEALTH. ')
					project = input('Which Project would you like to explore?')
							if project = 'Project Flage' :
								'Project Flage is the program you are running right now. '
			elif request1 == 'Translate'
				language = input('What languages am I translating?')
						if language == 'English to German'
								print('You have selected English to German')
								text = input('What would you like me to translate into German')
								
							
	else:
			time.sleep(2)
			print('Clearance code denied!')
			print('STEALTH has been informed of your attempt to impersonate our director.')

