class singer :
    def __init__(self,name,nationality,age) :
        self.name = name
        self.nationality = nationality
        self.age = age
        
    def info(self) :
        print(f"\n{self.name} is {self.nationality} singer who is {self.age} years old.")
        
class romance_(singer) :
    def __init__(self,name,nationality,age,songtype) :
        super().__init__(name,nationality,age)
        self.songtype = songtype
        
    def atif(self) :
        self.info()
        print(f"{self.name} sings {self.songtype} of songs.These romantic songs promote harmony,love and gunnah because songs are haram.")
        
class rap_(singer) :
    def _init_(self,name,nationality,age,songtype) :
        super()._init_(name,nationality,age)
        self.songtype = songtype
        
    def honey(self) :
        self.info()
        print(f"{self.name} sings {self.songtype} of songs.These rap songs promote energy and gunnah because songs are haram.")
              
a = romance_("Atif Aslam","Pakistani","40","romantic type")
b = romance_("Rahat Fateh","Pakistani","49","romantic and deep type")
c = rap_("Honey Singh","indian","36","rap type")
d = rap_("Badshah","indian","38","rap type")

a.atif()
b.atif()  
c.honey()
d.honey()