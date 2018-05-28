const Koa = require("koa");
const logger = require('koa-logger');
const bodyParser = require('koa-bodyparser');
const auth = require('./utils/auth');

const userRouter = require('./routes/user.routes.js');

const app = new Koa();

app.use(logger());
app.use(bodyParser());
app.use(auth.jsonErrorResponse());

app.use(userRouter.routes);
// app.use(userRouter.allowedMethods());

app.listen(3000);
