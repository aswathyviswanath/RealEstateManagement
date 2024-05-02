import random
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Ride
from .serializers import RideSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.pagination import PageNumberPagination
# from django.contrib.gis.geos import Point

class CustomPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    page_query_param = 'page_num'


class RideViewset(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = RideSerializer
    queryset = Ride.objects.all()
    pagination_class = CustomPagination

    def list(self, request):
        search_term = request.GET.get("search")
        queryset = self.queryset

        if search_term:

            queryset = queryset.filter(status__contains=search_term)

        paginated_queryset = self.paginate_queryset(queryset)

        serializer = RideSerializer(paginated_queryset, many=True)
        return self.get_paginated_response({'status': status.HTTP_200_OK, 'data': serializer.data})

    def destroy(self, *args, **kwargs):
        super().destroy(*args, **kwargs)
        return Response({'message': 'ride deleted succesfully'}, status=status.HTTP_200_OK)
    
    # @staticmethod
    # def update_ride_location(ride):
    #     # Simulate movement by updating ride's current location with random offsets
    #     ride.current_location = Point(
    #         ride.current_location.x + random.uniform(-0.01, 0.01),
    #         ride.current_location.y + random.uniform(-0.01, 0.01)
    #     )
    #     ride.save()
    

    # @action(detail=True, methods=['put'])
    # def update_location(self, request, pk=None):
    #     ride = self.get_object()
    #     latitude = request.data.get('latitude')
    #     longitude = request.data.get('longitude')
    #     if latitude is not None and longitude is not None:
    #         ride.current_location = Point(float(longitude), float(latitude))
    #         ride.save()
    #         return Response({'status': 'Location updated'}, status=status.HTTP_200_OK)
    #     else:
    #         return Response({'error': 'Latitude and longitude are required'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['put'])
    def start_ride(self, request, pk=None):
        ride = self.get_object()
        ride.status = 'STARTED'
        ride.save()
        return Response({'status': 'Ride started'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'])
    def complete_ride(self, request, pk=None):
        ride = self.get_object()
        ride.status = 'COMPLETED'
        ride.save()
        return Response({'status': 'Ride completed'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['put'])
    def cancel_ride(self, request, pk=None):
        ride = self.get_object()
        ride.status = 'CANCELLED'
        ride.save()
        return Response({'status': 'Ride cancelled'}, status=status.HTTP_200_OK)
