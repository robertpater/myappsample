//https://www.youtube.com/watch?v=yAHl_kpqr-k&list=PL7wAPgl1JVvUEb0dIygHzO4698tmcwLk9&index=2
//Coding Math: Episode 2 - Intro to Trigonometry
window.onload = function(){
    var canvas = document.getElementById("canvas"),
        context = canvas.getContext("2d"),
        width = canvas.width = window.innerWidth,
        height = canvas.height = window.innerHeight;

    context.translate(0, height / 2);
    context.scale(1, -1);
    for(var angle = 0; angle < Math.PI * 2; angle += .01){
        var x = angle * 200,
            y = Math.sin(angle) * 200;

        context.fillRect(x,y,5,5)
        //console.log(Math.sin(angle)); Ctr+Shift+J uruchamia konsole na ktorej widac zmiany
    }
};
