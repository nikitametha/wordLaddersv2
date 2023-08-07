
# Word Ladders V2

Rendition of the Word Ladders Game invented by Lewis Carroll: https://en.wikipedia.org/wiki/Word_ladder

Updated version equipped with tests and Github Actions pipeline with Docker, solely for author's learning.





## Authors

- [@nikitametha](https://www.nikitametha.com)



## Demo

Insert gif or link to demo


## Screenshots

![App Screenshot](https://via.placeholder.com/468x300?text=App+Screenshot+Here)


## Features

- Two modes
    - Play Game: System gives start and end word, user makes the word ladder.
    - PathFinder (Word Ladder Solver): User provides start and end word, system finds the word ladder.

- Play Game Mode
    - Hint provided after user enters a guess.
    - Button to give up next word also present.

- PathFinder
    - Finds shortest word path from start to end word (if present).
    - Tells user if either word is invalid dictionary word.



## Installation

Run with Docker

```bash
  TODO
```

    
## Run Locally
This project was created to run in a Docker container whose image can be found over at: TODO

Nevertheless, if you'd like to make changes to the code and run locally, then:



Clone the project

```bash
  git clone https://github.com/nikitametha/wordLaddersv2.git
```

Go to the project directory

```bash
  cd wordLaddersv2
```

Install pip for python if not already installed (below cmd is for Debian OS/Ubuntu)

```bash
   python -m pip install
```

Install Dependencies

```bash
   pip install -r requirements.txt
```

Start the flask server

```bash
  cd src
  python game_flask.py
```


## Improvements

- Improve design (main purpose of this project was backend, tests and devops)
- PathFinder input can check for invalid words as soon as user enters a word and before user clicks submit (using ajax)
