"""Delivery service."""


def calculate_platforms_needed(mass_robots: list[int], limit: int,
                               id_parcel: str):
    """Метод определения минимального количества платформ."""
    sorted_mass_robots: list[int] = sorted(mass_robots)
    index_left: int = 0
    index_right: int = len(mass_robots) - 1
    result: int = 0
    """Условие выполнения задачи."""
    while index_left <= index_right:
        if (sorted_mass_robots[index_left] +
           sorted_mass_robots[index_right]) <= limit:
            index_left = index_left + 1
        index_right = index_right - 1
        result = result + 1
        if index_left == index_right:
            result = result + 1
            break

    print(f"Обработка посылки с ID: {id_parcel}")
    return result


if __name__ == '__main__':
    weights_robots = [int(i) for i in input().split()]
    limit_mass = int(input())
    package_id = input("Введите ID посылки: ")
    print(calculate_platforms_needed(weights_robots, limit_mass, package_id))
