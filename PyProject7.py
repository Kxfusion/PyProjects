class Parent:
    def __init__(self, last_name, eye_color):
        print("Parent")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " +self.last_name)
        print("Eye Color - " +self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        Parent.__init__(self, last_name, eye_color)
        print("Child")
        self.toys = toys

    def show_info(self):
        print("Last Name - " +self.last_name)
        print("Eye Color - " +self.eye_color)
        print("Number of Toys - " +str(self.toys))

#George = Parent("Martin", "blue")
Angie = Child("Martin", "blue", 26)
Angie.show_info()
