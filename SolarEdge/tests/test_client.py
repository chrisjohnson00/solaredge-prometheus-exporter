from SolarEdge.SolarEdge import SolarEdge
from SolarEdge.Sites import Sites as mySites
from solaredge.api.client import Client, Sites
from unittest import mock
import pytest


def test_get_sites():
    # create mocks
    mock_site = mock.Mock(Sites)
    sites = {'sites': {'count': 1, 'site': [
        {'id': 12345, 'name': 'Johnson, Chris - 98765.00', 'accountId': 54321, 'status': 'Active', 'peakPower': 7.08,
         'lastUpdateTime': '2020-11-22', 'installationDate': '2018-10-10', 'ptoDate': '2018-10-28', 'notes': '',
         'type': 'Optimizers & Inverters',
         'primaryModule': {'manufacturerName': 'Mission Solar', 'modelName': 'MSE295SQ5T', 'maximumPower': 295.0},
         'uris': {'SITE_IMAGE': '/site/12345/siteImage/Johnson,%20Chris%20-%20Site%20Image.jpg',
                  'DATA_PERIOD': '/site/12345/dataPeriod',
                  'INSTALLER_IMAGE': '/site/12345/installerImage/SolarEdge%2520Image.png',
                  'DETAILS': '/site/12345/details', 'OVERVIEW': '/site/12345/overview'},
         'publicSettings': {'isPublic': False}}]}}

    site_attrs = {'get_sites.return_value': sites}
    mock_site.configure_mock(**site_attrs)
    mock_client = mock.Mock(Client)
    client_attrs = {'sites': mock_site}
    mock_client.configure_mock(**client_attrs)
    client = SolarEdge('X')
    client.client = mock_client
    assert client.get_sites() == sites


