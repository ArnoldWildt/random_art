import argparse
from expr_functions import build_expr
from image_plot import plot_image
import time


# red_expr = build_expr(.97)
# green_expr = build_expr(.97)
# blue_expr = build_expr(.97)
# print("red = " + str(red_expr))
# print("green = " + str(green_expr))
# print("blue = " + str(blue_expr))
# image = plot_image(red_expr, green_expr, blue_expr, 100)

# red_str = "math.sin(math.pi * quotient(pow(parabola(avg(0.17950211560429652, y * math.pi) * math.pi)), -1))"
# green_str = "(sqrt(pow(math.sin(0))) * -1)"
# blue_str = "parabola(mix(parabola(dip(y)), quotient(modulo(0, 1), dip(quotient(1, 0))), sqrt(level(1, quotient(mix(1 * math.pi, y, x), avg(0.3458170417828812, 0.1633586385516358)), level(0, 0.546544911177rred_expr, 0.23597017071203397), 0.5231512601863461)green_exprx = "math.sin(math.pi * math.sin(math.pi *blue_exprin(math.pi * (math.sin(math.pi * math.sin(math.pi * math.sin(math.pi * math.sin(math.pi * math.blue_canvasi * y))))) * math.cos(math.pi * math.sin(math.pi * math.cos(math.pi * avg(math.sin(math.pi * y), (x * x)))))))))"
x = "math.sin(math.pi * math.sin(math.pi * math.sin(math.pi * (math.sin(math.pi * math.sin(math.pi * math.sin(math.pi * math.sin(math.pi * math.cos(math.pi * y))))) * math.cos(math.pi * math.sin(math.pi * math.cos(math.pi * avg(math.sin(math.pi * y), (x * x)))))))))"
start = time.time()
image = plot_image(x, x, x, 300, is_str=True)
print(f"Took {time.time() - start}s")
# image = plot_image(red_str, green_str, blue_str, 300, is_str=True)

image.show()

if __name__ == "__main__":
    pass
