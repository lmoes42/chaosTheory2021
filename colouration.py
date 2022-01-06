from PIL import Image
from numpy import arange, log
from itertools import product

# The colouring algorithm we derived
def colouringAlgo(iteration: int, iterations: int, z: complex) -> float:
    try:
        colour = iteration - log(log(abs(z)) / log(iterations)) / log(2)
        return (min(254, colour), iteration)
    except RuntimeWarning:
        return (254, iteration)


# The function we will be applying
def mandelbrot(c: complex, bound = 2, iterations = 100) -> float:

    R       = max(abs(c), 2)
    z, i    = 0, 0

    while i < iterations:

        if (abs(z) > R):
            return colouringAlgo(i, iterations, z)

        z = pow(z, 2) + c
        i += 1

    return colouringAlgo(i, iterations, z)

print("Generating Grid")
grid = 0.000005
im = arange(0.03, 0.035, grid)
re = arange(-0.752,-0.748, grid)

# Compute the points
complexPlane = map(lambda a: complex(a[0],a[1]), product(re,im))

print("Creating canvas")
image = Image.new("RGB", (len(re), len(im)), "white")
pixels = image.load()

print("Computing points")
mandelbrotSet = list(map(mandelbrot, complexPlane))

print("Drawing on canvas")
imag = len(im)
for x, y in product(range(len(re)), range(imag)):
    colour, iterations = mandelbrotSet[x * imag + y]
    formattedColour = int(20 * colour)
    pixels[x, y] = (formattedColour, 2 * iterations, formattedColour)

print("Opening Image")
image.save(f'ZoomedMandelbrotColoured2.png')
image.show()
