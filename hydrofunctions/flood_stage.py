import requests

ResponseFormat = "json" # json, xml

# OLD web service dating to 2016; discontinued for new one?
url = "https://waterwatch.usgs.gov/webservices/floodstage"


def get_flood_stages(res_fmt: str = ResponseFormat):
    """Retrieves flood stages for all stations."""
    res = requests.get(url, params={"format": res_fmt})
    if res.ok:
        stages = res.json()
        return {site['site_no']: {k: v for k, v in site.items() if k != 'site_no'} for site in stages['sites']}

def get_flood_stage(stages, sites):
    """
    Retrieves flood stages for a list of station numbers.
    Args:
        sites: List of strings of site numbers.

    Returns: Dictionary of station numbers and their flood stages. If no flood stage for a station None is returned.

    """
    stations_stages = {}
    for site in sites:
        try:
            stations_stages[site] = stages[site]
        except KeyError:
            stations_stages[site] = None
    return stations_stages
