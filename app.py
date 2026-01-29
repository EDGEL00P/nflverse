"""
Flask backend for nflverse website - NFL data only
"""
import os
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='static', static_url_path='')
CORS(app)


@app.route('/')
def index():
    """Serve the main NFL page"""
    return send_from_directory('static', 'index.html')


# NFL API Endpoints

@app.route('/api/nfl/teams')
def get_nfl_teams():
    """Get all NFL teams"""
    teams = [
        {"id": 1, "name": "Kansas City Chiefs", "abbreviation": "KC", "conference": "AFC", "division": "West", "city": "Kansas City"},
        {"id": 2, "name": "San Francisco 49ers", "abbreviation": "SF", "conference": "NFC", "division": "West", "city": "San Francisco"},
        {"id": 3, "name": "Buffalo Bills", "abbreviation": "BUF", "conference": "AFC", "division": "East", "city": "Buffalo"},
        {"id": 4, "name": "Philadelphia Eagles", "abbreviation": "PHI", "conference": "NFC", "division": "East", "city": "Philadelphia"},
        {"id": 5, "name": "Baltimore Ravens", "abbreviation": "BAL", "conference": "AFC", "division": "North", "city": "Baltimore"},
        {"id": 6, "name": "Detroit Lions", "abbreviation": "DET", "conference": "NFC", "division": "North", "city": "Detroit"},
        {"id": 7, "name": "Dallas Cowboys", "abbreviation": "DAL", "conference": "NFC", "division": "East", "city": "Dallas"},
        {"id": 8, "name": "Miami Dolphins", "abbreviation": "MIA", "conference": "AFC", "division": "East", "city": "Miami"},
        {"id": 9, "name": "Green Bay Packers", "abbreviation": "GB", "conference": "NFC", "division": "North", "city": "Green Bay"},
        {"id": 10, "name": "Los Angeles Rams", "abbreviation": "LAR", "conference": "NFC", "division": "West", "city": "Los Angeles"},
        {"id": 11, "name": "Tampa Bay Buccaneers", "abbreviation": "TB", "conference": "NFC", "division": "South", "city": "Tampa Bay"},
        {"id": 12, "name": "Cincinnati Bengals", "abbreviation": "CIN", "conference": "AFC", "division": "North", "city": "Cincinnati"},
        {"id": 13, "name": "Seattle Seahawks", "abbreviation": "SEA", "conference": "NFC", "division": "West", "city": "Seattle"},
        {"id": 14, "name": "Los Angeles Chargers", "abbreviation": "LAC", "conference": "AFC", "division": "West", "city": "Los Angeles"},
        {"id": 15, "name": "New England Patriots", "abbreviation": "NE", "conference": "AFC", "division": "East", "city": "New England"},
        {"id": 16, "name": "Pittsburgh Steelers", "abbreviation": "PIT", "conference": "AFC", "division": "North", "city": "Pittsburgh"},
        {"id": 17, "name": "Cleveland Browns", "abbreviation": "CLE", "conference": "AFC", "division": "North", "city": "Cleveland"},
        {"id": 18, "name": "Minnesota Vikings", "abbreviation": "MIN", "conference": "NFC", "division": "North", "city": "Minnesota"},
        {"id": 19, "name": "New Orleans Saints", "abbreviation": "NO", "conference": "NFC", "division": "South", "city": "New Orleans"},
        {"id": 20, "name": "Atlanta Falcons", "abbreviation": "ATL", "conference": "NFC", "division": "South", "city": "Atlanta"},
        {"id": 21, "name": "Carolina Panthers", "abbreviation": "CAR", "conference": "NFC", "division": "South", "city": "Carolina"},
        {"id": 22, "name": "Tennessee Titans", "abbreviation": "TEN", "conference": "AFC", "division": "South", "city": "Tennessee"},
        {"id": 23, "name": "Jacksonville Jaguars", "abbreviation": "JAX", "conference": "AFC", "division": "South", "city": "Jacksonville"},
        {"id": 24, "name": "Indianapolis Colts", "abbreviation": "IND", "conference": "AFC", "division": "South", "city": "Indianapolis"},
        {"id": 25, "name": "Houston Texans", "abbreviation": "HOU", "conference": "AFC", "division": "South", "city": "Houston"},
        {"id": 26, "name": "Denver Broncos", "abbreviation": "DEN", "conference": "AFC", "division": "West", "city": "Denver"},
        {"id": 27, "name": "Las Vegas Raiders", "abbreviation": "LV", "conference": "AFC", "division": "West", "city": "Las Vegas"},
        {"id": 28, "name": "New York Giants", "abbreviation": "NYG", "conference": "NFC", "division": "East", "city": "New York"},
        {"id": 29, "name": "New York Jets", "abbreviation": "NYJ", "conference": "AFC", "division": "East", "city": "New York"},
        {"id": 30, "name": "Washington Commanders", "abbreviation": "WAS", "conference": "NFC", "division": "East", "city": "Washington"},
        {"id": 31, "name": "Chicago Bears", "abbreviation": "CHI", "conference": "NFC", "division": "North", "city": "Chicago"},
        {"id": 32, "name": "Arizona Cardinals", "abbreviation": "ARI", "conference": "NFC", "division": "West", "city": "Arizona"},
    ]
    return jsonify({"data": teams})


