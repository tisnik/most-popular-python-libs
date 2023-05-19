sizes="16 24 32 48 64 96 128 192 256 384 512 768 1024 1536 2048 3072 4096"

OUTFILE="numba1.times"
PREFIX="numba1"

rm $OUTFILE

for size in $sizes
do
    echo $size
    echo -n "$size " >> $OUTFILE
    /usr/bin/time --output $OUTFILE --append --format "%e %M" python3 mandelbrot_python.py $size $size 255 > "${PREFIX}_${size}_${size}.ppm"
done
