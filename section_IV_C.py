from cmp_lats_cdf_periods import *

if __name__ == '__main__':
    period_key_A = "superbowl"
    period_key_B = "halftime"
    period_key_C = "postsuperbowl"
    # period_key = "postsuperbowl"
    probe_key = "cloud2cloud"
    year = 2016


    provider = "GCE"
    #client = "client-01"
    #server = "cache-01"

    client = "client-02"
    server = "cache-02"


    '''
    provider = "Azure"
    #client = "client-07"
    #server = "cache-07"

    client = "client-08"
    server = "cache-08"
    '''
    '''
    provider = "AWS"
    client = "client-05"
    server = "cache-05"

    #client = "client-06"
    #server = "cache-06"
    '''


    data_A_pd = load_lats_by_client_srv(probe_key, period_key_A, year, client, server)
    print("The latency statistics between %s and %s during %s period is as follows." % (client, server, period_key_A))
    print("Mean latency: %.4f ms."% data_A_pd.mean())
    print("Min latency: %.4f ms." % data_A_pd.min())
    print("Max latency: %.4f ms." % data_A_pd.max())
    print("Latency STD: %.4f ms." % data_A_pd.std())
    data_B_pd = load_lats_by_client_srv(probe_key, period_key_B, year, client, server)
    print("The latency statistics between %s and %s during %s period is as follows." % (client, server, period_key_B))
    print("Mean latency: %.4f ms."% data_B_pd.mean())
    print("Min latency: %.4f ms." % data_B_pd.min())
    print("Max latency: %.4f ms." % data_B_pd.max())
    print("Latency STD: %.4f ms." % data_B_pd.std())
    data_C_pd = load_lats_by_client_srv(probe_key, period_key_C, year, client, server)
    print("The latency statistics between %s and %s during %s period is as follows." % (client, server, period_key_C))
    print("Mean latency: %.4f ms."% data_C_pd.mean())
    print("Min latency: %.4f ms." % data_C_pd.min())
    print("Max latency: %.4f ms." % data_C_pd.max())
    print("Latency STD: %.4f ms." % data_C_pd.std())