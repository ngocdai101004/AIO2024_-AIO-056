def precision(tp, fp):
    return tp / (tp + fp)


def recall(tp, fn):
    return tp / (tp + fn)


def f1_score(tp, fp, fn):
    pre = precision(tp, fp)
    rec = recall(tp, fn)
    return 2*(pre * rec) / (pre + rec)


def evaluate_clasification(tp, fp, fn):
    if not isinstance(tp, int):
        print("tp must be int")
        return False

    if not isinstance(fp, int):
        print("fp must be int")
        return False

    if not isinstance(fn, int):
        print("fn must be int")
        return False

    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp and fp and fn must begreater than zero")
        return False

    pre = precision(tp, fp)
    rec = recall(tp, fn)
    f1 = f1_score(tp, fp, fn)

    print(f"Precision is {pre}")
    print(f"Recall is {rec}")
    print(f"F1-Score is {f1}")

    return True


if __name__ == "__main__":
    a = evaluate_clasification(tp=91, fp=9, fn=70)
