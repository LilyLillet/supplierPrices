class iPhone:

    def __init__(self, model, memory, color, provisioner, price):
        self.model = model
        self.memory = memory
        self.color = color
        self.provisioner = provisioner
        self.price = price


    def __str__(self):
        return str(self.model) + ' ' + self.memory + ' ' + self.color + ' ' + self.provisioner + ' ' + str(self.price)