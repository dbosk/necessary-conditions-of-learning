SUBDIR+=	overview
SUBDIR+=	disposition
SUBDIR+=	ch1
SUBDIR+=	ch2
SUBDIR+=	ch3

# TOC: 8-10
# Ref: 300-315

.PHONY: chapters
chapters: NCOL-ch1.pdf
chapters: NCOL-ch2.pdf
chapters: NCOL-ch3.pdf
chapters: NCOL-ch4.pdf
chapters: NCOL-ch5.pdf
chapters: NCOL-ch6.pdf
chapters: NCOL-ch7.pdf

NCOL-ch1.pdf: NCOL-full.pdf
	pdfjam $< 18-36,300-315 -o $@

NCOL-ch2.pdf: NCOL-full.pdf
	pdfjam $< 37-55,300-315 -o $@

NCOL-ch3.pdf: NCOL-full.pdf
	pdfjam $< 56-98,300-315 -o $@

NCOL-ch4.pdf: NCOL-full.pdf
	pdfjam $< 99-144,300-315 -o $@

NCOL-ch5.pdf: NCOL-full.pdf
	pdfjam $< 145-180,300-315 -o $@

NCOL-ch6.pdf: NCOL-full.pdf
	pdfjam $< 181-271,300-315 -o $@

NCOL-ch7.pdf: NCOL-full.pdf
	pdfjam $< 272-299,300-315 -o $@

.PHONY: clean
clean:
	${RM} NCOL-ch1.pdf
	${RM} NCOL-ch2.pdf
	${RM} NCOL-ch3.pdf
	${RM} NCOL-ch4.pdf
	${RM} NCOL-ch5.pdf
	${RM} NCOL-ch6.pdf
	${RM} NCOL-ch7.pdf

INCLUDE_MAKEFILES=../makefiles
include ${INCLUDE_MAKEFILES}/subdir.mk
