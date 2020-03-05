#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse

# This is to help coaches and graders identify student assignments
__author__ = "jsinghw"


# Write functions and modify main() to call them
def get_special_paths(_dir):
    paths = []
    special = []
    reg = re.compile(r'.+(__).+(__).+')
    for i in range(0, len(_dir)):
        matched = reg.match(_dir[i])
        if matched:
            special.append(_dir[i])
    for i in range(0, len(special)):
        paths.append((os.path.abspath(special[i])))
    return(paths)


def copy_to(paths, _dir):
    if os.path.exists(_dir) is False:
        os.makedirs(_dir)
    for i in range(0, len(paths)):
        shutil.copy2(os.path.abspath(paths[i]), os.path.abspath(_dir))


def file_to(paths, zippath):
    print("Command I'm going to do:")
    command = "zip -j " + zippath + " " + " ".join(paths)
    print(command)
    try:
        for i in range(0, len(paths)):
            subprocess.call(["zip", "-j", zippath, paths[i]])
    except subprocess.CalledProcessError:
        print("zip error: Could not create output file " + zippath)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('from_dir', help='starting dir')
    args = parser.parse_args()

    special = get_special_paths(os.listdir(args.from_dir))

    if args.todir:
        copy_to(special, args.todir)
    elif args.tozip:
        file_to(special, args.tozip)
    else:
        print(special)


if __name__ == "__main__":
    main()
