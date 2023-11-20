iterations="1 10 100 1000 10000 100000 1000000"

OUTFILE="native.times"
PREFIX="native"

gcc mandelbrot.c -o mandelbrot

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" ./mandelbrot 256 256 $iter > "${PREFIX}_${iter}.ppm"
done

OUTFILE="native_optim.times"
PREFIX="native_optim"

gcc -Ofast mandelbrot.c -o mandelbrot

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" ./mandelbrot 256 256 $iter > "${PREFIX}_${iter}.ppm"
done
