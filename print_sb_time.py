from dataFolder import *
from json_utils import *
from ts2datestr import *

def print_sb_time(year):
    sb_period_time_file = "./config/sb_periods_%d.json" % year
    sb_periods = loadJson(sb_period_time_file)
    sb_period = sb_periods["superbowl"]
    print("The Super Bowl %d starts at %s and ends at %s" % (year, ts2date(sb_period["start"]), ts2date(sb_period["end"])))
    sb_halftime_period = sb_periods["halftime"]
    print("The Super Bowl %d Half time show starts at %s and ends at %s" % (year, ts2date(sb_halftime_period["start"]), ts2date(sb_halftime_period["end"])))
    sb_postsb_period = sb_periods["postsuperbowl"]
    print("The Post Super Bowl %d weekend period starts at %s and ends at %s" % (year, ts2date(sb_postsb_period["start"]), ts2date(sb_postsb_period["end"])))
    sb_ad_periods = sb_periods["advertisements"]
    ad_ind = 1
    for sb_ad_period in sb_ad_periods:
        print("The Super Bowl %d commercial %d starts at %s and ends at %s" % (
        year, ad_ind, ts2date(sb_ad_period["start"]), ts2date(sb_ad_period["end"])))

        ad_ind += 1

if __name__ == '__main__':
    year = 2015
    print_sb_time(year)
    print("#######################################################################################")
    year = 2016
    print_sb_time(year)
    print("#######################################################################################")
    year = 2017
    print_sb_time(year)