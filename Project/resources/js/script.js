// https://media1.tenor.com/images/9bc10e0d5763540af062bae2add60474/tenor.gif
events = {
    upload_button_click: function(){
        $(document).ready(function() {
            $("#upload_photo_button").click(function(){
                image_url = prompt('Insert Picture URL : ')
                if(image_url.includes('http') || image_url.includes('Http') || image_url.includes('Https') || image_url.includes('https')){
                    image = new Image();
                    image.src = image_url;

                    width = image.width;
                    height = image.height;
                    console.log(width)
                    console.log(height)
                    var paper = Raphael('#photo_preview', 170, 400, 0 ,100); // asezare in pagina
                    var img = paper.image(image_url, 0, 0, width, height);//.attr({ "clip-rect": "20,20,300,300" }); // poza
                }else{
                    alert('Invalid URL!')
                }
            }); 
        });    
    },

    read_url: function(event){
        readURL(event);
    }
}


function readURL(event){
    console.log(event)
    var getImagePath = URL.createObjectURL(event);
    console.log(getImagePath)
    return getImagePath
}

function init(){
    var paper = Raphael('#photo_preview', 170, 400, 0,100);
    var img = paper.image('https://media1.tenor.com/images/9bc10e0d5763540af062bae2add60474/tenor.gif', 0, 0, 335, 291)
           .attr({ "clip-rect": "20,20,300,300" });
    events.upload_button_click();    
}


init();


