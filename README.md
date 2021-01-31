# django_job_portal

Membuat Profesional Job Portal dengan menggunakan Python 3.9 dan Django v3.1
https://github.com/ingafter60/django_job_portal

# Section 3: Job Portal Project

## Section 1: Setup Homepage

### 1.99. What We Are Going To Build?

        PASS

### 2.100. How To Create Our Project

        modified:   .gitignore
        modified:   README.md
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py

### 3.101. How To Install PostgresQL Server

        PASS

### 4.102. How To Install Psycopg2 driver

        > pip install psycopg2

### 5.103. How TO Create postgres Database and set it up for Our Project

        > CREATE DATABASE django2021_mc_job_portal;
        > CREATE USER user2021 WITH PASSWORD '2021';
        > GRANT ALL PRIVILEGES ON DATABASE django2021_mc_job_portal TO user2021;
        modified:   README.md
        modified:   config/settings.py

### 6.104. Creating Static Files Directory and add assets to it

        modified:   README.md
        modified:   config/settings.py
        new file:   static/css/.DS_Store
        new file:   static/css/ajax-loader.gif
        new file:   static/css/animate.css
        ...
        new file:   static/css/aos.css

### 7.105. How To Create a new app and add template directory

        modified:   README.md
        modified:   config/settings.py
        new file:   jobs/__init__.py
        new file:   jobs/admin.py
        new file:   jobs/apps.py
        new file:   jobs/migrations/__init__.py
        new file:   jobs/models.py
        new file:   jobs/tests.py
        new file:   jobs/views.py

### 8.106. How To Create Our First Html File

        modified:   README.md
        modified:   config/urls.py
        new file:   jobs/urls.py
        modified:   jobs/views.py
        new file:   templates/jobs/home.html

### 9.107. How To Create Base Html with template inheritance

        modified:   .gitignore
        modified:   LICENSE
        modified:   README.md
        modified:   jobs/urls.py
        modified:   jobs/views.py
        new file:   templates/base.html
        deleted:    templates/jobs/home.html
        new file:   templates/jobs/index.html
        new file:   templates/jobs/partials/banner.html
        new file:   templates/jobs/partials/blog.html
        new file:   templates/jobs/partials/current_job_posts.html
        new file:   templates/jobs/partials/head.html
        new file:   templates/jobs/partials/newsletter.html
        new file:   templates/jobs/partials/number_of_jobs.html
        new file:   templates/jobs/partials/recently_added_jobs.html
        new file:   templates/jobs/partials/testimonial.html

### 10.108. Creating Our First Model
        
        See 11.109

### 11.109. +  10.108. (Creating Custom User) How To Create UserManager Class

        modified:   README.md
        modified:   config/settings.py
        modified:   config/urls.py
        new file:   users/__init__.py
        new file:   users/admin.py
        new file:   users/apps.py
        new file:   users/migrations/0001_initial.py
        new file:   users/migrations/__init__.py
        new file:   users/models.py
        new file:   users/tests.py
        new file:   users/urls.py
        new file:   users/views.py
        
### 12.110. How To Create Superuser

        modified:   README.md
        modified:   users/admin.py
        
### 13.111. How To Create Add And Update User Functions

        modified:   README.md
        modified:   users/admin.py

### 14.112. Create Job Model

        modified:   README.md
        modified:   jobs/admin.py
        new file:   jobs/migrations/0001_initial.py
        modified:   jobs/models.py

### 15.113. Add some entries to jobs table and Use A Generic View For Job Model

        modified:   README.md
        modified:   jobs/views.py

### 16.114. (Rendering jobs) How To List Our Jobs

        modified:   README.md
        modified:   jobs/views.py
        modified:   templates/jobs/partials/recently_added_jobs.html
        
### 17.115. How To Use Pagination

        modified:   README.md
        modified:   jobs/views.py
        modified:   templates/jobs/partials/recently_added_jobs.html
        
### 18.116. How To Create Category Model

        modified:   README.md
        modified:   config/settings.py
        modified:   jobs/admin.py
        new file:   jobs/migrations/0002_auto_20210131_1547.py
        modified:   jobs/models.py
        modified:   jobs/views.py
        modified:   templates/jobs/index.html
        renamed:    templates/jobs/partials/recently_added_jobs.html -> templates/jobs/partials/categories.html
        renamed:    templates/jobs/partials/current_job_posts.html -> templates/jobs/partials/job_posts.html
        
19.117. How To Solve Integrity Error For Our Categories
20.118. How To Display Categories in Our Template File
21.119. How To Create User Register Form
22.120. Creating User Register Html File
23.121. How To Register Our Users
24.122. How To Display Form Errors
25.123. How To Create Login and Logout Views
26.124. How To Create Profile Model
27.125. How To Install CkEditor
28.126. How To Create A User Profile
29.127. How To Create Our Urls
30.128. Creating User Profile Update Form
31.129. How To Update Users Profile
32.130. How To Create Urls For Authenticated Users
33.131. How To Post A New Job
34.132. How To Create Html File For Post A Job
35.133. How To Create Job Detail Page
36.134. Creating Category Detail View
37.135. Creating Category Detail Template File
38.136. Creating Search View
39.137. How To Create Search Results Template File
40.138. Finishing Search Template File
41.139. How To Create Apply Job Button
42.140. Fixing Some Small Problems For Apply Job Button
43.141. How To List Applied Candidates
44.142. Fixing Some Small Problems For Applied candidates
45.143. How To Create Employee Profile View
46.144. Creating Employee Profile Template File
47.145. How To Create Employer Posted Jobs View
48.146. How To Create Employer Posted Jobs Template File
49.147. How To Create Invite Model
50.148. How To Create Employee Invite Form
51.149. How To Display Invite Employee Form
52.150. How To Send An Invitation To Employees
53.151. How To Display Unread Messages
54.152. How To Display Number Of Unread Messages
55.153. How To Create Message Inbox Template File
56.154. How To Display Unread Messages
57.155. How To Display Messages
58.156. Solving Some Small Problems For Invite Model
59.157. How Create Update Job Template File
60.158. How To Update Our Jobs
61.159. How To Delete A Job
62.160. How To Display Our Statistics For Our Project
63.161. How To Create Wish List
64.162. How To Create Ajax Functions For Wish List
65.163. How To Create Views For Our Wish List
66.164. How To Display Correct Wish List Buttons
67.165. How To Create Our Wish List
68.166. Solving Some Small Problems For Wish List
69.167. How To Use SweetAlert2
70.168. Fixing Some Small Problems For Wish List Buttons Part1
71.169. Fixing Some Small Problems For Wish List Buttons Part2
72.170. How To Create Wish List Buttons For Job Detail Page
73.171. Fixing Some Small Problems For Our Project
74.172. How To Change Users Password
75.173. How To Reset User Password Part1
76.174. How To Reset User Password Part2
77.175. How To Reset User Password Part3
