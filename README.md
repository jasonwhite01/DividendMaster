# dividendMaster

Application that is used to perform different types of analysis of a given stocks' dividend

## Design

Command Line (Main.py ticker=xyz) + API (App.py via "Flask run") app

### Frontend

Undecided yet - perhaps Vue.js

### Backend

Python
SQLite3 Database


## Features

1. (App.py) Basic command line tool (with API's exposed via Flask) 
2. (Main.py) LLM Chat app to get recommendations about a ticker's dividend performance fitness for an income investor.

## Features to add

### Major Features

1. *Full Stack App:* Add javascript front end, have it call the exposed API's.
2. _Goal Seeking Simulation:_ Add ability to calculate how long it would take to reach a dollar earnings goal for a given stock's dividend.
   
### Minor Features

1. LLM Chat - create flags for types of investors (first 2 ideas: growth, income) and adjust LLM prompting appropriately.

## Tech Debt

1. Abstract the LLM functionality such that the backend app can call it as needed.
