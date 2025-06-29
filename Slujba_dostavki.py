"""Delivery service."""


def calculate_platforms_needed(mass_robots: list[int], limit: int):
    """Метод определения минимального количества платформ."""
    sorted_mass_robots = sorted(mass_robots)
    index_left: int = 0
    index_right: int = len(mass_robots) - 1
    result: int = 0
    """Условие выполнения задачи."""
    if max(sorted_mass_robots) > limit:
        print('Вес отдельного робота не может превышать limit.')
        return 'Задача не выполнима.'

    while index_left <= index_right:
        if sorted_mass_robots[index_left] + \
           sorted_mass_robots[index_right] <= limit:
            index_left = index_left + 1
        index_right = index_right - 1
        result = result + 1
        if index_left == index_right:
            result = result + 1
            break
    return result


if __name__ == '__main__':
    weights_robots = [int(i) for i in input().split()]
    limit_mass = int(input())
    print(calculate_platforms_needed(weights_robots, limit_mass))
