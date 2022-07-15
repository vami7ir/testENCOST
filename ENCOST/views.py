from django.db.models import Q
from django.views.generic import TemplateView
from rest_framework import generics

from ENCOST.models import Duration, Client, Equipment, Mode
from ENCOST.serializers import DurationSerializer


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['clients'] = Client.objects.all()
        context['equipments'] = Equipment.objects.all()
        context['modes'] = Mode.objects.all()
        context['api_url'] = 'api_duration/'
        return context


class DurationListAPIView(generics.ListAPIView):
    serializer_class = DurationSerializer
    filterset_fields = ['client', 'equipment', 'mode', 'minutes']

    def get_queryset(self):
        queryset = Duration.objects.all()
        query = self.request.query_params
        if query['time_start']:
            time_start_param = query['time_start'].split(':')
            queryset.filter(
                start__hour=time_start_param[0],
                start__minute=time_start_param[1],
                start__second=time_start_param[2]
            ).distinct()
        elif query['time_stop']:
            time_stop_param = query['time_stop'].split(':')
            queryset.filter(
                stop__hour=time_stop_param[0],
                stop__minute=time_stop_param[1],
                stop__second=time_stop_param[2]
            ).distinct()
        elif query['data_start']:
            date_start_param = query['data_start'].split('-')
            queryset = Duration.objects.filter(
                start__year=date_start_param[0],
                start__month=date_start_param[1],
                start__day=date_start_param[2]
            ).distinct()
        elif query['data_stop']:
            date_stop_param = query['data_stop'].split('-')
            queryset.filter(
                stop__year=date_stop_param[0],
                stop__month=date_stop_param[1],
                stop__day=date_stop_param[2]
            ).distinct()
        return queryset
