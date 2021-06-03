.PHONY: all
all: notes.pdf slides.pdf

LATEXFLAGS+=	-shell-escape

SRC+=		preamble.tex
SRC+=		abstract.tex contents.tex

FIGS+=		fig/part-whole.tikz
FIGS+=		contrast-color.tikz
FIGS+=		generalization-color.tikz
FIGS+=		fusion-color.tikz
FIGS+=		maja-writing.jpg
FIGS+=		part-whole.tikz

DEPENDS+=	bibedu.bib bibedu.sty ${FIGS}

notes.pdf: notes.tex
notes.pdf: ${SRC} ${DEPENDS}

slides.pdf: slides.tex
slides.pdf: ${SRC} ${DEPENDS}


.PHONY: clean
clean:
	${RM} notes.pdf slides.pdf


INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/tex.mk
INCLUDE_BIBEDU=../bibedu
include ${INCLUDE_BIBEDU}/bibedu.mk
