from solaredge.api.sites import Sites
from solaredge.api.error import IdentifierError
import requests
BASE_URL = 'https://monitoringapi.solaredge.com'


class Sites(Sites):
    def get_full_energy_details(self, site_id, start_time, end_time, time_unit):
        """
        get_energy_details in the super class actually calls "site energy", not "site energy details", this method
        calls the "site energy details" api
        Parameters:
            site_id (int): the ID of a site location (can be fetched from the get_sites function)
            start_time (string): the start date from when you want metrics (in the format yyyy-MM-DD hh:mm:ss)
            end_time (string): the end date until when you want metrics (in the format yyyy-MM-DD hh:mm:ss)
            time_unit (string): the unit to break data into
        Returns:
            response (json): a JSON dictionary containing the energy details for a site
        """
        if not site_id or not start_time or not end_time:
            raise IdentifierError("This API call needs to have a site_id, start_time and end_time.")

        api_endpoint = '/site/%s/energyDetails' % site_id
        full_api_url = BASE_URL + api_endpoint

        parameters = {
            'startTime': start_time,
            'endTime': end_time,
            'timeUnit': time_unit,
            'api_key': self.client.get_api_key()
        }

        response = requests.get(full_api_url, params=parameters)
        return response.json()

    def get_power(self, site_id, start_time, end_time):
        """
        Return the site power measurements in 15 minutes resolution
        Parameters:
            site_id (int): the ID of a site location (can be fetched from the get_sites function)
            start_time (string): the start date from when you want metrics (in the format yyyy-MM-DD hh:mm:ss)
            end_time (string): the end date until when you want metrics (in the format yyyy-MM-DD hh:mm:ss)
        Returns:
            response (json): a JSON dictionary containing the energy details for a site
        """
        if not site_id or not start_time or not end_time:
            raise IdentifierError("This API call needs to have a site_id, start_time and end_time.")

        api_endpoint = '/site/%s/power' % site_id
        full_api_url = BASE_URL + api_endpoint

        parameters = {
            'startTime': start_time,
            'endTime': end_time,
            'api_key': self.client.get_api_key()
        }

        response = requests.get(full_api_url, params=parameters)
        return response.json()
