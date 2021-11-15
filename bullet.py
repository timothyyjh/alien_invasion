import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""A class to handle the properties of a bullet."""

	def __init__(self, ai_game):
		"""Create a bullet object at the ship's current position."""
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.color

		# Create a bullet rect at (0, 0) and then set the correct position.
		self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midtop

		# Store the bullet's vertical trajectory value.
		self.y = float(self.rect.y)

	def update(self):
		"""Move bullets up the screen."""

		# Updates the decimal position of the bullet.
		self.y -= self.settings.bullet_speed

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect)