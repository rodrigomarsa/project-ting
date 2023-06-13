import pytest
from ting_file_management.priority_queue import PriorityQueue


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    assert priority_queue.__len__() == 0

    with pytest.raises(IndexError):
        priority_queue.search(-1)

    priority_queue.enqueue({"qtd_linhas": 4})
    assert priority_queue.__len__() == 1
    assert priority_queue.search(0) == {"qtd_linhas": 4}

    priority_queue.enqueue({"qtd_linhas": 7})
    assert priority_queue.search(1) == {"qtd_linhas": 7}
    priority_queue.enqueue({"qtd_linhas": 4})
    assert priority_queue.search(1) == {"qtd_linhas": 4}
    # [4, 4, 7]

    priority_queue.dequeue()
    assert priority_queue.__len__() == 2
    assert priority_queue.search(0) == {"qtd_linhas": 4}

    priority_queue.enqueue({"qtd_linhas": 4})
    assert priority_queue.search(0) == {"qtd_linhas": 4}
