---
active: false
alumni: false
bio: Master's Student
building: S.E. Wimberly Library
contact: false
director: false
email: eakgunduz2016@fau.edu
faculty: false
github: ''
image: /uploads/avatars/Eren-Akgunduz.jpg
images:
- path: /uploads/news-pictures/2023-Spring-Eren-at-Grand-Opening.JPG
instagram: ''
linkedin: ''
room: Sandbox
staff: false
student: true
title: Eren Akgunduz
twitter: ''
username: Eren-Akgunduz
vimeo: ''
website: ''
youtube: ''
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