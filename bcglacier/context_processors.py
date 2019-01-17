from .models import Parks

def basetest(request):

    plist = Parks.objects.values_list("name", flat=True)
    return {
        'parks': plist
    }
