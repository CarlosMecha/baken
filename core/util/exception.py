
class DumbException(Exception):
  """
  Exceptions for dumb programmers.
  """
  def __init__(self, msg):
    self.msg = msg

  def __str__(self):
    return "You're fired!: " + self.msg

class FileException(Exception):
  """
  File permission exception.
  """
  def __init__(self, f, msg):
    self.msg = msg
    self.f = f

  def __str__(self):
    return "File exception [" + self.f + "]: " + self.msg

