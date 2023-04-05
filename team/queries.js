const Pool = require('pg').Pool
const pool = new Pool({
    user : "postgres",
    database : "db_prediction_nodejs",
    host : "localhost",
    password : "Root420",
    port : 5432
})

const getTeams = (req, res)=>{
    pool.query("SELECT * FROM teams ORDER BY id ASC", (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const getTeamById = (req, res)=>{
    const id = parseInt(req.params.id)
    pool.query("SELECT * FROM teams WHERE id=$1",[id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const createTeam = (req, res)=>{
    const {name_team, logo_team} = req.body
    const id = parseInt(req.params.id)
    pool.query("INSERT INTO teams (name_team, logo_team) VALUES ($1, $2) RETURNING *", [name_team, logo_team], (error, results)=>{
        if(error){
            throw error
        }
        res.status(201).send(`teams add with ID : ${results.rows[0].id}`)
    })
}

const updateTeam = (req, res)=>{
    const id = parseInt(req.params.id)
    const {name_team, logo_team}=req.body

    pool.query("UPDATE teams SET name_team=$1,logo_team=$2 WHERE id = $3 ", [name_team,logo_team,id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`teams modified with ID : ${id}`)
    })
}

const deleteTeam =(req, res)=>{
    const id = parseInt(req.params.id)
    pool.query("DELETE FROM teams WHERE id = $1",[id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`delete team with ID : ${id}`)
    })
}

module.exports = {
    getTeams,
    getTeamById,
    createTeam,
    updateTeam,
    deleteTeam,
}

