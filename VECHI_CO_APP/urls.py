
from django.urls import path

# from VECHI_CO_APP import views
from VECHI_CO_APP import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.Login),
    path('login_post', views.login_post),
    path('admin_home', views.admin_home),
    path('logout', views.logout),
    path('add_service', views.add_service),
    path('add_service_post',views.add_service_post),
    path('view_serviceprovider_and_verify', views.view_serviceprovider_and_verify),
    path('view_verified_serviceprovider', views.view_verified_serviceprovider),
    path('view_complaint', views.view_complaint),
    path('view_feedback', views.view_feedback),
    path('view_rating_and_review', views.view_rating_and_review),
    path('change_password', views.change_password),
    path('change_password_post', views.change_password_post),
    path('update_service/<id>', views.update_service),
    path('update_service_post/<id>',views.update_service_post),
    path('delete_service/<id>',views.delete_service),
    path('view_users', views.view_users),
    path('view_service', views.view_service),
    path('send_reply/<id>', views.send_reply),
    path('send_reply_post/<id>', views.send_reply_post),
    path('approve_serviceprovider/<ajoy>',views.approve_serviceprovider),
    path('reject_serviceprovider/<id>',views.reject_serviceprovider),
    path('forgot_password',views.forgot_password),
    path('forgot_password_post',views.forgot_password_post),



    path('service_provider_home',views.serviceprovider_home),
    path('register_servuceprovider',views.register_servuceprovider),
    path('register_servuceprovider_post',views.register_servuceprovider_post),
    path('view_profile_and_update',views.view_profile_and_update),
    path('view_profile_and_update_post/<id>',views.view_profile_and_update_post),
    # path('view_services',views.view_services),
    # path('view_own_service_management',views.view_own_service_management),
    path('provider_add_own_service/<id>',views.provider_add_own_service),
    path('provider_own_service_post/<id>',views.provider_own_service_post),
    path('view_payment_history',views.view_payment_history),
    path('view_previous_history', views.view_previous_history),
    # path('View_profile', views.View_profile),
    path('view_request',views.view_request),
    path('approve_request/<id>',views.approve_request),
    path('reject_request/<id>',views.reject_request),
    path('updation_completion_status/<id>',views.updation_completion_status),
    path('updation_completion_status_post/<id>',views.updation_completion_status_post),
    path('view_review_and_rating', views.view_review_and_rating),
    path('provider_add_services', views.provider_add_services),
    path('provider_view_services', views.provider_view_services),
    path('delete_provider_service/<id>', views.delete_provider_service),
    path('service_provider_change_password', views.service_provider_change_password),
    path('service_provider_change_password_post', views.service_provider_change_password_post),


    path('and_login', views.and_login),
    path('and_signup', views.and_signup),
    path('and_view_service_provider', views.and_view_service_provider),
    path('and_view_booking', views.and_view_booking),
    path('and_send_feedback',views.and_send_feedback),
    path('and_view_service',views.and_view_service),
    path('and_book_service',views.and_book_service),
    path('and_view_reply',views.and_view_reply),
    path('and_send_complaint',views.and_send_complaint),
    path('android_send_rating',views.android_send_rating),
    path('android_offline_payment',views.android_offline_payment),
    path('android_online_payment',views.android_online_payment),


    #.............................................................. BANK PAYMENT

    path('android_add_bank',views.android_add_bank),
    path('android_view_bank',views.android_view_bank),
    path('android_delete_bank',views.android_delete_bank),
    path('android_online_payment',views.android_online_payment),
]
