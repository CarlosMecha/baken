
class Configurer(object):
  """
  Abstraction for configuring actions.
  """

  _help = False
  _version = False
  _params = {}

  def request_help(self, value):
    if (value):
      self._help = True

  def request_version(self, value):
    if (value):
      self._version = True

  def is_help_requested(self):
    return self._help

  def is_version_requested(self):
    return self._version

  def get_params(self):
    return self._params

  def add_param(self, key, value):
    self._params[key] = value

