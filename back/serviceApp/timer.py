from serviceApp.cron import IntraJob, GradeJob, NewsJob, TwitterJob, TwitchJob, FilmJob, AmazonJob, NetflixJob
import _thread
import time

def taskManager():
    _thread.start_new_thread(timer, ())

def timer():
    while(42):
        time.sleep(60)
        IntraJob()
        GradeJob()
        NewsJob()
        TwitterJob()
        TwitchJob()
        FilmJob()
        AmazonJob()
        NetflixJob()
