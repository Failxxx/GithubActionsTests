# Minimal makefile for Sphinx documentation

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).

# Comment '@persistent' decorator because fake-bpy-module defines it at 'None', which is not callable and causes errors during 'sphinx-build'
%: Makefile
	find ../addon/ -type f -name "*.py" -exec sed -i 's/@persistent/#@persistent/g' {} +
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	find ../addon/ -type f -name "*.py" -exec sed -i 's/#@persistent/@persistent/g' {} +
