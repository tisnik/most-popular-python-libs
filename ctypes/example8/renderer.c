void putpixel(unsigned char **pixel, const unsigned char *palette,
              int color_index) {
    int color_offset = color_index * 3;
    unsigned char *pal = (unsigned char *)(palette + color_offset);

    *(*pixel)++ = *pal++;
    *(*pixel)++ = *pal++;
    *(*pixel)++ = *pal;
    (*pixel)++;
}

void render_mandelbrot(unsigned int width, unsigned int height,
                       const unsigned char *palette, unsigned char *pixels) {
    int x, y;
    double cx, cy;
    double xmin = -2.0, ymin = -1.5, xmax = 1.0, ymax = 1.5;
    unsigned char *p = pixels;

    cy = ymin;
    for (y = 0; y < height; y++) {
        cx = xmin;
        for (x = 0; x < width; x++) {
            double zx = 0.0;
            double zy = 0.0;
            unsigned int i = 0;
            while (i < 150) {
                double zx2 = zx * zx;
                double zy2 = zy * zy;
                if (zx2 + zy2 > 4.0) {
                    break;
                }
                zy = 2.0 * zx * zy + cy;
                zx = zx2 - zy2 + cx;
                i++;
            }
            putpixel(&p, palette, i);
            cx += (xmax - xmin) / width;
        }
        cy += (ymax - ymin) / height;
    }
}

void render_julia(unsigned int width, unsigned int height,
                  const unsigned char *palette, unsigned char *pixels,
                  double cx, double cy) {
    int x, y;
    double zx0, zy0;
    double xmin = -1.5, ymin = -1.5, xmax = 1.5, ymax = 1.5;
    unsigned char *p = pixels;

    zy0 = ymin;
    for (y = 0; y < height; y++) {
        zx0 = xmin;
        for (x = 0; x < width; x++) {
            double zx = zx0;
            double zy = zy0;
            unsigned int i = 0;
            while (i < 150) {
                double zx2 = zx * zx;
                double zy2 = zy * zy;
                if (zx2 + zy2 > 4.0) {
                    break;
                }
                zy = 2.0 * zx * zy + cy;
                zx = zx2 - zy2 + cx;
                i++;
            }
            putpixel(&p, palette, i);
            zx0 += (xmax - xmin) / width;
        }
        zy0 += (ymax - ymin) / height;
    }
}
