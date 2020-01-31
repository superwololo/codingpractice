import copy

jobs = [
    ("a", 2, 100),
    ("b", 1, 19),
    ("c", 2, 27),
    ("d", 1, 25),
    ("e", 3, 15),
]

mtime = 3

def max_profit(jobs):
    solns = []
    max_profit_inner(jobs, 0, set(), 0, mtime, solns)
    return max(solns, key=lambda x:x[1])


def max_profit_inner(jobs, time, finished_jobs, total_profit, max_time, solns):

    if time >= max_time:
        solns.append((copy.copy(finished_jobs), total_profit))
        return

    for job_id, deadline, profit in jobs:
        if time < deadline and job_id not in finished_jobs:
            finished_jobs.add(job_id)
            total_profit += profit
            max_profit_inner(jobs, time+1, finished_jobs, total_profit, max_time, solns)
            finished_jobs.remove(job_id)
            total_profit -= profit


def set_available(available, deadline):
    for index in xrange(deadline, -1, -1):
        if available[index]:
            available[index] = False
            return True
    return False


def max_profit2(jobs):
    sorted_jobs = sorted(jobs, key=lambda x:-x[2])
    best_jobs = []
    total_profit = 0
    available = [True] * mtime

    for job_id, deadline, profit in sorted_jobs:
        if set_available(available, deadline-1):
            best_jobs.append(job_id)
            total_profit += profit
    return best_jobs, total_profit


print max_profit2(jobs)
