const { query } = require('express')

const Pool = require('pg').Pool
const pool = new Pool({
    user : "postgres",
    host : "localhost",
    password : 'Root420',
    database : 'db_prediction_nodejs',
    port : 5432
})

const getGames = (req, res)=>{
    pool.query('SELECT * FROM game ORDER BY id_game ASC', (error, games)=>{
        if(error){
            throw error
        }
        res.status(200).json(games.rows)
    })
}

const getGameById = (req, res) =>{
    const id = parseInt(req.params.id)

    pool.query('SELECT * FROM game WHERE id_game = $1', [id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const createGame = (req, res) =>{
    const {home_team_name, away_team_name} = req.body
    pool.query('INSERT INTO game (home_team_name, away_team_name) VALUES($1,$2) RETURNING *', [home_team_name, away_team_name], (error, results)=>{
        if(error){
            throw error
        }
        res.status(201).send(`game add with ID : ${results.rows[0].id_game}`)
    })
}

const updateGame = (req, res)=>{
    const id = parseInt(req.params.id)
    const {home_team_name, away_team_name} = req.body

    pool.query("UPDATE game SET home_team_name=$1, away_team_name=$2 WHERE id_game = $3 ",[home_team_name, away_team_name,id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`game modified with ID: ${id}`)
    })
}

const deleteGame = (req, res) => {
    const id = parseInt(req.params.id)

    pool.query('DELETE FROM game WHERE id_game = $1',[id],(error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`game delete with ID : ${id}`)
    })
}

module.exports = {
    getGames,
    getGameById,
    createGame,
    updateGame,
    deleteGame
}