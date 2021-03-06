from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

from patient.models import HospitalHistory, Patient
from patient.serializers import PatientHospitalSerializer, PatientSerializer
from .serializers import HospitalSerializer
from .models import Hospital
from rest_framework import permissions, generics, mixins


# Create your views here.

class HospitalListAPIView(ListCreateAPIView):
    serializer_class = HospitalSerializer
    queryset = Hospital.objects.all()
    permission_classes = (permissions.AllowAny,)  # allowing everyone to see all registered hospital


'''
All of a hospitals patients history,
Create and get health bill or health detail of all patients
'''


class PatientsHospitalListView(generics.GenericAPIView, mixins.ListModelMixin,
                               mixins.CreateModelMixin):
    serializer_class = PatientHospitalSerializer
    queryset = HospitalHistory.objects.all()

    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated, IsAdminUser]
    #
    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create(request)


'''
All of a hospitals particular patients history,health bill or health detail
'''


class PatientHospitalDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                             mixins.DestroyModelMixin):
    serializer_class = PatientHospitalSerializer
    queryset = HospitalHistory.objects.all()
    lookup_field = 'code_no'  # default lookup_field is our primary key bur to use something different

    def get(self, request, code_no=None):
        return self.retrieve(request, code_no)

    def put(self, request, code_no=None):
        return self.update(request, code_no)

    def delete(self, request, code_no=None):
        return self.destroy(request, code_no)


'''
An hospital can create a patient and view all patients profile
'''


class PatientsListView(generics.ListAPIView):
    serializer_class = PatientSerializer

    def get_queryset(self):
        user = self.request.user
        return Patient.objects.filter(user=user)


class PatientsCreatView(generics.GenericAPIView, mixins.CreateModelMixin):
    serializer_class = PatientSerializer

    queryset = Patient.objects.all()

    def post(self, request):
        return self.create(request)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


'''
An hospital can view a particular patients profile details
'''


class PatientDetails(generics.GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    lookup_field = 'code_no'

    def get(self, request, code_no=None):
        return self.retrieve(request, code_no)

    def put(self, request, code_no=None):
        return self.update(request, code_no)

    def delete(self, request, code_no=None):
        return self.destroy(request, code_no)
