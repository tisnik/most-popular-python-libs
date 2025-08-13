typedef struct {
    unsigned int width;
    unsigned int height;
    unsigned char *pixels;
} image_t;

typedef struct {
    unsigned int maxiter;
    double cx;
    double cy;
} rendering_params_t;
