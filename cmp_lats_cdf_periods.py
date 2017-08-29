from dataFolder import *
from json_utils import *
from ts2datestr import *
from convert_cloud_lats import *
from drawlibs.draw_cdf import *

def load_lats_by_provider(probe_key, period_key, year, provider):
    cur_data_folder = todraw_folder + "/" + str(year) + "/" + period_key + "/" + probe_key + "/"
    cloud_srvs = get_cloud_srvs_by_provider(year, provider)
    lats_files = glob.glob(cur_data_folder + "*")

    all_lats = []
    for lat_file in lats_files:
        cur_node = os.path.basename(lat_file)
        cur_lat = loadJson(lat_file)
        if cur_lat:
            cur_df = pd.DataFrame(cur_lat)
            for srv in cloud_srvs:
                print("Get the latency file from %s to %s. " % (cur_node, srv))
                denoted_df_ind = cur_df[srv].between(0, 500, inclusive=False)
                denoted_df = cur_df[denoted_df_ind][srv]
                # denoted_df = cur_df[srv]
                denoted_df_values = denoted_df.tolist()
                all_lats.extend(denoted_df_values)

    return all_lats

def load_mn_lats_by_provider(probe_key, period_key, year, provider):
    cur_data_folder = todraw_folder + "/" + str(year) + "/" + period_key + "/" + probe_key + "/"
    cloud_srvs = get_cloud_srvs_by_provider(year, provider)
    lats_files = glob.glob(cur_data_folder + "*")

    all_lats = []
    for lat_file in lats_files:
        cur_node = os.path.basename(lat_file)
        cur_lat = loadJson(lat_file)
        if cur_lat:
            cur_df = pd.DataFrame(cur_lat)
            for srv in cloud_srvs:
                print("Get the latency file from %s to %s. " % (cur_node, srv))
                denoted_df = cur_df[srv]
                denoted_df_mn = denoted_df.mean()
                all_lats.append(denoted_df_mn)
                print("Get the mean latency from %s to %s as %.4f ms. " %(cur_node, srv, denoted_df_mn))

    return all_lats

def load_lats_by_srv(probe_key, period_key, year, srvs):
    cur_data_folder = todraw_folder + "/" + str(year) + "/" + period_key + "/" + probe_key + "/"
    lats_files = glob.glob(cur_data_folder + "*")

    all_lats = []
    for lat_file in lats_files:
        cur_node = os.path.basename(lat_file)
        cur_lat = loadJson(lat_file)
        if cur_lat:
            cur_df = pd.DataFrame(cur_lat)
            for srv in srvs:
                if srv in list(cur_df):
                    print("Get the latency file from %s to %s. " % (cur_node, srv))
                    denoted_df_ind = cur_df[srv].between(0, 500, inclusive=False)
                    denoted_df = cur_df[denoted_df_ind][srv]
                    # denoted_df = cur_df[srv]
                    denoted_df_list = denoted_df.tolist()
                    if denoted_df_list:
                        all_lats.extend(denoted_df_list)
                        # print("Get the mean latency from %s to %s as %.4f ms. " %(cur_node, srv, denoted_df_mn))

    return all_lats

def load_mn_lats_by_srv(probe_key, period_key, year, srvs):
    cur_data_folder = todraw_folder + "/" + str(year) + "/" + period_key + "/" + probe_key + "/"
    lats_files = glob.glob(cur_data_folder + "*")

    all_lats = []
    for lat_file in lats_files:
        cur_node = os.path.basename(lat_file)
        cur_lat = loadJson(lat_file)
        if cur_lat:
            cur_df = pd.DataFrame(cur_lat)
            for srv in srvs:
                if srv in list(cur_df):
                    print("Get the latency file from %s to %s. " % (cur_node, srv))
                    denoted_df = cur_df[srv]
                    denoted_df_mn = denoted_df.mean()
                    if denoted_df_mn:
                        all_lats.append(denoted_df_mn)
                        print("Get the mean latency from %s to %s as %.4f ms. " %(cur_node, srv, denoted_df_mn))

    return all_lats

def load_std_lats_by_srv(probe_key, period_key, year, srvs):
    cur_data_folder = todraw_folder + "/" + str(year) + "/" + period_key + "/" + probe_key + "/"
    lats_files = glob.glob(cur_data_folder + "*")

    all_std_lats = []
    for lat_file in lats_files:
        cur_node = os.path.basename(lat_file)
        cur_lat = loadJson(lat_file)
        if cur_lat:
            cur_df = pd.DataFrame(cur_lat)
            for srv in srvs:
                if srv in list(cur_df):
                    print("Get the latency file from %s to %s. " % (cur_node, srv))
                    denoted_df = cur_df[srv]
                    denoted_df_std = denoted_df.std()
                    if denoted_df_std:
                        all_std_lats.append(denoted_df_std)
                        print("Get the std latency from %s to %s as %.4f ms. " %(cur_node, srv, denoted_df_std))

    return all_std_lats

