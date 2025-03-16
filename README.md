# Verbos

A game to help practice conjugating verbs in Brazilian Portuguese. This is to be played with another individual who will keep track of which conjugations were correct and which were incorrect.

## Initial Set-up

1. Clone this repository.
2. Create a file in the directory `verbos/` called `config.py`.
3. Copy and paste the template from `example_config.py` into `config.py`.
4. In the terminal, run `openssl rand -base64 24`.
5. Replace `your-secret-key` in `config.py` with the value returned in step 4 and save.
6. Return to your terminal, navigate to the directory `verbos/`, and run the following:

```
python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
```

## Using the App

Each time you start the app, you will need to run:
1. `source env/bin/activate`
2. `python3 run.py`

This will let you access the requirements installed during the initial set-up.

After this, open `http://localhost:8000/` in your browser and play the game.

When you are finished, return to your terminal and press CTRL+C to quit. Then to exit the virtual environment, run `deactivate`


