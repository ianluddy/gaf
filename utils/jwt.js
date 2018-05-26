const jwt = require("koa-jwt");
const cfg = require('../config.js');
const jwtInstance = jwt({secret: cfg.SECRET});
const jsonwebtoken = require("jsonwebtoken");

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

// function JWTVerification(ctx, next) {
//   return next().catch((err) => {
//     if (401 == err.status) {
//       ctx.status = 401;
//       ctx.body = {
//         "error": "Not authorized"
//       };
//     } else {
//       throw err;
//     }
//   });
// };

function JWTVerification() {
  return async (ctx, next) => {
    // if (!ctx.state.user || !ctx.state.user.role.includes(USER_ROLES.ADMIN)) {
    //   ctx.throw(HTTP_STATUS_CODES.UNAUTHORIZED);
    // }
    console.log(ctx);

    await next();
  };
}

module.exports.issue =  (payload) => {
  return jsonwebtoken.sign(payload, cfg.SECRET);
};

module.exports.jwt = () => jwtInstance;
module.exports.errorHandler = () => JWTErrorHandler;
module.exports.verificationHandler = () => JWTVerification;
