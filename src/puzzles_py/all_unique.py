def all_unique_1(word: str) -> bool:
    for i, ch in enumerate(word):
        if word.index(ch) != i:
            return False
    return True


def all_unique_2(word: str) -> bool:
    for ch in word:
        if len(word.replace(ch, "")) < len(word) - 1:
            return False
    return True


if __name__ == "__main__":

    assert all_unique_1("Cassidy") is False
    assert all_unique_1("cat & dog") is False
    assert all_unique_1("cat+dog") is True

    assert all_unique_2("Cassidy") is False
    assert all_unique_2("cat & dog") is False
    assert all_unique_2("cat+dog") is True
