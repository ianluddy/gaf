const jwt = require("koa-jwt");
const cfg = require('../config.js');
const ApiError = require('./errors.js').ApiError;
const jwtInstance = jwt({secret: cfg.SECRET});
const jsonwebtoken = require("jsonwebtoken");
const jwtDecode = require('jwt-decode');
const bcrypt = require('bcrypt');
const HttpStatus = require('http-status-codes');
const userService = require('../services/user.service.js');

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
    const token = jwtDecode(ctx.headers.authorization);
    const user = await userService.findOne({ email: token.email });
    if(!user) {
      ctx.throw(HttpStatus.UNAUTHORIZED);
    }
    ctx.state.user = user;
    await next();
  };
}

function jsonErrorResponse() {
  return async function middleware(ctx, next) {
    try {
      await next();
    } catch (err) {
      if (err instanceof ApiError && err.code && err.message) {
        ctx.status = 500;
        ctx.body = { errorCode: err.code, message: err.message };
      } else if (err.status) {
        ctx.status = err.status;
        ctx.body = { message: err.message };
      } else {
        ctx.status = 500;
        ctx.body = { message: err.message };
      }
      ctx.app.emit('error', err, ctx);
    }
  };
}

module.exports.issue = (payload) => {
  return jsonwebtoken.sign(payload, cfg.SECRET);
};

module.exports.jwt = () => jwtInstance;
module.exports.errorHandler = () => JWTErrorHandler;
module.exports.verificationHandler = JWTVerification;
module.exports.jsonErrorResponse = jsonErrorResponse;
