
//To dispplay the selected image
function showImage(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#img')
                .attr('src', e.target.result)
                .width(200)
                .height(250)
                .css("display","block");
            $('td').removeClass("imageBox");
        };

        reader.readAsDataURL(input.files[0]);
    }
}

// to display the Demographics tab by default on page load
function load()
{
    document.getElementById('Demographics').style.display = "block";
}

// to display the tabs according
function getForm(evt,ID)
{
    var i, tabcontent, tablinks;
    tabcontent = document.getElementsByClassName("container");
    for (i = 0; i < tabcontent.length; i++)
    {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tab");
    for (i = 0; i < tablinks.length; i++) 
    {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(ID).style.display = "block";
}