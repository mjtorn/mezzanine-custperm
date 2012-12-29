mezzanine-custperm
==================

``mezzanine-custperm`` is based on monkey-patching an admin class. You define which
admin you want to patch and which function will be used as its ``queryset`` method.

Usage
-----

INSTALLED_APPS = (
    ..., # Theme or whatever
   'mezzacustperm',
   'django.contrib.admin,
   ...
)

CUSTOM_PERMISSIONS = (
   ('mezzanine.blog.admin.BlogPostAdmin', 'your_site.utils.custom_permissions.allow_editors'),
)

Then what `your_site.utils.custom_permissions.allow_editors` might look like:

def allow_editors(self, request):
  """Method-like function to use with custom permission admins
  """

  qs = self.model._default_manager.get_query_set()

  ordering = self.get_ordering(request)
  if ordering:
      qs = qs.order_by(*ordering)

  if request.user.is_superuser:
      return qs
  elif request.user.groups.filter(name__icontains='editors').exists():
      return qs

    return qs.none()

Notes
-----

This should be safe to be used everywhere, as in no thread-safety kind of issues, but there's no warranty.

You can chain these into eg. `BlogPostAdmin` by defining many `CUSTOM_PERMISSIONS`
