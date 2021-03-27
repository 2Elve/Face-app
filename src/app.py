from face_identifier import face_id
import pygame, sys
import os

#Run Face ID
face_index = face_id()
profile = { 0 : 'Daniel',
			1 : 'Victor' }

music_genere = { 0 : 'Rock', 
			 	 1 : 'R&B' }

backgrounds = { 0 : 'Icons/backb1.png', 
				1 : 'Icons/backb1.png'}

class BUTTON:
	def __init__(self,icon,rect): 
		self.icon = icon 
		self.rect = rect
		self.width = self.rect.w
		self.height = self.rect.h
		self.center = self.rect.center

	def draw(self): 
		screen.blit(self.icon,self.rect)

	def clicked(self,pos): 
		if pos[0] > (self.center[0]-(self.width/2)) and pos [0] < (self.center[0]+(self.width/2)):
			if pos[1] > (self.center[1]-(self.height/2)) and pos [1] < (self.center[1]+(self.height/2)):
				return True
			
				
pygame.init()

screen = pygame.display.set_mode((800,450))
music_dir = os.path.dirname(os.path.abspath(__file__)) + "\\Music\\"  
print(music_dir)

#Caption and Icon
pygame.display.set_caption("Automovil App")
icon = pygame.image.load('Icons/car.png')
pygame.display.set_icon(icon)

clock = pygame.time.Clock()


#Loading App Elements
font = pygame.font.Font('Fonts/ShipporiMinchoB1-Regular.ttf',16)
user_name = font.render(profile[face_index], True,(255,255,255))
genere = font.render(music_genere[face_index], True,(255,255,255))

bg = pygame.image.load(backgrounds[face_index])

musicLogo = pygame.image.load('Icons/spotify.png')
musicRect = musicLogo.get_rect(center=(400,190))

playButton = pygame.image.load('Icons/play-button.png')
playRect = playButton.get_rect(center=(400,350))

pauseButton = pygame.image.load('Icons/pause.png')
pauseRect = pauseButton.get_rect(center=(400,350))

forwardButton = pygame.image.load('Icons/fast-forward.png')
forwardRect = forwardButton.get_rect(center=(500,350))

rewindButton = pygame.image.load('Icons/rewind.png')
rewindRect = rewindButton.get_rect(center=(300,350))

userLogo = pygame.image.load('Icons/user.png')
userRect = userLogo.get_rect(center=(700, 25))

#Loading Music Elements
paused = False
playlist = []
for name in os.listdir(music_dir + profile[face_index]):
	playlist.append(name)

listPointer = 0 
playlist_size = len(playlist)

music = pygame.mixer.music.load('Music/'+ profile[face_index] + '/' + playlist[listPointer])
pygame.mixer.music.play(0)

#Button Objects
logo = BUTTON(musicLogo,musicRect)
play = BUTTON(pauseButton,pauseRect)
forward = BUTTON(forwardButton,forwardRect)
rewind = BUTTON(rewindButton,rewindRect)
user = BUTTON(userLogo,userRect)

pygame.mixer.music.set_volume(0.1) 

while True:

	#Load Background
	screen.fill((0,0,0))
	screen.blit(bg,(0,0))

	#Get Current Song Name 
	s_name = playlist[listPointer].replace('.ogg','')
	current_song = font.render(s_name,True,(255,255,255))
	currentSongRect = current_song.get_rect(center=(400, 300))

	for event in pygame.event.get():
		mouse_pos = pygame.mouse.get_pos()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if logo.clicked(mouse_pos): 
				print('Logo clicked')

			if play.clicked(mouse_pos): 
				print('Play clicked')
				if play.icon == playButton:
					play.icon = pauseButton 
					pygame.mixer.music.unpause()
					paused = False
				else: 
					play.icon = playButton 
					pygame.mixer.music.pause()
					paused = True

			if forward.clicked(mouse_pos): 
				print('Forward clicked')
				play.icon = pauseButton
				paused = False
				if listPointer < playlist_size-1:
					listPointer += 1
				else: 
					listPointer = 0 
				music = pygame.mixer.music.load('Music/'+ profile[face_index] + '/' + playlist[listPointer])
				pygame.mixer.music.play(0)

			if rewind.clicked(mouse_pos): 
				print('Rewind clicked')
				play.icon = pauseButton
				paused = False
				if listPointer > 0:
					listPointer -= 1
				else: 
					listPointer = playlist_size-1 
				music = pygame.mixer.music.load('Music/'+ profile[face_index] + '/' + playlist[listPointer])
				pygame.mixer.music.play(0)

			if user.clicked(mouse_pos): 
				print('User clicked')


	#Skip if song finished 
	if pygame.mixer.music.get_busy() == False and paused == False:
		if listPointer < playlist_size-1:
			listPointer += 1
			music = pygame.mixer.music.load('Music/'+ profile[face_index] + '/' + playlist[listPointer])
			pygame.mixer.music.play(0)
		else:
			listPointer = 0 
			music = pygame.mixer.music.load('Music/'+ profile[face_index] + '/' + playlist[listPointer])
			pygame.mixer.music.play(0)


	#Render Icons  
	logo.draw()
	play.draw()
	forward.draw()
	rewind.draw()
	user.draw()

	#Render Text Elements 
	screen.blit(user_name, (720,15))
	screen.blit(genere, (385,260))
	screen.blit(current_song,currentSongRect)

	pygame.display.update()
	clock.tick(60)