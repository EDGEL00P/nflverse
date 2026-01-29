// NFL Dashboard JavaScript
const API_BASE = '';

// State management
let allTeams = [];
let allGames = [];
let allStandings = [];
let allPlayers = [];

// Initialize the app
document.addEventListener('DOMContentLoaded', () => {
    initializeTabs();
    loadTeams();
    loadGames();
    loadStandings();
    loadPlayers();
    setupFilters();
});

// Tab functionality
function initializeTabs() {
    const tabButtons = document.querySelectorAll('.tab-button');
    const tabContents = document.querySelectorAll('.tab-content');

    tabButtons.forEach(button => {
        button.addEventListener('click', () => {
            const tabName = button.getAttribute('data-tab');
            
            // Remove active class from all buttons and contents
            tabButtons.forEach(btn => btn.classList.remove('active'));
            tabContents.forEach(content => content.classList.remove('active'));
            
            // Add active class to clicked button and corresponding content
            button.classList.add('active');
            document.getElementById(tabName).classList.add('active');
        });
    });
}

// Load NFL Teams
async function loadTeams() {
    try {
        const response = await fetch(`${API_BASE}/api/nfl/teams`);
        const data = await response.json();
        
        // Validate response structure
        if (!data || !Array.isArray(data.data)) {
            throw new Error('Invalid response structure');
        }
        
        allTeams = data.data;
        displayTeams(allTeams);
    } catch (error) {
        console.error('Error loading teams:', error);
        document.getElementById('teamsContainer').innerHTML = 
            '<div class="error">Failed to load teams. Please try again later.</div>';
    }
}

function displayTeams(teams) {
    const container = document.getElementById('teamsContainer');
    
    if (teams.length === 0) {
        container.innerHTML = '<div class="loading">No teams found.</div>';
        return;
    }
    
    container.innerHTML = teams.map(team => `
        <div class="card">
            <h4>${team.name}</h4>
            <p><strong>Abbreviation:</strong> ${team.abbreviation}</p>
            <p><strong>City:</strong> ${team.city}</p>
            <div>
                <span class="badge badge-primary">${team.conference}</span>
                <span class="badge badge-secondary">${team.division}</span>
            </div>
        </div>
    `).join('');
}

// Load NFL Games
async function loadGames() {
    try {
        const response = await fetch(`${API_BASE}/api/nfl/games`);
        const data = await response.json();
        
        // Validate response structure
        if (!data || !Array.isArray(data.data)) {
            throw new Error('Invalid response structure');
        }
        
        allGames = data.data;
        displayGames(allGames);
    } catch (error) {
        console.error('Error loading games:', error);
        document.getElementById('gamesContainer').innerHTML = 
            '<div class="error">Failed to load games. Please try again later.</div>';
    }
}

function displayGames(games) {
    const container = document.getElementById('gamesContainer');
    
    if (games.length === 0) {
        container.innerHTML = '<div class="loading">No games found.</div>';
        return;
    }
    
    container.innerHTML = games.map(game => `
        <div class="game-card">
            <div class="game-info">
                <div class="game-teams">
                    ${game.away_team} @ ${game.home_team}
                </div>
                <div class="game-score">
                    ${game.away_score} - ${game.home_score}
                </div>
                <div class="game-meta">
                    ${game.week} • ${formatDate(game.date)} • ${game.status}
                </div>
            </div>
        </div>
    `).join('');
}

// Load NFL Standings
async function loadStandings() {
    try {
        const response = await fetch(`${API_BASE}/api/nfl/standings`);
        const data = await response.json();
        
        // Validate response structure
        if (!data || !Array.isArray(data.data)) {
            throw new Error('Invalid response structure');
        }
        
        allStandings = data.data;
        displayStandings(allStandings);
    } catch (error) {
        console.error('Error loading standings:', error);
        document.getElementById('standingsContainer').innerHTML = 
            '<div class="error">Failed to load standings. Please try again later.</div>';
    }
}

