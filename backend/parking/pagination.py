from rest_framework.pagination import PageNumberPagination


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 30

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        # Number of results in the current page
        response.data['num_results'] = len(data)
        return response
