const menu_active = (f) => {
    let menu_a = document.getElementById('menu-a')


    if (menu_a.style.display == 'none'){
        menu_a.style.display = 'flex'
    } else {
        menu_a.style.display = 'none'
    }
}