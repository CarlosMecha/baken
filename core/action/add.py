import shutil
import logging
from core.configurer import Configurer
from core.actiondef import Action

class AddAction(Action):
  """
  Add action: Starts tracking a file.
  """
  def __init__(self):
    super(AddAction, self).__init__(AddConfigurer())

  def run(self):
    print self.get_configurer()
    logging.debug("Adding stuff! %s to %s", self.get_configurer().get_in_file(), self.get_configurer().get_out_file())
    shutil.copyfile(self.get_configurer().get_in_file(), self.get_configurer().get_out_file())

  def get_name():
    return "add"


class AddConfigurer(Configurer):
  """
  Configurer for an 'add' action.
  """

  def __init__(self):
    super(AddConfigurer, self).__init__() # <-- Really? REALLY?
    self._in_file = None
    self._out_file = None
    self._force_override = False

  def get_in_file(self):
    return self._in_file

  def get_force_override(self):
    return self._force_override

  def get_out_file(self):
    return self._out_file

  def get_action_name(self):
    return AddAction.get_name()

  def set_in_file(self, in_file):
    logging.debug("Setting in file %s", in_file)
    self._in_file = in_file

  def set_out_file(self, out_file):
    logging.debug("Setting out file %s", out_file)
    self._out_file = out_file
   
  def set_force_override(self, value):
    if (value):
      self._force_override = True
       
