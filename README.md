
hello all!
<b><h1>This is images-api.</b></h1>

<h3>Live demo is here: https://images-api-task.herokuapp.com/api/login/

Four users and admin were created:</h3>

<li>user1_basic</li>
<li>user2_premium</li>
<li>user3_premium</li>
<li>user4_enterprise</li>
<p>and</p>
<li>admin <h4>login:admin pass:admin https://images-api-task.herokuapp.com/admin/</h4></li>

users login credecials eg: 
<br>
GET https://images-api-task.herokuapp.com/api/login/
<br>
POST:
<br>
<code>
{"username":"user3_premium",
"password":"userpass"} The password is the same in all users
</code>
<p>logout user: https://images-api-task.herokuapp.com/api/logout/</p>

<p>To see all user files go to https://images-api-task.herokuapp.com/api/images/</p>
<p>If you want to see links to an image, enter the full name of the file with the extension in HTML form (FileName)</p>
<br>
<p>If you want to add a new file, follow the link https://images-api-task.herokuapp.com/api/upload/</p>
********************************
<h4>TO DO:</h4>
<h4>* ability to fetch a link that expires after a number of seconds (user can specify any number between 300 and 30000)</h4>
<h4>* tests</h4>
********************************
<p>To setup project local you need install requirements and you should using settings_local.py</p>
<p>Run eg. py manage.py runserver --settings project.settings_local</p>