import logging
import re
from cli.util.exception import *

class ActionParser(object):
  """
  The base class for action argument parsers.

  """

  _DEFINES_PATTERN = "^-D(\w+(?:\.(?:\w)+)*)=(.*)$"

  def __init__(self, args):
    self._arguments = args
    self.regex = re.compile(self._DEFINES_PATTERN)

  def _parse_defines(self, configurer):
    """
    Parses custom parameters from command line.
    """
    if (len(self._arguments) == 0):
      return

    option = self._arguments[0]

    res = self.regex.search(option)
    if (res):
      self._arguments.pop(0)
      key = res.group(1).lower()
      value = res.group(2)
      logging.debug("Custom param: %s = %s", key, value)
      configurer.add_param(key, value)
      return configurer

    return

  
  def _parse_global_options(self, configurer):
    """
    Parses global options as -v and -h
    """
    if (len(self._arguments) == 0):
      return

    option = self._arguments[0].lower()

    if ("-h" == option):
      logging.debug("Help requested")
      self._arguments.pop(0)
      configurer.request_help(True)
      return configurer

    if ("-v" == option):
      logging.debug("Version requested")
      self._arguments.pop(0)
      configurer.request_version(True)
      return configurer

    return

  def _parse_action_options(self, configurer):
    """
    Custom options parser
    This method should be override.
    """
    raise DumbException("This method should be overrided. Ya dumb!")
  
  def _parse_action(self, configurer):
    """
    Action parser.
    This method should be override.
    """
    raise DumbException("This method should be overrided. Ya dumb!")

  def get_arguments(self):
    return self._arguments

  def parse(self, configurer):
    """
    Parses the CLI arguments.
    """
    while(len(self._arguments) > 0):
      length = len(self._arguments)
      # Options as -v, -h, etc.
      self._parse_global_options(configurer)
      # Custom action options.
      self._parse_action_options(configurer)
      # Action parameters
      self._parse_action(configurer)
      # Parse custom parameters
      self._parse_defines(configurer)
      if (length == len(self._arguments)):
        raise InvalidArguments("Unrecognized argument: " + str(self._arguments))

    return configurer
    
  def get_action_name(self):
    """
    Obtains the action's name.
    This method should be override.
    """
    raise DumbException("This method should be overrided. Ya dumb!")

