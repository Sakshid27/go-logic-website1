document.addEventListener('DOMContentLoaded', function() {
    // First slider
    let items = document.querySelectorAll('.slider:not(.slider-large) .item');
    let active = Math.floor(items.length / 2);
    
    // Second slider
    let items2 = document.querySelectorAll('.slider-large .item');
    let active2 = Math.floor(items2.length / 2);
    
    function loadShow(sliderItems, activeIndex, isLarge = false) {
        // Set active item
        sliderItems[activeIndex].style.transform = `none`;
        sliderItems[activeIndex].style.zIndex = 1;
        sliderItems[activeIndex].style.filter = 'none';
        sliderItems[activeIndex].style.opacity = 1;
        
        // Show items after active
        let stt = 0;
        for(let i = activeIndex + 1; i < sliderItems.length; i++) {
            stt++;
            sliderItems[i].style.transform = `translateX(${isLarge ? 140 : 120 * stt}px) scale(${1 - 0.2 * stt}) perspective(16px) rotateY(-1deg)`;
            sliderItems[i].style.zIndex = -stt;
            sliderItems[i].style.filter = 'blur(3px)';
            sliderItems[i].style.opacity = stt > 2 ? 0 : 0.6;
        }
        
        // Show items before active
        stt = 0;
        for(let i = activeIndex - 1; i >= 0; i--) {
            stt++;
            sliderItems[i].style.transform = `translateX(${isLarge ? -140 : -120 * stt}px) scale(${1 - 0.2 * stt}) perspective(16px) rotateY(1deg)`;
            sliderItems[i].style.zIndex = -stt;
            sliderItems[i].style.filter = 'blur(3px)';
            sliderItems[i].style.opacity = stt > 2 ? 0 : 0.6;
        }
    }
    
    // Initialize both sliders
    loadShow(items, active);
    loadShow(items2, active2);
    
    // First slider controls
    document.getElementById('next').onclick = function() {
        active = active + 1 < items.length ? active + 1 : active;
        loadShow(items, active);
    }
    
    document.getElementById('prev').onclick = function() {
        active = active - 1 >= 0 ? active - 1 : active;
        loadShow(items, active);
    }
    
    // Second slider controls
    document.getElementById('next2').onclick = function() {
        active2 = active2 + 1 < items2.length ? active2 + 1 : active2;
        loadShow(items2, active2);
    }
    
    document.getElementById('prev2').onclick = function() {
        active2 = active2 - 1 >= 0 ? active2 - 1 : active2;
        loadShow(items2, active2);
    }
});
