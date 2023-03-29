"use strict";
const express = require('express');
const app = express();
const http = require('http');
const httpServer = http.Server(app);
const io = require('socket.io')(httpServer);


app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
})


app.get('/socket.io.js', (req, res, next) => {
	return res.sendFile(__dirname + '/node_modules/socket.io-client/dist/socket.io.js');
});


io.on('connection', (socket) => {
    console.log("User is connected");

    socket.on('message', (data) => {
        socket.broadcast.emit('message', data);
    })

    // On click of "Pause" button, disconnects socket server
    // Note: Client in Python still running in background, clicking "Start" button will turn the server back on
    socket.on('pause', (data) => {
        console.log(data);
        socket.broadcast.emit('pause', data);
        socket.broadcast.emit('disconnect')
    })

    socket.on('disconnect', () =>{
        console.log('User Disconnected')
        socket.disconnect();
    })
})

httpServer.listen(3000, () => {
    console.log("Server is running on the port 3000");
})