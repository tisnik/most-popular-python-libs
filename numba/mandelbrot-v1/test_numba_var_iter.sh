iterations="1 10 100 1000 10000 100000 1000000"

OUTFILE="python_3_8.times"
PREFIX="python_3_8"

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3.8 mandelbrot_python.py 256 256 $iter 255 > "${PREFIX}_${iter}.ppm"
done

OUTFILE="python_3_9.times"
PREFIX="python_3_9"

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3.9 mandelbrot_python.py 256 256 $iter 255 > "${PREFIX}_${iter}.ppm"
done

OUTFILE="python_3_10.times"
PREFIX="python_3_10"

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3.10 mandelbrot_python.py 256 256 $iter 255 > "${PREFIX}_${iter}.ppm"
done

OUTFILE="python_3_11.times"
PREFIX="python_3_11"

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3.11 mandelbrot_python.py 256 256 $iter 255 > "${PREFIX}_${iter}.ppm"
done

OUTFILE="python_3_12.times"
PREFIX="python_3_12"

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3.12 mandelbrot_python.py 256 256 $iter 255 > "${PREFIX}_${iter}.ppm"
done
