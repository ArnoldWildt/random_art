import argparse
from datetime import date
import time
from expr_functions import build_expr
from image_plot import plot_image


def save_expr_file(saved_strings):
    with open(f"Expr_strings_{date.today()}.txt", "w") as save_file:
        for i, saved_string in enumerate(saved_strings):
            r, g, b = saved_string
            img_seg = f"image{i}\nred: {r}\ngreen: {g}\nblue: {b}\n\n"
            save_file.writelines(img_seg)


def read_file(path):
    with open(path) as expr_file:
        lines = expr_file.readlines()

    # Filters Lines with image and blank out
    def filter_func(x):
        return True if not x == "\n" and "image" not in x else False
    lines = list(filter(filter_func, lines))

    # Removes "red: ", "green: ", "blue: " from the start of the line
    txts_dict = {"r": 5, "g": 7, "b": 6}
    for i, line in enumerate(lines):
        lines[i] = line[txts_dict[line[0]]:]

    return lines


def create_images(num=50, prob=0.99, size=150, file_path=None):
    is_file = False

    if file_path:
        is_file = True
        expr_file = read_file(file_path)

    saved_strings = []

    start_time = time.time()

    for i in range(num):
        image_time = time.time()

        if file_path:
            red_expr, green_expr, blue_expr = expr_file[:3]
        else:
            red_expr = build_expr(prob)
            green_expr = build_expr(prob)
            blue_expr = build_expr(prob)

        image = plot_image(red_expr, green_expr, blue_expr, size, is_file)
        image.save(f"./images/image{i}.png")
        saved_strings.append([red_expr, green_expr, blue_expr])

        image_time = round(time.time() - image_time, 2)
        print(f"image{i}.png created! It took {image_time} secs")

    total_time = round(time.time() - start_time, 2)
    print(f"Done created {num} images! It took {total_time} secs")

    save_expr_file(saved_strings)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Creates random art")
    parser.add_argument("--num", metavar="Number of images",
                        type=int, default=50)
    parser.add_argument("--prob", metavar="Probability",
                        type=float, default=0.99)
    parser.add_argument("--size", metavar="Size of image",
                        type=int, default=150)
    parser.add_argument("--path", metavar="Expression file path", type=str)
    args = parser.parse_args()

    create_images(*vars(args).values())
