class Parent():
	  def __init__(self, last_name, eye_color):
	    self.last_name = last_name
	    self.eye_color = eye_color

	  def show_info(self):
	  	print("Last Name-"+self.last_name)
	  	print("Eye Color-"+self.eye_color)


class Child(Parent):
	  def __init__(self, last_name, eye_color, no_of_toys):
	  	print("Child constructor called")
	  	Parent.__init__(self, last_name, eye_color)
	  	self.no_of_toys = no_of_toys

	  def show_info(self):
	  	print("Last Name-"+self.last_name)
	  	print("Eye Color-"+self.eye_color)
	  	print("No of Toys-"+str(self.no_of_toys))

billy_cirus = Parent("Cyrus","blue")
#print(billy_cirus.last_name)

miley_cirus = Child("Cyrus","blue",5)
# print(miley_cirus.last_name)
# print(miley_cirus.no_of_toys)
#billy_cirus.show_info()
miley_cirus.show_info()