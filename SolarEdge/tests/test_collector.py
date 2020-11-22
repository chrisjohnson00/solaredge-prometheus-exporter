from SolarEdge.SolarEdgeCollector import SolarEdgeCollector
from SolarEdge.SolarEdge import SolarEdge
from unittest import mock
import prometheus_client
import collections


@mock.patch.object(prometheus_client.core.GaugeMetricFamily, 'add_metric')
def test_collect(mock_metric):
    collector = SolarEdgeCollector('x')
    mock_client = mock.Mock(SolarEdge)
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
    latest_reading = "5.0"
    client_attrs = {'get_sites.return_value': sites, 'get_latest_reading_for_site.return_value': latest_reading}
    mock_client.configure_mock(**client_attrs)
    collector.client = mock_client
    collections.deque(collector.collect())

    calls = [mock.call(labels=["12345", 'Johnson, Chris - 98765.00'], value="7.08"),
             mock.call(labels=["12345", 'Johnson, Chris - 98765.00'], value=latest_reading)]
    mock_metric.assert_has_calls(calls)
