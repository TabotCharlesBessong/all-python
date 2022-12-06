
class User:
  def __init__(self,userId,userName):
    self.id = userId
    self.name = userName
    self.followers = 0
    self.following = 0
  def follow(self,user):
    user.followers +=1
    self.following +=1

user1 = User('001','Charles')
user2 = User('002','Peter')

user1.follow(user2)
user2.follow(user1)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)