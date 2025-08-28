
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
	def __init__(self):
		self.attempts = 
		objects = self.create_objects
		self.room = Room(111, [])

	def create_objects(self):
		return [
			game_object("Sweater", 
									"It's a red sweater that had the number 12 stiched on it.", 
									"Someone has unstitched the second number",
									"It smells like lavender."),
			game_object("Couch", 
									"It's a couch that looks comfortable. It looks ", 
									"It's very soft.", 
									"It smells like old wood.")
		]
game_object = GameObject("rock", "It's gray and smooth.", "It's rough and cold.", "It smells like the earth.")

print(game_object.sniff())