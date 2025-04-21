
from rest_framework.decorators import action

from rest_framework import viewsets, generics, permissions, parsers, status
from rest_framework.response import Response

from . import  serializers,paginators
from .models import Category, Recruitment, New, User,Comment, Like
from . import perms


class CategoryViewsSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Category.objects.filter(active=True)
    serializer_class = serializers.CategorySerializer

class RecruitmentViewSet(viewsets.ViewSet, generics.ListAPIView):
    queryset = Recruitment.objects.filter(active=True)
    serializer_class = serializers.RecruitmentSerializer
    pagination_class = paginators.RecruitmentPaginator

    def get_queryset(self):
        query = self.queryset

        q = self.request.query_params.get('q')
        if q:
            query =query.filter(subject__icontains = q)

        cate_id =self.request.query_params.get('category_id')
        if cate_id:
                query = query.filter(category_id = cate_id)

        return query

    @action(methods=['get'], url_path='news', detail=True)
    def get_news(self, request, pk):
        news = self.get_object().new_set.filter(active=True)
        return Response(serializers.NewSerializer(news,many=True).data)

class NewViewSet(viewsets.ViewSet, generics.RetrieveAPIView):
    queryset = New.objects.prefetch_related('tags').filter(active = True)
    serializer_class = serializers.NewDetailSerializer

    def get_permissions(self):
        if self.action.__eq__('get_comments'):
            if self.request.method in ['POST']:
                return [permissions.IsAuthenticated()]
        elif self.action.__eq__('like'):
                return [permissions.IsAuthenticated()]

        return [permissions.AllowAny()]

    @action(methods=['get','post'], url_path='comments', detail = True)
    def get_comments(self, request, pk):
        if request.method.__eq__('POST'):
            t = serializers.CommentSerializer(data={
                'content': request.data.get('content'),
                'user': request.user.pk,
                'new': pk
            })
            t.is_valid(raise_exception=True)

            c = t.save()
            return Response(serializers.CommentSerializer(c).data, status=status.HTTP_201_CREATED)
        else:
           comments = self.get_object().comment_set.select_related('user').filter(active = True)
           p = paginators.CommentPaginator()
           page = p.paginate_queryset(comments, self.request)
           if page is not None:
                serializer =serializers.CommentSerializer(page, many=True)
                return p.get_paginated_response(serializer.data)
           else:
               return Response(serializers.CommentSerializer(comments, many=True).data)

    @action(methods=['post'], url_path='like', detail= True)
    def like(self, request, pk):
        li, created = Like.objects.get_or_create(user=request.user, new=self.get_object())

        if not created:
            li.active = not li.active

        li.save()

        return Response(serializers.NewDetailSerializer(self.get_object(), context={'request': request}).data)

class CommentViewSet(viewsets.ViewSet, generics.DestroyAPIView, generics.UpdateAPIView):
    queryset = Comment.objects.filter(active = True)
    serializer_class = serializers.CommentSerializer
    permission_classes = [perms.OwnerPerms]

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset =  User.objects.filter(is_active = True)
    serializer_class = serializers.UserSerializer
    parser_classes = [parsers.MultiPartParser]


    @action(methods=['get', 'patch'], url_path='current-user', detail=False, permission_classes=[permissions.IsAuthenticated])
    #detail false vi khong the ma co id ma tim lay duoc user
    def get_user(self,request):
        u = request.user
        if request.method.__eq__('PATCH'):
            for k,v in request.data.items():
                if k in ['first_name','last_name']:
                    setattr(u,k,v)
                elif k.__eq__('passowrd'):
                    u.set_password(v)
            u.save()
        return Response(serializers.UserSerializer(u).data)

