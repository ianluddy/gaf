const cfg = require('../config.js');
const db = require('monk')(cfg.MONGO_URL);
const userCollection = db.get('user');

module.exports.find = async function(collectionName) {
  return await db.get(collectionName).find({}, function(err, data){
    return data;
  });
}

module.exports.findOne = async function(collectionName, query) {
  return await db.get(collectionName).findOne(query, function(err, data){
    return data;
  });
}

module.exports.findMany = async function(collectionName, query) {
  return await db.get(collectionName).find(query, function(err, data){
    return data;
  });
}

module.exports.remove = async function(collectionName, query) {
  return await db.get(collectionName).remove(query, function(err, data){
    return data;
  });
}

module.exports.update = async function(collectionName, query, data) {
  return await db.get(collectionName).update(query, data);
}

module.exports.insertOne = async function(collectionName, data) {
  return await db.get(collectionName).insert(data);
}
