#!/usr/bin/env python
import sys
import os
import datetime
import subprocess

class Logger:
   def __init__(self, dir, filename):
      if os.path.isdir(dir):
          self.filename = dir+filename
      else:
          os.makedirs(dir)
          self.filename = dir+filename

      self.log_file = open(self.filename, "w+")


   def get_timestamp(self):
       return datetime.datetime.now() 

   def log(self, msg):
       timestamp = self.get_timestamp()
       self.log_file.write("{} {}\n".format(timestamp, msg))


