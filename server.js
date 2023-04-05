const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();

var corsOptions = {
  origin: "http://localhost:8081"
};

app.use(cors(corsOptions));

// parse requests of content-type - application/json
app.use(bodyParser.json());

// parse requests of content-type - application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: true }));

const db = require("./app/models");
const Role = db.role;

db.sequelize.sync

// db.sequelize.sync({force: true}).then(() => {
//   console.log('Drop and Resync Db');
//   initial();
// });
// simple route
app.get("/", (req, res) => {
  res.json({ message: "Welcome to prediction's application." });
});

//routes prediction
const pred = require('./app/predictions/queries')
app.get('/predictions',pred.getPredictions)
app.get('/prediction/:id', pred.getPredictionById)
app.post('/predictions', pred.createPrediction)
app.put('/predictions/:id', pred.updatePrediction)
app.delete('/prediction/:id', pred.deletePrediction)


//routes calendar
const cal = require('./app/calendar/queries')
app.get('/calendars',cal.getCalendars)
app.get('/calendar/:id', cal.getCalendarById)
app.post('/calendars', cal.createCalendar)
app.put('/calendars/:id', cal.updateCalendar)
app.delete('/calendar/:id', cal.deleteCalendar)

//routes Result
const rel = require('./app/result/queries')
app.get('/results',rel.getResults)
app.get('/result/:id', rel.getResultById)
app.post('/results', rel.createResult)
app.put('/results/:id', rel.updateResult)
app.delete('/result/:id', rel.deleteResult)


//routes games
const gam = require('./app/games/queries')
app.get('/games',gam.getGames)
app.get('/game/:id', gam.getGameById)
app.post('/games', gam.createGame)
app.put('/games/:id', gam.updateGame)
app.delete('/game/:id', gam.deleteGame)


//routes competition
const com = require('./app/competition/queries')
app.get('/competitions',com.getCompetitions)
app.get('/competition/:id', com.getCompetitionById)
app.post('/competitions', com.createCompetition)
app.put('/competitions/:id', com.updateCompetition)
app.delete('/competition/:id', com.deleteCompetition)

//routes Teams
const tea = require('./app/team/queries')
app.get('/teams',tea.getTeams)
app.get('/team/:id', tea.getTeamById)
app.post('/teams', tea.createTeam)
app.put('/teams/:id', tea.updateTeam)
app.delete('/team/:id', tea.deleteTeam)

// set port, listen for requests
const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}.`);
});

function initial() {
    Role.create({
      id: 1,
      name: "user"
    });
   
    // Role.create({
    //   id: 2,
    //   name: "moderator"
    // });
   
    Role.create({
      id: 2,
      name: "admin"
    });
  }

  // routes
require('./app/routes/auth.routes')(app);
require('./app/routes/user.routes')(app);
