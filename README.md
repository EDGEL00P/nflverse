# NFLVerse Web Dashboard

This repository is structured to mirror the upstream nflverse project layout so you can set up your own repo the same way.

<img src="https://github.com/user-attachments/assets/43cc10cd-42dd-4095-af96-0f109bee0a02" width="800">

An interactive web-based NFL data dashboard for exploring teams, games, players, and standings. Built with Flask and vanilla JavaScript for a fast, responsive experience.

## Installation

### R package (nflverse)

Upstream repository:
- Homepage: https://github.com/nflverse/nflverse/
- Git: https://github.com/nflverse/nflverse.git

To install the nflverse R package from CRAN:

```r
install.packages("nflverse")
```

For the development version:

```r
if (!require("pak")) install.packages("pak")
pak::pak("nflverse/nflverse")
```

Or install the prebuilt development build:

```r
install.packages("nflverse", repos = c("https://nflverse.r-universe.dev", getOption("repos")))
```

### Local dashboard (this repo)

The included Flask/JS dashboard can still be run locally:

```bash
git clone https://github.com/EDGEL00P/nflverse.git
cd nflverse
cp .env.example .env  # keeps local config consistent (port/debug)
pip install -r requirements.txt
python app.py
```

Then open your browser and navigate to `http://localhost:5000`

## Usage

Running `python app.py` will start a local Flask server that provides:

### Interactive Web Interface

The dashboard includes four main sections accessible via tabs:

1. **Teams** - View all 32 NFL teams with conference and division filters
2. **Games** - Browse recent playoff games with scores and game details  
3. **Standings** - Check current standings sorted by wins
4. **Players** - Search and explore featured NFL players

<img src="https://github.com/user-attachments/assets/16c34b48-7022-4a29-a75b-8dcf746acf9f" width="800">

### API Endpoints

The backend provides REST API endpoints for programmatic access:

```
GET /api/nfl/teams      - All NFL teams
GET /api/nfl/games      - Recent games
GET /api/nfl/standings  - Team standings
GET /api/nfl/players    - Featured players
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

## Features

The NFLVerse web dashboard provides:

- 🏈 **Teams Explorer** - Browse all 32 NFL teams with filtering by conference and division
- 📊 **Games Dashboard** - View recent playoff games with scores, dates, and game status
- 📈 **Standings Table** - Check team standings with win-loss records sorted by performance
- 👥 **Players Directory** - Explore featured NFL players with real-time search functionality
- 🎨 **Responsive Design** - Beautiful gradient theme with smooth animations that works on all devices
- ⚡ **Fast Performance** - Vanilla JavaScript with no heavy frameworks for instant interactions

## Getting Help

The best places to get help on this project are:

- The [nflverse discord](https://discord.com/invite/5Er2FBnnQa) (for both this project as well as anything NFL data related)
- [Opening an issue](https://github.com/EDGEL00P/nflverse/issues) for bug reports or feature requests

## Contributing

Many hands make light work! Here are some ways you can contribute to this project:

- **Report bugs or request features** - Open an [issue](https://github.com/EDGEL00P/nflverse/issues) if you'd like to request specific features or report a bug/error
- **Submit pull requests** - If you'd like to contribute code, please check out the repository and submit a PR
- **Improve documentation** - Help make the docs clearer and more comprehensive
- **Add features** - Implement new features like live updates or additional statistics

### Development Guidelines

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and test thoroughly
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## Project Structure

```
nflverse/
├── app.py                 # Flask backend application with API endpoints
├── requirements.txt       # Python dependencies
├── .gitignore            # Git ignore rules
├── .env.example          # Environment variables template
├── README.md             # This documentation
└── static/               # Frontend files
    ├── index.html        # Main HTML page
    ├── css/
    │   └── style.css     # Styles and animations
    └── js/
        └── nfl.js        # JavaScript functionality
```

## Deployment

For production deployment:

### Using Gunicorn (Recommended)

```bash
# Install Gunicorn
pip install gunicorn

# Run with Gunicorn
gunicorn app:app
```

### Cloud Platforms

The application is ready for deployment to:
- **Heroku** - Add a `Procfile` with `web: gunicorn app:app`
- **AWS Elastic Beanstalk** - Deploy using the AWS CLI
- **Google App Engine** - Add an `app.yaml` configuration
- **Azure App Service** - Deploy via Azure CLI or GitHub Actions

### Environment Variables

Set the `PORT` environment variable for custom port configuration:

```bash
export PORT=5000
python app.py
```

## Future Enhancements

- Integration with real NFL data APIs (nflfastR data, ESPN, official NFL API)
- Live score updates and real-time game tracking
- Advanced player statistics and performance metrics
- Game predictions and win probability analytics  
- User authentication and personalized team favorites
- Historical data visualization and trend analysis
- Mobile app version (React Native or Flutter)
- GraphQL API for more flexible data queries

## Terms of Use

The Python code for this project is released as open source under the **MIT License**. 

NFL data displayed in this application belongs to the National Football League and its respective owners, and are governed by their terms of use. This dashboard is for educational and demonstration purposes.

## License

MIT License - see LICENSE file for details

## Acknowledgments

Inspired by the [nflverse](https://github.com/nflverse/nflverse) R ecosystem for NFL data analysis. This web dashboard aims to provide an accessible browser-based interface for exploring NFL data.
