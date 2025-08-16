import random
import string

class Password:

    def __init__(self, strength = "mid", length = "unspecified"):
        
        if strength == "low" and length == "unspecified":
            length = 8
            
        if strength == "mid" and length == "unspecified":
            length = 12
        
        if strength == "high" and length == "unspecified":
            length = 16
            
        self.strength = strength
        self.length = length 
        
        passwordLow = string.ascii_letters
        passwordMid = string.ascii_letters + string.digits
        passwordHigh = string.ascii_letters + string.digits + string.punctuation
        
        if strength == "low":
            password = random.sample(passwordLow, self.length)
        elif strength == "mid":
            password = random.sample(passwordMid, self.length)
        else:
            password = random.sample(passwordHigh, self.length)
            
        self.password = ''.join(password)   
            
            
    @staticmethod        
    def show_input_universe():
        letters = list(string.ascii_letters)
        numbers = list(string.digits)
        punctuation = list(string.punctuation)