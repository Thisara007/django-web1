from django.http import HttpResponse
from .models import Collection,Piece
from django.views import generic

# Create your views here.
class index(generic.ListView):
    template_name ="genere\\generetemplates.html"
    def get_queryset(self):
        return Collection.objects.all

class details(generic.DeleteView):
   model = Collection
   template_name = "genere\\detailstemplates.html"
