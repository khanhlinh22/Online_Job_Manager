from rest_framework import pagination

class RecruitmentPaginator(pagination.PageNumberPagination):
    page_size = 3


class CommentPaginator(pagination.PageNumberPagination):
    page_size = 5