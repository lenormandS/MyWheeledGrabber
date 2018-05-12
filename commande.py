import pygame

class Commande():
	def __init__(self):
		self.position_X = 0
		self.position_Y = 0
		self.font = pygame.font.Font(None,36)

	def screensaver(self,item):
		pygame.image.save(item,'screenshot.jpg')
		
	def text_component(self,value,r,g,b):
		text = self.font.render('Intialize ' + value, 1, pygame.Color(r,g,b))
		return text
	
	def forward(self):
		print('forward function')

	def backward(self):
		print('backward function')

	def left(self):
		print('left function')

	def right(self):
		print('right function')
		
	def grab(self,item,value):
		item.blit(self.text_component(value,232,23,54),(10,10))
		pygame.display.update()

	def drop(self,item,value):
		item.blit(self.text_component(value,100,200,85),(10,10))
		pygame.display.update()
	
	def arm_rotation_forward(self):
		print('arm_rotation_forward function')
	
	def arm_rotation_backward(self):
		print('arm_rotation_backward function')
	
	def arm_rotation_right(self):
		print('arm_rotation_right function')
	
	def arm_rotation_left(self):
		print('arm_rotation_left function')
		
