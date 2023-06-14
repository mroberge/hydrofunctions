"""
test_online_resources
----------------------------------

This module can be used to check whether various online data servers are up
and returning the expected data.

These tests have all been named so that they will not be included in
the normal test suite using unittest or pytest.

List of Valid URL's for NWIS
----------------------------
Paste these into a web browser or use curl to use these URL's.


List of URL's that Return Errors or Specific Conditions

200: good request, but no data have been collected in this period.
https://waterservices.usgs.gov/nwis/iv/?format=json%2C1.1&sites=01541180&parameterCd=00060&period=P10D

400: didn't select a site
https://waterservices.usgs.gov/nwis/dv/?format=json%2C1.1&parameterCd=00060&startDT=2017-01-01&endDT=2017-12-31

400: site names are too short to be right, should be 8 digits
https://waterservices.usgs.gov/nwis/dv/?format=json%2C1.1&sites=51059%2C51061&parameterCd=00060&startDT=2017-01-01&endDT=2017-12-31

400: wrote countyCd twice
https://waterservices.usgs.gov/nwis/dv/?format=json%2C1.1&countyCd=51059&countyCd=51061&parameterCd=00060&startDT=2017-01-01&endDT=2017-12-31
"""
from hydrofunctions import hydrofunctions as hf

def will_NWIS_return_200_response():
    """This test should not be run as a part of the normal test suite.
    This is a resource test only!
    Because of the function name, it is not discoverable by Unittest or pytest.
    """

    expected = 200
    response = hf.get_nwis("01585200", "dv", "2001-01-01", "2001-01-02")
    actual = response.status_code
    assert expected == actual
    print("NWIS is up and running!")


if __name__ == "__main__":
    will_NWIS_return_200_response()
