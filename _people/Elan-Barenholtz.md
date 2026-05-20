From 21f7c4a527772915b5603f5e3a3ba59bae723ef6 Mon Sep 17 00:00:00 2001
From: Elan Barenholtz <elanbarenholtz@gmail.com>
Date: Wed, 20 May 2026 18:38:26 +0000
Subject: [PATCH] Add /people/bio/Elan-Barenholtz page and expand bio content

Sets an explicit permalink so the person page resolves at
/people/bio/Elan-Barenholtz (the URL the FAU College of Science
directory links to). Adds redirect_from for the old /people/
URL so existing links keep working. Expands the page with
positions, education, a research description, a 'Generative
Brain' section, scholarly service, and a working Google Scholar
link.
---
 _people/Elan-Barenholtz.md | 35 ++++++++++++++++++++++++-----------
 1 file changed, 24 insertions(+), 11 deletions(-)

diff --git a/_people/Elan-Barenholtz.md b/_people/Elan-Barenholtz.md
index d3df7f1..86e4437 100644
--- a/_people/Elan-Barenholtz.md
+++ b/_people/Elan-Barenholtz.md
@@ -16,8 +16,11 @@ images:
 - path: /uploads/news-pictures/2014-MM-DD-MPCR-Rover.jpg
 instagram: ''
 linkedin: https://www.linkedin.com/in/elan-barenholtz/
+permalink: /people/bio/Elan-Barenholtz/
 project_slugs:
 - Visuospatial-Learning-Capabilities-of-LLMs
+redirect_from:
+- /people/Elan-Barenholtz/
 room: Room 212
 staff: false
 student: false
@@ -35,29 +38,39 @@ Center for Complex Systems and Brain Sciences
 Center for the Future Mind  
 777 Glades Road  
 Boca Raton, FL 33431-0991  
-{{ page.building }}  
-{{ page.room }}  
+{{ page.building }}, {{ page.room }}  
 [{{ page.email }}](mailto:{{ page.email }})
 
+# Positions
+* Associate Professor of Psychology, Florida Atlantic University
+* Co-Founder & Co-Principal Investigator, Machine Perception and Cognitive Robotics (MPCR) Laboratory
+* Associate Director, Center for the Future Mind
+
 # Education
-* Ph.D., Rutgers University, New Brunswick
+* Ph.D., Experimental Psychology & Cognitive Science, Rutgers University, New Brunswick
 * M.A., Rutgers University, New Brunswick
+* Postdoctoral Fellow, Brown University
 
 # Research Interests
-* Deep Learning/Ai
-* Foundations of Langauge and Cognition
+* Foundations of language and cognition
+* Deep learning and large language models
 * Embedded computational neural models
+* Perception, learning, and object recognition
 
 # Research Description
-I use behavioral and embedded computational approaches (i.e., neural networks running in robots) to study the brain and behavior with the goal of developing a broad theoretical framework of neural function.
+I use behavioral and embedded computational approaches — neural networks running in robots — to study the brain and behavior, with the goal of developing a broad theoretical framework of neural function. Trained as an experimental psychologist, I began my career investigating human visual perception and object recognition. Over the past decade my work has increasingly turned to artificial intelligence, both as a tool for understanding the brain and as a subject of study in its own right.
+
+# The Generative Brain
+My current research develops the idea that language is an autonomous, *autoregressive* system — one that generates coherent continuations from its own internal structure rather than by describing an external world. This framework reframes memory, imagination, and the sense of self as products of sequential generation rather than storage and retrieval, and asks how far human cognition can be explained by the same principle that drives modern large language models. I write about these ideas for a general audience in my newsletter, [**The Generative Brain**](https://elanbarenholtz.substack.com).
 
 <iframe width="560" height="315" src="https://www.youtube.com/embed/7vKv1CtXtzI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
 
+# Scholarly Service
+* Reviewer, National Science Foundation review panels
+* Editorial Board Member, *Frontiers in Psychology*
+
 # Publications
-[**Google Scholar**]({{page.google-scholar}})
+[**Google Scholar profile**](https://scholar.google.com/citations?user=2grAjZsAAAAJ&hl=en)
 
+# Slideshow
 {% include slideshow.html %}
-
-{% comment %}
-![Dr-Barenholtz](/uploads/news-pictures/2021-May-10-Dr-Elan-Barenholtz.jpg)  
-{% endcomment %}
\ No newline at end of file
-- 
2.34.1
