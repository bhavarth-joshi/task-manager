const db = require('../config/db');

const createUser = (username, hashedPassword, callback) => {
    const query = `INSERT INTO users (username, password) VALUES (?, ?)`;
    db.run(query, [username, hashedPassword], callback);
};

const findUserByUsername = (username, callback) => {
    const query = `SELECT * FROM users WHERE username = ?`;
    db.get(query, [username], callback);
};

module.exports = {
    createUser,
    findUserByUsername,
};
