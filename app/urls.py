from django.urls import path

from .views import (
    home_view,
    about_view,
    experience_view,
    licenses_view,
    services_view,
    action_aechanism_view,
    join_as_expert_view,
    vocation_request_view,
    
    vocation_request_form_view,
    join_as_expert_form_view,
    vocation_request_form_from_home_view,
)

from .en_views import (
    home_view as en_home_view,
    about_view as en_about_view,
    experience_view as en_experience_view,
    licenses_view as en_licenses_view,
    services_view as en_services_view,
    action_aechanism_view as en_action_aechanism_view,
    join_as_expert_view as en_join_as_expert_view,
    vocation_request_view as en_vocation_request_view,
    vocation_request_form_view as en_vocation_request_form_view,
    join_as_expert_form_view as en_join_as_expert_form_view,
    vocation_request_form_from_home_view as en_vocation_request_form_from_home_view,
)


urlpatterns = [
    path("", home_view, name="home"),
    path("about/", about_view, name="about"),
    path("experience/", experience_view, name="experience"),
    path("licenses/", licenses_view, name="licenses"),
    path("services/", services_view, name="services"),
    path("action-aechanism/", action_aechanism_view, name="action_aechanism"),
    path("consultation-request/", vocation_request_view, name="consultation_request"),
    path("join/", join_as_expert_view, name="join_as_expert_officer"),
    path("join-form/", join_as_expert_form_view, name="join_as_expert_officer_form"),
    path("home-consultation-form", vocation_request_form_from_home_view, name="home_consultation_form"),
    path("consultation-form/", vocation_request_form_view, name="consultation_form"),
    
    
    
    # en paths
    path("en/", en_home_view, name="en_home"),
    path("en/about/", en_about_view, name="en_about"),
    path("en/experience/", en_experience_view, name="en_experience"),
    path("en/licenses/", en_licenses_view, name="en_licenses"),
    path("en/services/", en_services_view, name="en_services"),
    path("en/action-aechanism/", en_action_aechanism_view, name="en_action_aechanism"),
    path("en/consultation-request/", en_vocation_request_view, name="en_consultation_request"),
    path("en/join/", en_join_as_expert_view, name="en_join_as_expert_officer"),
    path("en/join-form/", en_join_as_expert_form_view, name="en_join_as_expert_officer_form"),
    path("en/home-consultation-form", en_vocation_request_form_from_home_view, name="en_home_consultation_form"),
    path("en/consultation-form/", en_vocation_request_form_view, name="en_consultation_form"),
]
