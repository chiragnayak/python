"""

    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import meeting_detail, room_detail, rooms_list, new_meeting, meetings_list

"""
observation (cnayak): order in which we put URLs below is important, as the first match from top to bottom
 will be entertained. So, keep the generic ones at last. 
"""
urlpatterns = [

    url(r'rooms_list', rooms_list, name='rooms_list'),  # url mapping
    url(r'room_detail/(?P<id>[0-9]+)/$', room_detail, name='room_detail'),  # url mapping
    url(r'(?P<id>[0-9]+)/$', meeting_detail, name='detail'),  # url mapping
    url(r'new_meeting', new_meeting, name='new_meeting'),  # url mapping
    url(r'meetings_list', meetings_list, name='meetings_list'),
    # path(r'meetings/<int:id>', meeting_detail),  # path is Django 2 feature
]
