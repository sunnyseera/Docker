
// Create Server
const http = require('http')
const server = http.createServer((req, res) => {
    console.log('A new connection has been made')
    res.end('Hello World on my server')
})

// Listen on a port 
const port = process.env.port || 8080
server.listen(port, () => console.log('Listening...'))

// To test this run the following
    //  node server.js
        // Go to http://localhost:8080
