from prometheus_client import core
from SolarEdge.SolarEdge import SolarEdge


class SolarEdgeCollector:
    """Collects metrics from SolarEdge APIs when requested from Prometheus."""

    def __init__(self, api_key):
        self.api_key = api_key
        self.client = SolarEdge(self.api_key)

    def collect(self):
        sites = self.client.get_sites()
        site_peak = core.GaugeMetricFamily('solaredge_site_peak', 'The peak power level for the site',
                                           labels=["site_id", "site_name"])
        site_energy = core.GaugeMetricFamily('solaredge_site_energy', 'The most recent energy level for the site',
                                             labels=["site_id", "site_name"])
        for site in sites['sites']['site']:
            site_peak.add_metric(labels=[str(site['id']), site['name']], value=str(site['peakPower']))
            yield site_peak
            site_energy.add_metric(labels=[str(site['id']), site['name']],
                                   value=self.client.get_latest_reading_for_site(site['id']))
            yield site_energy
