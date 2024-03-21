from django.shortcuts import render


def dashboard_view(request):
    from app.urls import urlpatterns
    context = {
        'urls': [get_name_and_url(u) for u in urlpatterns]
    }
    return render(request, "dashboard.html", context)


def get_name_and_url(url):
    name = getattr(url, 'app_name', None) or getattr(url, 'name', None)
    anchor = url.pattern._route
    return {'name': name, 'anchor': anchor}