def load_lats_by_client_srv(probe_key, period_key, year, client, server):
    cur_data_folder = todraw_folder + "/" + str(year) + "/" + period_key + "/" + probe_key + "/"
    client_names = loadJson("./config/cloud_clients_" + str(year) + ".json")
    if "post" in period_key:
        cur_client = client_names[client]["post_sb_name"]
    else:
        cur_client = client_names[client]["sb_name"]

    cur_client_file = cur_data_folder + cur_client + ".json"
    cur_client_lats = pd.DataFrame(loadJson(cur_client_file))

    cur_client_srv_lats_pd = cur_client_lats[server]

    return cur_client_srv_lats_pd



def get_cloud_srvs_by_provider(year, provider="ALL"):
    cloud_srvs = loadJson("./config/cloud_srv_" + str(year) + ".json")
    cloud_srv_keys = []
    if provider == "ALL":
        return cloud_srvs.keys()

    for srv_key in cloud_srvs:
        if cloud_srvs[srv_key]["provider"] == provider:
            cloud_srv_keys.append(srv_key)
    return cloud_srv_keys

def cmp3_lats_cdf(dataA, labelA, dataB, labelB, dataC, labelC, img_suffix):
    fig, ax = plt.subplots()
    draw_cdf(dataA, "k-", labelA)
    print("The maximum mean latency for %s is %.4f ms." % (labelA, max(dataA)))
    draw_cdf(dataB, "b--", labelB)
    print("The maximum mean latency for %s is %.4f ms." % (labelB, max(dataB)))
    draw_cdf(dataC, "r:", labelC)
    print("The maximum mean latency for %s is %.4f ms." % (labelC, max(dataC)))

    ax.set_xlabel(r'Probing Latencies (ms)', fontsize=20)
    ax.set_ylabel(r'Percentage of probing clients', fontsize=20)
    plt.xlim([0, 500])
    plt.ylim([0, 1])
    plt.legend(loc=4)

    imgName = img_folder + labelA + "-" + labelB + "-" + labelC + "-"+ img_suffix
    plt.savefig(imgName + ".jpg")
    plt.savefig(imgName + ".pdf")
    plt.savefig(imgName + ".png")
    plt.show()

def cmp_lats_cdf(dataA, labelA, dataB, labelB, img_suffix):
    fig, ax = plt.subplots()
    draw_cdf(dataA, "k-", labelA)
    print("The maximum mean latency for %s is %.4f ms." % (labelA, max(dataA)))
    draw_cdf(dataB, "b--", labelB)
    print("The maximum mean latency for %s is %.4f ms." % (labelB, max(dataB)))

    ax.set_xlabel(r'Probing Latencies (ms)', fontsize=20)
    ax.set_ylabel(r'Percentage of probing clients', fontsize=20)
    plt.xlim([0, 500])
    plt.ylim([0, 1])
    plt.legend(loc=4)

    imgName = img_folder + labelA + "-" + labelB + "-"+ img_suffix
    plt.savefig(imgName + ".jpg")
    plt.savefig(imgName + ".pdf")
    plt.savefig(imgName + ".png")
    plt.show()



if __name__ == '__main__':
    period_key_A = "superbowl"
    period_key_B = "halftime"
    period_key_C = "postsuperbowl"
    # period_key = "postsuperbowl"
    probe_key = "pl2host"
    # year = 2017
    year = 2017


    #provider = "Google Ads"
    #servers = ["doubleclick", "doubleclick-stat", "google-tag-manager"]

    # provider = "Twitter"
    # servers = ["twimg", "twitter", "videotwimg", "pbstwimg"]

    provider = "Facebook"
    servers = ["facebook", "fbcdn"]

    data_A = load_mn_lats_by_srv(probe_key, period_key_A, year, servers)
    data_B = load_mn_lats_by_srv(probe_key, period_key_B, year, servers)
    data_C = load_mn_lats_by_srv(probe_key, period_key_C, year, servers)

    cmp3_lats_cdf(data_A, period_key_A, data_B, period_key_B, data_C, period_key_C,
                 provider + "-" + probe_key + "-" + str(year))