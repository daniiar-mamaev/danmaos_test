from rest_framework import views
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response


class MyGenericListCreateView(views.APIView):
    queryset = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


class MyGenericRetrieveUpdateDestroyView(views.APIView):
    queryset = None
    serializer_class = None

    def get_objects(self, pk):
        # try:
        #     return self.queryset.get(id=pk)
        # except self.queryset.DoesNotExist:
        #     return Response({'detail': 'No object'}, status=404)
        return get_object_or_404(self.queryset.all(), pk=pk)

    def get(self, request, pk, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_objects(pk))
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_objects(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        self.get_objects(pk).delete()
        return Response(status=204)