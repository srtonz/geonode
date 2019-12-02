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

from dal import autocomplete

from guardian.shortcuts import get_objects_for_user
from django.conf import settings
from geonode.security.utils import get_visible_resources

from models import ResourceBase, Region, HierarchicalKeyword, ThesaurusKeywordLabel


class ResourceBaseAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        request = self.request

        permitted = get_objects_for_user(request.user, 'base.view_resourcebase')
        qs = ResourceBase.objects.all().filter(id__in=permitted)

        if self.q:
            qs = qs.filter(title__icontains=self.q).order_by('title')[:100]
            
        return get_visible_resources(
            qs,
            request.user if request else None,
            admin_approval_required=settings.ADMIN_MODERATE_UPLOADS,
            unpublished_not_visible=settings.RESOURCE_PUBLISHING,
            private_groups_not_visibile=settings.GROUP_PRIVATE_RESOURCES)


class RegionAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = Region.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)
        
        return qs


class HierarchicalKeywordAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        qs = HierarchicalKeyword.objects.all()

        if self.q:
            qs = qs.filter(slug__icontains=self.q)
        
        return qs


class ThesaurusKeywordLabelAutocomplete(autocomplete.Select2QuerySetView):

    def get_queryset(self):
        thesaurus = settings.THESAURUS
        tname = thesaurus['name']
        lang = 'en'
        ThesaurusKeywordLabel.objects.all().filter(lang=lang)


        if self.q:
            qs = qs.filter(keyword__thesaurus__identifier=tname)
        
        return qs
