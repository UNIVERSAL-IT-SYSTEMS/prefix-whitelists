import os
import sys
import portage
from portage.dbapi.porttree import portdbapi

portdir = os.path.realpath(sys.argv[1])

env = {}
env["PORTAGE_REPOSITORIES"] = """
[gentoo_prefix]
location = %s

""" % portdir

settings = portage.config(env=env)

portdb = portdbapi(mysettings=settings)
portdb.porttrees = [portdir]

for i in range(2, len(sys.argv)):
	for ebuild in portdb.cp_list(sys.argv[i]):
		for distfile in portdb.getFetchMap(ebuild):
			print(distfile)
