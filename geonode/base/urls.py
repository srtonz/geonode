import logging

from django.conf.urls import url
from django.conf import settings

from geonode.base.autocomplete_light_registry import (
    ResourceBaseAutocomplete, RegionAutocomplete,
    HierarchicalKeywordAutocomplete, ThesaurusKeywordLabelAutocomplete)

logger = logging.getLogger(__name__)


urlpatterns = [
    url(
        r'^autocomplete_response/$',
        ResourceBaseAutocomplete.as_view(),
        name='autocomplete_base',
    ),

    url(
        r'^autocomplete_region/$',
        RegionAutocomplete.as_view(),
        name='autocomplete_region',
    ),

    url(
        r'^autocomplete_hierachical_keyword/$',
        HierarchicalKeywordAutocomplete.as_view(),
        name='autocomplete_hierachical_keyword',
    ),
]


if hasattr(settings, 'THESAURUS') and settings.THESAURUS:
    thesaurus = settings.THESAURUS
    tname = thesaurus['name']
    ac_name = 'thesaurus_' + tname

    logger.debug('Registering thesaurus autocomplete for {}: {}'.format(tname, ac_name))

    urlpatterns.append(
        url(
        r'^thesaurus_inspire_themes/$',
        ThesaurusKeywordLabelAutocomplete.as_view(),
        name='thesaurus_inspire_themes',
        ),
    )
