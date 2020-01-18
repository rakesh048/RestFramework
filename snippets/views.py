from django.shortcuts import render
import json
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.permissions import IsAdminUser

################ using API View ###############################

# class SnippetList(APIView):
#
#     def get(self, request):
#         snippet = Snippet.objects.all()
#         serializer = SnippetSerializer(snippet, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

############# using generic view ########################################

class SnippetList(mixins.ListModelMixin,generics.GenericAPIView):
        queryset = Snippet.objects.all()
        serializer_class = SnippetSerializer
        permission_classes = [AllowAny]

        def get(self, request, *args, **kwargs):
            return self.list(request, *args, **kwargs)

############# using customise generic view ##########################################

class MultipleFieldLookupMixin(object):
    """
    Apply this mixin to any view or viewset to get multiple field filtering
    based on a `lookup_fields` attribute, instead of the default single field filtering.
    """

    def get_object(self):
        queryset = self.get_queryset()  # Get the base queryset
        queryset = self.filter_queryset(queryset)  # Apply any filter backends
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:  # Ignore empty fields.
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)  # Lookup the object
        self.check_object_permissions(self.request, obj)
        return obj

class SnippetDetail(MultipleFieldLookupMixin, mixins.DestroyModelMixin,generics.RetrieveAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    lookup_fields = ['pk']
    permission_classes = [AllowAny]

    #customise response based on our requirements

    def get(self, request, *args, **kwargs):
        response = super(SnippetDetail, self).get(request, *args, **kwargs)
        response.data['custom_value'] = 'list of current snippet'
        return Response({'data': response.data, 'success': True}, status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
