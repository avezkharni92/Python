#classes are blue print for objects
#objects are created by using classes as blueprint
#classes is having attributes = variables
#functions  in classes are called methods / behaviours
#to define the atttributes we use initialize funntion defined by __init__(self)
#self means object itself
#First we need to set class as class <class-name>:
#if there is attribute to be given then it must be given while calling function
#object can be created as shown    object = <class-name>(<attribute if defined>)
#attribute can be defined as shown object1.attribute = <attribute value>

#example of youtube subscribers 

class youtube_subscribe:
    def __init__(self, user, subscribers= 0, subscription = 0):
        self.subs = subscribers
        self.subsc = subscription
        self.user = user

    def subscribe(self, user):
        user.subs += 1
        self.subsc += 1

user1 = youtube_subscribe("Avez")
user2 = youtube_subscribe("Ayesha")
user1.subscribe(user2)
print(user1.subs)
print(user1.subsc)
print(user2.subs)
print(user2.subsc)

user1.subs = 10
user2.subs = 20
user1.subscribe(user2)
user2.subscribe(user1)

print(user1.subs)
print(user1.subsc)
print(user2.subs)
print(user2.subsc)

    
