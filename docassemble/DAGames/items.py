from docassemble.base.util import (
    DAList
    )


class Item(DAList):
  
  def init(self, *pargs, **kwargs):
    super().init(*pargs, **kwargs)
    self.object_type = DAList

  def visible_items(self, location):
    visible_things = []
    for item in self:
      if item.room == location:
        visible_things.append(item.name)
    return visible_things
    