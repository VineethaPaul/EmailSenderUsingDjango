from django.urls import path
from tableview.views import *

urlpatterns = [
    path('', TableView.as_view(), name='tableview'),
    path('/short', ShortTableView.as_view(), name='short_tableview'),
    path('/toggle', ToggleTableView.as_view(), name='toggle_tableview'),
    path('/msodataupload', MsoDataUploadView.as_view(), name='mso_data_uploadview'),
]
