class my_Laptop:
#     constructor/initalizer
    def __init__(self, color, ram, storage, model, generation, processor, make):
        self.color = color
        self.ram= ram
        self.storage= storage
        self. model = model
        self.generation = generation
        self.processor = processor
        self.make = make
        
    def specification(self):
        print(f'''
                    Color: {self.color}
                    Ram: {self.ram}
                    Storage: {self.storage}
                    Model: {self.model}
                    Generation:{self.generation}
                    make: {self.make}
                    Processor: {self.processor}
                            
        ''')
    def get_color(self):
        print (f"the color of laptop is {self.color}")

    def set_color (self, newcolor):
        colors=['black', "blue","white", "silver"]
        if newcolor in colors:
            self.color = newcolor
        else:
            print("color not available")
                