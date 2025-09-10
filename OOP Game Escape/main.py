
class GameObject:
	name = ""
	appearance = ""
	feel = ""
	smell = ""

	# initializes the object's attributes
	def __init__(self, name, appearance, feel, smell):
		self.name = name
		self.appearance = appearance
		self.feel = feel
		self.smell = smell

	# returns a string describing the appearance of the object
	def look(self):
		return f"You look at the {self.name}. {self.appearance}\n"

	# returns a string describing the feel of the object
	def touch(self):
		return f"You touch the {self.name}. {self.feel}\n"

	# returns a string describing the smell of the object
	def sniff(self):
		return f"You sniff the {self.name}. {self.smell}\n"

class Room:
	game_objects = []
	escape_code = 0

	# initializes the room's attributes
	def __init__(self, escape_code, game_objects):
		self.escape_code = escape_code
		self.game_objects = game_objects

	# returns true if the code is correct, false otherwise
	def check_code(self, code):
		return self.escape_code == code

	# returns a list of the names of all the game objects in the room
	def get_game_object_names(self):
		names = []
		for obj in self.game_objects:
			names.append(obj.name)
		return names

class Game:
	# initializes the game's attributes
	def __init__(self):
		self.attempts = 0
		objects = self.create_objects()
		self.room = Room(731, objects)

	# returns a list of game objects in the room
	def create_objects(self):
		return [
			GameObject("Sweater", 
									"It's a red sweater that had the number 12 stiched on it.", 
									"Someone has unstitched the second number",
									"It smells like lavender."),
			GameObject("Couch", 
									"It's a couch that looks comfortable. Aside from one of the legs missing. ", 
									"It's very soft.", 
									"It smells like old wood."),
			GameObject("Journal",
									"The final entry states that time should be in hours then minutes then seconds (H-M-S).",
									"It's very worn out.",
									"It smells like old paper."),
			GameObject("Spice rack",
									"There are 7 different spices in it.",
									"It's very dusty.",
									"It smells like cinnamon."),
			GameObject("Clock",
									"The hour hand is pointing towards the spice rack, the minute hand is pointing towards the couch, and the second hand is pointing towards the sweater.",
									"It's very dusty.",
									"It doesn't smell like anything.")
		]

	# gets the player's input and processes it
	def take_turn(self):
		prompt = self.get_room_prompt()
		selection = input(prompt)
		print(selection)

	# Gets the prompt for the room
	def get_room_prompt(self):
		prompt = "Enter the 3 digit lock code or choose an item to interact with:\n"
		names = self.room.get_game_object_names()
		index = 1
		for name in names:
			prompt += f"{name}\n"
			index += 1
		return prompt

	# Displays message to get type of interaction with object
	def select_object(self, index):
		selected_object = self.room.game_objects[index]
		prompt = self.get_object_interaction_string(selected_object.name)
		interaction = input(prompt)
		print(interaction)

	# Displays message to get type of interaction with object
	def get_object_interaction_string(self, name):
		return f"How do you want to interact with the {name}?\n1. Look\n2. Touch\n3. Smell\n"

game = Game()
game.take_turn()