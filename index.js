const Koa = require("koa");
const logger = require('koa-logger');
const bodyParser = require('koa-bodyparser');

const app = new Koa();

app.use(logger());
app.use(bodyParser());

app.use(require('./routes/user.routes.js').routes);//.use(router.allowedMethods());

app.listen(3000);
