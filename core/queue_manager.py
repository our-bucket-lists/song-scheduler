

class Queue:
    def __init__(self, id: int, quota: int) -> None:
        self._queue = []
        self._queue_backup = [[] for _ in range(100)]
        self.id = id
        self.quota = quota
        self.is_empty = True

    def _backup(self) -> None:
        self._queue_backup.pop(0)
        self._queue_backup.append(self._queue.copy())

    def append_request(self, song: dict) -> list:
        self._backup()
        self._queue.append(song)
        self.is_empty = len(self._queue) == 0
        return self._queue

    def update_queue(self, songs: list) -> list:
        self._backup()
        self._queue = songs
        self.is_empty = len(self._queue) == 0
        return self._queue

    def get_requests(self) -> list :
        return self._queue
    
    def get_latest_requests(self) -> list:
        result = []

        for _ in range(self.quota):
            self._backup()

            if len(self._queue) != 0:
                result.append(self._queue.pop(0))

        return result
    