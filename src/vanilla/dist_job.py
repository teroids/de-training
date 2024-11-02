def distribute_tasks(tasks, n_workers):
    workers = [[] for _ in range(n_workers)]
    
    for i, task in enumerate(tasks):
        print(i % n_workers)
        workers[i % n_workers].append(task)

    worker_sums = [sum(worker_tasks) for worker_tasks in workers]
    
    return worker_sums

# Example Usage
tasks = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
print(distribute_tasks(tasks, 3))