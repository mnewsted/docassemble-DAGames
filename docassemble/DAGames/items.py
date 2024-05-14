from docassemble.base.util import (
    DAList,
    Thing
    )


class ItemList(DAList):
  
  def init(self, *pargs, **kwargs):
    super().init(*pargs, **kwargs)
    self.object_type = Thing

  def visible_items(self, location):
    visible_things = []
    for item in self:
      if item.room == location:
        visible_things.append(item.name.text)
    return visible_things
  
  def inventory(self):
    held_things = []
    for item in self:
      if item.room == 999:
        held_things.append(item.name.text)
    return held_things
  
  def usable_items(self, location):
    usable_things = []
    usable_things = self.inventory() + self.visible_items(location)
    return usable_things
    