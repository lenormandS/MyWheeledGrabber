import pygame, sys
from pygame.locals import *
import pygame.camera
import pygame.joystick
import pygame.mixer
import os
from commande import Commande

class MWG(object):
	def __init__(self):
		try:
			self.size_X = sys.argv[1]
		except:
			self.size_X = 640
		try:
			self.size_Y = sys.argv[2]
		except:
			self.size_Y = 480
		
		pygame.init()
		pygame.camera.init()
		self.window = pygame.display.set_mode([int(self.size_X),int(self.size_Y)],RESIZABLE)
		self.label = pygame.display.set_caption("WheeledGrabber Control Windows")
		#self.cam = pygame.camera.Camera('/dev/video0',(int(self.size_X),int(self.size_Y)))
		self.cam = pygame.camera.Camera(pygame.camera.list_cameras()[0],(int(self.size_X),int(self.size_Y)))
		self.cam.start()
		self.commande = Commande()

	def run(self):
		while True:
			self.window.blit(self.cam.get_image(),(0,0))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

#evenement du clavier:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_F4 or event.key == pygame.K_q:
						sys.exit()
						
					if event.key == pygame.K_UP:
						self.commande.forward()
						
					if event.key == pygame.K_DOWN:
						self.commande.backward()
						
					if event.key == pygame.K_RIGHT:
						self.commande.right()
						
					if event.key == pygame.K_LEFT:
						self.commande.left()
						
					if event.key == pygame.K_a:
						self.commande.grab(self.window,'drop')
						
					if event.key == pygame.K_l:
						self.commande.drop(self.window,'grab')
						
					if event.key == pygame.K_s:
						self.commande.screensaver(self.window)
						
					if event.key == pygame.K_c:
						self.window.blit(self.commande.text_component('helloo',255,0,0),(10,10))
						pygame.display.update()
#evenement du joystick bouton:
				if event.type == pygame.JOYBUTTONDOWN:
					if event.button == 5: #fermeture de la pince
						self.commande.grab(self.window,'grab')
					if event.button == 4: #Ouverture de la pince
						self.commande.drop(self.window,'drop')
					else: 
						print(event.button)
				
#evenement du joystick axis:
				if event.type == pygame.JOYAXISMOTION:

					if (joystick.get_axis(0) > -32768 and joystick.get_axis(0) < 32768):
						if (joystick.get_axis(0) > -32768 and joystick.get_axis(0) < 0):
							self.commande.arm_rotation_left()

					if (joystick.get_axis(0) > 0 and joystick.get_axis(0) <= 32768):
						self.commande.arm_rotation_right()

					if (joystick.get_axis(1) > -32768 and joystick.get_axis(1) < 32768):
						if (joystick.get_axis(1) > -32768 and joystick.get_axis(1) < 0):
							self.commande.arm_rotation_forward()

					if (joystick.get_axis(1) > 0 and joystick.get_axis(1) <= 32768):
						self.commande.arm_rotation_backward()
#evenement du joystick hat:
				if event.type == pygame.JOYHATMOTION:

					if (joystick.get_hat(0) == (0,1)): #up
						self.commande.arm_rotation_forward()
					if (joystick.get_hat(0) == (0,-1)): #down
						self.commande.arm_rotation_backward()
					if (joystick.get_hat(0) == (1,0)): #droite
						self.commande.arm_rotation_right()
					if (joystick.get_hat(0) == (-1,0)): #gauche
						self.commande.arm_rotation_left()
				
#initialisation du joystick et des bouton et axis:
			joystick_count = pygame.joystick.get_count()

			for i in range(joystick_count):
				joystick = pygame.joystick.Joystick(i)
				joystick.init()

				buttons = joystick.get_numbuttons()
				axes = joystick.get_numaxes()
mwg = MWG()
mwg.run()