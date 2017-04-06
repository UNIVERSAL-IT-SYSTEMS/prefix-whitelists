import os
import sys
import portage
from portage.dbapi.porttree import portdbapi

portdir = os.path.realpath(sys.argv[1])
master = os.path.realpath(sys.argv[2])

env = {}
env["PORTAGE_REPOSITORIES"] = """
[gentoo]
location = %s

[prefix-tree]
location = %s
masters = gentoo

""" % (master, portdir)

settings = portage.config(env=env)

portdb = portdbapi(mysettings=settings)
portdb.porttrees = [portdir]

for package in portdb.cp_all():
	for ebuild in portdb.cp_list(package):
		for distfile in portdb.getFetchMap(ebuild):
			print(distfile)
