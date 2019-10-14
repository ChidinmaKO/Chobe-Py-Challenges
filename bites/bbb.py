def outer_func(msg):
  message = msg

  def inner_func():
    print(message)
  return inner_func()

hey_func = outer_func("hey")

bye_func = outer_func("bye")