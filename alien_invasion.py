import sys		# To exit the game when the player quits
import pygame	# To allow game functionalities
from settings import Settings # To use the settings from another module.
from ship import Ship

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
		self.screen = pygame.display.set_mode((self.settings.screen_width, 
		self.settings.screen_height))
		pygame.display.set_caption("Alien Invasion")

		self.bg_color = (self.settings.bg_color)
		# Ship requires one argument, an instance of AlienInvasion. This is the 
		# parameter that gives Ship access to the game's parameters such as
		# the screen property.
		self.ship = Ship(self)

	def run_game(self):
		"""Start the main loop for the game."""
		while True:
			# Watches for keyboard and mouse events.
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# To retrieve the latest screen update everytime this while loop
			# is run through.
			pygame.display.flip()

			self.screen.fill(self.bg_color)
			self.ship.blitme() # This is to draw the ship onto the screen.

if __name__ == '__main__':
	# Makes a game instance and runs the game.
	ai = AlienInvasion()
	ai.run_game()