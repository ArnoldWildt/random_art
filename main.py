import argparse
import time

from expr_functions import build_expr
from files import *
from image_plot import ImageGenerator
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def creat_images_list(file_path, num, prob):
    image_list = []

    if file_path:
        expr_file = read_file(file_path)
        for i in range(int(len(expr_file) / 3)):
            image_list.append(expr_file[:3])
            expr_file = expr_file[3:]
        return image_list

    for i in range(num):
        red_expr = build_expr(prob)
        green_expr = build_expr(prob)
        blue_expr = build_expr(prob)
        image_list.append([red_expr, green_expr, blue_expr])
        save_expr_file(image_list)
    return image_list


def build_img(image_expr, size, num):
    image_time = time.time()
    red_expr, green_expr, blue_expr = image_expr
    image = ImageGenerator().plot_image(
        red_expr, green_expr, blue_expr, size)
    image.save(f"./images/image{num}.png")

    image_time = round(time.time() - image_time, 2)
    print(f"image{num}.png created! It took {image_time} secs")


def build_img_(args):
    return build_img(*args)


def create_images(num=50, prob=0.99, size=150, file_path=None):
    start_time = time.time()
    image_list = creat_images_list(file_path, num, prob)

    # Combine image_expr ,size and image_number
    # to use it with ProcessPoolExecutor
    args_list = list(
        map(lambda img: (img, size, image_list.index(img)), image_list))

    with ProcessPoolExecutor() as exe:
        exe.map(build_img_, args_list)

    total_time = round(time.time() - start_time, 2)
    print(f"Done created {num} images! It took {total_time} secs")


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
