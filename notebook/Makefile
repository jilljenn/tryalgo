all::
	python make_notebook.py  --image-height 15mm --images figures ../tryalgo/
	typst compile notebook.typ
	pdfinfo notebook.pdf 2>/dev/null | grep Pages
