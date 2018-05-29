import { ApiError } from './errors';
import { SECRET } from '../config';

const jwt = require('koa-jwt');
const jsonwebtoken = require('jsonwebtoken');
const jwtDecode = require('jwt-decode');
const HttpStatus = require('http-status-codes');
const userService = require('../services/user.service.js');

const jwtInstance = jwt({ secret: SECRET });

function jwtErrorHandler(ctx, next) {
  return next().catch((err) => {
    if (err.status === 401) {
      ctx.status = 401;
      ctx.body = {
        error: 'Not authorized',
      };
    } else {
      throw err;
    }
  });
}

function jwtVerificationHandler() {
  return async (ctx, next) => {
    const token = jwtDecode(ctx.headers.authorization);
    const user = await userService.findOne({ email: token.email });
    if (!user) {
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

module.exports.jwtIssue = payload => jsonwebtoken.sign(payload, SECRET);
module.exports.jwt = () => jwtInstance;
module.exports.jwtErrorHandler = () => jwtErrorHandler;
module.exports.jwtVerificationHandler = jwtVerificationHandler;
module.exports.jsonErrorResponse = jsonErrorResponse;
