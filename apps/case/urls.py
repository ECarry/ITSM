from django.urls import path
from .views import *

app_name = 'case'
urlpatterns = [
    # 工单主页 http://127.0.0.1:8000/case
    path('', CaseView.as_view(), name="工单列表"),
    # 工单详情页 http://127.0.0.1:8000/case/1
    path('<int:case_pk>', CaseDetailView.as_view(), name="工单详情"),
    # 项目主页 http://127.0.0.1:8000/case/project
    path('project', ProjectView.as_view(), name="项目列表"),
    # 项目详情 http://127.0.0.1:8000/case/project/id
    path('project/<int:project_pk>', ProjectDetailView.as_view(), name="项目详情"),
    # 新建项目 http://127.0.0.1:8000/case/project/new_project
    path('project/new_project/', NewProjectView.as_view(), name="项目详情"),

]
