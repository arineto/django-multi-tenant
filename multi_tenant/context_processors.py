def subdomain(request):
    return {
        'subdomain': request.subdomain
    }


def tenant(request):
    return {
        'tenant': request.tenant
    }
