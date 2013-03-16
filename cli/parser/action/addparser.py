import logging
import core.util.filechecker as fc
from cli.parser.actionparser import ActionParser
from cli.util.exception import *
from core.util.exception import *
from core.action.add import AddAction

def get_parser():
  return AddParser

class AddParser(ActionParser):
  """
  Add action argument parser.
  [options] [-f] add <in-file> <out-file>
  """
  
  def __init__(self, args):
    super(AddParser, self).__init__(args) # <-- This is soooo ugly
    
  def _parse_action(self, configurer):
    """
    Parsing parsing...
    """
    args = self.get_arguments()
    if (len(args) == 0):
      return

    option = args[0].lower()
    if (option == "add"):
      logging.debug("Found add action.")
      if (len(args) >= 3):
        if (fc.can_read(args[1])):
          configurer.set_in_file(args[1])
        else:
          raise FileException(args[1], "This file doesn't exist.")

        if (fc.can_write(args[2], configurer.get_force_override())):
          configurer.set_out_file(args[2])
        else:
          raise FileException(args[2], "This file already exists or is not writable.")
        args.pop(0)
        args.pop(0)
        args.pop(0)

      else:
        raise InvalidArguments("add needs an in file and an out file.")

      return configurer


  def _parse_action_options(self, configurer):
    args = self.get_arguments()
    if (len(args) == 0):
      return

    option = args[0].lower()
    if (option == "-f"):
      logging.debug("Force override enable.")
      args.pop(0)
      configurer.set_force_override(True)
    
    return configurer


  def get_action_name():
    return AddAction.get_name()

