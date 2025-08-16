class Contact:
    def __init__(self, name, last_name, phone = None, email = None, display_mode="masked"):
        self.name = name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.display_mode = display_mode
        
    def __repr__(self):
        if self.display_mode == "masked":
            name_mid_length = len(self.name) // 2
            last_name_mid_length = len(self.last_name) // 2
            
            return f"Contact(name={self.name[0:name_mid_length]}" + ("*" * (len(self.name) - name_mid_length))  \
                + f",last_name={self.last_name[0:last_name_mid_length]}" + ("*" * (len(self.last_name) - last_name_mid_length))
        
        return f"Contact('{self.name}', '{self.last_name}', '{self.phone}', '{self.email}')"
        
    def __str__(self):
        return f"{self.last_name[0]}{self.name[0]}"
        
    def __eq__(self, other):
        if not isinstance(other, Contact):
            return False
        
        if (self.phone is not None and other.phone is not None) or (self.email is not None and other.email is not None):
            return self.phone == other.phone or self.email == other.email
        
        return self.name == other.name and self.last_name == other.last_name
    
    def __hash__(self):
        return hash((self.name, self.last_name, self.phone, self.email))
    
    def __format__(self, format_spec):
        if format_spec == "masked":
            return f"{self.last_name}{self.name}"
        
        return f"Contact(name={self.name}, last_name={self.last_name}, phone={self.phone}, email={self.email})"