from sample.views import list_samples

def home_page(request):
    return list_samples(request)
