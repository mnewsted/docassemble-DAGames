def get_command(input_text):
  input_text = input_text.lower()
  space_index = input_text.find(' ')
  if space_index == -1:
    return input_text
  else:
    return input_text[0:space_index]

def get_target(input_text):
  input_text = input_text.lower()
  space_index = input_text.find(' ')
  if space_index == -1:
    return ''
  else:
    return input_text[(space_index + 1):]
