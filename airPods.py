class airPods:

    def __init__(self, model, color, provisioner, price):
        self.model = model
        self.color = color
        self.provisioner = provisioner
        self.price = price

    def __str__(self):
        return str(self.model) + ' ' + self.color + ' ' + self.provisioner + ' ' + str(self.price)