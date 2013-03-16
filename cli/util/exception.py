
class InvalidArguments(Exception):
  
  def __init__(self, msg):
    self._msg = msg

  def __str__(self):
    return "Invalid arguments: " + self._msg


