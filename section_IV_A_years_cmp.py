from cmp_lats_cdf_periods import *

if __name__ == '__main__':
    year_A = 2015
    year_B = 2016
    year_C = 2017

    period_key = "postsuperbowl"
    # period_key = "postsuperbowl"
    probe_key = "pl2cloud"

    '''
    provider = "GCE"
    srv_A = "gc12"
    srv_B = "cache-02"
    srv_C = "gserver-01"

    '''
    '''
    provider = "Azure"
    srv_A = "az03"
    srv_B = "cache-07"
    srv_C = "server-02"
    '''

    provider = "AWS"
    srv_A = "aws03"
    srv_B = "cache-06"
    srv_C = "aws-server"

    data_A = load_mn_lats_by_srv(probe_key, period_key, year_A, srv_A)
    data_B = load_mn_lats_by_srv(probe_key, period_key, year_B, srv_B)
    data_C = load_mn_lats_by_srv(probe_key, period_key, year_C, srv_C)

    cmp_lats_cdf(data_A, str(year_A), data_B, str(year_B), data_C, str(year_C),
                 period_key + "-" + probe_key + "-" + provider)