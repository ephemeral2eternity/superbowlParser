from cmp_lats_cdf_periods import *
import numpy as np

if __name__ == '__main__':
    year = 2015
    # year = 2017
    period_key_A = "superbowl"
    period_key_B = "halftime"
    period_key_C = "postsuperbowl"
    probe_key = "pl2cloud"
    # provider = "AWS"
    provider = "ALL"

    ## Section IV-A, comparison of user to cloud vms latencies over different periods
    # srv="gc12"
    srvs=["gc11", "gc12", "gc13", "gc14", "gc15", "gc16", "az01", "az02", "az03", "az04", "az05", "aws01", "aws02", "aws03"]
    # srvs = ["gc11", "gc12", "gc13", "gc14", "gc15", "gc16"]
    # srvs = ["az01", "az02", "az03", "az04", "az05"]
    # srvs = ["aws01", "aws02", "aws03"]
    # srv="gserver-01"
    # srv = "cache-02"
    # srv = "aws02"
    # srv = "az02"

    data_A = load_lats_by_srv(probe_key, period_key_A, year, srvs)
    # data_A = load_lats_by_provider(probe_key, period_key_A, year, provider)
    # print(data_A)

    data_B = load_lats_by_srv(probe_key, period_key_B, year, srvs)
    # data_B = load_lats_by_provider(probe_key, period_key_B, year, provider)

    data_C = load_lats_by_srv(probe_key, period_key_C, year, srvs)
    # data_C = load_lats_by_provider(probe_key, period_key_C, year, provider)

    data_A_mn = np.mean(data_A)
    data_A_std = np.std(data_A)
    print("The latencies during %s have statistics: Mean %.4f ms and STD %.4f ms" %(period_key_A, data_A_mn, data_A_std))

    data_B_mn = np.mean(data_B)
    data_B_std = np.std(data_B)
    print("The latencies during %s have statistics: Mean %.4f ms and STD %.4f ms" %(period_key_B, data_B_mn, data_B_std))

    data_C_mn = np.mean(data_C)
    data_C_std = np.std(data_C)
    print("The latencies during %s have statistics: Mean %.4f ms and STD %.4f ms" %(period_key_C, data_C_mn, data_C_std))

    # cmp3_lats_cdf(data_A, period_key_A, data_B, period_key_B, data_C, period_key_C,  "US-srvs-" + probe_key + "-" + str(year))
    cmp3_lats_cdf(data_A, period_key_A, data_B, period_key_B, data_C, period_key_C, provider + "-" + probe_key + "-" + str(year))
