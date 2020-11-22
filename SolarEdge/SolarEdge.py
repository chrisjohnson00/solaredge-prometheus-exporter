from solaredge.api.client import Client
from SolarEdge.Sites import Sites
import datetime


class SolarEdge:
    def __init__(self, api_key):
        self.client = Client()
        self.client.set_api_key(api_key)
        self.client.sites = Sites(self.client)

    def get_sites(self):
        return self.client.sites.get_sites()

    def get_latest_reading_for_site(self, site_id):
        today = datetime.datetime.now()
        start_range = today.strftime("%Y-%m-%d 00:00:00")
        end_range = today.strftime("%Y-%m-%d %H:%M:%S")
        energy_details = self.client.sites.get_power(site_id, start_range,
                                                     end_range)
        values = energy_details['power']['values']
        last_reading = values.pop()
        last_value = 0 if last_reading['value'] is None else last_reading['value']
        return str(last_value)
