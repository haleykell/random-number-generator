# Software Engineering 1
###### Shawn Owen
###### Juliana Osgood
###### Haley Kell
###### Justin Santos

## Random Number Generator Documentation

## Links

Python VM: http://35.222.85.214/

Python AppEngine: http://random-number-generator-python.appspot.com/

Python AppEngine Europe-West-2 Zone B: https://python-app-new-server.appspot.com/

Java VM: http://35.246.72.72:8080/javarand/MyServlet

Java AppEngine: http://timing-253317.appspot.com/MyServlet


### How to create the App Engine:
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


### How to create the Java Servlet:

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


### Java VM 

1. Create a new VM instance on gcp
2. Install prereqs: Java jdk, tomcat.
3. clone the random-number-generator repo
4. Copy the app WEB-INF into tomcats webapps directory `cp repo/path/java-app-vm/src/main/webapp pathto/tomcat/webapps/[app_name]` and compile the java file into the copied `classes/` directory. `javac -d /webapps/app_name/WEB-INF/classes /java-app-vm/src/main/java/Servlet.java`
5. Update your connection host in tomcat to `0.0.0.0`, in /pathto/tomcat/conf/server.xml
6. In GCP, create a firewall rule to open up port 8080 for tcp.
7. Run tomcat, `tomcat/bin/startup.sh`
8. The app should be running at [external_ip/name_for_app/MyServlet].


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
