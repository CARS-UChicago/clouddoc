# Makefile for Sphinx documentation
#

SPHINXBUILD = sphinx-build
BUILDDIR    = _build
SPHINXOPTS  = -d $(BUILDDIR)/doctrees .
INSTALLDIR  = ../web/templates/doc

.PHONY: all html clean html install

all: html pdf

html:
	$(SPHINXBUILD) -b html $(SPHINXOPTS) $(BUILDDIR)/html

clean:
	-rm -rf $(BUILDDIR)/*

install: html
	cp -pr  $(BUILDDIR)/html/* $(INSTALLDIR)/.

latex:
	$(SPHINXBUILD) -a -b latex . $(BUILDDIR)/latex

pdf: latex
	cd $(BUILDDIR)/latex && make all-pdf
	cp -pr $(BUILDDIR)/latex/carsclouddata.pdf $(BUILDDIR)/html/carscloud.pdf

clean:
	-rm -rf $(BUILDDIR)/*
