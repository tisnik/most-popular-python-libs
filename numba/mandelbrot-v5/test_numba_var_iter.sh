iterations="1 10 100 1000 10000 100000"

OUTFILE="numba5.times"
PREFIX="numba5"

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3 mandelbrot_python.py 256 256 $iter 255 > "${PREFIX}_${iter}.ppm"
done
