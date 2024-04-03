

def func(x_1, x_2):
    return 3*x_1*x_2 - x_1**2*x_2 - x_1*x_2
    # return 2*x_1 + 4*x_2 - x_1**2 - 2*x_2**2

def diff_func(x_1, x_2):
    df_dx1 = 3*x_2 - 2*x_1*x_2 - x_2**2
    df_dx2 = 3*x_1 - x_1**2 - 2*x_1*x_2
    # df_dx1 = 2 - 2*x_1
    # df_dx2 = 4 - 4*x_2
    return df_dx1, df_dx2

def gradient_descent_method():
    e = 0.05
    lambda_val = 0.25
    x_1, x_2 = 2, 0
    df_dx1, df_dx2 = diff_func(x_1, x_2)
    print(f'Δf = ({df_dx1}; {df_dx2})')
    f_x0 = func(x_1, x_2)
    print(f'f(x) = {f_x0}')
    f_x = f_x0+2*e
    while abs(f_x - f_x0) > e:
        f_x0 = f_x
        x_1 = x_1 + lambda_val*df_dx1
        x_2 = x_2 + lambda_val*df_dx2
        print(f'x = ({x_1}; {x_2})')
        df_dx1, df_dx2 = diff_func(x_1, x_2)
        print(f'Δf = ({df_dx1}; {df_dx2})')
        f_x = func(x_1, x_2)
        print(f'f(x) = {f_x}')
    print('Итог:')
    print(f'x* =({x_1}; {x_2})')
    print(f'fmax = {f_x}')









gradient_descent_method()