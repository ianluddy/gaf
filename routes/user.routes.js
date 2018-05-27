const Router = require("koa-router");
const userService = require('../services/user.service.js');
const ObjectID = require("mongodb").ObjectID;
const HttpStatus = require('http-status-codes');
const auth = require("../utils/auth.js");

const router = new Router();

router.post("/login", async (ctx) => {
  const email = ctx.request.body.email;
  const password = ctx.request.body.password;
  const user = await userService.validatePassword(email, password);
  if (user) {
    ctx.body = { token: auth.issue({ email: user.email, id: user._id }) }
  }
});

router.use(auth.errorHandler()).use(auth.jwt());

router.get("/user", auth.verificationHandler(), async (ctx) => {
  ctx.body = await userService.find();
  ctx.status = HttpStatus.OK;
});

router.post("/user", auth.verificationHandler(), async (ctx) => {
  await userService.insert(ctx.request.body);
  ctx.status = HttpStatus.CREATED;
});

router.get("/user/:id", auth.verificationHandler(), async (ctx) => {
  const query = {"_id": ObjectID(ctx.params.id)};
  ctx.body = await userService.findOne(query);
  ctx.status = HttpStatus.OK;
});

router.put("/user/:id", auth.verificationHandler(), async (ctx) => {
  const query = {"_id": ObjectID(ctx.params.id)};
  const update = ctx.request.body;
  ctx.body = await userService.update(query, update);
  ctx.status = HttpStatus.OK;
});

router.delete("/user/:id", auth.verificationHandler(), async (ctx) => {
  const query = {"_id": ObjectID(ctx.params.id)};
  ctx.body = await userService.remove(query);
  ctx.status = HttpStatus.OK;
});

module.exports.routes = router.routes();
