const Koa = require("koa");
const logger = require('koa-logger');
const bodyParser = require('koa-bodyparser');

const authRouter = require('./routes/auth.routes.js');
const userRouter = require('./routes/user.routes.js');

const app = new Koa();

app.use(logger());
app.use(bodyParser());

app.use(authRouter.routes);
app.use(userRouter.routes);
// app.use(userRouter.allowedMethods());

app.listen(3000);
