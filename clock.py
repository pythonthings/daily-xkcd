import router
import clock_utils
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('cron', second=0, timezone="US/Pacific")
def scheduled_job():
    print("RUNNING JOB")
    timestr = clock_utils.get_time()
    router.run(timestr)

@sched.scheduled_job('cron', minute=0, timezone="US/Pacific")
def scheduled_job():
    timestr = clock_utils.get_time()
    router.run(timestr)

@sched.scheduled_job('cron', minute=30, timezone="US/Pacific")
def scheduled_job():
    timestr = clock_utils.get_time()
    router.run(timestr)

print("starting")
sched.start()
print("does it ever go here? :0")
