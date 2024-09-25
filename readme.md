# Homework3 Project Setup
##  set up:

1. Python Virtual Environments: Essential for managing project-specific dependencies.
2. Pytest: A powerful framework for writing and running Python tests.
3. Pylint: A tool for analyzing your Python code for errors and enforcing a coding standard.
4. Coverage: A tool for measuring the coverage of your unit tests.
5. Git: To practice version control techniques such as branching, merging, and using stash.

Additionally, we will delve into integrating these tools with Visual Studio Code (VSCode) and Windows Subsystem for Linux (WSL 2), enhancing your ability to manage development tasks.

## Instructions:
1. Create directory and use touch command create files same as followed Homework-2 project.

2. Install python virtual environment, so we can manage the virtual environment to issolate your dependences from the global version of python. we need to do this once for your computer, this is a global python package.   
    
    - sudo apt install python3-virtualenv
    
    - mkdir venv
    
    - virtualenv -p /usr/bin/python3 venv

3.  Go to venv folder and active virtual environment below command:
    
	1. source venv/bin/activate
	
4. Once the virtual environment is a active then install the python dependencies using  pytest, coverage and requirement.txt     
    1. pip install pytest
    2. pip install pytest-pylint
    3. pip install pytest-cov
    4. pip install -r requirements.txt

5. we can try do this save all our python libraries with current version into requirements.txt file.
    
    -> pip freeze > requirements.txt

Note When someone copies / clones your repository they will install the specfic library / dependency requirements for your project using the command:

   1.  pip install -r requirments.txt

6. Finally, Open VScode and test code.
    
   1. code .    

## Testing

1. pytest
2. pytest --pylint
3. pytest --pylint --cov

## Other commands used during project
 1. mv oldfile newfilename
 2. git remote remove origin
 3. rm -rf .pytest_cache
 4. Skipped files during pytest --pylint run add content in pytest.ini   file: [master]
     #force rechecking all files
      persistent = no
 5. To add multiple specific files: git add path/to/file1.py path/to/file2.py path/to/file3.py
