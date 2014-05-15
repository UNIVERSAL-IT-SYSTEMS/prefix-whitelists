import os
import sys

portdir = os.path.realpath(sys.argv[1])
configroot = os.path.realpath(sys.argv[2])

os.environ["PORTAGE_CONFIGROOT"] = configroot
os.environ["PORTAGE_REPOSITORIES"] = """
[gentoo_prefix]
location = %s

""" % portdir
os.environ["EPREFIX"] = configroot

import _emerge.actions
import _emerge.depgraph
import _emerge.create_depgraph_params


emerge_config = _emerge.actions.load_emerge_config()

opts = {'--pretend': True, '--emptytree': True, '--root-deps': True}
params = _emerge.create_depgraph_params.create_depgraph_params(opts, None)

success, mydepgraph, favorites = _emerge.depgraph.backtrack_depgraph(emerge_config.target_config.settings, emerge_config.trees, opts, params, None, ['@system'], None)

for item in mydepgraph._dynamic_config.digraph.all_nodes():
	if isinstance(item, _emerge.Package.Package):
		print(item.cp)
