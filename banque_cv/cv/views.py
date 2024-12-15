from django.shortcuts import render, redirect
from .models import CV, Experience, Formation, Langue, Competence, Projet
from .forms import CVForm, ExperienceForm, FormationForm, LangueForm, CompetenceForm, ProjetForm
from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string

def home(request):
    cvs = CV.objects.all()
    paginator = Paginator(cvs, 10)  # 10 CVs par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cv/home.html', {'page_obj': page_obj})

def add_cv(request):
    if request.method == 'POST':
        form = CVForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CVForm()
    return render(request, 'cv/add_cv.html', {'form': form})

def generate_pdf(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    html_string = render_to_string('cv_template.html', {'cv': cv})
    html = HTML(string=html_string)
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="cv_{cv.etudiant.nom}.pdf"'
    return response

def send_email(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    email = Mail(
        from_email='your_email@example.com',
        to_emails='recipient@example.com',
        subject='Your CV',
        html_content='Here is your CV attached.',
    )
    # Attach the PDF
    email.add_attachment(...)
    sg = sendgrid.SendGridAPIClient('your_sendgrid_api_key')
    response = sg.send(email)
    return HttpResponse('Email sent!')

from django.core.mail import EmailMessage
from django.http import JsonResponse
from .models import CV
from .utils import send_cv_by_email

def send_cv_email_view(request, cv_id):
    if request.method == 'POST':
        recipient_email = request.POST.get('email')
        if recipient_email:
            try:
                send_cv_by_email(cv_id, recipient_email)
                return JsonResponse({'status': 'success', 'message': 'CV envoyé avec succès.'})
            except Exception as e:
                return JsonResponse({'status': 'error', 'message': str(e)})
        else:
            return JsonResponse({'status': 'error', 'message': 'Adresse email manquante.'})

from django.http import HttpResponse
from weasyprint import HTML
from django.template.loader import render_to_string
from .models import CV

def generate_pdf(request, cv_id):
    cv = CV.objects.get(id=cv_id)
    html_string = render_to_string('cv/cv_template.html', {'cv': cv})
    html = HTML(string=html_string)
    pdf_file = html.write_pdf()
    response = HttpResponse(pdf_file, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="cv_{cv.user.username}.pdf"'
    return response

