import datetime

now_datetime = datetime.datetime.now()

class Job:
    
    def __init__(self, startHour, startMin, duration,cpu):
        self.startHour = startHour
        self.startMin = startMin
        self.duration = duration
        self.start = now_datetime.replace(hour=startHour, minute=startMin,second=0, microsecond=0)
        self.end = self.start + datetime.timedelta(minutes=duration)
        self.cpu = cpu

    def __str__(self):
        return f'{self.start} - {self.end}'

    def __rp(self):
            return f'{self.start} - {self.end}'

j1 = Job(20, 30, 90, 40)
j2 = Job(21, 30, 90, 50)
j3 = Job(21, 35, 10, 50)
j4 = Job(21, 40, 10, 50)

jobs = [j1,j2,j3,j4]

overlaps = []

for i, job in enumerate(jobs):
    k = i +1
    overlap = [job]
    while k<len(jobs):
        next_job = jobs[k] 
        if job.end > next_job.start:
            overlap.append(next_job)
        k = k + 1
    overlaps.append(overlap)

max_= 0
for o in overlaps:
    max_cpu = 0
    for j in jobs:
        max_cpu += j.cpu
    max_ = max(max_, max_cpu)

print(max_)