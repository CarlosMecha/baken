
class Action(object):
  """
  Base class for baken actions.
  """
  _configurer = None

  def __init__(self, configurer):
    self._configurer = configurer

  def get_configurer(self):
    return self._configurer

  def set_configurer(self, configurer):
    self._configuerer = configurer

  def run(self):
    """
    Runs the action.
    This method should be overrided.
    """
    raise DumbException("This method should be overrided. Ya dumb!")


