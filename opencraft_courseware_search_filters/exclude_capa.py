"""
Create ExcludeCapaSearchFilterGenerator from LmsSearchFilterGenerator
"""
from lms.lib.courseware_search.lms_filter_generator import LmsSearchFilterGenerator


class ExcludeCapaSearchFilterGenerator(LmsSearchFilterGenerator):  # pylint: disable=too-few-public-methods
    """
    Class to provide a set of custom filters for the search. Inherits from the
    default LmsSearchFilterGenerator, which in turn inherits from
    edx-search.filter_generator.SearchFilterGenerator Use by setting
    SEARCH_FILTER_GENERATOR: "opencraft_courseware_search_filters.ExcludeCapaSearchFilterGenerator"

    This filter excludes CAPA results from searches, in addition to the
    defaults provided by LmsSearchFilterGenerator.
    """

    def exclude_dictionary(self, **kwargs):
        """
        Exclude CAPA results
        """
        exclude_dictionary = super().exclude_dictionary(
            **kwargs
        )
        exclude_dictionary["content_type"] = "CAPA"
        return exclude_dictionary
