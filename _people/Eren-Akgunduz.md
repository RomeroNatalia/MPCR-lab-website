---
title:          Eren Akgunduz
username:       Eren-Akgunduz
image:          /uploads/avatars/Eren-Akgunduz.jpg # /uploads/avatars/Eren-Akgunduz 
bio:            Master's Student
email:          eakgunduz2016@fau.edu
website:        #
laboratory:     Machine Perception and Cognitive Robotics Lab (MPCR)
building:       S.E. Wimberly Library
room:           Sandbox
active:         false
alumni:         false
contact:        false
faculty:        false
staff:          false
student:        true
github:         # https://github.com/
instagram:      # https://www.instagram.com/
linkedin:       #
twitter:        # https://twitter.com/
vimeo:          # https://vimeo.com/
youtube:        # https://www.youtube.com/


images:
  - path: /uploads/news-pictures/2023-Spring-Eren-at-Grand-Opening.JPG
---

# Contact Information
Department of Electrical Engineering and Computer Science  
777 Glades Road  
Boca Raton, FL 33431-0991  
{{ page.building }}  
{{ page.room }}  
[{{ page.email }}](mailto:{{ page.email }})

# Education
* M.S., Artificial Intelligence, Florida Atlantic University (In progress)
* B.S., Biology, Florida Atlantic University (2021)

{% if page.website %}
# Personal Website
[**{{ page.website | remove: "https://" }}**]({{ page.website }})
{% endif %}

# Photos
{% include slideshow.html %}