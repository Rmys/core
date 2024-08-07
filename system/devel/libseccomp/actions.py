#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools, get

def setup():
    autotools.configure("PYTHON=python3")

def build():
    autotools.make()

def check():
    autotools.make("check")

def install():
     autotools.rawInstall("DESTDIR=%s" % get.installDIR())
