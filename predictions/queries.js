const { query } = require('express')

const Pool = require('pg').Pool
const pool = new Pool({
    user : "postgres",
    host : "localhost",
    password : 'Root420',
    database : 'db_prediction_nodejs',
    port : 5432
})

const getPredictions = (req, res)=>{
    pool.query('SELECT * FROM prediction ORDER BY id_prediction ASC', (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const getPredictionById = (req, res) =>{
    const id = parseInt(req.params.id)

    pool.query('SELECT * FROM prediction WHERE id_prediction = $1', [id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const createPrediction = (req, res) =>{
    const {condition, prediction_status} = req.body
    const id = parseInt(req.params.id)
    pool.query('INSERT INTO prediction (condition, prediction_status) VALUES($1,$2) RETURNING *', [condition,prediction_status], (error, results)=>{
        if(error){
            throw error
        }
        res.status(201).send(`prediction add with ID : ${results.rows[0].id_prediction}`)
    })
}

const updatePrediction = (req, res)=>{
    const id = parseInt(req.params.id_prediction)
    const {condition, prediction_status} = req.body

    pool.query("UPDATE prediction SET condition=$1, condition_status = $2 WHERE id = $3 ",[condition,prediction_status,id_prediction], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`predition modified with ID: ${id}`)
    })
}

const deletePrediction = (req, res) => {
    const id = parseInt(req.params.id_prediction)

    pool.query('DELETE FROM prediction WHERE id = $1',[id_prediction],(error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`prediction delete with ID : ${id}`)
    })
}

module.exports = {
    getPredictions,
    getPredictionById,
    createPrediction,
    updatePrediction,
    deletePrediction
}