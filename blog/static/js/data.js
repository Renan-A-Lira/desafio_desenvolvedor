var doubletapDeltaTime_ = 700;
var doubletap1Function_ = null;
var doubletap2Function_ = null;
var doubletapTimer = null;

function tap(singleTapFunc, doubleTapFunc, id) {
    if (doubletapTimer==null) {
    // First tap, we wait X ms to the second tap
        doubletapTimer = setTimeout(() =>{
            doubletapTimeout()
        }, doubletapDeltaTime_);
        doubletap1Function_ = singleTapFunc;
        doubletap2Function_ = doubleTapFunc;
    } else {
    // Second tap
        clearTimeout(doubletapTimer);
        doubletapTimer = null;
        doubletap2Function_(id);
    }
}

function doubletapTimeout() {
// Wait for second tap timeout
    doubletap1Function_;
    doubleTapTimer = null;
}




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
            setLikesCount(data.count_like, data.action, id)
          })
    })
}




function setLikesCount(count_like, action, image_id){
    likes = document.getElementById(`like-count-${image_id}`)
    likes.innerHTML = `${count_like} curtidas`
    let icon_like = document.getElementById(`like-image-${image_id}`)
    let icon_deslike = document.getElementById(`notlike-image-${image_id}`)
    let icon_heart_like_img = document.getElementById(`heart-like-img-${image_id}`)
    if (action){
        icon_like.style.display='flex'
        icon_deslike.style.display='none'
        icon_heart_like_img.style.fontSize = '8rem'
        icon_heart_like_img.style.display = 'flex'
        setTimeout(()=>{
            icon_heart_like_img.style.fontSize='0'
            icon_heart_like_img.style.display = 'none'
        }, 1000)
    } else {
        icon_like.style.display='none'
        icon_deslike.style.display='flex'
        icon_heart_like_img.style.fontSize='0'
        icon_heart_like_img.style.display = 'none'
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