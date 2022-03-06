### Motivation
This project is inspired by the topic of identity fraud. These days, most internet users leave enough information on the web for their identity to be misused by others. Even with the most basic information such as name, country of birth, age and occupation, the internet could have a pretty good sense of who you are as a person and could even use your identity with a bad intention. This project creates a spooky interface where users can input some of this basic information and then using openai's most powerful nlp machine the program tries to imitate the person with an AI voice. I decided to present the output as a web app because most of users' information is left unprotected on the web and hence this interface serves to remind the users of this open and not always safe medium. I use a retro TV static background in order to create an impression that their computer has been hacked and that they are now forced to give off their basic information. I use openai's nlp machine because the output indeed feels very natural with temperature <= 0.6 which makes the threat of identity theft seems imminent to the user.

### Setup
1. Clone the repository
2. Start a virtual environment
   ```
   $ python3 -m venv venv
   $ . venv/bin/activate
   ```
3. Install requirements and additional upgrades
   ```
   $ pip3 install -r requirements.txt
   $ pip3 install PyObjC # upgrade for subprocess in Python2
   ```
4. Start the program
   ```
   $ . venv/bin/activate # start virtual environment if it has not been started already
   $ flask run
   ```