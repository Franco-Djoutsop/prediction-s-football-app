const Pool = require('pg').Pool
const pool = new Pool({
    user : "postgres",
    database : "db_prediction_nodejs",
    host : "localhost",
    password : "Root420",
    port : 5432
})

const getCompetitions = (req, res)=>{
    pool.query("SELECT * FROM competitions ORDER BY id_competition ASC", (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const getCompetitionById = (req, res)=>{
    const id = parseInt(req.params.id)
    pool.query("SELECT * FROM competitions WHERE id_competition=$1",[id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const createCompetition = (req, res)=>{
    const {competition_name, team_status} = req.body
    const id = parseInt(req.params.id)
    pool.query("INSERT INTO competitions (competition_name, team_status) VALUES ($1, $2) RETURNING *", [competition_name, team_status], (error, results)=>{
        if(error){
            throw error
        }
        res.status(201).send(`competitions add with ID : ${results.rows[0].id_competition}`)
    })
}

const updateCompetition = (req, res)=>{
    const id = parseInt(req.params.id)
    const {competition_name, team_status}=req.body

    pool.query("UPDATE competitions SET competition_name=$1,team_status=$2 WHERE id_competition = $3 ", [competition_name,team_status,id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`competitions modified with ID : ${id}`)
    })
}

const deleteCompetition =(req, res)=>{
    const id = parseInt(req.params.id)
    pool.query("DELETE FROM competitions WHERE id_competition = $1",[id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`delete competitions with ID : ${id}`)
    })
}

module.exports = {
    getCompetitions,
    getCompetitionById,
    createCompetition,
    updateCompetition,
    deleteCompetition
}

