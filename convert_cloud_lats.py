from json_utils import *
from dataFolder import *
import glob
import os
import re
import pandas as pd

#####################################################################################
## @descr: Merge all the latencies probed from planetlab nodes to cloud servers for super bowl 2015
##         The data is dumped to the folder todraw_folder with each planetlab node as a file
## @params: period_to_get_key  ---- denote the period of latencies to extract
##                                  superbowl: the period of superbowl game
##                                  halftime: the period of superbowl half time show
##                                  postsuperbowl: the same time game period in a common weekend
#####################################################################################
def convert_pl2cloud_lats_2015(period_to_get_key):
    sb_periods = loadJson("./config/sb_periods_2015.json")
    period_to_get = sb_periods[period_to_get_key]
    period_start = period_to_get["start"]
    period_end = period_to_get["end"]

    out_folder = todraw_folder + "2015/" + period_to_get_key + "/pl2cloud/"

    if "post" in period_to_get_key:
        pl_folders = glob.glob(post_sb_ping_folder_2015 + "*/")
    else:
        pl_folders = glob.glob(sb_ping_folder_2015 + "*/")
    for pl_node_folder in pl_folders:
        lats_files = glob.glob(pl_node_folder + "*" + sb_pl2cloud_suffix_2015)
        cur_node_file_path = os.path.dirname(pl_node_folder)
        path_elements = cur_node_file_path.split('\\')
        cur_node = path_elements[1]
        print("Converting latency files for node %s"%cur_node)
        cur_node_lats = []
        for lat_file in lats_files:
            base_lat_file = os.path.basename(lat_file)
            file_strs = base_lat_file.split("_")
            ts = int(file_strs[1])
            if (ts <= period_end) and (ts >= period_start):
                lats = loadJson(lat_file)
                lats["timestamp"] = ts
                cur_node_lats.append(lats)

        cur_node_lats_file = out_folder + cur_node + ".json"
        dumpJson(cur_node_lats, cur_node_lats_file)

#####################################################################################
## @descr: Merge all the latencies probed from planetlab/cloud nodes to cloud/cdn hosts for super bowl at a given year
##         The data is dumped to the folder todraw_folder with each planetlab node as a file
## @params: period_key  ---- denote the period of latencies to extract
##                                  superbowl: the period of superbowl game
##                                  halftime: the period of superbowl half time show
##                                  postsuperbowl: the same time game period in a common weekend
##          probe_key ---- denote the probing type
##                          pl2cloud: the probing is from planetlab nodes to cloud servers
##                          cloud2cloud: the probing is from cloud nodes to cloud servers
##                          pl2host: the probing is from planetlab nodes to CDN hosts
##                          cloud2host: the probing is from cloud nodes to CDN hosts
##          year ---- can be 2016 or 2017
#####################################################################################
def merge_lats(period_key, probe_key, year):
    if year == 2016:
        sb_periods = loadJson("./config/sb_periods_2016.json")
    else:
        sb_periods = loadJson("./config/sb_periods_2017.json")

    period_to_get = sb_periods[period_key]
    period_start = period_to_get["start"]
    period_end = period_to_get["end"]

    source_data_folder = get_data_folder(period_key, probe_key, year)

    data_suffix = get_data_suffix(probe_key)

    all_files = glob.glob(source_data_folder + "*" + data_suffix)

    all_node_lats = {}
    for cur_file in all_files:
        cur_file_name = os.path.basename(cur_file)
        cur_node = cur_file_name.split('_')[0]
        if cur_node not in all_node_lats.keys():
            all_node_lats[cur_node] = []

        print("Read node file: %s" % cur_file_name)
        cur_file_json = csv2jsonfloat(cur_file)
        all_node_lats[cur_node].extend(cur_file_json)

    out_folder = todraw_folder + str(year) + "/" + period_key + "/" + probe_key + "/"
    for node in all_node_lats:
        print("Processing node file %s" % node)
        cur_node_lats = all_node_lats[node]
        cur_node_lats_pd = pd.DataFrame(cur_node_lats)
        sorted_cur_node_lats_pd = cur_node_lats_pd.sort_values(by="Timestamp")
        sorted_cur_node_in_range = sorted_cur_node_lats_pd[sorted_cur_node_lats_pd["Timestamp"].between(period_start, period_end)]
        sorted_cur_node_in_range.rename(columns=lambda x: x.replace('sb', ''), inplace=True)

        cur_node_lats_in_range_json = json.loads(sorted_cur_node_in_range.to_json(orient='records'))
        dumpJson(cur_node_lats_in_range_json, out_folder + node + ".json")

#####################################################################################
## @descr: Get the data suffix by the probe_key
## @params: probe_key ---- denote the probing type
##                          pl2cloud: the probing is from planetlab nodes to cloud servers
##                          cloud2cloud: the probing is from cloud nodes to cloud servers
##                          pl2host: the probing is from planetlab nodes to CDN hosts
##                          cloud2host: the probing is from cloud nodes to CDN hosts
#####################################################################################
def get_data_suffix(probe_key):
    if "host" in probe_key:
        data_suffix = sb_pinghost_suffix
    else:
        data_suffix = sb_pingcloud_suffix
    return data_suffix

#####################################################################################
## @descr: Get the data folder for the data to be merged
## @params: period_key  ---- denote the period of latencies to extract
##                                  superbowl: the period of superbowl game
##                                  halftime: the period of superbowl half time show
##                                  postsuperbowl: the same time game period in a common weekend
##          probe_key ---- denote the probing type
##                          pl2cloud: the probing is from planetlab nodes to cloud servers
##                          cloud2cloud: the probing is from cloud nodes to cloud servers
##                          pl2host: the probing is from planetlab nodes to CDN hosts
##                          cloud2host: the probing is from cloud nodes to CDN hosts
##          year ---- can be 2016 or 2017
#####################################################################################
def get_data_folder(period_key, probe_key, year):
    if "pl" in probe_key:
        if year == 2016:
            if "post" in period_key:
                source_data_folder = post_sb_pl_folder_2016
            else:
                source_data_folder = sb_pl_folder_2016
        else:
            if "post" in period_key:
                source_data_folder = post_sb_pl_folder_2017
            else:
                source_data_folder = sb_pl_folder_2017
    else:
        if year == 2016:
            if "post" in period_key:
                source_data_folder = post_sb_cloud_folder_2016
            else:
                source_data_folder = sb_cloud_folder_2016
        else:
            if "post" in period_key:
                source_data_folder = post_sb_cloud_folder_2017
            else:
                source_data_folder = sb_cloud_folder_2017
    return source_data_folder


if __name__ == '__main__':
    ## Convert all latency files for superbowl 2015
    # convert_pl2cloud_lats_2015("superbowl")
    # convert_pl2cloud_lats_2015("halftime")
    # convert_pl2cloud_lats_2015("postsuperbowl")


    ## Merge all latency files for super bowl 2016 or super bowl 2017
    period_key = "superbowl"
    # period_key = "halftime"
    # period_key = "postsuperbowl"
    # probe_key = "pl2cloud"
    probe_key = "cloud2cloud"
    # probe_key = "pl2host"
    # probe_key = "cloud2host"
    year = 2016
    # year = 2017
    merge_lats(period_key, probe_key, year)
















