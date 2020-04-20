from django.urls import path
import PolyCloudService.views

urlpatterns = [
    path('PolyCloudAppService', PolyCloudService.views.app_service),
    path('login', PolyCloudService.views.login),
    path('register', PolyCloudService.views.register),
    path('ChangePassword', PolyCloudService.views.change_password),
    path('GenPolymerData', PolyCloudService.views.generate_main_activity_plastics_data),
    path('GetMaterialName', PolyCloudService.views.get_material_list_activity_data),
    path('GetMaterialNo', PolyCloudService.views.get_polymer_no_list_activity_data),
    path('GetMaterialDetail', PolyCloudService.views.get_material_detail),
    path('SearchMaterial', PolyCloudService.views.search_material),
    path('GetMonitorData', PolyCloudService.views.gen_monitor_data),
]
