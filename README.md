# Software Engineering 1
###### Shawn Owen
###### Juliana Osgood
###### Haley Kell
###### Justin Santos

## Random Number Generator Documentation

## Links

Python VM US: http://35.222.85.214/

Python VM Europe-West-2 Zone B: http://34.89.105.129/

Python AppEngine US: http://random-number-generator-python.appspot.com/

Python AppEngine Europe-West-2 Zone B: https://python-app-new-server.appspot.com/

Java VM US:

Java VM Europe-West-2 Zone B: http://35.246.72.72:8080/javarand/MyServlet

Java AppEngine US: http://timing-253317.appspot.com/MyServlet

Java AppEngine Europe-West-2 Zone B: http://timing-experiment-254603.appspot.com/MyServlet


### How to create the Python App Engine:
After creating the python code, we can create the app engine to store and deploy it. 

1. First create your project by selecting either an existing project or by creating a new one. 
2. Open the Google Cloud Shell by opening the >_ icon on the top toolbar.
3. Create your directory folder wherever you’d like to save your project using the mkdir command, for instance “mkdir RandomNumberGenerator”
4. Several files will need to be made inside of this folder, and we’ll start with the main python file. Use the command “vim main.py” and this will give you a place to put your code. Enter a capital “A” and then you can edit the file. Insert your code, and when you are done, hit “escape” then type in “:wq”
5. Using the same steps above, create another file using vim called “app.yaml” and inside of that put in “runtime: python37” and close it.
6. Create another file called “requirements.txt” and inside of that type “Flask==1.0.2” and then close it.
7. Now we can test and activate the app. Use the code below create an isolated VM
```
virtualenv --python python3 \ 
    ~/envs/RandomNumberGenerator
```
8. Activate using this code
```
source \ 
    ~/envs/RandomNumberGenerator/bin/activate
```
9. Use pip to install your project dependencies for flask inside of the previously created requirements.txt
```
pip install -r requirements.txt
```
10. Run your program using the command “python main.py”
11. Use “gcloud app create” to create the app space. 
12. Deploy the app using this code. Where it says “Random-number-generator” you can type whatever you want the URL to your code to be.
```
gcloud app deploy app.yaml \
    --project \
    Random-number-generator 
```
13. Visit the app using the URL you created!

### How to create the Python VM: 

1. Create a new project in Google Cloud Platform
2. Navigate to the Compute Engine page and create a new VM instance with the settings f1-micro, Ubuntu 18.04 LTS, and enable HTTP and HTTPS traffic.

<img src="/createinstance.png" width="881" height="344">

<img src="/pythonvmspecs.png" width="240" height="523">

3. Connect to the instance through SSH, which is a button that will launch the VM.

<img src="/snapshotssh.png" width="784" height="293">

4. Execute the command "sudo apt update && sudo apt upgrade"
5. Type "hostname" to find hostname of the server and edit the host file with "sudo nano /etc/hosts". Under the localhost line, type the IP address of the server, press tab and type the hostname. The IP can be found on the Compute Engine page under external IP.
6. Set up a firewall by executing the following commands:
> "sudo apt install ufw"
> "sudo ufw default allow outgoing"
> "sudo ufw default deny incoming"
> "sudo ufw allow ssh"
> "sudo ufw allow http/tcp"
> "sudo ufw enable"
7. Clone this repository with the command "git clone https://github.com/haleykell/random-number-generator/"
8. Switch to the python-app directory with "cd python-app"
9. Install pip with "sudo apt install python3-pip"
10. Install the virtual environment with "sudo apt install python3-venv"
11. Create a virtual environment with "python3 -m venv venv"
12. Activate the virtual environment with "source venv/bin/activate"
13. Install project dependencies with "pip install -r requirements.txt"
14. Install nginx with "sudo apt install nginx"
15. Install gunicorn with "pip install gunicorn"
16. Update nginx config file by doing the following:
sudo rm /etc/nginx/sites-enabled/default
sudo nano /etc/nginx/sites-enabled/random-number-generator
17. Copy the contents of RandomNumberFlask/nginx_config.txt into the file. Change [The IP Address of the Server] to your IP.
18. Restart nginx server with "sudo systemctl restart nginx"
19. Install supervisor with "sudo apt install supervisor"
20. Set up supervisor with "sudo nano /etc/supervisor/conf.d/random_number_generator.conf"
21. Find out the number of workers for gunicorn with (2 * number of cores) + 1 (execute "nproc --all" to find number of cores). This number will most likely be a 3.
22. Copy the contents of RandomNumberFlask/supervisor_config.txt into the file and change [Your Username] and [Number of Workers]
23. Make the log files by doing the following:
24. Do "sudo mkdir -p /var/log/random-number-generator"
25. Then "sudo touch /var/log/random-number-generator/random-number-generator.err.log"
26. Then do "sudo touch /var/log/random-number-generator/random-number-generator.out.log"
27. Restart supervisor with "sudo supervisorctl reload"
28. Setup a static IP for your virtual machine by going to the VPC Network page on GCP
29. Under the "External IP addresses" find the IP address being used by the VM instance
30. Switch "Emphemral" to "Static" and reserve an IP with any name you find appropriate
31. To access the random number generator navigate to "http://[The IP Address of the Server]"

