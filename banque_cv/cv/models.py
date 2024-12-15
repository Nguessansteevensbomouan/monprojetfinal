from django.db import models
from users.models import User

class CV(models.Model):
    titre = models.CharField(max_length=100)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cv')

class Experience(models.Model):
    poste = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    description = models.TextField()
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='experiences')

class Formation(models.Model):
    diplome = models.CharField(max_length=100)
    etablissement = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField(null=True, blank=True)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='formations')

class Langue(models.Model):
    libelle = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='langues')

class Competence(models.Model):
    libelle = models.CharField(max_length=50)
    niveau = models.CharField(max_length=50)
    cv = models.ForeignKey(CV, on_delete=models.CASCADE, related_name='competences')

from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from users.models import User

def generate_cv_pdf(request, user_id):
    user = User.objects.get(id=user_id)
    html_content = render_to_string('cv_template.html', {'user': user})
    pdf_file = HTML(string=html_content).write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="cv_{user.username}.pdf"'
    return response

from django.core.mail import EmailMessage

def send_cv_email(request, user_id):
    user = User.objects.get(id=user_id)
    email = EmailMessage(
        'Votre CV',
        'Veuillez trouver en pièce jointe votre CV généré.',
        'from@example.com',
        [user.email],
    )
    pdf_content = generate_cv_pdf(request, user_id).content
    email.attach(f'cv_{user.username}.pdf', pdf_content, 'application/pdf')
    email.send()

