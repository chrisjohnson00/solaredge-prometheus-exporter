from prometheus_client import core, exposition
from flask import Flask
from SolarEdge import SolarEdgeCollector
import os

application = Flask(__name__)


@application.route('/')
def hello():
    get_config("API_KEY")
    return "Welcome to the SolarEdge Prometheus Exporter.  The metrics can be found on /metrics"


@application.route('/metrics')
def metrics():
    registry = core.CollectorRegistry(auto_describe=False)
    registry.register(SolarEdgeCollector.SolarEdgeCollector(get_config("API_KEY")))
    return exposition.generate_latest(registry)


def get_config(key: str) -> str:
    if os.environ.get(key):
        return os.environ.get(key)
    raise Exception("{} environment variable not found".format(key))


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=8080)
