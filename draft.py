class Human:
    def __init__(self):
        pass
        # self.race
        # self.gender
        
    def nice_people(self):
        self.speak_up = "when convenient to self"
        self.sustain_personal_loss = "not an option"
        self.self_perception = "I'm a nice person, I try to do good things"
        self.motto = "smile and say nice things, stay neutral and objective, and won't participate in uncomfortable topics"
        self.act_when_it_matters = "revisit first attribute"
        self.life_purpose = "Pursuit of 'happiness'"
        print(f"""{self.self_perception}. 
            But mostly {self.speak_up}, and when it comes to personal loss, it's {self.sustain_personal_loss}.
            I will always {self.motto}.
            My life's purpose is {self.life_purpose}
            """)

    def principled_people(self):
        self.speak_up = "when sees something wrong"
        self.sustain_personal_loss = "accept this is possible"
        self.self_perception = "I'm not sure if I'm nice, or good, I try to be"
        self.motto = "I care about truth, justice, and what is right"
        self.act_when_it_matters = True
        self.life_purpose = "ensuring consistency of my inner belief with my actions"
        print(f"""{self.self_perception}. 
            I try to speak up {self.speak_up}, and when it comes to personal loss, I {self.sustain_personal_loss}.
            {self.motto}.
            My life's purpose is {self.life_purpose}
            """)
human = Human()
print(human.nice_people())
print(human.principled_people())
