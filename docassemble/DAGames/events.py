from docassemble.base.util import (
    DAList,
    Thing
    )


class EventList(DAList):
  
  def init(self, *pargs, **kwargs):
    super().init(*pargs, **kwargs)
    self.object_type = Thing

  def event_check(self, location, target):
    for event in self:
      if (event.location == location or event.location == 999) and event.trigger_item == target:
        if event.done == False:
          return event.name.text, event.effect_index
        else:
          return event.already_done_text, 999
    return "pass", -1