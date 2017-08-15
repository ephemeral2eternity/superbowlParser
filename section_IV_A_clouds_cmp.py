from cmp_lats_cdf_periods import *

if __name__ == '__main__':
    year = 2015
    # period_key = "superbowl"
    period_key = "halftime"
    # period_key = "postsuperbowl"
    probe_key = "pl2cloud"
    provider_A = "GCE"
    provider_B = "AWS"
    provider_C = "Azure"

    ## Section IV-A, comparison of user to cloud vms latencies over different periods
    srv_A = "gc15"
    srv_B = "aws01"
    srv_C = "az03"

    data_A = load_mn_lats_by_srv(probe_key, period_key, year, srv_A)
    #data_A = load_mn_lats_by_provider(probe_key, period_key, year, provider_A)
    # print(data_A)
    data_B = load_mn_lats_by_srv(probe_key, period_key, year, srv_B)
    #data_B = load_mn_lats_by_provider(probe_key, period_key, year, provider_B)
    data_C = load_mn_lats_by_srv(probe_key, period_key, year, srv_C)
    #data_C = load_mn_lats_by_provider(probe_key, period_key, year, provider_C)

    cmp_lats_cdf(data_A, provider_A, data_B, provider_B, data_C, provider_C, period_key + "-" + probe_key + "-" + str(year))
    # cmp_lats_cdf(data_A, period_key_A, data_B, period_key_B, data_C, period_key_C, provider + "-" + probe_key + "-" + str(year))
