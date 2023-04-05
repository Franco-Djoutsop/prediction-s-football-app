const { query } = require('express')

const Pool = require('pg').Pool
const pool = new Pool({
    user : "postgres",
    host : "localhost",
    password : 'Root420',
    database : 'db_prediction_nodejs',
    port : 5432
})

const getResults = (req, res)=>{
    pool.query('SELECT * FROM result ORDER BY id_result ASC', (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const getResultById = (req, res) =>{
    const id = parseInt(req.params.id)

    pool.query('SELECT * FROM result WHERE id_result = $1', [id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const createResult = (req, res) =>{
    const {score} = req.body
    pool.query('INSERT INTO result (score) VALUES($1) RETURNING *', [score], (error, results)=>{
        if(error){
            throw error
        }
        res.status(201).send(`result add with ID : ${results.rows[0].id_result}`)
    })
}

const updateResult = (req, res)=>{
    const id = parseInt(req.params.id)
    const {score} = req.body

    pool.query("UPDATE result SET score=$1 WHERE id_result = $2 ",[score,id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`result modified with ID: ${id}`)
    })
}

const deleteResult = (req, res) => {
    const id = parseInt(req.params.id)

    pool.query('DELETE FROM result WHERE id_result = $1',[id],(error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`result delete with ID : ${id}`)
    })
}

module.exports = {
    getResults,
    getResultById,
    createResult,
    updateResult,
    deleteResult
}