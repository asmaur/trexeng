from django.shortcuts import render, HttpResponse
import json
# Create your views here.

def index(request):
    return render(request, "trexapp/index.html")

def sobre(request):
    return render(request, "trexapp/sobre.html")

def contato(request):
    return render(request, "trexapp/contato.html")

def ppci(request):
    return render(request, "trexapp/ppci.html")

def eletricos(request):
    return render(request, "trexapp/eletrico.html")

def estruturas(request):
    return render(request, "trexapp/estrutura.html")

def bim_3d(request):
    return render(request, "trexapp/bim-3d.html")

def hidro_sanitarios(request):
    return render(request, "trexapp/hidro-sanitario.html")

def reformas(request):
    return render(request, "trexapp/reforma.html")


def contact_message(request):
    message = None  # "Erro ao enviar a mensagem ..!"
    resp = 'resposta sent'
    data = json.loads(request.body.decode("utf-8"))
    print(data['full_name'])

    if request.method == "POST":
        name = data['full_name']
        company = data['company_name']
        mail = data['email']
        phone = data['phone']
        subject = data['subject']
        mes = data['message']

        message = 'Company: ' + company + '\n' + 'Subjet: ' + subject + '\n' + 'Phone: ' + phone + '\n' + 'Email: ' + mail + '\n' + 'message: ' + mes
        print(message)
        # reply_to = [mail],from_email=mail,headers={'Content-Type': 'text/plain'},
        try:
            ctx = {
                'name': name,
                'company': company,
                'subject': subject,
                'phone': phone,
                'message': mes
            }
            mailing = render_to_string('mercato/sentmail.htm', ctx)
            email = EmailMessage(
                subject,
                mailing,
                from_email='contact@br-mercato.com',
                to=['contact@br-mercato.com'],
                reply_to=[mail],

            )
            email.content_subtype = 'html'
            email.send()

            # send_mail(subject, message, mail, ['contact@br-mercato.com'])
            resp = {"sent": True}

        except Exception as ex:

            print(ex)
            resp = {"sent": False}

    return HttpResponse(status=200, content_type='application/json', content=json.dumps(resp))


def error_404_view(request, exception):
    return render(request, 'mercato/error.html', {}, status=404)


def error_403_view(request, exception):
    return render(request, 'mercato/error.html', {}, status=403)