#constructor
class User:

  def __init__(self, user_id, user_name) -> None:
    print("New user being created")
    #attributes creation
    self.id = user_id
    self.name = user_name
    self.followers = 0  # settinng default value --> no need to define in parameter
    self.following = 0
    #methods creation

  def follow(self, user):
    user.followers +=1
    self.following +=1


# we can initialize an object instead of doig this
# user_1 = User()
# user_1.id = "001"
# user_1.name = "Hanna"

# user_2 = User()
# user_2.id = "002"
# user_2.name = "baba"
# print(user_1.id)

# initialize
user_1 = User("001", "hanna")
print(user_1.id)
print(user_1.name)
print(user_1.followers)

user_2 = User("002","baba")

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.followers)