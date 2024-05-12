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
    