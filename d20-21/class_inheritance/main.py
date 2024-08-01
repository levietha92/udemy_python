class CuteAnimals:
    def __init__(self):
        self.eyes = 2
        self.fur = "floofy"
        self.legs = 4
    
    def breath(self):
        print("exhale inhale")

    def make_cute_noises(self):
        print("aaachii")

class Pandas(CuteAnimals):
    def __init__(self):
        super().__init__() #must have the bracket here to pull the attributes from superior Class

    def breath(self):
        super().breath()
        print("A bit of snorting")

    def eat_bamboo(self):
        print(""" Yummy
        
      ___           ___           ___           ___           ___           ___     
     /  /\         /  /\         /  /\         /  /\         /  /\         /  /\    
    /  /::\       /  /::\       /  /::|       /  /::\       /  /::\       /  /::\   
   /  /:/\:\     /  /:/\:\     /  /:|:|      /  /:/\:\     /  /:/\:\     /  /:/\:\  
  /  /::\ \:\   /  /::\ \:\   /  /:/|:|__   /  /::\ \:\   /  /:/  \:\   /  /:/  \:\ 
 /__/:/\:\_\:| /__/:/\:\_\:\ /__/:/_|::::\ /__/:/\:\_\:| /__/:/ \__\:\ /__/:/ \__\:\
 \  \:\ \:\/:/ \__\/  \:\/:/ \__\/  /~~/:/ \  \:\ \:\/:/ \  \:\ /  /:/ \  \:\ /  /:/
  \  \:\_\::/       \__\::/        /  /:/   \  \:\_\::/   \  \:\  /:/   \  \:\  /:/ 
   \  \:\/:/        /  /:/        /  /:/     \  \:\/:/     \  \:\/:/     \  \:\/:/  
    \__\::/        /__/:/        /__/:/       \__\::/       \  \::/       \  \::/   
        ~~         \__\/         \__\/            ~~         \__\/         \__\/    

        """)

po = Pandas()
po.make_cute_noises()
po.eat_bamboo()
po.breath()
po.eyes