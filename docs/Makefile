# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

repos:
	mkdir -p "$(SOURCEDIR)/_repos"
	cd "$(SOURCEDIR)/_repos" \
	&& rm -fr * \
	&& git clone git@github.com:7wmr/sphinx-demo-child-1.git \
	&& git clone git@github.com:7wmr/sphinx-demo-child-2.git

html:
	rm -fr "$(BUILDDIR)/html"
	@$(SPHINXBUILD) -M html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

conf:
	@$(SPHINXBUILD) -b confluence "$(SOURCEDIR)" "$(BUILDDIR)/confluence" -E -a -v

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
