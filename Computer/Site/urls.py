from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^mouse/(?P<pk>\d+)/$', views.M_MouseDetailView.as_view(), name='mouse-detail'),
    re_path(r'^keyboard/(?P<pk>\d+)/$', views.K_KeyboardDetailView.as_view(), name='keyboard-detail'),
    re_path(r'^headset/(?P<pk>\d+)/$', views.H_HeadSetDetailView.as_view(), name='headset-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('mouse/create/', views.add_mouse, name='mouse_create'),
    path('mouse/delete/<int:id>/', views.delete_mouse, name='deletemouse'),
    path('mouse/update/<int:id>/', views.update_mouse, name='updatemouse'),
    path('keyboard/create/', views.add_keyboard, name='keyboard_create'),
    path('keyboard/delete/<int:id>/', views.delete_keyboard, name='deletekeyboard'),
    path('keyboard/update/<int:id>/', views.update_keyboard, name='updatekeyboard'),
    path('headset/create/', views.add_headset, name='headset_create'),
    path('headset/delete/<int:id>/', views.delete_headset, name='deleteheadset'),
    path('headset/update/<int:id>/', views.update_headset, name='updateheadset'),
    path(r'mouses/', views.FilterSearchMouse, name='mouses'),
    path(r'keyboards/', views.FilterSearchKeyboard, name='keyboards'),
    path(r'headsets/', views.FilterSearchHeadset, name='headsets'),
    path(r'login/', views.user_login, name='login'),
    path(r'register/', views.register, name='register'),
]
