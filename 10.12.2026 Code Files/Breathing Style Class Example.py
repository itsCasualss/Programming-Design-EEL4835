class BreathingStyle: #Class
    origin = "Sun Breathing" #Class Variable
    
    def __init__(self,name,user): #__init__ (Constructor)
        self.name = name #Instance Variable
        self.user = user #Instance Varibale
        
    def form(self): #Method 
        return f"{self.user} performs a form of {self.name}"
    
class WaterBreathing(BreathingStyle): #Inheritance
    def __init__(self,user): 
        super().__init__("Water Breathing", user) #super()
        
    def form(self): #Method Overriding
        return f"{self.user} unleashes Water Surface Slash!" 
    
tanjiro = WaterBreathing("Tanjiro") #Object (Instance)
print(tanjiro.form())
print(tanjiro.origin) #Class Variable
