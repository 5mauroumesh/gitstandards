from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    

    path('full-test/', Full_Test.as_view(), name='full-test'),
    path('master-test/', Master_Test.as_view(), name='master-test'),
    path('url-test/', URL_Test.as_view(), name='url-test'),
    path('pageindex-test/', PageIndex_Test.as_view(), name='pageindex-test'),
    path('gtmetrix-test/', GTMetrix_Test.as_view(), name='gtmetrix-test'),
    path('ssl-test/', SSL_Test.as_view(), name='ssl-test'),
    path('webpage-performance-test/', Webpage_Perfomance_Test.as_view(), name='webpage-performance-test'),
    path('website-audit-test/', Website_Audit_Test.as_view(), name='website-audit-test'),
    path('domain-index-test/', Domain_Index_Test.as_view(), name='domain-index-test'),
    path('pingdom-tools-test/', Pingdom_Tools_Test.as_view(), name='pingdom-tools-test'),
    path('on-map-test/', Map_Test.as_view(), name='map-test'),
    path('dns-test/', DNS_Test.as_view(), name='dns-test'),
    path('mobile-friendly-test/', Mobile_Friendly_Test.as_view(), name='mobile-test'),
    path('html-validation-test/', HTML_Validation_Test.as_view(), name='html-validation-test'),
    path('social-profile-test/', Social_Profile_Test.as_view(), name='social-profile-test'),
    path('seo-report-test/', SEO_Report_Test.as_view(), name='seo-report-test'),
    path('speciality-in-locality/', Speciality_In_Locality.as_view(), name='speciality-in-locality'),
    path('speciality-in-locality-places/', Speciality_Locality_Places.as_view(), name='speciality-in-locality-places'),
    path('speciality-in-locality-organic/', Speciality_Locality_Organic.as_view(), name='speciality-in-locality-organic'),
    path('speciality-in-locality-organic-score/', Speciality_Locality_Organic_Score.as_view(), name='speciality-in-locality-organic-score'),
    path('speciality-in-locality-places-score/', Speciality_Locality_Places_Score.as_view(), name='speciality-in-locality-places-score'),
    
]