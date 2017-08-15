from cmp_lats_cdf_periods import *

if __name__ == '__main__':
    year = 2017
    period_key_A = "superbowl"
    period_key_B = "halftime"
    period_key_C = "postsuperbowl"
    probe_key = "pl2cloud"
    provider = "GCE"

    ## Section IV-A, comparison of user to cloud vms latencies over different periods
    # srv="gc12"
    srv="gserver-01"
    # srv = "cache-02"
    # srv = "aws02"
    # srv = "az02"

    data_A = load_mn_lats_by_srv(probe_key, period_key_A, year, srv)
    #data_A = load_mn_lats_by_provider(probe_key, period_key_A, year, provider)
    # print(data_A)
    data_B = load_mn_lats_by_srv(probe_key, period_key_B, year, srv)
    #data_B = load_mn_lats_by_provider(probe_key, period_key_B, year, provider)
    data_C = load_mn_lats_by_srv(probe_key, period_key_C, year, srv)
    #data_C = load_mn_lats_by_provider(probe_key, period_key_C, year, provider)

    cmp_lats_cdf(data_A, period_key_A, data_B, period_key_B, data_C, period_key_C, srv + "-" + probe_key + "-" + str(year))
    # cmp_lats_cdf(data_A, period_key_A, data_B, period_key_B, data_C, period_key_C, provider + "-" + probe_key + "-" + str(year))
