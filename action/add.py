from action import *
import shutil

class BakenAdd(BakenAction):
  def run(self):
    print "Adding stuff!"
    shutil.copyfile("test/test.txt", "auto-text.txt")

