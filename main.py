import pygame, sys
from pygame.locals import *
import pygame.camera
import pygame.joystick
import pygame.mixer
import os

class MWG(object):
	def __init__(self):
		pygame.init()
		pygame.camera.init()
		self.fenetre = pygame.display.set_mode([640,480],RESIZABLE)
		self.label = pygame.display.set_caption("WheeledGrabber Control Windows")
		self.font = pygame.font.Font(None,36)
		self.size = (640,480)
		self.cam0 = pygame.camera.Camera('/dev/video0',self.size)
		self.cam0.start()

	def forward(self):
		print('forward function')
	
	def backward(self):
		print('backward function')
		
	def left(self):
		print('left function')
		
	def right(self):
		print('right function')
		
	def grab(self):
		text = self.font.render("Initialization grab", 1, pygame.Color(232,25,150))
		self.fenetre.blit(text,(10,10))
		pygame.display.update()

	def drop(self):
		print('drop function')
	
	def arm_rotation_forward(self):
		print('arm_rotation_forward function')
	
	def arm_rotation_backward(self):
		print('arm_rotation_backward function')
	
	def arm_rotation_right(self):
		print('arm_rotation_right function')
	
	def arm_rotation_left(self):
		print('arm_rotation_left function')
		
	def run(self):
		while True:
			image = self.cam0.get_image()
			self.fenetre.blit(image,(0,0))
			pygame.display.update()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

#evenement du clavier:
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_F4 or event.key == pygame.K_q:
						sys.exit()
					if event.key == pygame.K_UP:
						self.forward()
					if event.key == pygame.K_DOWN:
						self.backward()
					if event.key == pygame.K_RIGHT:
						self.right()
					if event.key == pygame.K_LEFT:
						self.left()
					if event.key == pygame.K_a:
						self.grab()
					if event.key == pygame.K_l:
						self.drop()
					if event.key == pygame.K_s:
						screensaver(fenetre)
					if event.key == pygame.K_c:
						text = self.font.render("hello", 1, pygame.Color(255,0,0))
						self.fenetre.blit(text,(10,10))
						pygame.display.update()
#evenement du joystick bouton:
				if event.type == pygame.JOYBUTTONDOWN:
					if event.button == 5: #fermeture de la pince
						self.grab()
					if event.button == 4: #Ouverture de la pince
						self.drop()
					else: 
						print(event.button)
				
#evenement du joystick axis:
				if event.type == pygame.JOYAXISMOTION:

					if (joystick.get_axis(0) > -32768 and joystick.get_axis(0) < 32768):
						if (joystick.get_axis(0) > -32768 and joystick.get_axis(0) < 0):
							self.arm_rotation_left()

					if (joystick.get_axis(0) > 0 and joystick.get_axis(0) <= 32768):
						self.arm_rotation_right()

					if (joystick.get_axis(1) > -32768 and joystick.get_axis(1) < 32768):
						if (joystick.get_axis(1) > -32768 and joystick.get_axis(1) < 0):
							self.arm_rotation_forward()

					if (joystick.get_axis(1) > 0 and joystick.get_axis(1) <= 32768):
						self.arm_rotation_backward()
#evenement du joystick hat:
				if event.type == pygame.JOYHATMOTION:

					if (joystick.get_hat(0) == (0,1)): #up
						self.arm_rotation_forward()
					if (joystick.get_hat(0) == (0,-1)): #down
						self.arm_rotation_backward()
					if (joystick.get_hat(0) == (1,0)): #droite
						self.arm_rotation_right()
					if (joystick.get_hat(0) == (-1,0)): #gauche
						self.arm_rotation_left()
				
#initialisation du joystick et des bouton et axis:
			joystick_count = pygame.joystick.get_count()

			for i in range(joystick_count):
				joystick = pygame.joystick.Joystick(i)
				joystick.init()

				buttons = joystick.get_numbuttons()
				axes = joystick.get_numaxes()
mwg = MWG()
mwg.run()