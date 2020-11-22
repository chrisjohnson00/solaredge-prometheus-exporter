# solaredge-prometheus-exporter
A Prometheus exporter for SolarEdge solar panel monitoring

## Deploy

### Kubernetes with Helm

Update `deploy/helm/values.yaml` for your timezone and API key, then run:

    helm repo add chrisjohnson00 https://raw.githubusercontent.com/chrisjohnson00/helm-charts/master/
    helm repo update
    kubectl create ns solaredge
    helm upgrade solaredge chrisjohnson00/flask-chart --install --atomic -n solaredge -f deploy/helm/values.yaml

### Kubernetes

Update `deploy/manifests/deployment.yaml` for your timezone and API key, then run:

    kubectl create ns solaredge
    kubectl apply -f deploy/manifests/deployment.yaml


### Docker

   docker run -d -e API_KEY=YOUR_KEY -e TZ=YOURTZ -p 8080:8080 chrisjohnson00/solaredge-prometheus-exporter


## Prometheus configuration

If you are using Kubernetes, and have not disabled the default Prometheus annotation based scraping, you don't need to 
do anything with Prometheus, the deployments from this repo will include the appropriate annotations for Prometheus to 
pick it up.

If you aren't running in Kubernetes, here's what you need to know to configure it:

 - Port: 8080
 - Path: /metrics
 
## Prometheus metrics

The two metrics exposed by this exporter are:
 - `solaredge_site_peak` - The value provided is in `kw`
 - `solaredge_site_energy` - The value provided is in `w`
 
Included in all metrics are the following labels:
 - `site_id`
 - `site_name`

## Need help?

Submit an issue and I'll jump on it ASAP, thanks!
