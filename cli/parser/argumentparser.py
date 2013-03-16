import os, sys, re, logging, getopt
import importlib
from cli.util.exception import *
from cli.parser.actionparser import ActionParser


class ArgumentParser:
  """
  Main argument parser.
  It defines the action, the action arguments and the options join.
  """

  _PATTERN = "^((\w+)parser)\.py$"
  _PACKAGE = "cli.parser.action"
  _NOT_ACTION_PARSERS = []
  _ROUTE = os.path.join(os.getcwd(), "cli", "parser", "action")
  _parsers = {}

  def __init__ (self, actions, args=None):
    """
    If args is not defined, it will use the sys.argv array.
    
    Also, imports parsers for this package.
    """

    self._arguments = args if args else sys.argv[1:]
    self._actions = actions
    regex = re.compile(self._PATTERN)

    for f in os.listdir(self._ROUTE):
      res = regex.search(f)
      if (res):
        parser_name = res.group(1).lower()
        action = res.group(2).lower()
        if (action not in self._NOT_ACTION_PARSERS 
            and action in self._actions.keys()):
          self._parsers[action] = importlib.import_module(
            self._PACKAGE + "." + os.path.splitext(f)[0]
          )

          logging.debug("Imported %s", f)


  def parse(self):
    """
    Parses arguments from CLI. It retrieves the configuration
    object defining the action and its options.
    """
    parser_module = None

    # Which action?
    for arg in self._arguments:
      arg = arg.lower()
      #TODO: If an global option contains an action value, it will fail.
      if (arg in self._parsers.keys()):
        parser_module = self._parsers[arg]
        break

    if (not parser_module):
      raise InvalidArguments("Not action defined.")

    parser = parser_module.get_parser()

    return parser(self._arguments).parse(self._actions[arg].get_configurer())

