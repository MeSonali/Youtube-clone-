document.querySelectorAll('.sidebar__section__link').forEach(link => {
    link.addEventListener('click', function() {
        
        document.querySelectorAll('.sidebar__section__link').forEach(item => {
            item.classList.remove('sidebar__section__link--selected');
            item.querySelector('svg').style.fill = 'rgb(96, 96, 96)'; 
        });

       
        this.classList.add('sidebar__section__link--selected');
        this.querySelector('svg').style.fill = '#f00';
    });
});