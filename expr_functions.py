from inspect import getmembers, isclass
import random
import none_input_expr
import one_output_expr
import multi_output_expr

end_operators = [op[1] for op in getmembers(none_input_expr, isclass)]
norm_operators = [op[1] for module in [one_output_expr, multi_output_expr]
                  for op in getmembers(module, isclass)]


def build_expr(prob: float):
    if random.random() < prob:
        return random.choice(norm_operators)(prob)
    else:
        return random.choice(end_operators)()


def string_to_expr():
    raise NotImplemented
