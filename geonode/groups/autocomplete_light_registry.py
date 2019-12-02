# -*- coding: utf-8 -*-
#########################################################################
#
# Copyright (C) 2016 OSGeo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#########################################################################

from django.db.models import Q
from dal import autocomplete

from .models import GroupProfile, GroupCategory


class GroupProfileAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = GroupProfile.objects.all()

        if self.q:
            qs = qs.filter(Q(title__istartswith=self.q))
        
        return qs

class GroupCategoryAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):

        qs = GroupCategory.objects.all()


        if self.q:
            qs = qs.filter(Q(name__icontains=self.q))
        
        return qs

