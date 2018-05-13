import pygame

class Commande():
	def __init__(self):
		self.position_X = 0
		self.position_Y = 0
		self.font = pygame.font.Font(None,36)
	
		
	def get_position_X(self):
		return (self.font.render('Position X : ' + str(self.position_X),1,pygame.Color(0,255,0)))
		
	def get_position_Y(self):
		return (self.font.render('Position Y : ' + str(self.position_Y),1,pygame.Color(0,255,0)))

	def screensaver(self,item):
		pygame.image.save(item,'screenshot.jpg')
		
	def text_component(self,value,r,g,b):
		text = self.font.render('Intialize ' + value, 1, pygame.Color(r,g,b))
		return text
		
	def initialize(self,text):
		return (self.font.render('System ' + text,1,pygame.Color(255,0,0)))

	def forward(self):
		self.position_Y = self.position_Y+1

	def backward(self):
		self.position_Y = self.position_Y-1

	def left(self):
		self.position_X = self.position_X-1

	def right(self):
		self.position_X = self.position_X+1
		
	def grab(self,item,value):
		item.blit(self.text_component(value,232,23,54),(10,40))
		pygame.display.update()

	def drop(self,item,value):
		item.blit(self.text_component(value,100,200,85),(10,40))
		pygame.display.update()
	
	def arm_rotation_forward(self):
		print('arm_rotation_forward function')
	
	def arm_rotation_backward(self):
		print('arm_rotation_backward function')
	
	def arm_rotation_right(self):
		print('arm_rotation_right function')
	
	def arm_rotation_left(self):
		print('arm_rotation_left function')
		
