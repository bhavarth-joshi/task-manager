require('dotenv').config(); // Load environment variables from .env file
const express = require('express');
const cors = require('cors');
const authRoutes = require('./routes/authRoutes');

const app = express();
const PORT = process.env.PORT || 5000;

// CORS Middleware (Move this before route handling)
app.use(cors({
    origin: 'http://localhost:5173', // Vue app frontend
    credentials: true
}));

// Middleware to parse JSON requests
app.use(express.json());

// Register routes
app.use('/api/auth', authRoutes);

// Start server
app.listen(PORT, () => {
    console.log(`Auth server running on http://localhost:${PORT}`);
});