#### To change the region: 

1. Ensure you are in the project containing your original Python VM
2. Create a snapshot of your previously created VM (steps shown above). 

<img src="/createsnapshot.png" width="815" height="289">

3. Using this snapshot, create a new instance. Use the settings f1-micro and enable HTTP and HTTPS traffic, and select whichever region you would like to host your VM in. For the boot disk, navigate to snapshots, and select the snapshot you created above.

<img src="/pythonsnapinvm.png" width="825" height="565">

4. Use your new IP located under "External IP addresses" to navigate to your VM in your new region!

### How to create the Java App Engine Servlet:

1. Install Tomcat (http://tomcat.apache.org/) and extract the zipped files to a folder.
2. Create a new Intellij Project by choosing Java Enterprise and checking Web Application.
3. Set the Application Server by clicking New -> Tomcat Server and setting the home folder to the folder where you extracted the zipped files.
4. Click Next through the rest of project setup.
5. Run -> Tomcat will start the server and display the current webpage.
6. In the src folder, create a class called Servlet which extends javax.servlet.http.HttpServlet.
7. Create a method called doGet() with the following signature:
```
protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException
```
8. Inside that method, use PrintWriter writer = response.getWriter().
9. Use the writer to write html to the webpage.
10. For our use case, use Random and the rand.nextInt() to generate the random number through the writer:
```
Random rand = new Random();
writer.print(rand.nextInt(1000000));
```
11. The web.xml file should contain the following:
```
<web-app xmlns="http://xmlns.jcp.org/xml/ns/javaee"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://xmlns.jcp.org/xml/ns/javaee http://xmlns.jcp.org/xml/ns/javaee/web-app_3_1.xsd"
         version="4.0">
       
<servlet>
    <servlet-name>MyServlet</servlet-name>
    <servlet-class>Servlet</servlet-class>
</servlet>
       
<servlet-mapping>
    <servlet-name>MyServlet</servlet-name>
    <url-pattern>/MyServlet</url-pattern>
</servlet-mapping>
       
</web-app>
```
12. Index.jsp should contain:
```
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <title>Random Number Generator</title>
</head>
<body>
<h2>Random Number Generator</h2>
<p>To generate a random number click <a href="MyServlet">here</a></p>
<p>Refresh that page for a new number.</p>
</body>
</html>
```
13. Click Run -> Run Tomcat -> check restart server to redeploy new changes. This will automatically open the web page.
14. On Google Cloud, follow the tutorial to create a Java App Engine
15. Replace web.xml, index.html, and DemoServlet.java with the files described above
16. Continue the tutorial to deploy the app


### How to run the Request Application:
1. On Google Cloud Platform, either create a new project or choose an existing
   one.
2. Open the Google Cloud Shell by clicking the > _ icon on the top toolbar.
3. Clone this repository using the command "git clone
   https://github.com/haleykell/random-number-generator/".
4. Move into the request-app directory by using the command "cd
   random-number-generator/request-app"
5. Ensure that a Python verion higher than 3.5 is installed by issuing the
   command "python3 --version". If Python 3.5 or higher is not present, follow
   this guide on how to update: https://cloud.google.com/python/setup.
6. Run the script with the command "python3 ./main.py". The output should look
   similar to this:
```
Time for requests: 4.410743713378906e-05

<h1> 205919
<h1> 921422
<html><body>808243</body></html>
```
