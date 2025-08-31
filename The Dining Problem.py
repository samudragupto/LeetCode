import threading

class DiningPhilosophers:
    def __init__(self):
        self.forks = [threading.Lock() for _ in range(5)]
        self.eating_lock = threading.Lock()
        
    def wantsToEat(self, philosopher, pickLeftFork, pickRightFork, eat, putLeftFork, putRightFork):
        left_fork_id = philosopher
        right_fork_id = (philosopher + 1) % 5
        
        with self.eating_lock:
            if philosopher % 2 == 0:
                self.forks[left_fork_id].acquire()
                pickLeftFork()
                self.forks[right_fork_id].acquire()
                pickRightFork()
            else:
                self.forks[right_fork_id].acquire()
                pickRightFork()
                self.forks[left_fork_id].acquire()
                pickLeftFork()
            
            eat()
            if philosopher % 2 == 0:
                putRightFork()
                self.forks[right_fork_id].release()
                putLeftFork()
                self.forks[left_fork_id].release()
            else:
                putLeftFork()
                self.forks[left_fork_id].release()
                putRightFork()
                self.forks[right_fork_id].release()
