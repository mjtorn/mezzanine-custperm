from mezzanine.utils.importing import import_dotted_path

from django.conf import settings
from django.contrib import admin

def tweak(model, cust_func):
    """Overload the admin model with custom permissions
    """

    #print 'Tweaking %s at 0x%x, %s' % (model, id(model), cust_func)

    class CustomPermissionAdmin(admin.ModelAdmin):
        """Create a custom permission admin
        """

        queryset = cust_func

    bases = list(model.__bases__)
    bases_names = [b.__name__ for b in bases]
    oa_idx = bases_names.index('OwnableAdmin')
    bases.insert(oa_idx, CustomPermissionAdmin)
    model.__bases__ = tuple(bases)

if hasattr(settings, 'CUSTOM_PERMISSIONS'):
    for admin_model_name, cust_func_name in settings.CUSTOM_PERMISSIONS:
        admin_model = import_dotted_path(admin_model_name)
        cust_func = import_dotted_path(cust_func_name)

        tweak(admin_model, cust_func)

        #print '\t', [(id(b), b) for b in admin_model.__bases__]

# EOF