@app.route('/api/nfl/games')
def get_nfl_games():
    """Get NFL games"""
    games = [
        {
            "id": 1,
            "home_team": "Kansas City Chiefs",
            "away_team": "Baltimore Ravens",
            "home_score": 17,
            "away_score": 10,
            "date": "2024-01-28",
            "week": "Conference Championship",
            "status": "Final",
            "quarter": "Final"
        },
        {
            "id": 2,
            "home_team": "San Francisco 49ers",
            "away_team": "Detroit Lions",
            "home_score": 34,
            "away_score": 31,
            "date": "2024-01-28",
            "week": "Conference Championship",
            "status": "Final",
            "quarter": "Final"
        },
        {
            "id": 3,
            "home_team": "Kansas City Chiefs",
            "away_team": "Buffalo Bills",
            "home_score": 27,
            "away_score": 24,
            "date": "2024-01-21",
            "week": "Divisional Round",
            "status": "Final",
            "quarter": "Final"
        },
        {
            "id": 4,
            "home_team": "San Francisco 49ers",
            "away_team": "Green Bay Packers",
            "home_score": 24,
            "away_score": 21,
            "date": "2024-01-20",
            "week": "Divisional Round",
            "status": "Final",
            "quarter": "Final"
        },
        {
            "id": 5,
            "home_team": "Baltimore Ravens",
            "away_team": "Houston Texans",
            "home_score": 34,
            "away_score": 10,
            "date": "2024-01-20",
            "week": "Divisional Round",
            "status": "Final",
            "quarter": "Final"
        },
        {
            "id": 6,
            "home_team": "Detroit Lions",
            "away_team": "Tampa Bay Buccaneers",
            "home_score": 31,
            "away_score": 23,
            "date": "2024-01-21",
            "week": "Divisional Round",
            "status": "Final",
            "quarter": "Final"
        },
    ]
    return jsonify({"data": games})


@app.route('/api/nfl/standings')
def get_nfl_standings():
    """Get NFL standings"""
    standings = [
        {"team": "Baltimore Ravens", "conference": "AFC", "wins": 13, "losses": 4, "ties": 0, "division": "North"},
        {"team": "Miami Dolphins", "conference": "AFC", "wins": 11, "losses": 6, "ties": 0, "division": "East"},
        {"team": "Kansas City Chiefs", "conference": "AFC", "wins": 11, "losses": 6, "ties": 0, "division": "West"},
        {"team": "Buffalo Bills", "conference": "AFC", "wins": 11, "losses": 6, "ties": 0, "division": "East"},
        {"team": "Houston Texans", "conference": "AFC", "wins": 10, "losses": 7, "ties": 0, "division": "South"},
        {"team": "Cleveland Browns", "conference": "AFC", "wins": 11, "losses": 6, "ties": 0, "division": "North"},
        {"team": "Pittsburgh Steelers", "conference": "AFC", "wins": 10, "losses": 7, "ties": 0, "division": "North"},
        {"team": "San Francisco 49ers", "conference": "NFC", "wins": 12, "losses": 5, "ties": 0, "division": "West"},
        {"team": "Dallas Cowboys", "conference": "NFC", "wins": 12, "losses": 5, "ties": 0, "division": "East"},
        {"team": "Detroit Lions", "conference": "NFC", "wins": 12, "losses": 5, "ties": 0, "division": "North"},
        {"team": "Tampa Bay Buccaneers", "conference": "NFC", "wins": 9, "losses": 8, "ties": 0, "division": "South"},
        {"team": "Philadelphia Eagles", "conference": "NFC", "wins": 11, "losses": 6, "ties": 0, "division": "East"},
        {"team": "Los Angeles Rams", "conference": "NFC", "wins": 10, "losses": 7, "ties": 0, "division": "West"},
        {"team": "Green Bay Packers", "conference": "NFC", "wins": 9, "losses": 8, "ties": 0, "division": "North"},
    ]
    return jsonify({"data": standings})


@app.route('/api/nfl/players')
def get_nfl_players():
    """Get NFL players"""
    players = [
        {"id": 1, "name": "Patrick Mahomes", "team": "Kansas City Chiefs", "position": "QB", "number": "15"},
        {"id": 2, "name": "Josh Allen", "team": "Buffalo Bills", "position": "QB", "number": "17"},
        {"id": 3, "name": "Lamar Jackson", "team": "Baltimore Ravens", "position": "QB", "number": "8"},
        {"id": 4, "name": "Brock Purdy", "team": "San Francisco 49ers", "position": "QB", "number": "13"},
        {"id": 5, "name": "Christian McCaffrey", "team": "San Francisco 49ers", "position": "RB", "number": "23"},
        {"id": 6, "name": "Travis Kelce", "team": "Kansas City Chiefs", "position": "TE", "number": "87"},
        {"id": 7, "name": "Tyreek Hill", "team": "Miami Dolphins", "position": "WR", "number": "10"},
        {"id": 8, "name": "CeeDee Lamb", "team": "Dallas Cowboys", "position": "WR", "number": "88"},
        {"id": 9, "name": "Dak Prescott", "team": "Dallas Cowboys", "position": "QB", "number": "4"},
        {"id": 10, "name": "Jalen Hurts", "team": "Philadelphia Eagles", "position": "QB", "number": "1"},
        {"id": 11, "name": "Joe Burrow", "team": "Cincinnati Bengals", "position": "QB", "number": "9"},
        {"id": 12, "name": "Justin Jefferson", "team": "Minnesota Vikings", "position": "WR", "number": "18"},
    ]
    return jsonify({"data": players})


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)
