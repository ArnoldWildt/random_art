from datetime import date


def save_expr_file(saved_strings):
    with open(f"./expressions/Expr_strings_{date.today()}.txt", "w") as save_file:
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
