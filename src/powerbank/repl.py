from typing import TextIO

base_print = print


def print(
    *values: object,
    file: TextIO | str | None = None,
    **kwargs
) -> None:
    if isinstance(file, str):
        with open(file, "w") as fd:
            base_print(*values, **kwargs, file=fd)
    else:
        base_print(*values, **kwargs, file=file)


def lines(*args, **kwargs):
    with open(*args, **kwargs) as fd:
        return list(fd)

# https://fr.wikipedia.org/wiki/S%C3%A9quence_d%27%C3%A9chappement_ANSI
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797


def rewind():
    base_print("\r\033[K", end='', flush=True)
