// 1. Tab Değiştirme (Seminars, Universities vs.)
function showTab(type) {
    const title = document.getElementById('tab-title');
    const text = document.getElementById('tab-text');
    
    // Butonların aktiflik durumunu temizle
    document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
    event.target.classList.add('active');

    if(type === 'univ') {
        title.innerText = "Revolution in University Education";
        text.innerText = "Following lectures is no longer a nightmare for students studying abroad.";
    } else if(type === 'seminar') {
        title.innerText = "Global Seminars";
        text.innerText = "Participate in international conferences with real-time translation support.";
    } else if(type === 'language') {
        title.innerText = "Language Schools";
        text.innerText = "Accelerate your language learning process with AI-powered assistance.";
    }
}

// 2. Başa Dön Oku Mantığı
const topBtn = document.getElementById("backToTop");
window.onscroll = function() {
    if (document.documentElement.scrollTop > 300) {
        topBtn.style.display = "block";
    } else {
        topBtn.style.display = "none";
    }
};

function scrollToTop() {
    window.scrollTo({ top: 0, behavior: 'smooth' });
}
