function x()
{
	$(function () {
	        $("upload_pic").change(function () {
	            if (this.files && this.files[0]) {
	                var reader = new FileReader();

	                reader.onload = imageIsLoaded;
	                reader.readAsDataURL(this.files[0]);
	            }
	        });
	    });

    function imageIsLoaded(e) {
        $('#uploaded_pic').attr('src', e.target.result);
        $('#yourImage').attr('src', e.target.result);
    };
}

document.getElementById("show_pic").addEventListener("click", x);