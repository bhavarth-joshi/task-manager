const bcrypt = require('bcryptjs');
const jwt = require('jsonwebtoken');
const { createUser, findUserByUsername } = require('../models/userModel');

const register = async (req, res) => {
    const { username, password } = req.body;
    const hashedPassword = await bcrypt.hash(password, 10);

    findUserByUsername(username, (err, user) => {
        if (user) return res.status(400).json({ message: 'User already exists' });

        createUser(username, hashedPassword, (err) => {
            if (err) return res.status(500).json({ message: 'Registration failed' });
            res.status(201).json({ message: 'User registered successfully' });
        });
    });
};

const login = async (req, res) => {
    const { username, password } = req.body;

    findUserByUsername(username, async (err, user) => {
        if (!user) return res.status(400).json({ message: 'Invalid credentials' });

        const isMatch = await bcrypt.compare(password, user.password);
        if (!isMatch) return res.status(400).json({ message: 'Invalid credentials' });

        const token = jwt.sign({ id: user.id }, process.env.JWT_SECRET, { expiresIn: '1d' });
        res.json({ token });
    });
};

module.exports = { register, login };
