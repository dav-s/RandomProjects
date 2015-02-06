var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");

var ps = [];


var anim_frame = window.requestAnimationFrame ||
                window.mozRequestAnimationFrame ||
                window.webkitRequestAnimationFrame;

drawSegments(ctx, ps);

c.addEventListener("click", function(event){
    ps.push(new Point(event.pageX - c.offsetLeft, event.pageY - c.offsetTop));
    clearCanvas(ctx, c);
    drawSegments(ctx, ps);
}, false);

function clickStart(){
    animateBezierCurve(ctx, ps, 1);
}

function clickUndo(){
    ps.pop();
    clearCanvas(ctx, c);
    drawSegments(ctx, ps);

}

function clickReset(){
    ps = [];
    clearCanvas(ctx, c);
}

function animateBezierCurve(ctx, ps, pc){
    var cperc = 0;
    var tps = [];
    var anim = function(){
        if(cperc>100) {
            clearCanvas(ctx, c);
            drawSegments(ctx, ps);
            drawLines(ctx, tps);
            return;
        }

        clearCanvas(ctx, c);

        drawLines(ctx, tps);

        drawSegmentWeb(ctx, ps, cperc);
        tps.push(getWebMid(ps, cperc));
        cperc += pc;

        anim_frame(anim);
    };
    anim();
}

function getWebMid(ps, perc){
    while(ps.length>1){
        ps = getPercentSegments(ps, perc);
    }
    return ps[0];
}


function Point(x, y){
    this.x = x;
    this.y = y;
}

function clearCanvas(ctx, canvas){
    ctx.moveTo(0,0);
    ctx.clearRect(0, 0, canvas.width, canvas.height);
}

function drawLine(ctx, p1, p2){
    ctx.beginPath();
    ctx.moveTo(p1.x, p1.y);
    ctx.lineTo(p2.x, p2.y);
    ctx.stroke();
}

function drawLines(ctx, ps){
    for(var i = 0; i < ps.length-1; i++){
        drawLine(ctx, ps[i], ps[i+1]);
    }
}

function drawSquare(ctx, p, r){
    ctx.fillRect(p.x-r/2, p.y-r/2, r, r);
}

function drawSegment(ctx, p1, p2){
    drawSquare(ctx, p1, 4);
    drawLine(ctx, p1, p2);
    drawSquare(ctx, p2, 4);
}

function drawSegments(ctx, ps){
    if(ps.length<1){
        return;
    }
    drawSquare(ctx, ps[0], 4);
    for(var i = 1; i < ps.length; i++){
        drawLine(ctx, ps[i-1], ps[i]);
        drawSquare(ctx, ps[i], 4);
    }
}

function getPercentSegments(ps, perc){
    var nps = [];
    for(var i = 0; i < ps.length-1; i++){
        nps.push(new Point(ps[i].x + (ps[i+1].x-ps[i].x)*(perc/100.0),
                           ps[i].y + (ps[i+1].y-ps[i].y)*(perc/100.0)));
    }
    return nps;
}

function drawSegmentWeb(ctx, ps, perc){
    drawSegments(ctx, ps);
    while(ps.length>1){
        ps = getPercentSegments(ps, perc);
        drawSegments(ctx, ps);
    }
}