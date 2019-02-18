// https://media1.tenor.com/images/9bc10e0d5763540af062bae2add60474/tenor.gif
events = {
    upload_button_click: function(paper){
        $(document).ready(function() {
            document.getElementById("upload-photo-button").click(function(){
                console.log('---#1')
                image_url = document.getElementById('input-photo').value
                console.log(image_url)
                console.log(image_url.toString()+ '/---#2')
                if(image_url.includes('http') || image_url.includes('Http') || image_url.includes('Https') || image_url.includes('https')){
                    image = new Image();
                    image.src = image_url;
                    console.log('--- #3')
                    width = image.width;
                    height = image.height;
                    
                    paper.image(image_url, 0, 0, width, height);//.attr({ "clip-rect": "20,20,300,300" }); // poza

                    paper.text(width-100, height+15, "ellipse").attr({'font-size': 30,fill: '#00ff00'});

                    console.log(width)
                    console.log(height)
                    console.log(image.src)
                }else{
                    alert('Invalid URL!')
                }
            }); 
        });    
    },

}



function init(){
    var paper = new Raphael('photo-preview',0,0,0,0); // asezare in pagina
    paper.image();
    // var img = paper.image('https://media1.tenor.com/images/9bc10e0d5763540af062bae2add60474/tenor.gif', 0, 0, 335, 291)
    //        .attr({ "clip-rect": "20,20,300,300" });
    console.log('#0')
    events.upload_button_click(paper);    
}


init();


