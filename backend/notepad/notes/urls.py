from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import NoteViewSet, HelloWorld, token_obtain_pair, token_refresh

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='note')
urlpatterns = router.urls

urlpatterns = [
    path('hello/', HelloWorld.as_view(), name='hello-world'),
    path('token/', token_obtain_pair, name='token_obtain_pair'),
    path('token/refresh/', token_refresh, name='token_refresh'),
    
]