from .models import Socio

def context_socios(request):
    return {
        'socios': Socio.objects.all()
    }