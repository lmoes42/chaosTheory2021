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
def julia(z: complex, bound = 2, iterations = 100) -> float:
    R = max(abs(z), 2)
    i = 0
    while i < iterations:
        if (abs(z) > R):
            return colouringAlgo(i, iterations, z)
        try:
            z = (3 * pow(z,2) - 1) / (5 * pow(z,3) - 3 * z)
        except ZeroDivisionError:
            return 100
        i += 1
    return colouringAlgo(i, iterations, z)

print("Generating Grid")
grid = 0.01
im = arange(-2, 2, grid)
re = arange(-4, 1.5, grid)

# Compute the points
complexPlane = map(lambda a: complex(a[0],a[1]), product(re,im))

print("Creating canvas")
image = Image.new("RGB", (len(re), len(im)), "white")
pixels = image.load()

print("Computing points")
juliaSet = list(map(julia, complexPlane))

print("Drawing on canvas")
imag = len(im)
for x, y in product(range(len(re)), range(imag)):
    colour, iterations = juliaSet[x * imag + y]
    formattedColour = int(20 * abs(colour))
    pixels[x, y] = (formattedColour, 2 * iterations, formattedColour)

print("Opening Image")
image.save(f'juliaColoured1.png')
image.show()
