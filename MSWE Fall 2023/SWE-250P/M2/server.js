const http = require("http"); // http used to create server
const fs = require("fs"); // file used to read html/css/images
const path = require("path"); // path used for images directory



const server = http.createServer((req, res) => {
    if (req.url === '/' || req.url === '/index.html') {
        // Rendering HTML
        fs.readFile('index.html', function (error, data) {
            if (error) {
                res.writeHead(404, { 'Content-Type': 'text/html' });
                res.write('File not found');
            } else {
                res.write(data);
            }
            res.end();
        });
        
    } else if (req.url === '/style.css') {
        // Rendering CSS
        fs.readFile('style.css', function (error, data) {
            if (error) {
                res.writeHead(404, { 'Content-Type': 'text/html' });
                res.write('File not found');
            } else {
                res.write(data);
            }
            res.end();
        });

    } else {
        // Serve image files
        const imagePath = path.join(__dirname, req.url);
        fs.readFile(imagePath, function (error, data) {
            if (error) {
                res.writeHead(404, { 'Content-Type': 'text/html' });
                res.write('Image not found');
            } else {
                res.write(data);
            }
            res.end();
        });
    }
}).listen(80);

console.log('Server is running at http://localhost:80/');

