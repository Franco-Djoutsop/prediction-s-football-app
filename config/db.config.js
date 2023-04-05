//|___________________________________|
//|  configuration base de donnees    |
//|___________________________________|


module.exports = {
    HOST: "localhost",
    USER: "postgres",
    PASSWORD: "Root420",
    DB: "db_prediction_nodejs",
    dialect: "postgres",
    pool: {
      max: 5,
      min: 0,
      acquire: 30000,
      idle: 10000
    }
  };
