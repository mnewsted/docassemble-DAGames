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
    usable_things = self.visible_items(location) + self.inventory()
    return usable_things

  def get_description(self, thing):
    for item in self:
      if item.name.text == thing:
        return item.desc
    return "Something's wrong..."
  
  def list_inventory_as_fields(self):
    things_in_fields = list()
    for item in self.inventory():
      things_in_fields.append( { item: item.capitalize() } )
    things_in_fields.append( { "cancel": "Nevermind. I don't want to do this." } )
    return things_in_fields

  def list_visible_as_fields(self, location):
    things_in_fields = list()
    for item in self.visible_items(location):
      things_in_fields.append( { item: item.capitalize() } )
    things_in_fields.append( { "cancel": "Nevermind. I don't want to do this." } )
    return things_in_fields

  def list_usable_as_fields(self, location):
    things_in_fields = list()
    for item in self.usable_items(location):
      things_in_fields.append( { item: item.capitalize() } )
    things_in_fields.append( { "cancel": "Nevermind. I don't want to do this." } )
    return things_in_fields

  def is_moveable(self, thing):
    for item in self:
      if item.name.text == thing:
        if item.moveable:
          return True
        else:
          return False
    return

  def add_to_inventory(self, location, thing):
    for item in self:
      if item.name.text == thing and item.room == location and item.moveable == True:
        item.room = 999
        return
    return
  
  def remove_from_inventory(self, location, thing):
    for item in self:
      if item.name.text == thing and item.room == 999:
        item.room = location
        return
    return
