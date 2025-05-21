const http = require('http');
const fs = require('fs');
const path = require('path');

const BACKEND_URL = 'http://localhost:5000';

const server = http.createServer((req, res) => {
    if (req.url === '/') {
        const filePath = path.join(__dirname, 'index.html');
        fs.readFile(filePath, (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('Internal Server Error');
            } else {
                res.writeHead(200, { 'Content-Type': 'text/html' });
                res.end(data);
            }
        });
    } else if (req.url === '/frontend.js') {
        const filePath = path.join(__dirname, 'frontend.js');
        fs.readFile(filePath, (err, data) => {
            if (err) {
                res.writeHead(500, { 'Content-Type': 'text/plain' });
                res.end('Internal Server Error');
            } else {
                res.writeHead(200, { 'Content-Type': 'application/javascript' });
                res.end(data);
            }
        });
    } else if (req.url === '/products') {
        const backendReq = http.request(`${BACKEND_URL}/data`, backendRes => {
            let data = '';
            backendRes.on('data', chunk => {
                data += chunk;
            });
            backendRes.on('end', () => {
                res.writeHead(backendRes.statusCode, { 'Content-Type': 'application/json' });
                res.end(data);
            });
        });

        backendReq.on('error', err => {
            res.writeHead(500, { 'Content-Type': 'text/plain' });
            res.end('Error communicating with backend');
        });

        backendReq.end();
    } else {
        res.writeHead(404, { 'Content-Type': 'text/plain' });
        res.end('Not Found');
    }
});

server.listen(3000, () => {
    console.log('Frontend server is running on http://localhost:3000');
});