const Router = require("koa-router");
const userService = require('../services/user.service.js');
const ObjectID = require("mongodb").ObjectID;
const HttpStatus = require('http-status-codes');
const jwt = require("../utils/jwt.js");

const router = new Router();

router.post("/auth", async (ctx) => {
  let username = ctx.request.body.username;
  let password = ctx.request.body.password;

  if ( true ) { // TODO
    ctx.body = {
      token: jwt.issue({
        user: username, // TODO
      })
    }
  } else {
    ctx.status = 401;
    ctx.body = {error: "Invalid login"}
  }
});

module.exports.routes = router.routes();
