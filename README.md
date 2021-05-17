# Simple-OCR-Tool
A simple web application, where you can upload an image and get its text content

Clone the app on your local machine and do ```cd Simple-OCR-Tool```  .


1.) First install python3. ( Version 3.6 and above will work )
  * ```$ sudo apt-get update```
  * ```$ sudo apt-get install python3.6```

2.) Install pip3. 
  * ```sudo apt-get -y install python3-pip```
     

3.) Install pytesseract and tesseract . 
  * ```pip3 install pytesseract```
  * ```sudo apt-get install tesseract-ocr```

4.) Install django ( version 3 and above will work) .
  * ```pip3 install django```
  
After ensuring these dependencies are installed, run the following command:
  * ```python3 manage.py runserver```
  * Open you browser and go to the following url :- ```http://127.0.0.1:8000/```.
  * If it shows that port already in use, add any other number , like  ```python3 manage.py runserver number```, and go to ```http://127.0.0.1:number/```.
