//|______________________________|
//|  creation de la table team   |
//|______________________________|


module.exports = (sequelize, Sequelize)=>{
    const Team = sequelize.define("team", {
        id_team :{
            type: Sequelize.INTEGER,
            primarykey: true
        },
        name_team:{
            type: Sequelize.STRING
        },
        logo_team:{
            type:Sequelize.STRING
        }
    })
    return Team
}