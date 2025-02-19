#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import shelltools

def build():
    shelltools.export("KCONFIG_NOTIMESTAMP", "1")
    autotools.make()

def install():
    pisitools.insinto("/usr/lib/initcpio", "busybox")
