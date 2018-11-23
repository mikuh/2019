"""集合覆盖问题示例
用贪婪算法
"""

# 需要覆盖的州
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# 广播站覆盖范围
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()


def set_covered(states_needed, best_station=None, final_stations=set()):
    states_covered = set()
    for station, station_cover_states in stations.items():
        covered = states_needed & station_cover_states
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    states_needed -= states_covered
    final_stations.add(best_station)
    if states_needed:
        return set_covered(states_needed, best_station, final_stations)
    return final_stations


final_stations = set_covered(states_needed)
print(final_stations)
