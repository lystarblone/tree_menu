from django.template.response import TemplateResponse

def index_view(request):
    return TemplateResponse(request, 'menu/index.html', {'request': request})