"""
LMS Filter Generator Utilities File

Mocks certain classes used with testing to substitute creating
a django app. The django app with the installed apps were causing 
a lot of problems. This was a much easier and simpler solution
"""

class SearchFilterGenerator:
    """
    Creates mock SearchFilterGenerator class to be used with testing
    """
    def exclude_dictionary(self, **kwargs):  # pylint: disable=unused-argument
        """
        Exclude results
        """
        return dict()

class LmsSearchFilterGenerator(SearchFilterGenerator):
    """
    Creates mock LmsSearchFilterGenerator class to be used with testing
    """
