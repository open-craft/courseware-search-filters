from lms.lib.courseware_search.lms_filter_generator import LmsSearchFilterGenerator


class ExcludeCapaSearchFilterGenerator(LmsSearchFilterGenerator):
    """
    Class to provide a set of custom filters for the search. Inherits from the
    default LmsSearchFilterGenerator, which in turn inherits from
    edx-search.filter_generator.SearchFilterGenerator Use by setting
    SEARCH_FILTER_GENERATOR:
    "cloudera_search.filter.LmsCustomSearchFilterGenerator"

    This filter excludes CAPA results from searches, in addition to the
    defaults provided by LmsSearchFilterGenerator.
    """

    def exclude_dictionary(self, **kwargs):
        """
        Exclude CAPA results
        """
        exclude_dictionary = super(LmsSearchFilterGenerator, self).exclude_dictionary(
            **kwargs
        )
        exclude_dictionary["content_type"] = "CAPA"
        return exclude_dictionary
