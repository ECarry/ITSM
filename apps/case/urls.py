from django.urls import path
from .views import *

app_name = 'case'
urlpatterns = [
    # 工单列表主页 http://127.0.0.1:8000/case
    path('', CaseView.as_view(), name="case_list"),
    # 工单详情页 http://127.0.0.1:8000/case/detail/pk
    path('detail/<int:case_pk>', CaseDetailView.as_view(), name="case_Detail"),
    # 新建工单 http://127.0.0.1:8000/case/new_case
    path('new_case/', NewCaseFormView.as_view(), name="new_case"),
    # 项目列表主页 http://127.0.0.1:8000/case/project
    path('project', ProjectView.as_view(), name="project_list"),
    # 项目详情 http://127.0.0.1:8000/case/project/id
    path('project/<int:project_pk>', ProjectDetailView.as_view(), name="project_detail"),
    # 新建项目 http://127.0.0.1:8000/case/project/new_project
    path('project/new_project/', NewProjectView.as_view(), name="new_project"),
    # 服务器列表 http://127.0.0.1:8000/case/server
    path('server', ServerView.as_view(), name="server_list"),
    # 新建服务器 http://127.0.0.1:8000/case/server/new_server
    path('server/new_server', NewServerFormView.as_view(), name="new_server"),
]
