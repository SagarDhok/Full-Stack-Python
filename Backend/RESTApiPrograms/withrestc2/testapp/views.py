# from django.shortcuts import render
# from rest_framework.views import APIView
# from rest_framework.response import Response

# class TestAPIView(APIView):
#     def get(self, request, *args, **kwargs):
#         colors = ['RED', 'YELLOW', 'GREEN', 'BLUE']
#         return Response({
#             'msg': 'Happy Valentines Day....',
#             'colors': colors
#         })

#     def put(self, request, *args, **kwargs):
#         return Response({'msg': 'This response from PUT method APIView'})

#     def delete(self, request, *args, **kwargs):
#         return Response({'msg': 'This response from DELETE method APIView'})

#     def patch(self, request, *args, **kwargs):
#         return Response({'msg': 'This response from PATCH method APIView'})


from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
class TestViewSet(ViewSet):
                def list(self,request):
                             colors = ['RED','YELLOW','GREEN','BLUE']
                             return Response({'msg':'RCB won the IPL Cup','colors':colors})


                def retrieve(self,request,pk=None):
                            return Response({'msg':'This response from RETRIEVE method ViewSet'})
                
                def update(self,request,pk=None):
                            return Response({'msg':'This response from UPDATE method ViewSet'})
                def partial_update(self,request,pk=None):
                           return Response({'msg':'This response from PARTIAL_UPDATE method ViewSet'})
                def destroy(self,request,pk=None):
                           return Response({'msg':'This response from DESTROY method ViewSet'})
