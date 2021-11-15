class Settings:
	"""Where all the settings of Alien Invasion are stored."""

	def __init__(self):
		"""Initializes the game's settings."""
		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (230, 230, 230)

		# Ship's speed
		self.ship_speed = 1.5

		# Bullet settings
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (0, 0, 255)
		