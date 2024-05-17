PYTHON=python3
COMPILER=gcc
LINKER=gcc

# GCCOPTIONS=-O9 -ffast-math
CCOPTIONS=-O9

INCLUDE_DIR:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_python_inc())")
LIBRARY_DIR:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBDIR'))")
PYTHON_LIB:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('LIBRARY')[3:-2])")
SYSLIBS:=$(shell $(PYTHON) -c "from distutils import sysconfig; print(sysconfig.get_config_var('SYSLIBS'))")


all: mandelbrot_cython

mandelbrot_cython: mandelbrot_cython.o
	$(LINKER) -o $@ $^ -L$(LIBRARY_DIR) -l$(PYTHON_LIB) $(SYSLIBS)

mandelbrot_cython.o: mandelbrot_cython.c
	$(COMPILER) $(CCOPTIONS) -I$(INCLUDE_DIR) -c $<

mandelbrot_cython.c: mandelbrot_cython.py
	cython --embed $<

clean:
	rm -f mandelbrot_cython
	rm -f mandelbrot_cython.c
	rm -f mandelbrot_cython.o
