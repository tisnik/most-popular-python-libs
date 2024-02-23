#include <stdint.h>

void render_test_rgb_image(unsigned int width, unsigned int height,
                           uint32_t *pixels, unsigned char green) {
    unsigned int i, j;
    unsigned int *p = pixels;

    for (j = 0; j < height; j++) {
        for (i = 0; i < width; i++) {
            unsigned int color = (i << 16) + (green << 8) + j;
            *p++ = color;
        }
    }
}