function displayStandings(standings) {
    const container = document.getElementById('standingsContainer');
    
    if (standings.length === 0) {
        container.innerHTML = '<div class="loading">No standings found.</div>';
        return;
    }
    
    // Create a copy before sorting to avoid mutating the original array
    const sortedStandings = [...standings].sort((a, b) => b.wins - a.wins);
    
    container.innerHTML = `
        <div class="standings-table">
            <div class="standings-header">
                <div class="standings-cell">Team</div>
                <div class="standings-cell">W</div>
                <div class="standings-cell">L</div>
                <div class="standings-cell">T</div>
                <div class="standings-cell">Conference</div>
                <div class="standings-cell">Division</div>
            </div>
            ${sortedStandings.map((team, index) => `
                <div class="standings-row ${index % 2 === 0 ? 'even' : 'odd'}">
                    <div class="standings-cell"><strong>${team.team}</strong></div>
                    <div class="standings-cell">${team.wins}</div>
                    <div class="standings-cell">${team.losses}</div>
                    <div class="standings-cell">${team.ties}</div>
                    <div class="standings-cell">
                        <span class="badge badge-primary">${team.conference}</span>
                    </div>
                    <div class="standings-cell">
                        <span class="badge badge-secondary">${team.division}</span>
                    </div>
                </div>
            `).join('')}
        </div>
    `;
}

// Load NFL Players
async function loadPlayers() {
    try {
        const response = await fetch(`${API_BASE}/api/nfl/players`);
        const data = await response.json();
        
        // Validate response structure
        if (!data || !Array.isArray(data.data)) {
            throw new Error('Invalid response structure');
        }
        
        allPlayers = data.data;
        displayPlayers(allPlayers);
    } catch (error) {
        console.error('Error loading players:', error);
        document.getElementById('playersContainer').innerHTML = 
            '<div class="error">Failed to load players. Please try again later.</div>';
    }
}

function displayPlayers(players) {
    const container = document.getElementById('playersContainer');
    
    if (players.length === 0) {
        container.innerHTML = '<div class="loading">No players found.</div>';
        return;
    }
    
    container.innerHTML = players.map(player => `
        <div class="card">
            <h4>${player.name}</h4>
            <p><strong>Team:</strong> ${player.team}</p>
            <p><strong>Position:</strong> ${player.position}</p>
            <p><strong>Number:</strong> #${player.number}</p>
        </div>
    `).join('');
}

// Setup filters
function setupFilters() {
    // Team filters
    const conferenceFilter = document.getElementById('conferenceFilter');
    const divisionFilter = document.getElementById('divisionFilter');
    
    if (conferenceFilter) {
        conferenceFilter.addEventListener('change', filterTeams);
    }
    
    if (divisionFilter) {
        divisionFilter.addEventListener('change', filterTeams);
    }
    
    // Standings filter
    const standingsConferenceFilter = document.getElementById('standingsConferenceFilter');
    if (standingsConferenceFilter) {
        standingsConferenceFilter.addEventListener('change', filterStandings);
    }
    
    // Player search
    const playerSearch = document.getElementById('playerSearch');
    if (playerSearch) {
        playerSearch.addEventListener('input', filterPlayers);
    }
}

function filterTeams() {
    const conference = document.getElementById('conferenceFilter').value;
    const division = document.getElementById('divisionFilter').value;
    
    let filtered = allTeams;
    
    if (conference) {
        filtered = filtered.filter(team => team.conference === conference);
    }
    
    if (division) {
        filtered = filtered.filter(team => team.division === division);
    }
    
    displayTeams(filtered);
}

function filterStandings() {
    const conference = document.getElementById('standingsConferenceFilter').value;
    
    let filtered = allStandings;
    
    if (conference) {
        filtered = filtered.filter(team => team.conference === conference);
    }
    
    displayStandings(filtered);
}

function filterPlayers() {
    const searchTerm = document.getElementById('playerSearch').value.toLowerCase();
    
    let filtered = allPlayers;
    
    if (searchTerm) {
        filtered = filtered.filter(player => 
            player.name.toLowerCase().includes(searchTerm) ||
            player.team.toLowerCase().includes(searchTerm) ||
            player.position.toLowerCase().includes(searchTerm)
        );
    }
    
    displayPlayers(filtered);
}

// Utility functions
function formatDate(dateString) {
    if (!dateString) {
        return 'Date TBD';
    }
    
    try {
        const date = new Date(dateString);
        if (isNaN(date.getTime())) {
            return 'Invalid Date';
        }
        return date.toLocaleDateString('en-US', { 
            month: 'short', 
            day: 'numeric', 
            year: 'numeric' 
        });
    } catch (error) {
        console.error('Error formatting date:', error);
        return 'Invalid Date';
    }
}
