from ball import Ball, CollisionResponse
import pygame
from pygame import Color, Rect
import sys
from math import fabs


class BallWorld(object):
	SCREEN_WIDTH, SCREEN_HEIGHT = 500, 600
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT), 0, 32)
		self.clock = pygame.time.Clock()
		self.balls = []
		self.balls.append(Ball(300, 30, 5, -30, 20, Color('yellow'), 'yellow'))
		self.balls.append(Ball(x=20, y=30, speed=5, angle=-22, r=15, color=Color('red'), name='red'))
		self.balls.append(Ball(60, 80, 8, -60, 20, Color('blue'), 'blue'))		
		self.border = Rect(5, 5, 490, 590)
		
	def update(self):
		timeStep = 1
		
		while timeStep > CollisionResponse.T_EPSILON:
			tMin = timeStep
			#check collision with other balls
			for i in range(len(self.balls)):
				for j in range(len(self.balls)):
					if i < j:
						self.balls[i].detect_collision_with_other_ball(self.balls[j], tMin)
						self.balls[i].log_collision('1)')
						self.balls[j].log_collision('2)')
					if self.balls[i].collision_response.t < tMin:
						tMin = self.balls[i].collision_response.t
			#check collision with box border:
			for b in self.balls:
				b.detect_collision_with_box(self.border, tMin)
				if b.collision_response.t < tMin:
					tMin = b.collision_response.t		
			for b in self.balls:
				b.log('ball ')
				b.update(tMin)
				b.log('ball after update')
			timeStep -= tMin
	
	def log(self, ball, description):
		print description, 'x', ball.x, 'y', ball.y	

	def draw(self):
		pygame.draw.rect(self.screen, Color("grey"), self.border)
		for b in self.balls:
			b.draw(self.screen)
	
	def quit(self):
		sys.exit()

	def run(self):
		pygame.key.set_repeat(30, 30)
		while True:
			time_passed = self.clock.tick(30)
			self.update()
			self.draw()
			for e in pygame.event.get():
				#if e.type == pygame.KEYDOWN:
					#if e.key == pygame.K_RETURN:
						#self.update()
						#self.draw()
				if e.type == pygame.QUIT:
					self.quit()		
			pygame.display.flip()								
	
if __name__=="__main__":
	bw = BallWorld()
	bw.run()
