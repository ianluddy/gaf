const cfg = require('../config.js');
const errors = require('../utils/errors.js');
const bcrypt = require("bcrypt");
const userCollection = require('monk')(cfg.MONGO_URL).get('user');

async function findOne(query) {
  return userCollection.findOne(query);
}

async function remove(query) {
  return userCollection.remove(query);
}

async function update(query, data) {
  const user = await findOne(query);

  if (user.email != data.email)
    await validateEmail(data.email);

  data.password = bcrypt.hashSync(data.password, cfg.SALT_ROUNDS);
  return userCollection.update(query, data);
}

async function insert(data) {
  await validateEmail(data.email);
  data.password = bcrypt.hashSync(data.password, cfg.SALT_ROUNDS);
  return userCollection.insert(data);
}

async function validatePassword(email, password) {
  const user = await findOne({ email });

  if (!user)
    throw new errors.ApiError(errors.ERRORS.USER_NOT_FOUND);

  if (!bcrypt.compareSync(password, user.password))
    throw new errors.ApiError(errors.ERRORS.PASSWORD_INCORRECT);

  return user;
}

async function validateEmail(email) {
  if (await userCollection.findOne({ email }))
    throw new errors.ApiError(errors.ERRORS.USER_EXISTS);
}

module.exports.remove = remove;
module.exports.findOne = findOne;
module.exports.insert = insert;
module.exports.update = update;
module.exports.validatePassword = validatePassword;
