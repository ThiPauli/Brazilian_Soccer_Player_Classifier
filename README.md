# Soccer Player Classifier

## Project Overview
- Classify 7 brazillian soccer players using 2 different approaches.
1) Cassio (goalkeeper from Corinthians)
2) Diego Souza (forward from Grêmio)
3) Fred (forward from Fluminense)
4) Gabriel Barbosa (forward from Flamengo)
5) German Cano (forward from Vasco)
6) Hulk (forward from Atlético Mineiro)
7) Marinho (forward from Santos)

## Projects:
### Project 1
- Applied Haar cascades for face and eyes detection in order to train our model
- The best accuracy was from Logistic Regression model after using Grid Search CV defining the models and hypertune parameters.
- Created a web server and a website to make new predictions.

The folder Brazillian Soccer Player Classifier using Haar cascades structure is defined as follow:
* UI : This contains the UI website code
* server: Python flask server
* model: Contains python notebook for model building

### Setup:
1. [Download](https://github.com/ThiPauli/Brazilian_Soccer_Player_Classifier/archive/refs/heads/main.zip) the repository
   
2. Install some Dependencies (if necessary)
    ```
    pip install opencv-python, PyWavelets, requests
    ```
3. Run the code [server](https://github.com/ThiPauli/Brazilian_Soccer_Player_Classifier/blob/main/Brazillian%20Soccer%20Player%20Classifier%20using%20Haar%20cascades/server/server.py) from Brazillian Soccer Player Classifier using Haar cascades folder to launch the web server.
    ```
    python server.py
    ```
4. Open the [website](https://github.com/ThiPauli/Brazilian_Soccer_Player_Classifier/blob/main/Brazillian%20Soccer%20Player%20Classifier%20using%20Haar%20cascades/UI/app.html)
5. Drag and drop images to make new predictions.

![](Brazillian-Soccer-Player-Classifier-using-Haar-cascades/web_page.PNG)

The seed idea for this project part was taken from codebasics channel from youtube, which I give the credits.

### Project 2
