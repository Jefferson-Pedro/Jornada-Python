$(document).ready(function() {
    var socket = io("localhost:5000")
    socket.on("connect", function() {
        console.log("conectou");
    });

    socket.on("message", function(data) {
        console.log("enviou mensagem");
        $("#chat-container").append($('<p>').text(data));
        // Scroll to the bottom of the chat container
        $("#chat-container").scrollTop($("#chat-container")[0].scrollHeight);
    });

    $("#botao").on('click', function() {
        console.log("clicou botao");
        socket.send($('#usuario').val() + ": " + $('#mensagem').val());
        $('#mensagem').val('');
    });
    $("#mensagem").on('keypress', function() {
        if (event.key === "Enter") {
            console.log("deu enter");
            socket.send($('#usuario').val() + ": " + $('#mensagem').val());
            $('#mensagem').val('');
        }
    });
});