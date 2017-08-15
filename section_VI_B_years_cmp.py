from cmp_lats_cdf_periods import *

if __name__ == '__main__':
    # period_key = "superbowl"
    # period_key = "halftime"
    period_key = "postsuperbowl"
    # period_key = "postsuperbowl"
    probe_key = "pl2host"
    # year = 2017
    yearA = 2016
    yearB = 2017

    # provider = "papajohns"
    provider = "netflix"
    # servers = ["papajohns"]
    servers = ["netflix"]


    data_A = load_mn_lats_by_srv(probe_key, period_key, yearA, servers)
    data_B = load_mn_lats_by_srv(probe_key, period_key, yearB, servers)


    cmp_lats_cdf(data_A, str(yearA), data_B, str(yearB),
                 provider + "-" + probe_key + "-" + period_key)