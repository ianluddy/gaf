import { ERRORS, ApiError } from '../utils/errors';
import { MONGO_URL, SALT_ROUNDS } from '../config';

const bcrypt = require('bcrypt');
const userCollection = require('monk')(MONGO_URL).get('user');

async function validateEmail(email) {
  if (await userCollection.findOne({ email })) {
    throw new ApiError(ERRORS.USER_EXISTS);
  }
}

async function findOne(query) {
  return userCollection.findOne(query);
}

async function remove(query) {
  return userCollection.remove(query);
}

async function update(query, data) {
  const user = await findOne(query);

  if (user.email !== data.email) {
    await validateEmail(data.email);
  }

  data.password = bcrypt.hashSync(data.password, SALT_ROUNDS);
  return userCollection.update(query, data);
}

async function insert(data) {
  await validateEmail(data.email);

  data.password = bcrypt.hashSync(data.password, SALT_ROUNDS);
  return userCollection.insert(data);
}

async function validatePassword(email, password) {
  const user = await findOne({ email });

  if (!user) {
    throw new ApiError(ERRORS.USER_NOT_FOUND);
  }

  if (!bcrypt.compareSync(password, user.password)) {
    throw new ApiError(ERRORS.PASSWORD_INCORRECT);
  }

  return user;
}

module.exports.remove = remove;
module.exports.findOne = findOne;
module.exports.insert = insert;
module.exports.update = update;
module.exports.validatePassword = validatePassword;
