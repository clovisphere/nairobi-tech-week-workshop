#!/usr/bin/env python3
from locust import HttpLocust, TaskSet, task
import random

MAX_WAIT_TIME = 3000
MIN_WAIT_TIME = 1000

class UserAction(TaskSet):
    
    @task(2)
    def home(self):
        self.client.get('/index.php')

    @task(5)
    def reserve(self):
        _from = ['Paris', 'Philadelphia', 'Boston', 'Portland', 'San Diego', 'Mexico City', 'São Paolo']
        _to = ['London', 'Rome', 'Buenos Aires', 'New York', 'Dublin', 'Cairo']

        # build payload
        payload = {
            'fromPort': random.choice(_from),
            'toPort': random.choice(_to) 
        }

        self.client.post('/reserve.php', data=payload)
    
    @task(3)
    def purchase(self):
        self.client.get('/purchase.php')
    
    @task(1)
    def confirmation(self):
        self.client.get('/confirmation.php')

class User(HttpLocust):
    task_set = UserAction
    min_wait = MIN_WAIT_TIME
    max_wait = MAX_WAIT_TIME
