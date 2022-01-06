from PIL import Image
from numpy import arange, log
from itertools import product

# The colouring algorithm we derived
def colouringAlgo(iteration: int, iterations: int, z: complex) -> float:
    global n
    try:
        colour = iteration - log(log(abs(z)) / log(iterations)) / log(n)
        return (min(254, colour), iteration)
    except RuntimeWarning:
        return (254, iteration)


# The function we will be applying
def multibrot(c: complex, bound = 2, iterations = 100) -> float:
    global n

    R       = max(abs(c), 2)
    z, i    = 0, 0

    while i < iterations:

        if (abs(z) > R):
            return colouringAlgo(i, iterations, z)

        try:
            z = pow(z, n) + c
        except ZeroDivisionError:
            return (0, i)
        i += 1

    return colouringAlgo(i, iterations, z)

print("Generating Grid")
grid = 0.01
im = arange(-2, 2, grid)
re = arange(-2, 2, grid)

# Compute the points



# for n in arange(2, 3.2, 0.2):
n = 42
print(f'Creating canvas for {n}')
complexPlane = map(lambda a: complex(a[0],a[1]), product(re,im))
image = Image.new("RGB", (len(re), len(im)), "white")
pixels = image.load()

print(f'Computing points for {n}')
multibrotSet = list(map(multibrot, complexPlane))

print("Drawing on canvas")
imag = len(im)
for x, y in product(range(len(re)), range(imag)):
    colour, iterations = multibrotSet[x * imag + y]
    formattedColour = int(20 * colour)
    pixels[x, y] = (formattedColour, 2 * iterations, formattedColour)

print("Opening Image")
image.save(f'multibrot{n}Coloured.png')
# image.show()
