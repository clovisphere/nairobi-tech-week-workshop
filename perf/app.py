#!/usr/bin/env python3
from locust import HttpLocust, TaskSet, task

MAX_WAIT_TIME = 5000
MIN_WAIT_TIME = 5000

class UserAction(TaskSet):
    
    @task(1)
    def home(self):
        self.client.get('/index.php')

    def reserve(self):
        pass

    def purchase(self):
        pass
    
    def confirmation(self):
        pass

class User(HttpLocust):
    task_set = UserAction
    min_wait = MIN_WAIT_TIME
    max_wait = MAX_WAIT_TIME
