from cmp_lats_cdf_periods import *

if __name__ == '__main__':
    # period_key = "superbowl"
    # period_key = "halftime"
    period_key = "postsuperbowl"
    probe_key = "pl2host"
    year = 2017


    provider_A = "Level_3"
    provider_B = "Akamai"
    provider_C = "LimeLight"
    #client = "client-01"
    #server = "cache-01"
    servers_A = ["foxsports-l3c", "foxsports-l3c2", "sb17-pre-l3c", "sb17-pre-l3c2"]
    servers_B = ["foxsports-akc", "foxsports-akc-us", "foxsports-akc-us2", "foxsports-akc2", "sb17-pre-akc2", "sb17-pre-akc"]
    servers_C = ["sb17-pre-llc", "sb17-pre-llc2"]


    data_A = load_mn_lats_by_srv(probe_key, period_key, year, servers_A)
    data_B = load_mn_lats_by_srv(probe_key, period_key, year, servers_B)
    data_C = load_mn_lats_by_srv(probe_key, period_key, year, servers_C)

    cmp_lats_cdf(data_A, provider_A, data_B, provider_B, data_C, provider_C,
                 period_key + "-" + probe_key + "-" + str(year))