.PHONY:	docs
docs:	changes	## run Sphinx to build html pages
	cd rst && \
	sphinx-build -b html -d _build/doctrees . ../docs

.PHONY:	docs-clean
docs-clean:
		rm -rf rst/_build/doctrees

.PHONY: pdf
pdf:	## build PDF docs
	pip install . && \
	cd rst && \
	sphinx-build -b latex -d _build/doctrees . _build/latex && \
	cd _build/latex && \
	pdflatex pylit.tex && \
	cp pylit.pdf ../../../docs

