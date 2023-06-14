from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from django.urls.conf import re_path
from rest_framework.routers import DefaultRouter

from .views import (
    CriteriaViewSet,
    NiokrProjectCreateView,
    NiokrProjectDeleteView,
    NiokrProjectDetailView,
    NiokrProjectsDatesView,
    NiokrProjectsOutputView,
    NiokrProjectUpdateView,
    NiokrUserCreateView,
    NiokrUserView,
    ProjectCreateView,
    ProjectDeleteView,
    ProjectDetailView,
    ProjectsDatesView,
    ProjectsOutputView,
    ProjectUpdateView,
    ProjectViewSet,
    EquipmentsOutputView,
    EquipmentCreateView,
    UserNiokrProjectsOutputView,
    UserProjectsOutputView,
    UmnikProjectsOutputView,
    USSProjectsOutputView,
    NIOKRViewSet,
    NIOKRCriteriaViewSet,
    ProjectsExcelDownload,
    add_responsible,
    change_criteria,
    change_niokr_criteria,
    add_umnik,
    delete_umnik,
    add_uss,
    delete_uss,
)

router = DefaultRouter()
router.register(r"api/projects", ProjectViewSet)
router.register(r"api/criteria", CriteriaViewSet)
router.register(r"api/niokr", NIOKRViewSet)
router.register(r"api/niokr_criteria", NIOKRCriteriaViewSet)

urlpatterns = [
    path("", ProjectsOutputView.as_view(), name="index_url"),
    path("projects/", ProjectsOutputView.as_view(), name="projects_list_url"),
    path(
        "projects/<int:pk>/",
        ProjectDetailView.as_view(),
        name="project_detail_url",
    ),
    path(
        "project_delete/<int:pk>/",
        ProjectDeleteView.as_view(),
        name="project_delete_url",
    ),
    path(
        "project_update/<int:pk>",
        ProjectUpdateView.as_view(),
        name="project_update_url",
    ),
    path(
        "download_projects/",
        ProjectsExcelDownload.as_view(),
        name="download_excel_url",
    ),
    path("projects/create/", ProjectCreateView.as_view(), name="project_create_url"),

    path("equipments/", EquipmentsOutputView.as_view(), name="equipments_list_url"),
    path("equipments/create/", EquipmentCreateView.as_view(), name="equipment_create_url"),

    path(
        "my_projects/",
        UserProjectsOutputView.as_view(),
        name="user_projects_list_url",
    ),
    path(
        "my_umnik/",
        UmnikProjectsOutputView.as_view(),
        name="umnik_projects_list_url",
    ),
    path(
        "my_uss/",
        USSProjectsOutputView.as_view(),
        name="uss_projects_list_url",
    ),
    path(
        "project/<int:pk>/",
        ProjectsOutputView.as_view(),
        name="project_output_pk_url",
    ),
    path("change_criteria/", change_criteria, name="change_criteria"),
    path("add_responsible/", add_responsible, name="add_responsible"),
    path("api/project-dates/", ProjectsDatesView.as_view()),
    path("niokr/", NiokrProjectsOutputView.as_view(), name="niokr_index_url"),
    path(
        "niokr_user/<int:pk>/",
        NiokrUserView.as_view(),
        name="niokr_user_url",
    ),
    path(
        "niokr_projects/",
        NiokrProjectsOutputView.as_view(),
        name="niokr_projects_list_url",
    ),
    path(
        "niokr_projects/<int:pk>/",
        NiokrProjectDetailView.as_view(),
        name="niokr_project_detail_url",
    ),
    path(
        "niokr_project_delete/<int:pk>/",
        NiokrProjectDeleteView.as_view(),
        name="niokr_project_delete_url",
    ),
    path(
        "niokr_project_update/<int:pk>",
        NiokrProjectUpdateView.as_view(),
        name="niokr_project_update_url",
    ),
    path(
        "niokr_projects/create/",
        NiokrProjectCreateView.as_view(),
        name="niokr_project_create_url",
    ),
    path(
        "niokr_user/create/",
        NiokrUserCreateView.as_view(),
        name="niokr_user_create_url",
    ),
    path(
        "my_niokr_projects/",
        UserNiokrProjectsOutputView.as_view(),
        name="user_niokr_projects_list_url",
    ),
    path(
        "niokr_project/<int:pk>/",
        NiokrProjectsOutputView.as_view(),
        name="niokr_project_output_pk_url",
    ),
    path("change_niokr_criteria/", change_niokr_criteria, name="change_niokr_criteria"),
    path("add_umnik/<int:pk>/", add_umnik, name="add_umnik"),
    path("delete_umnik/<int:pk>/", delete_umnik, name="delete_umnik"),
    path("add_uss/<int:pk>/", add_uss, name="add_uss"),
    path("delete_uss/<int:pk>/", delete_uss, name="delete_uss"),
    path("api/niokr_project-dates/", NiokrProjectsDatesView.as_view()),
    re_path("^", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
