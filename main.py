from typing import Iterator

from sympy import symbols, diff, sin, cos, log, sqrt, pi


def frange(start: float, end: float, step: float) -> Iterator[float]:
    while start <= end:
        yield start
        start += step


def task1() -> None:
    print("Завдання 1")

    delta_x = 0.01
    delta_y = 0.05

    x, y = symbols("x y", real=True)
    f = sin(x ** 2 + y) + log(x) + y
    df_dx = diff(f, x)
    df_dy = diff(f, y)

    df = sqrt((df_dx * delta_x) ** 2 + (df_dy * delta_y) ** 2)
    rf = df / f

    print(f"Аналітичний вираз для абсолютної похибки: {df}")
    print(f"Аналітичний вираз для відносної похибки: {rf}")

    for ex in frange(1 - delta_x, 1 + delta_x, delta_x):
        for ey in frange(2 - delta_y, 2 + delta_y, delta_y):
            print(
                f"f({ex:.2f}, {ey:.2f}): "
                f"df = {df.evalf(subs={x: ex, y: ey}):.5f}, "
                f"rf = {rf.evalf(subs={x: ex, y: ey}):.5f}"
            )


def task2() -> None:
    print("Завдання 2")

    delta_x = 0.02
    delta_y = 0.05

    x, y = symbols("x y", real=True)
    f = cos(y ** 2 + 1) + log(x ** 2 * y) + x
    df_dx = diff(f, x)
    df_dy = diff(f, y)

    df = sqrt((df_dx * delta_x) ** 2 + (df_dy * delta_y) ** 2)
    rf = df / f

    print(f"Аналітичний вираз для абсолютної похибки: {df}")
    print(f"Аналітичний вираз для відносної похибки: {rf}")

    for ex in frange(1 - delta_x, 1 + delta_x, delta_x):
        for ey in frange(2 - delta_y, 2 + delta_y, delta_y):
            print(
                f"f({ex:.2f}, {ey:.2f}): "
                f"df = {df.evalf(subs={x: ex, y: ey}):.5f}, "
                f"rf = {rf.evalf(subs={x: ex, y: ey}):.5f}"
            )


def task3() -> None:
    print("Завдання 3")

    value_R = 2
    value_H = 3
    percent_delta_V = 0.1

    R, H = symbols("R H", real=True)

    V = pi * R ** 2 * H
    value_delta_V = (percent_delta_V * V).evalf(subs={R: value_R, H: value_H})

    dVdR = diff(V, R)
    dVdH = diff(V, H)

    delta_R = value_delta_V / (2 * dVdR)
    delta_H = value_delta_V / (2 * dVdH)

    value_delta_R = delta_R.evalf(subs={R: value_R, H: value_H})
    value_delta_H = delta_H.evalf(subs={R: value_R, H: value_H})

    print(f"Абсолютна похибка вимірювання радіуса: {value_delta_R:.5f} м")
    print(f"Абсолютна похибка вимірювання висоти: {value_delta_H:.5f} м")

    normal_V = V.evalf(subs={R: value_R, H: value_H})
    err_normal_V = V.evalf(subs={R: value_R - value_delta_R, H: value_H - value_delta_H})
    err = abs(err_normal_V / normal_V - 1)

    print("Перевірка:")
    print(f"V = {normal_V:.3f}")
    print(f"Verr = {err_normal_V:.3f}")
    print(f"Похибка: {err:.2f}")


def main() -> None:
    task1()
    print()

    task2()
    print()

    task3()


if __name__ == '__main__':
    main()
