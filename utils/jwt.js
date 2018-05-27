const jwt = require("koa-jwt");
const cfg = require('../config.js');
const jwtInstance = jwt({secret: cfg.SECRET});
const jsonwebtoken = require("jsonwebtoken");
const jwtDecode = require('jwt-decode');
const HttpStatus = require('http-status-codes');

function JWTErrorHandler(ctx, next) {
  return next().catch((err) => {
    if (401 == err.status) {
      ctx.status = 401;
      ctx.body = {
        "error": "Not authorized"
      };
    } else {
      throw err;
    }
  });
};

function JWTVerification() {
  return async (ctx, next) => {
    ctx.state.user = jwtDecode(ctx.headers.authorization);
    if( false ) { // TODO
      ctx.throw(HttpStatus.UNAUTHORIZED);
    }
    await next();
  };
}

module.exports.issue =  (payload) => {
  return jsonwebtoken.sign(payload, cfg.SECRET);
};

module.exports.jwt = () => jwtInstance;
module.exports.errorHandler = () => JWTErrorHandler;
module.exports.verificationHandler = JWTVerification;
