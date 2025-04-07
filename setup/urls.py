"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from rest_framework import routers
from api_onechart.api import viewsets
from django.contrib import admin

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers, permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from api_onechart.api import viewsets
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="OneChart API",
        default_version='v1',
        description="Sistema para controle de partidas de Futebol",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contato@financeiro.com.br"),
        license=openapi.License(name="Free"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

router = routers.DefaultRouter()
router.register(r'clubes', viewsets.ClubeViewSet, basename="Clube")
router.register(r'jogadores', viewsets.JogadorViewSet, basename="Jogador")
router.register(r'partidas', viewsets.PartidaViewSet, basename="Partida")
router.register(r'torcidas', viewsets.TorcidaViewSet, basename="Torcida")
router.register(r'rankings', viewsets.RankingViewSet, basename="Ranking")
router.register(r'estatisticas', viewsets.EstatisticasViewSet, basename="Estatisticas")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]

urlpatterns += [
    path('swaggerjson/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)