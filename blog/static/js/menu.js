const menu_active = (f) => {
    let menu_a = document.getElementById('menu-a')


    if (menu_a.style.display == 'none'){
        menu_a.style.display = 'flex'
    } else {
        menu_a.style.display = 'none'
    }
}

fetch(`https://${window.location.host}/image/like`,{
    method: 'GET',
}).then((res) => {
    res.json().then(data => {
        console.log(data.count)
      })
})