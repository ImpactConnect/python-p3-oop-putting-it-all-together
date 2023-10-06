#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size
        self.condition = "Used"
        
    def check_size(self):
        if not isinstance(self.size, int):
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        
stan_smith = Shoe("Adidas", 9)
stan_smith.size = "not an integer"
stan_smith.check_size()