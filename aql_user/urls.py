from django.urls import path
from aql_user.views import common

urlpatterns=[
    path('register/',common.RegisterUserView.as_view({'post':'create'})),

    path('email/activate/',common.EmailConfirm.as_view({'post':'request_token'})),
    path('email/verify/',common.VerifyEmail.as_view(),name='email_verify'),
    path('reset_password/',common.ResetPassword.as_view({'get':'get'}),name='reset_password'),
    path('new_password/',common.UpdatePassword.as_view({'post':'post'}),name='new_password'),

    path('token/',common.TokenObtainPairView.as_view()),
    path('token/refresh/',common.TokenRefreshView.as_view()),

    path('users/me/',common.SelfView.as_view({'get':'get'})),

    path('logout/',common.LogoutFormView.as_view())
]