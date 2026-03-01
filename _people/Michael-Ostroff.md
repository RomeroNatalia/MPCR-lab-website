---
active: false
alumni: true
bio: Ph.D. Student
building: ''
contact: false
director: false
email: mostroff2015@fau.edu
faculty: false
github: ''
image: /uploads/avatars/Michael-Ostroff.jpg
images:
- path: /uploads/news-pictures/2023-Spring-Michael.JPG
instagram: ''
linkedin: ''
room: ''
staff: false
student: true
title: Michael Ostroff
twitter: ''
username: Michael-Ostroff
vimeo: ''
website: ''
youtube: ''
---

# Contact Information
Department of Physics  
Center for Complex Systems and Brain Sciences   
Center for the Future Mind  
777 Glades Road  
Boca Raton, FL 33431-0991  
{% if page.building %}
{{ page.building }}  
{{ page.room }}  
{% endif %}
[{{ page.email }}](mailto:{{ page.email }})

# Education
* Ph.D., Physics, Florida Atlantic University (In progress)  
* M.S., Physics, Florida Atlantic University (In progress)  
* B.S., Physics, Florida Atlantic University  
 
{% if page.website %}
# Personal Website
[**{{ page.website | remove: "https://" }}**]({{ page.website }})
{% endif %}

# Demos

<iframe src="https://www.youtube-nocookie.com/embed/o_1ytIefGpE" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Photos
{% include slideshow.html %}