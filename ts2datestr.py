import time
import datetime

#####################################################################################
## @descr: Convert the timestamp to the date time string in the format of "YYYY-MM-DD HH:MM:SS"
## @params: ts ---- the timestamp in "int"
## @return: the date string that denotes the date time in the format of "YYYY-MM-DD HH:MM:SS"
#####################################################################################
def ts2date(ts):
    dt = datetime.datetime.utcfromtimestamp(ts)
    dt_str = dt.strftime("%Y-%m-%d %H:%M:%S")
    return dt_str

if __name__ == '__main__':
    ## Super bowl 2017
    # ts_start = 1486337400
    # ts_end = 1486351800

    ## Post super bowl 2017
    # ts_start = 1486942200
    # ts_end = 1486956600

    ## Half time super bowl 2016
    ts_start = 1422805301
    ts_end = 1422977839
    dt_start_str = ts2date(ts_start)
    dt_end_str = ts2date(ts_end)
    print("Start timestamp %d" %ts_start)
    print("End timestamp %d" % ts_end)
    print("Start date is: " + dt_start_str)
    print("End date is: " + dt_end_str)


