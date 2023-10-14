import logging
from core.queue_manager import Queue



class Scheduler:
    def __init__(self, groups: dict) -> None:
        self.queues = [Queue(id, quota) for id, quota in groups.items()]
        self._whole_schedule = []
        self._latest_schedule = []
        self._current_turn = 0

    def _is_all_queues_empty(self) -> bool:
        return not False in [queue.is_empty for queue in self.queues]
    
    def set_current_turn(self, group_id: int) -> int:
        try:
            self._current_turn = self.queues.index((group_id, _))
        except:
            logging.warning(f'The group id "{group_id}" does not exist.')
        finally:
            return self._current_turn
    
    def get_latest_schedule(self, num) -> list:
        result = []
        pointer = self._current_turn
        while len(result) < num + 1 and not self._is_all_queues_empty():
            if not self.queues[pointer].is_empty:
                result.extend(self.queues[pointer].get_latest_requests())
            pointer = (pointer + 1) % len(self.queues)
        return result

    

