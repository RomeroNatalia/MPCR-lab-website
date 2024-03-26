---
title:          Michael Ostroff
username:       Michael-Ostroff
image:          /uploads/avatars/Michael-Ostroff.jpg
bio:            Ph.D. Student
email:          mostroff2015@fau.edu
website:        # 
laboratory:     # Machine Perception and Cognitive Robotics Lab (MPCR)
building:       # S.E. Wimberly Library
room:           # Sandbox
active:         true
alumni:         false
contact:        false
faculty:        false
staff:          false
student:        true
github:         # https://github.com/
instagram:      # https://www.instagram.com/
linkedin:       # https://www.linkedin.com/in/
twitter:        # https://twitter.com/
vimeo:          # https://vimeo.com/
youtube:        "https://www.youtube.com/@PerpetualScience" # https://www.youtube.com/

images:
  - path: /uploads/news-pictures/2023-Spring-Michael.JPG
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