from django.urls import path
from .views import home, add_cv, generate_pdf, send_email

urlpatterns = [
    path('', home, name='home'),
    path('add/', add_cv, name='add_cv'),
    path('generate-pdf/<int:cv_id>/', generate_pdf, name='generate_pdf'),
    path('send-email/<int:cv_id>/', send_email, name='send_email'),
]
