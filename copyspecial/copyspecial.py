#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dir):
  list = os.listdir(dir)
  return [os.path.abspath(os.path.join(dir, name)) for name in list if re.search(r'__\w+__', name)]

def copy_to(paths, dir):
  os.makedirs(dir)
  for path in paths:
    shutil.copy(path, dir)

def zip_to(paths, zippath):
  command = 'zip -j ' + zippath + ' ' + ' '.join(paths)
  print 'Command I\'m goin to do: ' + command
  (status, output) = commands.getstatusoutput(command)
  if status:
    sys.stderr.write(output)
    sys.exit(status)
  print output

def main():
  # This basic command line argument parsing code is provided.
  # Add code to call your functions below.

  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]
  if not args:
    print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
    sys.exit(1)

  # todir and tozip are either set from command line
  # or left as the empty string.
  # The args array is left just containing the dirs.
  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  tozip = ''
  if args[0] == '--tozip':
    tozip = args[1]
    del args[0:2]

  if len(args) == 0:
    print "error: must specify one or more dirs"
    sys.exit(1)

  list = []
  for dir in args:
    list.extend(get_special_paths(dir))

  if not tozip and not todir:
    print '\n'.join(list)
  if todir:
    copy_to(list, todir)
  if tozip:
    zip_to(list, tozip)

  
if __name__ == "__main__":
  main()
