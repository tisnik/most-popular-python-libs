#include <stdlib.h>

typedef struct {
    unsigned int width;
    unsigned int height;
} image_size_t;

typedef struct {
    unsigned int maxiter;
    double cx;
    double cy;
} rendering_params_t;


void render_mandelbrot(image_size_t *image_size,
                       const unsigned char *palette, unsigned char *pixels,
                       rendering_params_t *rendering_params) {
    free(image_size);
    free(rendering_params);
}

void render_julia(image_size_t *image_size,
                  const unsigned char *palette, unsigned char *pixels,
                  rendering_params_t *rendering_params) {
    free(image_size);
    free(rendering_params);
}
