from docassemble.base.util import (
    DAList,
    Thing
    )


class RoomList(DAList):
  
  def init(self, *pargs, **kwargs):
    super().init(*pargs, **kwargs)
    self.object_type = Thing

  def is_valid_exit(self, location, direction):
    if direction in self[location].exits:
      return True
    else:
      return False   

  def visible_exits(self, location):
    exits = []
    for dir in self[location].exits:
      exits.append(full_direction(dir))
    return exits
                   
def short_direction(dir):
  if len(dir) == 1:
    return dir
  if len(dir) == 2:
    if dir == 'up':
      return dir[0]
    else:
      return dir
  if dir in [ 'north', 'south', 'east', 'west', 'up', 'down']:
    return dir[0]
  else:
    return dir[0] + dir[5]

  
def full_direction(dir):
  direction_pairs = { 'n':'north', 's':'south', 'e':'east', 'w':'west', 'u':'up', 'd':'down', 'nw':'northwest', 'ne':'northeast', 'sw':'southwest', 'se':'southeast' }
  short_dir = short_direction(dir)
  return direction_pairs[short_dir]
