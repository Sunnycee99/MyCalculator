def get_input():
    with open("input.txt") as f:
        res = f.read()
    return res


def get_output(res):
    with open("res.txt", "w") as f:
        f.write(res)
