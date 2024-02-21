void render_test_rgb_image(unsigned int width, unsigned int height,
                           unsigned char *pixels, unsigned char green) {
    unsigned int i, j;
    unsigned char *p = pixels;

    for (j = 0; j < height; j++) {
        for (i = 0; i < width; i++) {
            *p++ = i;
            *p++ = green;
            *p++ = j;
            p++;
        }
    }
}

void render_test_palette_image(unsigned int width, unsigned int height,
                               const unsigned char *palette,
                               unsigned char *pixels) {
    unsigned int i, j;
    unsigned char *p = pixels;

    for (j = 0; j < height; j++) {
        for (i = 0; i < width; i++) {
            int color = i * 3;
            *p++ = palette[color];
            *p++ = palette[color + 1];
            *p++ = palette[color + 2];
            p++;
        }
    }
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
            {
                int r = i * 2;
                int g = i * 3;
                int b = i * 5;

                *p++ = r;
                *p++ = g;
                *p++ = b;
                p++;
            }
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
            {
                int r = i * 2;
                int g = i * 3;
                int b = i * 5;

                *p++ = r;
                *p++ = g;
                *p++ = b;
                p++;
            }
            zx0 += (xmax - xmin) / width;
        }
        zy0 += (ymax - ymin) / height;
    }
}