@pytest.mark.parametrize("details,expected",
                         [({'power': {'timeUnit': 'QUARTER_OF_AN_HOUR', 'unit': 'W', 'measuredBy': 'INVERTER',
                                      'values': [{'date': '2020-11-23 00:00:00', 'value': None},
                                                 {'date': '2020-11-23 00:15:00', 'value': None},
                                                 {'date': '2020-11-23 00:30:00', 'value': None},
                                                 {'date': '2020-11-23 00:45:00', 'value': None},
                                                 {'date': '2020-11-23 01:00:00', 'value': None},
                                                 {'date': '2020-11-23 01:15:00', 'value': None},
                                                 {'date': '2020-11-23 01:30:00', 'value': None},
                                                 {'date': '2020-11-23 01:45:00', 'value': None},
                                                 {'date': '2020-11-23 02:00:00', 'value': None},
                                                 {'date': '2020-11-23 02:15:00', 'value': None},
                                                 {'date': '2020-11-23 02:30:00', 'value': None},
                                                 {'date': '2020-11-23 02:45:00', 'value': None},
                                                 {'date': '2020-11-23 03:00:00', 'value': None},
                                                 {'date': '2020-11-23 03:15:00', 'value': None},
                                                 {'date': '2020-11-23 03:30:00', 'value': None},
                                                 {'date': '2020-11-23 03:45:00', 'value': None},
                                                 {'date': '2020-11-23 04:00:00', 'value': None},
                                                 {'date': '2020-11-23 04:15:00', 'value': None},
                                                 {'date': '2020-11-23 04:30:00', 'value': None},
                                                 {'date': '2020-11-23 04:45:00', 'value': None},
                                                 {'date': '2020-11-23 05:00:00', 'value': None},
                                                 {'date': '2020-11-23 05:15:00', 'value': None},
                                                 {'date': '2020-11-23 05:30:00', 'value': None},
                                                 {'date': '2020-11-23 05:45:00', 'value': None},
                                                 {'date': '2020-11-23 06:00:00', 'value': None},
                                                 {'date': '2020-11-23 06:15:00', 'value': None},
                                                 {'date': '2020-11-23 06:30:00', 'value': None},
                                                 {'date': '2020-11-23 06:45:00', 'value': 0.0},
                                                 {'date': '2020-11-23 07:00:00', 'value': 7.609861},
                                                 {'date': '2020-11-23 07:15:00', 'value': 368.38998},
                                                 {'date': '2020-11-23 07:30:00', 'value': 899.25885},
                                                 {'date': '2020-11-23 07:45:00', 'value': 1310.3344},
                                                 {'date': '2020-11-23 08:00:00', 'value': 1744.3247},
                                                 {'date': '2020-11-23 08:15:00', 'value': 2054.188},
                                                 {'date': '2020-11-23 08:30:00', 'value': 2345.9941},
                                                 {'date': '2020-11-23 08:45:00', 'value': 2692.443},
                                                 {'date': '2020-11-23 09:00:00', 'value': 3007.5164},
                                                 {'date': '2020-11-23 09:15:00', 'value': 3382.6335},
                                                 {'date': '2020-11-23 09:30:00', 'value': 3769.2332},
                                                 {'date': '2020-11-23 09:45:00', 'value': 4041.636},
                                                 {'date': '2020-11-23 10:00:00', 'value': 4161.5317},
                                                 {'date': '2020-11-23 10:15:00', 'value': 4441.122},
                                                 {'date': '2020-11-23 10:30:00', 'value': 4533.564},
                                                 {'date': '2020-11-23 10:45:00', 'value': 4587.6016},
                                                 {'date': '2020-11-23 11:00:00', 'value': 4648.775},
                                                 {'date': '2020-11-23 11:15:00', 'value': 4668.177},
                                                 {'date': '2020-11-23 11:30:00', 'value': 4663.3237},
                                                 {'date': '2020-11-23 11:45:00', 'value': 4588.056},
                                                 {'date': '2020-11-23 12:00:00', 'value': 4512.6567},
                                                 {'date': '2020-11-23 12:15:00', 'value': 4489.872},
                                                 {'date': '2020-11-23 12:30:00', 'value': 4392.8555},
                                                 {'date': '2020-11-23 12:45:00', 'value': 4265.3535},
                                                 {'date': '2020-11-23 13:00:00', 'value': 4086.3923},
                                                 {'date': '2020-11-23 13:15:00', 'value': 3859.571},
                                                 {'date': '2020-11-23 13:30:00', 'value': 3648.2664},
                                                 {'date': '2020-11-23 13:45:00', 'value': 3536.7324}]}}, '3536.7324'),
                          ({'power': {'timeUnit': 'QUARTER_OF_AN_HOUR', 'unit': 'W', 'measuredBy': 'INVERTER',
                                      'values': [{'date': '2020-11-23 00:00:00', 'value': None},
                                                 {'date': '2020-11-23 00:15:00', 'value': None},
                                                 {'date': '2020-11-23 00:30:00', 'value': None},
                                                 {'date': '2020-11-23 00:45:00', 'value': None},
                                                 {'date': '2020-11-23 01:00:00', 'value': None},
                                                 {'date': '2020-11-23 01:15:00', 'value': None},
                                                 {'date': '2020-11-23 01:30:00', 'value': None},
                                                 {'date': '2020-11-23 01:45:00', 'value': None},
                                                 {'date': '2020-11-23 02:00:00', 'value': None},
                                                 {'date': '2020-11-23 02:15:00', 'value': None},
                                                 {'date': '2020-11-23 02:30:00', 'value': None},
                                                 {'date': '2020-11-23 02:45:00', 'value': None},
                                                 {'date': '2020-11-23 03:00:00', 'value': None},
                                                 {'date': '2020-11-23 03:15:00', 'value': None},
                                                 {'date': '2020-11-23 03:30:00', 'value': None},
                                                 {'date': '2020-11-23 03:45:00', 'value': None},
                                                 {'date': '2020-11-23 04:00:00', 'value': None},
                                                 {'date': '2020-11-23 04:15:00', 'value': None},
                                                 {'date': '2020-11-23 04:30:00', 'value': None},
                                                 {'date': '2020-11-23 04:45:00', 'value': None},
                                                 {'date': '2020-11-23 05:00:00', 'value': None},
                                                 {'date': '2020-11-23 05:15:00', 'value': None},
                                                 {'date': '2020-11-23 05:30:00', 'value': None},
                                                 {'date': '2020-11-23 05:45:00', 'value': None},
                                                 {'date': '2020-11-23 06:00:00', 'value': None},
                                                 {'date': '2020-11-23 06:15:00', 'value': None},
                                                 {'date': '2020-11-23 06:30:00', 'value': None}]}}, '0')])
def test_get_latest_reading_for_site(details, expected):
    # create mocks
    mock_site = mock.Mock(mySites)
    site_attrs = {'get_power.return_value': details}
    mock_site.configure_mock(**site_attrs)
    mock_client = mock.Mock(Client)
    client_attrs = {'sites': mock_site}
    mock_client.configure_mock(**client_attrs)
    client = SolarEdge('X')
    client.client = mock_client
    assert client.get_latest_reading_for_site(0) == expected
