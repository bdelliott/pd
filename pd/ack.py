import pd


def all():
    """List and ack all assigned incidents"""
    try:
        import pd_config as cfg
    except ImportError:
        raise Exception("Failed to find a 'pd_config' module with required config")

    api = pd.PagerDutyAPI(cfg.api_key, cfg.subdomain, cfg.user_id)
    
    incidents = api.list_incidents()

    if len(incidents) == 0:
        print "No assigned incidents."
        return

    for incident in incidents:
        print "Incident:"
        print "  Id: %(id)s" % incident
        print "  Status: %(status)s" % incident
        print "  Info: %(incident_key)s" % incident
        print "  Details: %(trigger_details_html_url)s" % incident

        incident_id = incident['id']
        print api.update_incident(incident_id)
