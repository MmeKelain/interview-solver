def reverse_a_thing(reverse_me):
  my_type = type(reverse_me)
  if my_type is str:
    return reverse_string(reverse_me)
  elif my_type is list:
    return reverse_me[::-1]
