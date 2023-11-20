iterations="1 10 100 1000 10000 100000 1000000"

OUTFILE="mypyc_no_type_hints.times"
PREFIX="mypyc_no_type_hints"

rm $OUTFILE

for iter in $iterations
do
    echo $iter
    echo -n "$iter " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3 -c "import mandelbrot_5" 256 256 $iter > "${PREFIX}_${iter}.ppm"
done
