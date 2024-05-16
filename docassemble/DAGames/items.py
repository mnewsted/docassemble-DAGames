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

  def get_description(self, thing):
    for item in self:
      if item.name.text == thing:
        return item.desc
    return "Something's wrong..."
  
  def list_as_fields(self, location):
    things_in_fields = list()
    for item in self.usable_items(location):
      things_in_fields.append( { item: item.capitalize() } )
    return things_in_fields

  