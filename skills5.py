class DNABase:
    
    bases = {'adenine', 'thymine', 'cytosine', 'guanine'}
    base_shorts = {
        'A': 'adenine', 
        'T': 'thymine', 
        'C': 'cytosine', 
        'G': 'guanine'
        }
    
    
    def __init__(self, neucleotide):
        self.base = neucleotide
        
    def get_nucleotide(self):
        return self._base
    
    def set_nucleotide(self, value):
        if value.lower() in self.bases:
            self._base = value.lower()
        elif value.upper() in self.base_shorts:
            self._base = self.base_shorts[value.upper()]
        else:   
            raise ValueError(f"{value} is not a recognized DNA nucleotide")
    
    def __repr__(self):
        return f"DNAbbase(nucleotide='{self.base}')"
            
            
    base = property(get_nucleotide, set_nucleotide)