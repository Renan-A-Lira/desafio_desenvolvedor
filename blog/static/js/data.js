function setlike(id){

    let data = {
        image_id: id
    }
    
    fetch(`https://${window.location.host}/image/like`, {
        method: 'POST',
        body: JSON.stringify(data),
        headers: { 'Accept': 'application/json, text/plain, */*',
        'Content-Type': 'application/json',
        "X-CSRFToken": getCookie('csrftoken') },
    }).then(res =>{
        res.json().then(data => {
            console.log(data)
            setLikesCount(data.count_like, data.action, id)
          })
    })
}




function setLikesCount(count_like, action, image_id){
    likes = document.getElementById(`like-count-${image_id}`)
    likes.innerHTML = `${count_like} curtidas`
    let icon_like = document.getElementById(`like-image-${image_id}`)
    let icon_deslike = document.getElementById(`notlike-image-${image_id}`)
    if (action){
        icon_like.style.display='flex'
        icon_deslike.style.display='none'
    } else {
        icon_like.style.display='none'
        icon_deslike.style.display='flex'
    }
}



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}