from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from usuarios.models import DatosExtras

class DatosExtrasInline(admin.StackedInline):
    model = DatosExtras
    can_delete = False
    verbose_name_plural = 'Datos Extras'

class CustomUserAdmin(UserAdmin):
    inlines = (DatosExtrasInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_hobbies')  # Agregar 'get_hobbies' a list_display

    def get_hobbies(self, obj):
        return obj.datosextras.hobbies if hasattr(obj, 'datosextras') else '-'  # Mostrar hobbies en el panel de administración

    get_hobbies.short_description = 'Hobbies'  # Personalizar el nombre de la columna en el panel de administración

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
