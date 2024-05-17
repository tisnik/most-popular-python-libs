PYTHON=python3
COMPILER=gcc
LINKER=gcc

CFLAGS=-O9

INCLUDE_DIR:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc())")
LIBRARY_DIR:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
PYTHON_LIB:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBRARY')[3:-2])")
SYSLIBS:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('SYSLIBS'))")


all:	add_numbers_1 \
	add_numbers_2 \
	add_numbers_3 \
	add_numbers_4 \
	add_numbers_5 \
	add_numbers_7


.PHONY:	clean

# Výsledky překladu do C chceme ponechat i po doběhnutí Make
.PRECIOUS: %.c

clean:
	rm -f *.o \
	rm -f *.c \
	rm -f add_numbers_[1-7]


# Pravidlo pro slinkovani vsech objektovych souboru a vytvoreni
# vysledne spustitelne aplikace.
%:	%.o
	$(LINKER) -o $@ -L$(LIBRARY_DIR) -l$(PYTHON_LIB) $(SYSLIBS) $<


# Pravidlo pro preklad kazdeho zdrojoveho souboru v C do prislusneho
# objektoveho souboru.
%.o:	%.c
	$(COMPILER) $(CFLAGS) -I$(INCLUDE_DIR) -c $< -o $@


# Pravidlo pro preklad kazdeho zdrojoveho souboru v Pythonu nebo Cythonu
# do prislusneho souboru C
%.c:	%.py
	cython -a --embed $<

%.c:	%.pyx
	cython -a --embed $<
