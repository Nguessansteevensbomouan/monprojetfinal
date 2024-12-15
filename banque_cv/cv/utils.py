from django.core.mail import EmailMessage
from weasyprint import HTML
from django.template.loader import render_to_string
from .models import CV

def send_cv_by_email(cv_id, recipient_email):
    """
    Fonction pour générer un CV en PDF et l'envoyer par email.
    """
    # Récupération des informations du CV
    cv = CV.objects.get(id=cv_id)
    experiences = cv.experiences.all()
    formations = cv.formations.all()
    langues = cv.langues.all()
    competences = cv.competences.all()
    projets = cv.projets.all()

    # Rendu HTML pour le PDF
    context = {
        'cv': cv,
        'experiences': experiences,
        'formations': formations,
        'langues': langues,
        'competences': competences,
        'projets': projets,
    }
    html_content = render_to_string('cv/cv_template.html', context)

    # Génération du fichier PDF
    pdf_file = HTML(string=html_content).write_pdf()

    # Configuration de l'email
    subject = f"CV de {cv.user.username}"
    message = "Veuillez trouver ci-joint le CV demandé."
    email = EmailMessage(subject, message, to=[recipient_email])
    email.attach(f"{cv.titre}.pdf", pdf_file, "application/pdf")

    # Envoi de l'email
    email.send()
