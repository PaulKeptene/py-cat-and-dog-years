from typing import Any


def get_human_age(cat_age: int, dog_age: int) -> list:
    list_with_ages: list[Any] = []

    if cat_age < 15:
        list_with_ages.append(0)
    elif cat_age < 24:
        list_with_ages.append(1)
    else:
        list_with_ages.append(2 + ((cat_age - 24) // 4))

    if dog_age < 15:
        list_with_ages.append(0)
    elif dog_age < 24:
        list_with_ages.append(1)
    else:
        list_with_ages.append(2 + ((dog_age - 24) // 5))

    return list_with_ages
