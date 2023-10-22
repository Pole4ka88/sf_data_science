from collections import defaultdict
from collections import deque


def task_manager(tasks):
    task_dict = defaultdict(deque)
    office_deque = deque()
    voltage_deque = deque()
    for elem in tasks:
        elem1 = deque(elem)
        for number, name in elem1:
            task_dict[name].append(number)

    return task_dict


print(task_manager(
    tasks=[(36871, 'office', False), (40690, 'office', False), (35364, 'voltage', False), (41667, 'voltage', True),
           (33850, 'office', False)]))