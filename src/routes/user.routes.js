const Router = require('koa-router');
const userService = require('../services/user.service.js');
const { ObjectID } = require('mongodb').ObjectID;
const HttpStatus = require('http-status-codes');
const auth = require('../utils/auth.js');

const router = new Router();

router.post('/login', async (ctx) => {
  const { email } = ctx.request.body;
  const { password } = ctx.request.body;
  const user = await userService.validatePassword(email, password);
  if (user) {
    ctx.body = { token: auth.issue({ email: user.email, id: user._id }) };
  }
});

router.post('/register', auth.verificationHandler(), async (ctx) => {
  await userService.insert(ctx.request.body);
  ctx.status = HttpStatus.CREATED;
});

router.use(auth.errorHandler()).use(auth.jwt());

router.get('/user/:id', auth.verificationHandler(), async (ctx) => {
  if (ctx.params.id !== ctx.state.user._id.toString()) {
    ctx.throw(HttpStatus.UNAUTHORIZED);
  }

  const query = { _id: ObjectID(ctx.params.id) };

  ctx.body = await userService.findOne(query, ctx.state.user);
  ctx.status = HttpStatus.OK;
});

router.put('/user/:id', auth.verificationHandler(), async (ctx) => {
  if (ctx.params.id !== ctx.state.user._id.toString()) {
    ctx.throw(HttpStatus.UNAUTHORIZED);
  }

  const query = { _id: ObjectID(ctx.params.id) };
  const update = ctx.request.body;

  ctx.body = await userService.update(query, update, ctx.state.user);
  ctx.status = HttpStatus.OK;
});

router.delete('/user/:id', auth.verificationHandler(), async (ctx) => {
  if (ctx.params.id !== ctx.state.user._id.toString()) {
    ctx.throw(HttpStatus.UNAUTHORIZED);
  }

  const query = { _id: ObjectID(ctx.params.id) };

  ctx.body = await userService.remove(query, ctx.state.user);
  ctx.status = HttpStatus.OK;
});

module.exports.routes = router.routes();
