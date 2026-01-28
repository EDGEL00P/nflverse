# NFLVerse Web Dashboard

<img src="https://github.com/user-attachments/assets/43cc10cd-42dd-4095-af96-0f109bee0a02" width="800">

An interactive NFL data dashboard for exploring teams, games, players, and standings. Built with Flask and vanilla JavaScript for a fast, responsive experience.

## Features

**NFLVerse** provides an easy-to-use web interface for:

- 🏈 **Teams** - Browse all 32 NFL teams with filtering by conference and division
- 📊 **Games** - View recent playoff games with scores and dates
- 📈 **Standings** - Check team standings with win-loss records sorted by performance
- 👥 **Players** - Explore featured NFL players with real-time search functionality
- 🎨 **Interactive UI** - Responsive design with smooth animations and live filtering

<img src="https://github.com/user-attachments/assets/16c34b48-7022-4a29-a75b-8dcf746acf9f" width="800">

## Installation

The easiest way to get started with the NFLVerse web dashboard is to clone it from GitHub and install dependencies:

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Quick Start

Clone the repository and install:

```bash
git clone https://github.com/EDGEL00P/nflverse.git
cd nflverse
pip install -r requirements.txt
```

Or use the development version:

```bash
# Clone the repository
git clone https://github.com/EDGEL00P/nflverse.git
cd nflverse

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Then open your browser and navigate to `http://localhost:5000`

## Usage

Running the NFLVerse dashboard will start a local Flask server that provides:

### Interactive Web Interface

The dashboard includes four main sections accessible via tabs:

1. **Teams** - View all NFL teams with conference and division filters
2. **Games** - Browse recent games with scores and game details
3. **Standings** - Check current standings sorted by wins
4. **Players** - Search and explore featured NFL players

### API Endpoints

The backend provides REST API endpoints for programmatic access:

```python
# Teams
GET /api/nfl/teams           # Get all NFL teams

# Games  
GET /api/nfl/games           # Get recent games

# Standings
GET /api/nfl/standings       # Get team standings

# Players
GET /api/nfl/players         # Get featured players
```

### Example Usage

```bash
# Get all teams
curl http://localhost:5000/api/nfl/teams

# Get games
curl http://localhost:5000/api/nfl/games

# Get standings
curl http://localhost:5000/api/nfl/standings
```

## Project Structure

```
nflverse/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── .env.example          # Environment variables template
├── README.md             # Documentation
└── static/               # Frontend files
    ├── index.html        # Main HTML page
    ├── css/
    │   └── style.css     # Styles and animations
    └── js/
        └── nfl.js        # JavaScript functionality
```

## Deployment

For production deployment:

1. Set environment variables:
```bash
export PORT=5000
```

2. Use a production WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn app:app
```

For deployment to cloud platforms, the application is ready for:
- Heroku
- AWS Elastic Beanstalk
- Google App Engine
- Azure App Service

## Getting Help

The best places to get help with this project are:

- Opening an [issue](https://github.com/EDGEL00P/nflverse/issues) for bug reports or feature requests
- The [nflverse discord](https://discord.com/invite/5Er2FBnnQa) for general R/NFL data questions
- Check existing issues and pull requests

## Contributing

Many hands make light work! Here are some ways you can contribute to this project:

- **Report bugs** - Open an issue if you find a bug or have a feature request
- **Submit pull requests** - Contributions are welcome! Please check existing issues first
- **Improve documentation** - Help make the docs clearer and more comprehensive
- **Add features** - Implement new features like live updates or additional statistics

### Development Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes thoroughly
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## Future Enhancements

- Integration with real NFL data APIs (nflfastR, ESPN, etc.)
- Live score updates and real-time game tracking
- Advanced player statistics and performance metrics
- Game predictions and win probability analytics
- User authentication and personalized favorites
- Historical data visualization and trend analysis
- Mobile app version

## Terms of Use

The code for this project is released as open source under the **MIT License**. 

NFL data displayed in this application belongs to the National Football League and its respective owners, and is governed by their terms of use. This dashboard is for educational and demonstration purposes.

## License

MIT License - see LICENSE file for details

## Acknowledgments

Inspired by the [nflverse](https://github.com/nflverse/nflverse) R ecosystem for NFL data analysis.

