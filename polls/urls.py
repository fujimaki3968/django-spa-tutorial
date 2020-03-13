from rest_framework.routers import DefaultRouter

from .api import QuestionViewSet

question_router = DefaultRouter()
question_router.register(r'', QuestionViewSet)
