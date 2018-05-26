const database = require('../utils/database.js');
const collection = 'user';

module.exports.find = async function() {
  return await database.find(collection);
}

module.exports.findOne = async function(query) {
  return await database.findOne(collection, query);
}

module.exports.findMany = async function(query) {
  return await database.find(collection, query);
}

module.exports.remove = async function(query) {
  return await database.remove(collection, query);
}

module.exports.update = async function(query, data) {
  return await database.update(collection, query, data);
}

module.exports.insertOne = async function(data) {
  return await database.insertOne(collection, data);
}
