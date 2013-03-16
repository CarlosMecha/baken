import os.path

def can_read(filename):
  return (os.path.isfile(filename) and os.access(filename, os.R_OK))

def can_write(filename, force):
  return (force and os.access(filename, os.W_OK)) or (not os.path.isfile(filename))
  
