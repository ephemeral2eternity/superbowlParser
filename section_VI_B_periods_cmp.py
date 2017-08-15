from cmp_lats_cdf_periods import *

if __name__ == '__main__':
    period_key_A = "superbowl"
    period_key_B = "halftime"
    period_key_C = "postsuperbowl"
    # period_key = "postsuperbowl"
    probe_key = "pl2host"
    # year = 2017
    year = 2016

    # provider = "papajohns"
    provider = "netflix"
    # servers = ["papajohns"]
    servers = ["netflix"]


    data_A = load_mn_lats_by_srv(probe_key, period_key_A, year, servers)
    data_B = load_mn_lats_by_srv(probe_key, period_key_B, year, servers)
    data_C = load_mn_lats_by_srv(probe_key, period_key_C, year, servers)

    cmp3_lats_cdf(data_A, period_key_A, data_B, period_key_B, data_C, period_key_C,
                 provider + "-" + probe_key + "-" + str(year))