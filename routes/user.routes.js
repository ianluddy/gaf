const Router = require("koa-router");
const userService = require('../services/user.service.js');
const ObjectID = require("mongodb").ObjectID;
const HttpStatus = require('http-status-codes');
const jwt = require("../utils/jwt.js");

const router = new Router();

router.use(jwt.errorHandler()).use(jwt.jwt());

router.get("/user", async (ctx) => {
  ctx.body = await userService.find();
  ctx.status = HttpStatus.OK;
});

router.post("/user", async (ctx) => {
  await userService.insertOne(ctx.request.body);
  ctx.status = HttpStatus.CREATED;
});

router.get("/user/:id", async (ctx) => {
  const query = {"_id": ObjectID(ctx.params.id)};
  ctx.body = await userService.findOne(query);
  ctx.status = HttpStatus.OK;
});

router.put("/user/:id", async (ctx) => {
  const query = {"id": ObjectID(ctx.params.id)};
  const update = ctx.request.body;
  ctx.body = await userService.update(query, update);
  ctx.status = HttpStatus.OK;
});

router.delete("/user/:id", async (ctx) => {
  const query = {"id": ObjectID(ctx.params.id)};
  ctx.body = await userService.remove(query);
  ctx.status = HttpStatus.OK;
});

module.exports.routes = router.routes();
