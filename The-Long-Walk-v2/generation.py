import random
import linecache

        

class jackpoint:
    """a subtrail tacked onto the main trail at a certain point. allows for shortcuts, or the 'scenic' route"""
    def __init__(self, instance, length):
        self.instance = instance
        self.jackpoint = random.randint(5, length - 5)
        self.player_position = 0
        self.jackname = get_name()
        self.length = random.randint(self.jackpoint, length)
        self.reentry = random.randint(self.jackpoint, length)
        
        if self.length > length - self.jackpoint:
          self.length == (length - self.jackpoint)
     
class MainTrail:
    """single main trail. reach the end to win. serves as a hub for all off trails"""

    def __init__(self):
        self.name = get_name()
        self.length = random.randint(100, 200)
        self.player_position = 0
        self.currentJack = -1
        self.entryAt = 0

        self.jack1 = jackpoint(0, self.length)
        self.jack2 = jackpoint(1, self.length)
        self.jack3 = jackpoint(2, self.length)
        self.jack4 = jackpoint(3, self.length)

        self.jackpoints = [self.jack1, self.jack2, self.jack3, self.jack4]
        
def generate_trail_names():
    """just sends main trail into game loop"""
    mainTrail = MainTrail()
    return mainTrail
    
def get_name():
  """cobbles together a procedural name for a trail"""
  unNamed = []
  thing = random.randint(1, 15)
  if thing == 12:
    unNamed.append(str(random.randint(1,999)))
    unNamed.append(" ")

  elif thing == 15:
    pass

  else:
    unNamed.append(linecache.getline("resources/adjectives.txt", thing).rstrip("\n"))
    unNamed.append(" ")
  
  unNamed.append(linecache.getline("resources/trail_subject.txt", random.randint(1, 19)).rstrip("\n"))
  unNamed.append(" ")
  unNamed.append(linecache.getline("resources/end_caps.txt", random.randint(1, 10)).rstrip("\n"))
  return "".join(unNamed)