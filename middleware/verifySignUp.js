//|_________________________________________________________|
//|  verifier si les informations existent deja dans la bd  |
//|_________________________________________________________|



const db = require("../models");
const ROLES = db.ROLES;
const User = db.user;

checkDuplicateNumberOrEmail = (req, res, next) => {
  // Number
  User.findOne({
    where: {
      number: req.body.number
    }
  }).then(user => {
    if (user) {
      res.status(400).send({
        message: "Failed! number is already in use!"
      });
      return;
    }

    // Email
    User.findOne({
      where: {
        email: req.body.email
      }
    }).then(user => {
      if (user) {
        res.status(400).send({
          message: "Failed! Email is already in use!"
        });
        return;
      }

      next();
    });
  });
};

checkRolesExisted = (req, res, next) => {
  if (req.body.roles) {
    for (let i = 0; i < req.body.roles.length; i++) {
      if (!ROLES.includes(req.body.roles[i])) {
        res.status(400).send({
          message: "Failed! Role does not exist = " + req.body.roles[i]
        });
        return;
      }
    }
  }
  
  next();
};

const verifySignUp = {
  checkDuplicateNumberOrEmail: checkDuplicateNumberOrEmail,
  checkRolesExisted: checkRolesExisted
};

module.exports = verifySignUp;