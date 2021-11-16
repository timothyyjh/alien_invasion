import sys		# To exit the game when the player quits
import pygame
from pygame.constants import KEYDOWN	# To allow game functionalities
from settings import Settings # To use the settings from another module.
from ship import Ship
from bullet import Bullet
from alien import Alien

class AlienInvasion:
	"""Overall class to manage game assets and behavior."""

	def __init__(self):
		"""Initializes the game and creates its resources."""
		# Initializes the pygame module's background settings for the game to
		# work properly.
		pygame.init()
		self.settings = Settings()

		# Argument (1200, 800) is a tuple to define the dimensions of the game
		# window. It is assigned to self.screen so it is accesible to all
		# methods in the class.
		self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption("Alien Invasion")

		self.bg_color = (self.settings.bg_color)
		# Ship requires one argument, an instance of AlienInvasion. This is the 
		# parameter that gives Ship access to the game's parameters such as
		# the screen property.
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.aliens = pygame.sprite.Group()

		self._create_fleet()

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			self.bullets.update()
			self._update_bullets()
		
	# Methods/functions that start with an underscore are helper functions.
	def _check_events(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)
			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)
			
	# We can use elif because it's "FOR EVENT", so it's constantly checking.
	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = True
		elif event.key == pygame.K_q:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Creates a new default bullet and add it to the bullets group."""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_screen(self):		
		pygame.display.flip()
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme() # This is to draw the ship onto the screen.

		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)

	def _update_bullets(self):
		# To get rid of bullets that have disappeared so they don't consume
		# memory.
		for bullet in self.bullets.copy():
			# This means the bullet has passed the top of the screen
			if bullet.rect.bottom <= 0: 
				self.bullets.remove(bullet)

	def _create_fleet(self):
		"""CREATE A FLEET OF ALIENS"""
		# MAKE AN ALIEN
		alien = Alien(self)
		self.aliens.add(alien)

if __name__ == '__main__':
	# Makes a game instance and runs the game.
	ai = AlienInvasion()
	ai.run_game()