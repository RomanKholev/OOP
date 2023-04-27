from Cat import Cat
from Owl import Owl
from Salmon import Salmon
from Dog import Dog
cat = Cat("cat1", 5)
cat.voice()
print(cat.getAge())

dog = Dog("dog", 10)
dog.voice()
salmon = Salmon("sal", 20)
salmon.addHunger(5)
salmon.feed("eggs")
salmon.isHungry()
salmon.feed("bread")
salmon.isHungry()

owl = Owl("owl1", 6)
owl.addHunger(5)
owl.addHunger(5)
owl.isHungry()
owl.feed(4, dog)
owl.isHungry()
owl.feed(4, cat)
owl.isHungry()
owl.feed(16, salmon)
owl.isHungry()
