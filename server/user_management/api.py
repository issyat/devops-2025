from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'status': 'API is working',
        'version': '1.0',
        'endpoints': {
            'metrics': reverse('prometheus-django-metrics', request=request),
        }
    })
