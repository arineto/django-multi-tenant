def subdomain(request):
    return {
        'subdomain': request.subdomain
    }


def tenant(request):
    return {
        'tenant': request.tenant
    }


def theme(request):
    return {
        'theme': request.tenant.theme if request.tenant else None
    }
