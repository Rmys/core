# -*- coding: utf-8 -*-

import os
import piksemel
import subprocess
import os

def updateInitrd(filepath):
    patterns = ("/lib/modules", "/usr/lib/initcpio", "/boot/kernel", "/bin/busybox")
    parse = piksemel.parse(filepath)
    for xmlfile in parse.tags("File"):
        path = xmlfile.getTagData("Path")
        if not path.startswith("/"):
            path = "/%s" % path
        if path.startswith(patterns):
            version = path.split("/")[3]
            os.environ['PATH'] = '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/opt/bin'
            subprocess.call(["mkinitcpio","-k","%s"% version ,"-g","/boot/initramfs-%s-fallback.img"% version,"-S","autodetect"])
            subprocess.call(["mkinitcpio","-k","%s"% version ,"-c","/etc/mkinitcpio.conf","-g","/boot/initramfs-%s.img"% version])
            if os.path.exists("/proc/cmdline"):
                os.system("/usr/bin/update-grub")
            break

def setupPackage(metapath, filepath):
    updateInitrd(filepath)

def cleanupPackage(metapath, filepath):
    pass

def postCleanupPackage(metapath, filepath):
    pass
