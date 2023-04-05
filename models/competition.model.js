//|______________________________|
//|  creation de la table competition   |
//|______________________________|

const { Sequelize } = require(".");


module.exports = (sequelize, Sequelize)=>{
    const Comp = sequelize.define("competition" ,{
        id_competition:{
            type : Sequelize.INTEGER,
            primaryKey:true
        },
        competition_name :{
            type: Sequelize.STRING
        },
        team_status:{
            type: Sequelize.STRING
        }
    })

    return Comp;
}