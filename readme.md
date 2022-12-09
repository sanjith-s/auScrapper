Steps to run the project:

1. Install the required packages
 >>pip install -m requirement.txt
 
2. Install uvicorn
>>Pip install uvicorn

3. Check your chrome version and download the corresponding driver from [here](https://chromedriver.storage.googleapis.com/index.html)

4. Create a folder 'seleniumDriver' in C drive and move chromedriver.exe to the folder

5. Run the file
>>python.exe -m uvicorn main:app --reload