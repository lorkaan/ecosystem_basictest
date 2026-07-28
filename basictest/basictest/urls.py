"""
URL configuration for basictest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse

def health(request):
    return JsonResponse({"status": "ok"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health),
    path(
        "api/users/",
        include("ecosystem_foundations.users.urls")
    ),
    path(
        "api/watchdog/",
        include("ecosystem_foundations.watchdog.urls")
    ),
    path(
        "api/automation/",
        include("ecosystem_foundations.automation.urls")
    ),
    path(
        "api/queries/",
        include("ecosystem_foundations.storedquery.urls")
    ),
    path(
        "api/labels/",
        include("ecosystem_foundations.labels.urls")
    ),
    path(
        "api/iam/",
        include("ecosystem_foundations.iam.urls")
    ),
    path(
        "api/global/",
        include("ecosystem_foundations.globalparams.urls")
    ),
    path(
        "api/alerts/",
        include("ecosystem_alerts.alerts.urls")
    ),
    path(
        "api/schedule/",
        include("ecosystem_schedule.schedule.urls")
    )
]
