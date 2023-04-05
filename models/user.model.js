//|______________________________|
//|  creation de la table user   |
//|______________________________|

module.exports = (sequelize, Sequelize) => {
    const User = sequelize.define("users", {
      number: {
        type: Sequelize.STRING
      },
      email: {
        type: Sequelize.STRING
      },
      password: {
        type: Sequelize.STRING
      }
    });
  
    return User;
  };