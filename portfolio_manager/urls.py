from django.urls import path, include
from portfolio_manager.views import PortfolioView, FileDownloadView
urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('download_file', FileDownloadView.as_view(), name='file_download'),
]
