const fs = require('fs')

module.exports = {
    devServer: {
        open: process.platform === 'darwin',
        host: 'localhost',
        port: 8080, // CHANGE YOUR PORT HERE!
        https: {
            key: fs.readFileSync('../key.pem'),
            cert: fs.readFileSync('../cert.pem'),
        },
        hotOnly: false,
    },
}