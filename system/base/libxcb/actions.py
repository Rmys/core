# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    pisitools.flags.add("-DNDEBUG")

    autotools.autoreconf("-vfi")
    options = " --disable-static \
                         --enable-xevie \
                         --enable-xprint \
                         --enable-xinput \
                         --enable-xkb \
                         --without-launchd \
                         --without-doxygen"
    
    if get.buildTYPE() == "emul32":
        options += " --libdir=/usr/lib32"
                         
    autotools.configure(options)

    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make("-j1")

def install():
    autotools.rawInstall("-j1 DESTDIR=%s" % get.installDIR())
    
    if get.buildTYPE() == "emul32":
        return

    pisitools.dodoc("COPYING", "NEWS", "README*")
