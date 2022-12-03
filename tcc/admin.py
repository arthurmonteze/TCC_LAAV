from django.contrib import admin

from .models import Dispositivo
from .models import Professor
from .models import Secretaria
from .models import Usuario

admin.site.register(Dispositivo)
admin.site.register(Professor)
admin.site.register(Secretaria)
admin.site.register(Usuario)