from core.scheduler import Scheduler


def test_senario_1():
    data = {
        'B1': 1,
        'B2': 1,
        'B3': 1,
        'A1': 2,
        'A4': 2,
        'A3': 2,
        'A4': 2,
    }
    s = Scheduler(groups=data)
    assert s.get_latest_schedule(10) == []
    s.queues[0].append_request({'code':1, 'name': 'cool'})
    assert s.get_latest_schedule(10) == ['1']
    s.queues[1].append_request('2')
    assert s.get_latest_schedule(10) == ['1', '2']
    s.queues[2].append_request('3')
    assert s.get_latest_schedule(10) == ['1', '2', '3']
    s.queues[2].append_request('4')
    assert s.get_latest_schedule(10) == ['1', '2', '3', '4']
    s.queues[2].append_request('5')
    assert s.get_latest_schedule(10) == ['1', '2', '3', '4', '5']
    s.queues[1].append_request('6')
    assert s.get_latest_schedule(10) == ['1', '2', '6', '3', '4','5']
    s.queues[1].append_request('7')
    assert s.get_latest_schedule(10) == ['1', '2', '6', '3', '4', '7','5']

if __name__ == '__main__':
    test_senario_1()