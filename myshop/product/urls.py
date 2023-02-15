from django.urls import path
from .views import *

urlpatterns = [
    path('male/', MaleView.as_view(), name='male'),
    path('female/', FemaleView.as_view(), name='female'),
    path('jeans-female/', JeansListFemaleView.as_view(), name='jeans-female'),
    path('jeans-male/', JeansListMaleView.as_view(), name='jeans-male'),
    path('shirt-male/', ShirtListMaleView.as_view(), name='shirt-male'),
    path('shirt-female/', ShirtListFemaleView.as_view(), name='shirt-female'),
    path('tshirt-male/', TshirtListMaleView.as_view(), name='tshirt-male'),
    path(
        'tshirt-female/', TshirtListFemaleView.as_view(), name='tshirt-female'
    ),
    path('cap-male/', CapListMaleView.as_view(), name='cap-male'),
    path('cap-female/', CapListFemaleView.as_view(), name='cap-female'),
    path('scarf-male/', ScarfListMaleView.as_view(), name='scarf-male'),
    path('scarf-female/', ScarfListFemaleView.as_view(), name='scarf-female'),
    path(
        '<slug:sex>/<slug:category>/<slug:slug>/',
        ProductDetailView.as_view(),
        name='detail',
    ),
]
