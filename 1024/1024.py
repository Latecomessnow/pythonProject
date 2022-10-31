def calculate_res(nums, ops):
    try:
        r1 = my_op(nums[0], nums[1], ops[0])
        r2 = my_op(r1, nums[2], ops[1])
        r3 = my_op(r2, nums[3], ops[2])
    except ZeroDivisionError:
        return 0
    return r3


def my_op(x, y, op):
    if op == '+':
        return x + y
    elif op == '-':
        return x - y
    elif op == '*':
        return x * y
    elif op == '/':
        try:
            return x // y
        except ZeroDivisionError:
            raise ZeroDivisionError
    elif op == '**':
        try:
            return int(x ** y)
        except ZeroDivisionError:
            raise ZeroDivisionError
    elif op == '&':
        return x & y
    elif op == '|':
        return x | y
    elif op == '^':
        return x ^ y
    elif op == '>>':
        return x >> y
    elif op == '<<':
        return x << y


if __name__ == '__main__':
    nums = [0,955,7,2,16,6,4,5,2,13,7,2,31,1,2,4,6,2,2,2,0]  # 填拥有的数字卡
    ops = [">>", "^", "&", "&", "^", "*"]  # 请填入拥有的符号卡

    from itertools import permutations

    for n_perm in permutations(nums, 4):
        for o_perm in permutations(ops, 3):
            res = calculate_res(n_perm, o_perm)
            if res == 1024:
                print(n_perm, o_perm)



