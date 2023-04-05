const { query } = require('express')

const Pool = require('pg').Pool
const pool = new Pool({
    user : "postgres",
    host : "localhost",
    password : 'Root420',
    database : 'db_prediction_nodejs',
    port : 5432
})

const getCalendars = (req, res)=>{
    pool.query('SELECT * FROM calendar ORDER BY id_Calendar ASC', (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const getCalendarById = (req, res) =>{
    const id = parseInt(req.params.id_calendar)

    pool.query('SELECT * FROM calendar WHERE id_Calendar = $1', [id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).json(results.rows)
    })
}

const createCalendar = (req, res) =>{
    const {date} = req.body
    pool.query('INSERT INTO calendar (date) VALUES($1) RETURNING *', [date], (error, results)=>{
        if(error){
            throw error
        }
        res.status(201).send(`Calendar add with ID : ${results.rows[0].id_calendar}`)
    })
}

const updateCalendar = (req, res)=>{
    const id = parseInt(req.params.id)
    const {date} = req.body

    pool.query("UPDATE calendar SET date=$1 WHERE id_calendar = $2 ",[date,id], (error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`calendar modified with ID: ${id}`)
    })
}

const deleteCalendar = (req, res) => {
    const id = parseInt(req.params.id)

    pool.query('DELETE FROM calendar WHERE id_calendar = $1',[id],(error, results)=>{
        if(error){
            throw error
        }
        res.status(200).send(`Calendar delete with ID : ${id}`)
    })
}

module.exports = {
    getCalendars,
    getCalendarById,
    createCalendar,
    updateCalendar,
    deleteCalendar
}