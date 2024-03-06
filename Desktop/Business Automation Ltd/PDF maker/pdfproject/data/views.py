from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm
from .models import Contact
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def home(request):
    form = ContactForm()
    contacts = Contact.objects.all()
    return render(request, 'home.html', {'form': form, 'contacts': contacts})

def save_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else: 
            return JsonResponse({'success': False})
        
def download_pdf(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    template_path = 'contact_pdf.html'
    context = {'contact': contact}
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="contact.pdf"'
    template = get_template(template_path)
    html = template.render(context)
    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response