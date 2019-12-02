# # -*- coding: utf-8 -*-
# #########################################################################
# #
# # Copyright (C) 2016 OSGeo
# #
# # This program is free software: you can redistribute it and/or modify
# # it under the terms of the GNU General Public License as published by
# # the Free Software Foundation, either version 3 of the License, or
# # (at your option) any later version.
# #
# # This program is distributed in the hope that it will be useful,
# # but WITHOUT ANY WARRANTY; without even the implied warranty of
# # MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# # GNU General Public License for more details.
# #
# # You should have received a copy of the GNU General Public License
# # along with this program. If not, see <http://www.gnu.org/licenses/>.
# #
# #########################################################################

from django.db.models import Q
from dal import autocomplete

from .models import Profile


class ProfileAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Profile.objects.all().exclude(Q(username='AnonymousUser') | Q(is_active=False))

        if self.q:
            qs = qs.filter(Q(username__icontains=self.q) | Q(email__icontains=self.q) | Q(first_name__icontains=self.q) | Q(last_name__icontains=self.q))
        
        return qs