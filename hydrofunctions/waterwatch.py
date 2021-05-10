import requests
# import pandas as pd

# WaterWatch won't receive any new features but it will continue to operate.
url = "https://waterwatch.usgs.gov/webservices/floodstage"


def __get_flood_stages(site_number: str = None):
    """
    Retrieves flood stages for USGS stations.
    Args:
        param site_number: Optional USGS station number. If not provided flood stages for all stations are retrieved.

    Returns: Dictionary of station numbers and corresponding flood stages
    """
    # response formats: json | xml | csv
    params = {"format": "json"}
    if site_number:
        params['site'] = site_number
    res = requests.get(url, params=params)
    if res.ok:
        stages = res.json()
        return {
            site["site_no"]: {k: v for k, v in site.items() if k != "site_no"}
            for site in stages["sites"]
        }


def filter_flood_stages(all_flood_stages, sites_numbers=None):
    """Filters flood states of specific station numbers"""
    stations_stages = {}
    for site_nb in sites_numbers:
        try:
            stations_stages[site_nb] = all_flood_stages[site_nb]
        except KeyError:
            stations_stages[site_nb] = None
    return stations_stages


def get_flood_stage(sites_numbers=None, output_format=None):
    """
    Retrieves flood stages for a list of station numbers.
    Args:
        sites_numbers: List of strings of USGS site numbers.
        output_format: Optional output format. Returns dict if 'dict' else returns pd.DataFrame

    Returns: Dictionary of station numbers and their flood stages. If no flood stage for a station None is returned.

    Example
        >> stations = ["07144100", "07144101"]
        >> res = get_flood_stage(stations, output_format="dict")  # dictionary output
        >> print(res)
        {'07144100': {'action_stage': '20', 'flood_stage': '22', 'moderate_flood_stage': '25', 'major_flood_stage': '26'},
         '07144101': None}
        >> print(get_flood_stage(stations))
    """
    all_stages = __get_flood_stages()

    if sites_numbers:
        stations_stages = filter_flood_stages(all_stages, sites_numbers)
    else:
        stations_stages = all_stages

    # if output_format == "dict":
    return stations_stages
    # else:
    #     return pd.DataFrame(stations_stages).T
