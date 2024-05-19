from docassemble.base.util import (
    DAList,
    Thing
    )


class EventList(DAList):
  
  def init(self, *pargs, **kwargs):
    super().init(*pargs, **kwargs)
    self.object_type = Thing

def event_check(self, location, target):
  for event in events:
    if event.exists(location, target):
      if event.done == False:
        return event.name.text, event.effect_index
      else:
        return event.aldready_done_text, 999
    else:
  return "pass", -1

def exists(self, location, target):
  for event in events:
    if event.location == location and event.trigger_item == target:
      return True
    else:
      return False
